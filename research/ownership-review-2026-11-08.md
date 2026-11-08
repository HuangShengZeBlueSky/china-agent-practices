# Trae Agent 与 CloudBase 的归属、许可及版本复核

2026-11-08，P1-01 子单元。静态核查。

| 来源 | 一手归属与许可 | 固定版本和备份边界 |
| --- | --- | --- |
| Trae Agent | [TRAE 官方发布](https://www.trae.ai/blog/product_update_0625?v=1)点名 `bytedance/trae-agent`，区分公开组件和文中评测流程。[根许可](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/LICENSE)归属 ByteDance 及关联方，MIT。 | 默认分支 main，未归档。固定提交 `e839e559ac61bdd0e057c375dd1dee391fee797d`（2026-02-05 UTC）与 10-26 审计相同，既有整仓归档见 [manifest](../snapshots/bytedance/trae-agent/e839e559ac61bdd0e057c375dd1dee391fee797d/manifest.json)。没有重新下载该归档。 |
| CloudBase AI Toolkit | [云开发文档](https://docs.cloudbase.net/ai/cloudbase-ai-toolkit/prompts/how-to-use)和[腾讯云 MCP 条目](https://developer.cloud.tencent.com/mcp/server/11698)指向腾讯官方仓库。[当前根许可](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/8ec7084e0483e408573b7bd26ff7f3f4e02a788f/LICENSE)归属 Tencent CloudBase，MIT，与 10-26 版本 Git blob 一致。 | 默认分支 main，未归档。当前提交 `8ec7084e0483e408573b7bd26ff7f3f4e02a788f`（2026-11-07 UTC）。既有目录有 `f49b8d4`、`5a1c427` 整包，10-26 的 `4f68e9060c94327c1a39aa282ad17a03a4d7dfe5` 与当前提交本轮保存指定文件，整包仍缺。 |

## 版本差异如何影响工程判断

CloudBase 的 [固定对照](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/compare/4f68e9060c94327c1a39aa282ad17a03a4d7dfe5...8ec7084e0483e408573b7bd26ff7f3f4e02a788f)返回 265 个领先提交、0 个落后提交，文件列表返回 300 条。文件列表只作为抽样入口，不据此声明总变更文件数或覆盖完整。两个固定 `mcp/package.json` 的包版本分别为 2.36.1、2.37.5；源码版本号不能证明注册表或托管端正在运行对应代码。[旧包定义](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/4f68e9060c94327c1a39aa282ad17a03a4d7dfe5/mcp/package.json) · [新包定义](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/8ec7084e0483e408573b7bd26ff7f3f4e02a788f/mcp/package.json)

固定 [CloudBase MCP 技能](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/8ec7084e0483e408573b7bd26ff7f3f4e02a788f/config/source/skills/cloudbase-mcp/SKILL.md)将会话工具未注册、鉴权未就绪、绑定环境不符、签名或网关失败分开处理。它要求写入前通过 `auth(action="status")` 获得 `auth_status: "READY"` 且 `current_env_id` 匹配；当前无原生工具时，技能给出 CLI 回退与 mcporter 调用指引。这里证实的是文档中的处置策略。尚需追到 MCP 注册过滤、服务端鉴权及 CLI 环境解析，才能判断换通道后是否仍有同样权限与副作用约束。对比列表里的插件市场文件、技能与分发工作流均有变动，旧技能结论继续绑定原版本。当前 [README](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/8ec7084e0483e408573b7bd26ff7f3f4e02a788f/README.zh-CN.md)将 Toolkit 源仓、插件发布仓、单技能分发和 npm 区分，分发仓与宿主实际加载的字节尚未核对。

Trae Agent [宿主入口](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/agent/agent.py)调用 `new_task` 后视配置初始化 MCP，执行 `execute_task`，并在其 `finally` 中尝试清理 MCP 客户端；初始化位于这段 `try` 之前，不能从该入口推断初始化失败一定得到同一清理。固定 [OpenAI 适配器](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/utils/llm_clients/openai_client.py)在复用历史时把本轮转换后的消息追加到 `message_history`，工具结果随之进入下一次调用输入。这个证据支持公开 CLI 的上下文路径，不能外推商业客户端、其他供应商适配器或评测编排。官方发布中的多模型候选、回归筛选与选择器属于作者报告；本轮未核查完整评测器、论文和复现条件。

检索日期 2026-11-08。查询包括“字节 Trae Agent 开源 官方 Lakeview”“腾讯 云开发 CloudBase AI Toolkit MCP CLI 迁移”“Trae Agent ByteDance official open source GitHub”及官网域名限制。产品论坛普通回复和社区转载只用于发现。官网网页保留链接和原创说明；CloudBase 版本作为既有来源增量，不纳入冻结技能路径。未执行安装、模型或线上 API。

两版源包从固定下载地址取得，均可读取 tar 成员并计算 SHA256，见 [机器记录](evidence/2026-11-08/source-review.json)。整包未发布到主仓库，当前提交只保存 7 份指定原文。Git 推送预检缺少认证，当前以仓库连接器提交可复核的小文件。
