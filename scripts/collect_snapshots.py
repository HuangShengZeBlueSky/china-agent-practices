#!/usr/bin/env python3
"""原文备份器：输入来源目录，下载固定提交的完整仓库归档并展开全部技能依赖。

保留原始 tar.gz 字节、SHA256、逐文件清单和上游许可；不执行上游文件。
语义解读由研究任务完成，本程序只识别明确的 SKILL.md 文件与目录关系。
支持 pinned（研究引用版本）、latest（当前默认分支）及 both（两者）。
"""
from __future__ import annotations
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tarfile
import tempfile
from datetime import datetime, timezone
import urllib.request
import time

ROOT = Path(__file__).resolve().parents[1]
CHUNK = 8 * 1024 * 1024


def digest(data):
    """输入字节；计算 SHA256；输出内容校验标识。"""
    return hashlib.sha256(data).hexdigest()


def get_json(url):
    """输入 GitHub 公开 API 地址；读取 JSON；输出已解析结果，不输出令牌。"""
    headers = {'User-Agent': 'china-agent-practices-snapshot', 'Accept': 'application/vnd.github+json'}
    if os.environ.get('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=90) as response:
        return json.load(response)


def source_map():
    """读取来源目录；按真实 GitHub 仓库归并版本和材料；输出备份配置。"""
    result = {}
    for source in json.loads((ROOT / 'catalog/sources.json').read_text())['sources']:
        if not source['url'].startswith('https://github.com/'):
            continue
        repo = '/'.join(source['url'].split('/')[3:5])
        item = result.setdefault(repo, {'repository': repo, 'pinned': source['commit'], 'source_ids': [], 'inspected': [], 'licenses': []})
        item['source_ids'].append(source['id'])
        item['inspected'].extend(f['path'] for f in source['inspected_files'])
        item['licenses'].append(source['license'])
    return result


def download(repo, commit, target):
    """输入仓库和固定提交；流式下载完整源码归档并重试网络失败；输出大小与 SHA256。"""
    url = f'https://codeload.github.com/{repo}/tar.gz/{commit}'
    for attempt in range(3):
        try:
            h = hashlib.sha256()
            size = 0
            with urllib.request.urlopen(url, timeout=180) as response, target.open('wb') as out:
                while block := response.read(1024 * 1024):
                    out.write(block)
                    h.update(block)
                    size += len(block)
            return size, h.hexdigest()
        except Exception:
            target.unlink(missing_ok=True)
            if attempt == 2:
                raise
            time.sleep(2 + attempt)


def snapshot(source, commit):
    """输入来源及提交；备份完整归档、技能目录和证据文件；输出可检查的版本清单。"""
    repo = source['repository']
    folder = ROOT / 'snapshots' / repo / commit
    manifest_path = folder / 'manifest.json'
    if manifest_path.exists():
        return json.loads(manifest_path.read_text())
    folder.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='agent-original-') as temp:
        archive = Path(temp) / 'source.tar.gz'
        size, checksum = download(repo, commit, archive)
        parts = []
        with archive.open('rb') as incoming:
            n = 0
            while block := incoming.read(CHUNK):
                name = f'source.tar.gz.part{n:04d}'
                (folder / name).write_bytes(block)
                parts.append({'path': name, 'bytes': len(block), 'sha256': digest(block)})
                n += 1
        all_files = []
        skills = []
        preserved = []
        with tarfile.open(archive, 'r:gz') as tar:
            members = []
            for member in tar.getmembers():
                path = PurePosixPath(member.name)
                if len(path.parts) < 2:
                    continue
                relative = PurePosixPath(*path.parts[1:])
                if path.is_absolute() or '..' in relative.parts:
                    raise ValueError('归档包含不安全路径')
                members.append((member, relative.as_posix()))
            roots = {str(PurePosixPath(p).parent) for m, p in members if m.isfile() and PurePosixPath(p).name == 'SKILL.md'}
            for member, path in members:
                entry = {'path': path, 'bytes': member.size, 'kind': 'file' if member.isfile() else 'symlink' if member.issym() else 'other'}
                if member.issym() or member.islnk():
                    entry['link_target'] = member.linkname
                all_files.append(entry)
                if not member.isfile():
                    continue
                parent_paths = PurePosixPath(path).parents
                in_skill = any(str(p) in roots for p in parent_paths) or '.' in roots
                license_file = PurePosixPath(path).name.lower().startswith(('license', 'licence', 'copying', 'notice'))
                root_readme = '/' not in path and PurePosixPath(path).name.lower().startswith('readme')
                if in_skill or license_file or root_readme or path in source['inspected']:
                    content = tar.extractfile(member).read()
                    dest = folder / 'files' / path
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(content)
                    record = {'path': path, 'bytes': len(content), 'sha256': digest(content)}
                    preserved.append(record)
                    if PurePosixPath(path).name == 'SKILL.md':
                        skills.append({**record, 'directory': str(PurePosixPath(path).parent), 'status': 'snapshot_only'})
        manifest = {'repository': repo, 'commit': commit, 'captured_at': datetime.now(timezone.utc).isoformat(), 'source_ids': source['source_ids'], 'license_notes': source['licenses'], 'archive_url': f'https://codeload.github.com/{repo}/tar.gz/{commit}', 'archive_sha256': checksum, 'archive_bytes': size, 'archive_parts': parts, 'archive_file_count': len(all_files), 'skills_count': len(skills), 'files': preserved, 'skills': skills, 'git_history_included': False, 'submodule_lfs_note': '源码归档不包括子模块内容、Git 历史及未内嵌的 LFS 对象；符号链接保存在原归档，不作为本地可执行链接展开。'}
        (folder / 'tree.json').write_text(json.dumps(all_files, ensure_ascii=False), encoding='utf-8')
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
        return manifest


