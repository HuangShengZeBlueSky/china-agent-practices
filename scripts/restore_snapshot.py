#!/usr/bin/env python3
"""输入快照目录和输出文件路径；逐片校验并重组原始源码归档，不执行或解压上游代码。"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    """解析目录和输出位置；核对每片及总摘要；输出与下载原件字节一致的 tar.gz。"""
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('directory', type=Path)
    p.add_argument('output', type=Path)
    a = p.parse_args()
    manifest = json.loads((a.directory / 'manifest.json').read_text())
    if a.output.exists():
        raise SystemExit('输出已存在，拒绝覆盖')
    h = hashlib.sha256()
    try:
        with a.output.open('xb') as output:
            for part in manifest['archive_parts']:
                data = (a.directory / part['path']).read_bytes()
                if hashlib.sha256(data).hexdigest() != part['sha256']:
                    raise ValueError('分片校验失败：' + part['path'])
                output.write(data)
                h.update(data)
        if h.hexdigest() != manifest['archive_sha256']:
            raise ValueError('完整归档校验失败')
    except Exception:
        a.output.unlink(missing_ok=True)
        raise
    print('完整归档已恢复，SHA256 校验通过：', a.output)


if __name__ == '__main__':
    main()
