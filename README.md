# 中国科技公司 Agent 工程拆解

从公开实现中学习中国科技公司怎样构建 Agent（智能体）：提示词怎样装配，Skill（技能包）怎样写与加载，CLI（命令行工具）、API（程序接口）和 MCP 怎样提供能力，工具如何执行，错误如何恢复，任务怎样验收，以及这些经验怎样持续维护。

**[打开研究看板](https://china-agent-engineering-atlas.stormy-star-1873.chatgpt.site)** · [来源目录](catalog/README.md) · [十二类方法](docs/method-map.md) · [归档作者怎么做](cases/archive-collection-method.md)

## 原文快照与完整备份

已保存来源目录中全部 31 个公开 GitHub 仓库的版本快照。[打开原文总目录](snapshots/README.md)，可查看完整源码归档、所有技能目录、参考资料、脚本和资产；[逐篇学习笔记](cases/original-reading-workbook.md)单独记录已读范围与机制理解。正文保持原样，备份、解读、业务实跑分别记状态。

当前快照统计和完整性报告以 [快照清单](catalog/snapshots.json) 与 [校验报告](catalog/snapshot-verification.json) 为准。原始源码归档按 8 MiB 分片保存，附 SHA256 内容校验，可用 scripts/restore_snapshot.py 恢复。它们不包含全部 Git 历史、外部子模块或外置 LFS 对象。技能路径数含历史、测试样例与跨版本重复，不等于独立业务技能数。

云端备份工作流已经实际运行并完成校验；目前为手动触发，没有启用每日计划，也不把确定性下载称为模型自动解读。原文阅读入口在研究看板左侧“技能原文快照库”。

## 本轮已经完成什么

检查日期为 **2026-10-21**。从首版的 15 条来源扩展为 **35 条研究记录**，涉及 **14 家公司相关材料与 1 家研究机构**，覆盖 **31 个独立 GitHub 仓库**及官方产品文档。已静态核对 **187 个去重后的材料入口**，包括实现、提示、技能、参考说明、README 和许可证；大型文件的阅读范围在记录中说明，不表示逐行审计。研究记录中有 31 条官方源码记录、1 条官方文档记录和 3 条第三方归档记录；同一仓库可支持多个研究主题。

另外，为用户提供的第三方归档建立 **2,792 个 `SKILL.md` 路径**的元数据索引，分为当前主目录 2,581 个、删除历史 211 个。完整索引不计作逐篇深读，也不等于独立技能或厂商全量目录。当前路径按 Git blob 去重为 2,553 份内容；作者四份产品 README 合计的 1,199 个条目使用不同口径，尚未逐项对齐。

在材料上建立了 **12 个工程方法主题、4 条学习路线、6 份公司或专题长文**，并提供可搜索、筛选、站内阅读和记录学习进度的看板。本轮没有运行上游系统、调用业务服务或测量性能收益。

## 怎样开始看

想快速浏览，打开研究看板，在“资料库”按公司、提示词、技能、CLI、工具、MCP、沙箱、上下文、评估等主题筛选。点“查看拆解”能读到学习重点、具体原文、固定提交、许可和证据边界；点“阅读中文拆解”直接在页面内打开研究笔记。

想形成自己的方法，从 [方法地图](docs/method-map.md) 或看板的“学习路线”开始。四条路线分别围绕写业务技能、可靠使用工具、理解 Agent 运行骨架、建设长期研究库，每条都给出阅读步骤和最后应留下的产物。

想先建立直观理解，读 [用搭建题库看懂 Skill、CLI 和模型](docs/lark-walkthrough.md)。它是明确标为示意的任务，不是真实豆包运行轨迹。

看板可以收藏、设置阅读状态、记笔记和导出学习记录。这些个人记录只保存在当前浏览器，不跨设备同步；它们与研究来源的核查等级分别记录。详细用法见 [看板说明](docs/dashboard.md)。

## 覆盖范围

| 公司 / 机构 | 已读项目与资料 | 重点学什么 |
| --- | --- | --- |
| 字节／飞书／扣子 | Lark CLI 与官方 Skills、Eino、Trae Agent、Coze Studio、Coze Loop、DeerFlow 2.x、UI-TARS Desktop | 业务知识分工、技能加载、提示构图、大结果处理、GUI 动作与评估链 |
| 阿里巴巴及相关开源来源 | Qwen Code、Qwen-Agent、AgentScope、AgentScope Runtime；阿里来源的 OpenSandbox | 提示与工具对齐、消息路径、能力启用、服务封装、非幂等执行与异步状态 |
| 腾讯 | CloudBase AI Toolkit、CodeBuddy／WorkBuddy 文档、BrowserSkill、Tencent RTC Skills、SkillHub 官方 Skills | 业务路由、失败恢复、引用状态、会话工具、经验维护、静态校验边界 |
| 蚂蚁集团 | AWorld CLI | 技能激活证据、摘要提示、工作区上下文与检查点 |
| 百度 | AppBuilder SDK | 云端工具请求、本地执行与调用编号回传 |
| 华为 | openJiuwen agent-core | 技能入口、读取工具与文档实现漂移 |
| 美团 | VitaBench 1.0 | 工具前后条件、完整轨迹与任务评价 |
| 小米 | mimoagent | Agent、环境、模型和评分分层；工具真实执行语义 |
| 京东 | JoyAgent-JDGenie | 计划与执行职责、产物状态、并发工具结果配对 |
| 快手 | KwaiAgents Lite | 逐步规划、历史上下文与细粒度评测；Lite 版和许可边界 |
| 网易有道 | LobsterAI | 技能安装／启用／加载分层，桌面产品与 OpenClaw 运行时桥接 |
| 月之暗面、MiniMax、智谱（扩展对照） | Kimi CLI 历史 Python 版、MiniMax Skills／MCP、Open-AutoGLM | 技能作用域、任务阶段、异步媒体工具、截图与动作循环 |
| 上海人工智能实验室（研究机构） | Lagent、MindSearch | 消息与动作分层、并发搜索图、引用汇总及实现耦合 |
| ahang1598 第三方归档 | Doubao、WorkBuddy、QwenWork，另以 ChatGPT／Codex 作归档方法对照 | 本地采集、版本与删除历史、目录统计、六个代表技能的交接和验收协议 |

公开源码不能代表相应公司全部线上产品。公司维护的项目可能建立在社区框架之上；第三方市场包、上游库和原作者贡献在案例里单独说明。OpenSandbox 已迁至 opensandbox-group；AgentScope Runtime 公告能力迁入 2.0 并准备归档；Kimi CLI 的旧 Python 仓库已归档。看板卡片会提示这些维护状态，证据链接见 [平台扩展](cases/platforms-expansion.md) 和 [生态扩展](cases/ecosystem-expansion.md)。

## 这轮最值得学的几件事

**工具的行为契约直接影响模型能否做对。** 飞书把参数、适用指引、领域技能和详细参考分开；mimoagent 说明进程、并发、超时和退出码；OpenSandbox 针对非幂等 SSE 启动请求绕开自动重试。设计工具时需要同时回答“怎么调”和“调完意味着什么”。

**上下文管理需要可追溯的实现。** Eino 将技能元数据和正文的加载分开，Qwen Code 用会话工具声明快照筛选相关提示，DeerFlow 在输出预算中间件启用时外置大结果并提供回读路径。阅读它们应追踪实际模型消息，而非只比较提示词的文字长度。

**结束、格式正确和业务成功是不同证据。** Trae 的结束工具、Open-AutoGLM 的 finished、TRTC 的静态字符串检查、SkillHub 的报告字段校验、Coze Loop 的评委模型输出，都需要各自的解释边界。VitaBench 的独立轨迹评价提供了另一种可研究的验收方式。这些实现都没有被本仓实跑验证。

**采集只是研究的起点。** ahang1598 的脚本将本机缓存、路径差异、同路径内容的哈希比较、删除归档、自动索引和 Git 提交接起来；近期学习总结由模型另行整理。我们借鉴其可追溯结构，在此基础上增加来源分级、机制拆解、协议差异、学习路线与个人实践记录。

上述结论的具体文件和固定版本见 [方法地图](docs/method-map.md) 与下列案例。每项方法都保留“观察到什么”和“建议怎样试”的区别。

## 内容入口

| 内容 | 入口 |
| --- | --- |
| 初始公司案例 | [字节与飞书](cases/bytedance-lark.md)、[阿里与腾讯](cases/alibaba-tencent.md)、[百度／华为／美团／小米](cases/baidu-huawei-meituan-xiaomi.md) |
| 本轮新增案例 | [平台、运行时与官方技能](cases/platforms-expansion.md)、[京东／快手／网易及扩展生态](cases/ecosystem-expansion.md) |
| 归档作者拆解 | [采集与六个代表样本](cases/archive-collection-method.md)、[详细研究数据](catalog/archive-research.json)、[完整路径索引](catalog/archive-skill-index.json) |
| 汇总与学习 | [方法地图](docs/method-map.md)、[方法卡数据](catalog/methods.json)、[学习路线数据](catalog/learning-paths.json) |
| 来源 | [可读目录](catalog/README.md)、[结构化记录](catalog/sources.json) |
| 继续积累 | [研究方法](docs/research-method.md)、[采集到学习的流程](docs/collection-workflow.md)、[案例模板](templates/case-study.md)、[研究任务模板](templates/research-task.md) |
| 看板 | [本地入口](dashboard/index.html)、[使用与维护](docs/dashboard.md) |
| 范围与进度 | [后续路线](ROADMAP.md)、[变更记录](CHANGELOG.md)、[来源与使用说明](NOTICE.md) |

## 本地生成与浏览

在仓库根目录运行：

```bash
python3 scripts/build_dashboard.py
python3 -m http.server 8080 --directory dashboard
```

浏览器打开 `http://localhost:8080`。生成脚本使用 Python 标准库，校验目录结构后重建来源目录、方法地图和网页数据。看板使用静态 HTML、CSS、JavaScript，无需安装上游 Agent 或调用模型。

来源扩展、结论更新和页面生成仍由实际研究任务驱动；本轮没有设置后台定时采集。原文保留在上游，本仓保存原创分析、元数据与链接。个人 GitHub 仓库的创建和推送状态与看板托管独立记录，不因看板上线而自动完成。