def collect_one(source, mode):
    """输入来源与版本策略；解析并收集固定版本；输出成功记录或明确错误。"""
    try:
        refs = [source['pinned']] if mode in ('pinned', 'both') else []
        if mode in ('latest', 'both'):
            info = get_json('https://api.github.com/repos/' + source['repository'])
            head = get_json(f"https://api.github.com/repos/{source['repository']}/commits/{info['default_branch']}")['sha']
            refs.append(head)
        results = [snapshot(source, ref) for ref in dict.fromkeys(refs)]
        print(json.dumps({'repository': source['repository'], 'versions': len(results), 'skills': sum(x['skills_count'] for x in results), 'bytes': sum(x['archive_bytes'] for x in results)}, ensure_ascii=False), flush=True)
        return {'repository': source['repository'], 'ok': True, 'commits': list(dict.fromkeys(refs))}
    except Exception as error:
        print(json.dumps({'repository': source['repository'], 'error': str(error)}, ensure_ascii=False), flush=True)
        return {'repository': source['repository'], 'ok': False, 'error': str(error)}


def write_index(results):
    """扫描已完成版本；汇总覆盖率与错误；输出仓库总索引和 GitHub 可读入口。"""
    versions = []
    for path in sorted((ROOT / 'snapshots').glob('*/*/*/manifest.json')):
        m = json.loads(path.read_text())
        versions.append({k: m[k] for k in ('repository', 'commit', 'captured_at', 'archive_bytes', 'archive_sha256', 'skills_count', 'archive_file_count')})
    index = {'updated_at': datetime.now(timezone.utc).isoformat(), 'scope': 'catalog/sources.json 中全部 GitHub 来源；每个版本保留完整源码归档与所有 SKILL.md 所在目录。不是互联网全部技能。', 'runs': results, 'versions': versions, 'repositories': len({v['repository'] for v in versions}), 'skill_paths_across_versions': sum(v['skills_count'] for v in versions), 'bytes': sum(v['archive_bytes'] for v in versions)}
    (ROOT / 'catalog/snapshots.json').write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# 原文快照库', '', '完整仓库源码归档＋全部技能及目录依赖。原文未经改写；已备份不表示已经解读或实跑。', '', '归档分为 8 MiB 分片，使用恢复脚本按清单重组并验证 SHA256。Git 历史、子模块及外置 LFS 对象不包括在源码归档内。', '', '| 来源 | 固定提交 | 技能路径 | 完整归档字节 | 本地原文与清单 |', '| --- | --- | ---: | ---: | --- |']
    for v in versions:
        base = f"{v['repository']}/{v['commit']}"
        lines.append(f"| {v['repository']} | {v['commit'][:12]} | {v['skills_count']} | {v['archive_bytes']} | [全部原文]({base}/files) · [清单]({base}/manifest.json) |")
    lines += ['', '## 本轮失败', ''] + [f"- {r['repository']}: {r['error']}" for r in results if not r['ok']]
    (ROOT / 'snapshots/README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return index


def main():
    """解析命令参数；并发下载公开数据；写入统一索引；部分失败返回非零退出码。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=['pinned', 'latest', 'both'], default='both')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--repository')
    args = parser.parse_args()
    sources = source_map()
    chosen = [v for k, v in sources.items() if not args.repository or k == args.repository]
    if not chosen:
        raise SystemExit('未找到来源')
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda s: collect_one(s, args.mode), chosen))
    index = write_index(results)
    print(json.dumps({k: index[k] for k in ('repositories', 'skill_paths_across_versions', 'bytes')}), flush=True)
    raise SystemExit(0 if all(r['ok'] for r in results) else 1)


if __name__ == '__main__':
    main()
