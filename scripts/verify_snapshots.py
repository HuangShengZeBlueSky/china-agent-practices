#!/usr/bin/env python3
"""校验全部归档分片、原始整包和展开原文；可从已有归档恢复被忽略的文件，不执行上游内容。"""
import argparse
import hashlib
import json
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def main():
    """读取清单和修复选项；核对每片、总摘要及原文；输出可追溯校验报告。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repair', action='store_true')
    args = parser.parse_args()
    reports = []
    for path in sorted((ROOT / 'snapshots').glob('*/*/*/manifest.json')):
        manifest = json.loads(path.read_text())
        h, errors, restored = hashlib.sha256(), [], 0
        missing = {f['path'] for f in manifest['files'] if not (path.parent / 'files' / f['path']).is_file()}
        with tempfile.TemporaryDirectory(prefix='snapshot-integrity-') as temp:
            archive = Path(temp) / 'source.tar.gz'
            with archive.open('wb') as output:
                for part in manifest['archive_parts']:
                    data = (path.parent / part['path']).read_bytes()
                    if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
                        errors.append('分片校验失败：' + part['path'])
                    h.update(data)
                    if args.repair and missing:
                        output.write(data)
            if h.hexdigest() != manifest['archive_sha256']:
                errors.append('完整归档摘要不一致')
            if args.repair and missing and not errors:
                with tarfile.open(archive, 'r:gz') as tar:
                    for member in tar:
                        relative = PurePosixPath(*PurePosixPath(member.name).parts[1:])
                        if '..' in relative.parts or relative.is_absolute():
                            raise ValueError('原归档包含不安全路径')
                        name = relative.as_posix()
                        if member.isfile() and name in missing:
                            out = path.parent / 'files' / name
                            out.parent.mkdir(parents=True, exist_ok=True)
                            out.write_bytes(tar.extractfile(member).read())
                            restored += 1
            for file in manifest['files']:
                original = path.parent / 'files' / file['path']
                if not original.is_file():
                    errors.append('缺失原文：' + file['path'])
                    continue
                data = original.read_bytes()
                if len(data) != file['bytes'] or hashlib.sha256(data).hexdigest() != file['sha256']:
                    errors.append('原文字节不一致：' + file['path'])
            tree = json.loads((path.parent / 'tree.json').read_text())
            expected = {f['path'] for f in tree if f['kind'] == 'file' and PurePosixPath(f['path']).name == 'SKILL.md'}
            if expected != {s['path'] for s in manifest['skills']}:
                errors.append('技能路径覆盖不完整')
        reports.append({'repository': manifest['repository'], 'commit': manifest['commit'], 'parts_verified': len(manifest['archive_parts']), 'files_verified': len(manifest['files']), 'restored': restored, 'errors': errors})
    result = {'checked_at': datetime.now(timezone.utc).isoformat(), 'ok': not any(r['errors'] for r in reports), 'versions': len(reports), 'files_verified': sum(r['files_verified'] for r in reports), 'parts_verified': sum(r['parts_verified'] for r in reports), 'reports': reports}
    (ROOT / 'catalog/snapshot-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({k: v for k, v in result.items() if k != 'reports'}), flush=True)
    raise SystemExit(0 if result['ok'] else 1)


if __name__ == '__main__':
    main()
