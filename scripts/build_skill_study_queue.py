#!/usr/bin/env python3
"""从既有原文索引生成可分批阅读的全量技能台账，保留人工进度。

入口正文按 file_id 分组仅为复用阅读；每个路径仍有独立依赖和宿主核查状态。
本脚本不读取或运行上游脚本，不自动产生语义总结，也不标记研究完成。
"""

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_json(path, value):
    """把结构化台账写成 UTF-8 JSON，保持每条记录可逐项定位。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def build_queue():
    """合并原文出现位置与已有阅读记录；任何旧记录和人工状态都不静默删除。"""
    source = ROOT / 'catalog/original-skills.json'
    source_data = source.read_bytes()
    catalog = json.loads(source_data)
    output = ROOT / 'catalog/skill-study'
    existing = {}
    for path in sorted(output.glob('groups-*.json')):
        for group in json.loads(path.read_text())['groups']:
            existing[group['content_id']] = group
    groups = {}
    seen_ids = set()
    for skill in catalog['skills']:
        assert skill['id'] not in seen_ids, '重复技能路径 ID'
        seen_ids.add(skill['id'])
        key = skill['file_id']
        assert len(key) == 64 and all(c in '0123456789abcdef' for c in key)
        group = groups.setdefault(key, existing.get(key, {
            'content_id': key, 'entry_status': 'not_read', 'analysis_file': None,
            'solution_file': None, 'occurrences': []
        }))
        known = {x['source_id']: x for x in group['occurrences']}
        if skill['id'] not in known:
            group['occurrences'].append({
                'source_id': skill['id'], 'repository': skill['repository'],
                'commit': skill['commit'], 'path': skill['path'],
                'prior_reading': skill.get('reading'),
                'dependency_status': 'not_checked', 'host_status': 'not_checked',
                'review_status': 'pending', 'execution_status': 'not_run',
                'equivalence_evidence': None
            })
        if skill.get('reading') and group['entry_status'] == 'not_read':
            group['entry_status'] = 'prior_entry_read_only'
            group['analysis_file'] = 'cases/original-reading-workbook.md'
    for key, old in existing.items():
        groups.setdefault(key, old)
    assert len(groups) == catalog['stats']['unique_skill_contents'], '固定基线变化，先显式升级范围'
    assert sum(len(g['occurrences']) for g in groups.values()) == catalog['stats']['skill_paths'], '固定基线路径变化'
    shards = []
    for prefix in '0123456789abcdef':
        values = sorted((g for k, g in groups.items() if k[0] == prefix), key=lambda g: g['content_id'])
        path = output / f'groups-{prefix}.json'
        write_json(path, {'groups': values})
        shards.append({'path': path.relative_to(ROOT).as_posix(), 'groups': len(values),
                       'occurrences': sum(len(g['occurrences']) for g in values)})
    states = Counter(g['entry_status'] for g in groups.values())
    index = {
        'schema_version': 1, 'created_on': '2026-10-25',
        'baseline_repository_commit': 'febcdbe196c9b7303837aa77057b765327238f37',
        'source_path': 'catalog/original-skills.json',
        'source_git_blob': 'c693648be3dbd0326a4ee962c6e30ef782180f8f',
        'source_local_sha256': hashlib.sha256(source_data).hexdigest(),
        'scope': '全部既有路径；分组只证明入口字节相同，不证明依赖或宿主等价',
        'baseline_stats': catalog['stats'], 'content_groups': len(groups),
        'occurrences': sum(len(g['occurrences']) for g in groups.values()),
        'entry_states': dict(states), 'shards': shards
    }
    write_json(output / 'index.json', index)
    assert len(groups) == catalog['stats']['unique_skill_contents'], '首轮基线分组不一致'
    assert index['occurrences'] == catalog['stats']['skill_paths'], '首轮路径覆盖不一致'
    print(json.dumps({k: index[k] for k in ('content_groups', 'occurrences', 'entry_states')}, ensure_ascii=False))


if __name__ == '__main__':
    build_queue()
