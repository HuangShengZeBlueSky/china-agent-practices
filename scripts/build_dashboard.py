#!/usr/bin/env python3
"""把已审阅的目录与原创研究文档打包为静态看板数据，不抓取或执行上游代码。

输入是 catalog 下的 JSON 和本仓 Markdown；输出是 dashboard/data.js。
语义分类与方法提炼由研究者维护，脚本只做结构检查、统计和确定性序列化。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "prompt": "提示词", "agent": "Agent 编排", "skill": "Skill 技能",
    "cli": "CLI 命令行", "tool": "工具契约", "api": "API 接口",
    "mcp": "MCP", "sandbox": "沙箱执行", "memory": "记忆与上下文",
    "evaluation": "评估验收", "observability": "轨迹与观测",
}


def read_json(path: Path, fallback: object) -> object:
    """输入 JSON 路径；存在时读取并解析，否则返回给定默认值。"""
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else fallback


def validate_sources(sources: list[dict]) -> None:
    """检查来源标识、文件链接、分类和本地案例；遇到数据冲突即停止生成。"""
    seen = set()
    for source in sources:
        source_id = source["id"]
        if source_id in seen:
            raise ValueError(f"重复来源标识：{source_id}")
        seen.add(source_id)
        for key in ("company", "project", "url", "source_type", "license", "checked_at", "methods", "evidence_limits"):
            if not source.get(key):
                raise ValueError(f"{source_id} 缺少 {key}")
        case = (ROOT / source["case_file"]).resolve()
        if not case.is_relative_to(ROOT) or not case.is_file():
            raise ValueError(f"{source_id} 中文拆解不存在")
        if not source.get("inspected_files"):
            raise ValueError(f"{source_id} 没有具体阅读材料")
        for category in source.get("categories", []):
            if category not in CATEGORIES:
                raise ValueError(f"{source_id} 未知分类 {category}")
        if source.get("commit") and (len(source["commit"]) != 40 or any(c not in "0123456789abcdef" for c in source["commit"])):
            raise ValueError(f"{source_id} 提交 SHA 格式错误")
        for material in source["inspected_files"]:
            if urlparse(material["url"]).scheme != "https":
                raise ValueError(f"{source_id} 材料不是 HTTPS 地址")


def collect_documents() -> dict[str, dict]:
    """读取仓库原创文档，以相对路径为键返回标题与 Markdown，供站内阅读。"""
    paths = [ROOT / "README.md", ROOT / "NOTICE.md", ROOT / "ROADMAP.md", ROOT / "CHANGELOG.md", ROOT / "catalog/README.md"]
    paths += sorted((ROOT / "cases").glob("*.md"))
    paths += sorted((ROOT / "docs").glob("*.md"))
    paths += sorted((ROOT / "templates").glob("*.md"))
    documents = {}
    for path in paths:
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            title = next((line[2:] for line in content.splitlines() if line.startswith("# ")), path.stem)
            documents[path.relative_to(ROOT).as_posix()] = {"title": title, "markdown": content}
    return documents


def write_readable_catalog(sources: list[dict], updated_at: str) -> None:
    """从同一份来源数据生成 Markdown 索引，避免网页与仓库目录分开维护。"""
    labels = {"official_code": "官方源码", "official_docs": "官方文档", "third_party_archive": "第三方归档"}
    rows = ["# 来源目录", "", f"检查日期：{updated_at}。共 {len(sources)} 条研究记录。每条按研究主题组织，同一仓库可支持多个主题，因此条目数不等于独立仓库数。", "", "全部为静态阅读；具体覆盖范围见文件记录。完整第三方技能路径索引在 [archive-skill-index.json](archive-skill-index.json)，不计入逐篇深读数量。", "", "| 项目 | 组织 / 来源 | 重点 | 中文拆解 |", "| --- | --- | --- | --- |"]
    for source in sources:
        rows.append(f"| [{source.get('short_title', source['project'])}]({source['url']}) | {source.get('company_group', source['company'])} · {labels[source['source_type']]} | {source['summary']} | [阅读](../{source['case_file']}) |")
    for source in sources:
        rows.extend(["", f"## {source['project']}", "", f"来源类型：{labels[source['source_type']]}。检查日：{source['checked_at']}。固定提交：`{source.get('commit') or '文档页面，无提交号'}`。", "", f"许可：{source['license']}", "", f"**学习重点：** {source['learning_value']}", "", "具体阅读材料：", ""])
        rows.extend(f"- [{material['path']}]({material['url']})：{material['purpose']}" for material in source['inspected_files'])
        rows.extend(["", "证据边界：", ""])
        rows.extend(f"- {limit}" for limit in source['evidence_limits'])
    (ROOT / "catalog/README.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def write_method_map(methods: list[dict], sources: list[dict]) -> None:
    """将人工维护的方法卡转换为可在 GitHub 阅读的说明，保留原文与边界。"""
    by_id = {source["id"]: source for source in sources}
    lines = ["# 十二类工程问题与方法对照", "", "这些方法来自公开实现与技能文件的静态阅读。每项将观察到的机制、我们建议做的练习和未验证边界分别记录。效果需要在自己的任务上验证。", "", "| 工程问题 | 首先看哪些项目 |", "| --- | --- |"]
    for method in methods:
        names = [by_id[source_id].get("short_title", by_id[source_id]["project"]) for source_id in method["source_ids"]]
        lines.append(f"| {method['title']} | {'、'.join(names)} |")
    for index, method in enumerate(methods, 1):
        lines.extend(["", f"## {index}. {method['title']}", "", f"**要解决的问题。** {method['problem']}", "", f"**观察到的机制。** {method['mechanism']}", "", f"**迁移练习。** {method['practice']}", "", f"**证据边界。** {method.get('boundary', '静态阅读，未实跑。')}", "", "阅读来源：", ""])
        for source_id in method["source_ids"]:
            source = by_id[source_id]
            lines.append(f"- [{source.get('short_title', source['project'])}]({source['url']}) · [中文拆解](../{source['case_file']}) · 固定提交 `{source.get('commit') or '文档页面'}`")
    (ROOT / "docs/method-map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_payload(download_url: str | None) -> dict:
    """聚合目录、方法、路线与归档索引；统计按组织、仓库和文件分别去重。"""
    catalog = read_json(ROOT / "catalog/sources.json", {})
    sources = catalog["sources"]
    validate_sources(sources)
    write_readable_catalog(sources, catalog["updated_at"])
    methods = read_json(ROOT / "catalog/methods.json", [])
    paths = read_json(ROOT / "catalog/learning-paths.json", [])
    ids = {source["id"] for source in sources}
    for entry in methods:
        if not set(entry.get("source_ids", [])) <= ids:
            raise ValueError(f"方法 {entry['id']} 引用了不存在的来源")
    for path in paths:
        for step in path["steps"]:
            if not set(step.get("source_ids", [])) <= ids:
                raise ValueError(f"路线 {path['id']} 引用了不存在的来源")
    write_method_map(methods, sources)
    organizations = {s.get("company_group", s["company"]) for s in sources if s["source_type"] != "third_party_archive"}
    repositories = set()
    for source in sources:
        parsed = urlparse(source["url"])
        if parsed.netloc.lower() == "github.com":
            parts = parsed.path.strip("/").split("/")
            if len(parts) >= 2:
                repositories.add("/".join(parts[:2]).lower())
    return {
        "updated_at": catalog["updated_at"],
        "verification_note": catalog["verification_note"],
        "sources": sources,
        "categories": CATEGORIES,
        "methods": methods,
        "learning_paths": paths,
        "archive": read_json(ROOT / "catalog/archive-inventory.json", {}),
        "documents": collect_documents(),
        "download_url": download_url,
        "stats": {
            "sources": len(sources), "organizations": len(organizations),
            "repositories": len(repositories),
            "materials": len({item["url"] for source in sources for item in source["inspected_files"]}),
            "official_sources": sum(s["source_type"] != "third_party_archive" for s in sources),
            "archive_sources": sum(s["source_type"] == "third_party_archive" for s in sources),
        },
    }


def main() -> None:
    """处理输出参数，生成可离线加载的数据脚本，并打印不含正文的统计。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dashboard/data.js")
    parser.add_argument("--download-url", default=None)
    args = parser.parse_args()
    payload = build_payload(args.download_url)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    args.output.write_text("// 此文件由 scripts/build_dashboard.py 生成。\nwindow.ATLAS_DATA = " + encoded + ";\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), **payload["stats"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
