#!/usr/bin/env python3
"""云端备份入口：逐仓库收集并分批提交，避免一次推送全部大归档；不执行任何上游代码。"""
import argparse
import json
import subprocess
from collect_snapshots import ROOT, source_map, collect_one, write_index


def git(*args):
    """输入固定 Git 子命令参数；在本研究仓库执行；失败时停止并保留已完成提交。"""
    return subprocess.run(['git', *args], cwd=ROOT, check=True)


def commit_push(paths, message):
    """输入本仓成果路径；仅有变化时提交并推送 main；输出可追溯提交记录。"""
    git('add', '--', *paths)
    if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=ROOT).returncode:
        git('commit', '-m', message)
        git('push', 'origin', 'HEAD:main')


def main():
    """读取来源目录和版本策略；逐仓库备份并提交，最后生成原文阅读器及本轮汇总。"""
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode', choices=['pinned', 'latest', 'both'], default='both')
    args = p.parse_args()
    git('config', 'user.name', 'Agent Research Archive')
    git('config', 'user.email', 'archive@users.noreply.github.com')
    results = []
    for source in source_map().values():
        result = collect_one(source, args.mode)
        results.append(result)
        write_index(results)
        paths = ['catalog/snapshots.json', 'snapshots/README.md']
        if (ROOT / 'snapshots' / source['repository']).exists():
            paths.append('snapshots/' + source['repository'])
        commit_push(paths, '备份原文：' + source['repository'])
    subprocess.run(['python3', 'scripts/build_original_library.py'], cwd=ROOT, check=True)
    commit_push(['catalog/original-skills.json', 'dashboard/originals'], '生成全部已备份技能的原文阅读库')
    raise SystemExit(0 if all(r['ok'] for r in results) else 1)


if __name__ == '__main__':
    main()
