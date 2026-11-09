# MiniMax MCP 官方归属与整包证据复核

2026-11-09，P1-01。MiniMax 开放平台 MCP 指南在正文链接官方 Python 和 JavaScript 实现，并推荐 CLI 作为接入方式。本次只核 Python 仓库。默认分支 main，仓库未归档，最新提交仍是 2026-08-20 的 `0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a`，与 10-26 审计相同。固定根许可为 MIT，包清单版本为 0.0.19。此版本号来自源码，未与包仓实际发布对照，也不据此推断 JS 或商业服务行为。[官方指南](https://platform.minimax.io/docs/guides/mcp-guide) · [固定许可证](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/LICENSE) · [包清单](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/pyproject.toml)

直接读回主仓中的既有整包分片并计算 SHA256，与原 manifest 一致；从归档逐项抽读许可证、两种 README、包清单、四份实现与两份测试，10 个成员的 Git blob 与上游固定版本一致。补展开 5 个文件便于查阅，整包是既有备份。开放平台网页只存链接。本轮未运行上游脚本、MCP 或远端服务。

中英文检索分别使用“MiniMax 开放平台 MCP 官方 本地文件 视频”及“MiniMax official MCP GitHub video query retrieve file”。关键事实依官方指南、固定源和归档验证；搜索摘要未作结论。既有[多模态适配分析](../cases/ecosystem-expansion.md)保留，本轮新增[视频查询与交付边界](solutions/minimax-mcp-video-delivery.md)。
