# Coze Studio归属与公开边界补证

2026-11-06，P1-01子单元。固定版本fefb05ff27be1da939612fbf9faf5db62583b8ae，本日GitHub API默认分支main、archived=false，HEAD仍为该版本。仅更新此仓核查日期，不把31仓全部视作本日复查。

[BytePlus官方文章](https://www.byteplus.com/de/blog/coze-open-sources-ai-agent-tools)署名Coze Team、2025-07-29，正文分别直接链接Coze Studio和Coze Loop，补强官网到仓库归属链。此处只取归属证据，不采纳宣传性效果承诺。Coze Loop本日未重新读取固定许可证与源码，不算完成其版本缺口。

[固定README](../snapshots/coze-dev/coze-studio/fefb05ff27be1da939612fbf9faf5db62583b8ae/files/README.md)明确开源版与商业版有功能差异，致谢Eino、FlowGram、Hertz；不能把整个底层框架归为项目原创。[LICENSE-APACHE](../snapshots/coze-dev/coze-studio/fefb05ff27be1da939612fbf9faf5db62583b8ae/files/LICENSE-APACHE)全文已核对为Apache-2.0，保存原样；网页许可未确认，不镜像网页全文。

[消息模板源码](../snapshots/coze-dev/coze-studio/fefb05ff27be1da939612fbf9faf5db62583b8ae/files/backend/domain/agent/singleagent/internal/agentflow/node_chat_prompt.go)全文仅定义chatPrompt：Jinja2系统消息、历史占位符(true)、用户输入占位符(false)，并引用REACT_SYSTEM_PROMPT_JINJA2。它不能独立证明工具权限、恢复或验收。既有平台案例的更广构图结论保留原阅读范围；本轮不冒充全链重新审计。

本轮共核对6份既有原文：Coze3份与飞书3份，远端规范快照逐字一致、Git blob与manifest SHA256一致；完整源码包未重新下载，新增原文0，完整备份新增0。详见[清单](evidence/2026-11-06/source-manifest.json)。P1其他归属、迁移和10版本缺口未关闭，网站未部署。
