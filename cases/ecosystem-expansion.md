# 生态扩展：九个公开项目里的技能、工具与执行边界

检查日期：2026-10-21。本文新增九项公开来源，覆盖月之暗面、MiniMax、智谱、京东、快手、网易有道和上海人工智能实验室。月之暗面、MiniMax、智谱标为**模型公司**；上海人工智能实验室标为**研究机构**；京东、快手、网易标为**大厂**。这是研究范围的分类，不能把研究机构或模型公司直接计入“互联网大厂”的数量。

**验证深度：源码静态核对，未实跑。** 已读取每个项目的实现文件、许可和归属材料；没有安装上游依赖、执行上游脚本、调用模型或连接业务账户。下文“源码可见”表示固定提交中的行为；“文档说明”表示项目方给出的范围或承诺；“迁移建议”是本仓库的分析。文件全文留在上游，本仓库保存原创说明与固定链接。

## 按工程问题选读

| 工程问题 | 项目 | 身份与特别边界 |
| --- | --- | --- |
| 技能目录怎样进入真实 CLI 执行循环？ | Kimi CLI | 模型公司；研究的是已归档 Python 版 |
| 怎样把工程知识写成可交接、可验收的技能？ | MiniMax Skills | 模型公司；同时包含官方与社区条目 |
| 长时间运行的 API 怎样变成 Agent 工具？ | MiniMax MCP | 模型公司；适配层不包含宿主 Agent |
| 视觉模型怎样驱动手机操作？ | Open-AutoGLM | 模型公司；完成信号须与实际业务结果区分 |
| 规划和执行如何交接状态与产物？ | JoyAgent-JDGenie | 京东；固定默认 data_agent 分支 |
| 简单规划循环与能力评测怎么组织？ | KwaiAgents / KAgentSys-Lite | 快手；Lite 与论文完整版不同，许可含非商业条件 |
| 技能安装、启用、加载与运行时怎样对接？ | LobsterAI | 网易有道；底层运行时依赖 OpenClaw |
| 模型消息、历史与工具执行怎样分层？ | Lagent | 研究机构；基础 Agent 框架 |
| 并行搜索如何汇合答案和引用？ | MindSearch | 研究机构；保留图状态和来源映射 |

## 月之暗面 Kimi CLI：技能目录必须接进真实循环

**来源与版本。** [MoonshotAI 官方仓库](https://github.com/MoonshotAI/kimi-cli)固定提交为 `9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82`，主许可为 [Apache-2.0](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/LICENSE)。[NOTICE](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/NOTICE)明确 Moonshot AI 版权，并注明技能创建材料复用了 OpenAI Codex 的代码。[该提交 README](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/README.md)已将 Python 版标为归档，指向后继 MoonshotAI/kimi-code。因此本节是一个可阅读的历史实现，不是当前 Kimi Code 的安装指南或完整架构说明。

**输入与上下文，源码可见。** [Agent 装配器](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/soul/agent.py)读取工作目录信息、环境、项目 AGENTS.md 和技能目录，再生成系统提示词变量。[技能模块](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/skill/__init__.py)为每个技能保留名称、描述、路径及 Project、User、Extra、Built-in 四种作用域；同名技能按发现优先级只保留第一项。呈现给模型的是按作用域分组的索引，而不是所有技能正文。[系统模板](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/agents/default/system.md)要求在任务需要时读取正文，利用作用域区分用户说的“项目里的技能”和“用户级技能”。

**执行、回写与停止，源码可见。** [KimiSoul 执行循环](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/soul/kimisoul.py)将系统提示、当前历史和实际工具集合传给模型步骤函数，等待工具完成，再把助手消息与工具结果加入上下文。该回写过程使用异步取消保护，减少中断发生在消息追加中途的机会。每步前可触发上下文压缩，并保存检查点；模型调用有可重试错误分类和次数上限。没有工具调用、工具被拒绝、重复调用触发停止和步数耗尽是不同路径，不能统一写成“任务成功”。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [技能模块](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/skill/__init__.py)：看索引、作用域和正文读取 |
| 2 | [Agent 装配器](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/soul/agent.py)：看技能、项目规则、内置工具与 MCP 如何汇合 |
| 3 | [执行循环](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/soul/kimisoul.py)：沿模型调用、工具结果、上下文和停止原因阅读 |

**迁移建议与未验证事项。** 可以先给自己的技能索引增加“来源作用域”和“正文路径”，再记录每轮的明确停止原因。验证时分别观察同名技能覆盖、读取失败、工具拒绝与步数耗尽，不能只测一条正常对话。本轮没有验证技能命中率、压缩质量、断线恢复或检查点的真实效果；尤其不能把这份旧实现的结论直接套到后继 CLI。

## MiniMax Skills：把开发流程与产物验收写在一起

**来源与版本。** [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills)固定提交为 `60aaae52bb2af8162732751a4332f62a5fef518b`，[主许可](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/LICENSE)为 MIT，并明确 MiniMax 版权。[项目目录](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/README.md)区分 Official 与 Community 条目；[来源说明](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/CREDITS.md)列出 Anthropic、Expo 等上游材料。因此“官方组织维护”与“所有内容均为该公司原创”是两种不同结论。

**输入与上下文，技能正文可见。** [fullstack-dev 技能](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/fullstack-dev/SKILL.md)面向全栈开发需求，描述中同时列出触发范围与排除范围，正文先整理技术栈、服务类型、数据库、接口和认证需求，再做架构决策。用户已经给出的信息可以沿用。长文通过主题索引指向 API、认证、数据库与发布等参考资料。这个仓库提供知识包；宿主何时把清单、正文、文件或历史装入模型请求，要由所用 CLI 的实现另外确认。

**执行与完成，文档要求。** 技能要求宿主实施代码后完成构建、服务启动、接口检查和前后端连通验证，再交接运行命令、关键文件及未完成事项。[发布参考文件](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/fullstack-dev/references/release-checklist.md)进一步将需求对应到测试证据，并区分功能验收、非功能验收、部署准备与上线后验证。这里能学到的是产物标准的组织方式；文字中的“必须”不表示运行时已经强制检查。

**独立的技能包检查，源码可见。** [校验器](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/.claude/skills/pr-review/scripts/validate_skills.py)检查头部元数据、技能名与目录名是否一致、描述是否为空，并扫描若干凭据模式；许可与其他元数据缺失只是警告。它没有证明生成的应用满足需求，也不是完整的 YAML 解析器或语义审查系统。技能结构通过、宿主遵循了流程、产物验收通过，需要分别记录。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [全栈技能](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/fullstack-dev/SKILL.md)：触发边界、需求到交接的流程 |
| 2 | [发布检查表](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/fullstack-dev/references/release-checklist.md)：如何要求真实验收证据 |
| 3 | [校验脚本](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/.claude/skills/pr-review/scripts/validate_skills.py)：哪些规则已经程序化，哪些仍靠模型遵循 |

**迁移建议与未验证事项。** 为自己的技能补上三件事：何时不用、要交付什么、什么证据算完成。对元数据做小而明确的程序检查，对业务结果另设验收。本轮只读代表性技能和校验器，未执行它们，未审查仓库全部条目，也没有据技能措辞推断代码质量提升。

## MiniMax MCP：受理任务、处理中和产物就绪应当分开

**来源与版本。** [MiniMax 官方 MCP 指南](https://platform.minimax.io/docs/guides/mcp-guide)直接链接 Python 与 JavaScript 实现；本节研究 [Python 仓库](https://github.com/MiniMax-AI/MiniMax-MCP)的 `0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a`，许可为 [MIT](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/LICENSE)。检查日官方指南与 README 均建议优先考虑 MiniMax CLI；这里保留的是 MCP 适配层的工程拆解。

**输入与上下文，源码可见。** 输入是宿主选定的工具及参数，例如视频提示、首帧、时长和返回目录。[server.py](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/minimax_mcp/server.py)通过工具声明把参数含义与异步使用方式提供给 MCP 客户端；宿主 Agent 的系统提示词、技能选择和会话历史不在这个服务中。[API 客户端](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/minimax_mcp/client.py)处理鉴权、HTTP 错误与服务业务错误，异常信息可携带 Trace-Id，便于对照服务端请求。

**执行与结果，源码可见。** 视频生成先提交得到 task_id（任务编号）。异步模式立即返回编号，并指引后续调用查询工具；查询区分处理未完成、失败和成功。成功后再取 file_id（文件编号）、获取下载地址，并按资源模式返回远程 URL 或保存到本地。同步模式在服务内轮询，但不能把“轮询次数有限”解释为严格的墙钟时间上限，因为所读客户端没有统一设置网络请求超时。

**完成与错误的边界。** 在所读视频路径中，成功和失败都可能以 TextContent（文本内容）返回。宿主应检查状态语义及真实产物，不能只把“工具返回了一段文字”视为成功。API 请求成功、生成任务成功、结果文件已取得、文件内容符合用户要求，是四个不同的阶段；该适配层主要覆盖前三者。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [配置文档](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/README-CN.md)：宿主接入与 URL／本地资源模式 |
| 2 | [工具实现](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/minimax_mcp/server.py)：generate_video 和 query_video_generation 的完整状态路径 |
| 3 | [请求封装](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/minimax_mcp/client.py)：鉴权、服务错误和追踪编号 |

**迁移建议与未验证事项。** 将自己的长任务工具设计成“提交返回任务编号—查询返回状态—成功后取产物”，并为宿主提供稳定的机器可读状态。后一项是本仓库的改进建议，不是该版本所有工具已经实现的事实。本轮没有调用 API、产生媒体或验证真实超时与重试表现。

## 智谱 Open-AutoGLM：通过下一张截图闭合操作回路

**来源与版本。** [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)的 [README](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/README.md)把项目与智谱 AI 产品、BigModel 和 ZhipuAI 模型发布对应起来。固定提交为 `86f55382982fb054e8fc98ca80609dff8a2cdc3c`，源码主许可为 [Apache-2.0](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/LICENSE)；README 还单独链接 [部署与使用规范](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/resources/privacy_policy.txt)。模型权重和外部设备组件的许可不能仅凭源码 LICENSE 一并推断。

**输入与模型调用前的上下文，源码可见。** [PhoneAgent](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/agent.py)接收自然语言任务，每步取得当前应用与屏幕截图。首步加入系统规则、任务和截图；以后追加当前屏幕信息。模型返回后，程序从刚才的用户消息移除图像，继续保留文本和动作历史，因此后续步骤主要观察最新截图，而非无限累积所有历史图像。

**执行与反馈，源码可见。** [动作处理器](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/actions/handler.py)把模型给出的动作名映射到有限处理函数，转换归一化坐标，再调用设备适配层。通常的动作参数通过 AST（抽象语法树）读取字面量，而非直接求值执行模型文本。点击动作含有 message 时进入确认回调；登录或验证码等场景可以进入人工接管回调。动作结果返回 StepResult，但主循环没有把每次 ActionResult 都作为标准工具消息追加，下一张截图是主要观察反馈。

**完成不能只看结束标志。** 源码分别保留 success（本步是否成功）与 finished（是否结束）。模型错误会结束流程，动作文本无法解析也会转成 finish；超过最大步数则返回对应说明。由此可见，“循环已经停下”与“真实界面完成目标”必须另行判断。确认回调也依赖动作被正确标记，不能据此声称执行器独立识别了所有敏感业务操作。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [主循环](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/agent.py)：最新截图、历史清理与停止分支 |
| 2 | [动作处理器](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/actions/handler.py)：解析、分派、坐标与人工接管 |
| 3 | [部署规范](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/resources/privacy_policy.txt)：区分本地执行、云端模型及数据流向 |

**迁移建议与未验证事项。** 为视觉 Agent 保留“动作前界面—动作—动作后界面”的验收证据，并把失败原因和结束状态分字段表达。若实际任务需要确认，应在执行层建立能独立检查的规则。本轮未连接设备、运行 ADB/HDC、测试 iOS 或测量任务完成率；不代表智谱闭源产品的完整实现。

## 京东 JoyAgent-JDGenie：规划器与执行器共享产物，不必共享全部职责

**来源与版本。** [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie)在 [README](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/README.md)明确列出所属京东企业信息化、协同办公与物流数据团队。固定的是默认 `data_agent` 分支提交 `2417e0b8b636d941ad5fb14c59b20dddfef5375d`，许可为 [Apache-2.0](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/LICENSE)。分支名属于证据的一部分，不能把其他分支或技术报告中的系统能力自动拼到本条记录。

**输入与上下文，源码可见。** [规划器](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/PlanningAgent.java)和 [执行器](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/ExecutorAgent.java)都从当前工具集合生成名称与描述概要，并注入原任务、日期、SOP（标准作业流程）及已有产物。提示词保留初始快照，每轮替换动态文件信息。规划器自己的可用工具主要是计划管理；执行器拿到的是业务工具集合，因此两者知道的能力范围与可实际操作的对象有清晰分工。

**执行、回传与产物，源码可见。** [基础执行器](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/BaseAgent.java)可并发运行同一轮工具调用，用调用编号汇总结果；执行器再按原调用逐个写回记忆。原生函数调用模式生成带调用 ID 的工具消息，结构解析模式则把结果附加在上一条助手消息中。输出给界面的计划、任务、工具结果和任务摘要有不同事件类型；工具正文可按配置截断。

**停止与失败的边界。** 执行器没有新的工具调用时结束当前子任务；规划器检查计划状态，并返回下一任务或结束。[计划工具](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/tool/common/PlanningTool.java)本身允许标记步骤，也允许 finish 将步骤置为 completed。计划全部完成是一个状态条件，并不是独立验证产物内容的证明。工具异常会转成错误文字；达到步数上限会返回终止说明，业务级重试或补偿需要在具体工具中另查。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [PlanningAgent](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/PlanningAgent.java)：规划上下文与下一任务 |
| 2 | [ExecutorAgent](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/ExecutorAgent.java)：工具结果与任务摘要 |
| 3 | [BaseAgent](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/BaseAgent.java)、[PlanningTool](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/tool/common/PlanningTool.java)：并发关联、异常与计划状态 |

**迁移建议与未验证事项。** 在自己的多 Agent 系统里先统一任务 ID、工具调用 ID、产物列表和结束原因，再决定是否需要更多角色。为“completed”补一个可查询的产物验收证据，避免把规划器的自报完成当成最终标准。本轮没有启动整套服务、生成报告或复核 README 中的排行榜数字。

## 快手 KwaiAgents：轻量规划循环与论文完整版要分开读

**来源与版本。** [KwaiKEG/KwaiAgents](https://github.com/KwaiKEG/KwaiAgents)的 [README](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/README.md)明确说明项目来自快手 KwaiKEG。固定提交为 `3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c`。主 [LICENSE.txt](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/LICENSE.txt)是 **CC-BY-NC-SA-4.0**，包含非商业和相同方式共享条件；它不能被笼统归入 MIT/Apache 式的可商用代码。

**公开范围，文档说明。** 仓库提供 KAgentSys-Lite、模型、数据与评测相关材料。README 明确 Lite 版比论文系统工具少、没有完整版记忆机制，并从 BabyAGI、Auto-GPT 等项目演进而来。该说明约束的是所公开系统与论文完整版的关系，不能把论文中所有能力都算作当前源码可运行能力。

**输入与上下文，源码可见。** [轻量 Agent](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/agents/kagent.py)会将最近三轮对话和已完成任务及其结果拼成文本；[提示词模块](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/agents/prompts.py)再组合角色说明、目标、当前时间、工具描述与这份历史。也就是说，缺少论文中的专门记忆机制，并不等于完全不使用历史。[工具描述转换器](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/utils/function_utils.py)从函数说明提取参数含义，降低提示词和工具接口分别维护的成本。

**执行、完成与评测，源码可见。** 循环每次规划一个任务，解析 JSON，按名字选择本地工具执行，再将结果加入已完成任务列表，最后用独立总结提示生成回答。工具异常常返回空字符串；结束路径包括结束工具、无需工具、未知工具以及迭代上限。[评测实现](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/benchmark/benchmark_eval.py)进一步按工具名精确匹配与参数、规划文本的 ROUGE 相似度等计算指标。这有助于定位接口选择或参数问题，但不等同于真实环境里的端到端业务完成率。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [KAgentSys-Lite](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/agents/kagent.py)：任务循环、历史和错误返回 |
| 2 | [提示词构造](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/agents/prompts.py)、[工具说明转换](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/utils/function_utils.py)：上下文如何组装 |
| 3 | [细粒度评分](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/benchmark/benchmark_eval.py)：判断到底测的是文本、工具还是任务结果 |

**迁移建议与未验证事项。** 可借鉴“每步一项可执行任务—明确记录工具结果—再规划”的最小闭环，并为工具错误提供结构化信息。评测同时保留参数正确性与真实任务完成性，避免只优化文本匹配。该快照较早，本轮未验证旧依赖、搜索服务和模型接口在检查日仍可运行，也不据历史表格推断今天的能力排名。

## 网易有道 LobsterAI：技能管理是产品层与运行时之间的一份契约

**来源与版本。** [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)固定提交为 `b649d5c80f25887e6d0c1ff04024150f7476da5d`。[中文 README](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/README_zh.md)明确由网易有道开发维护，[MIT 许可](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/LICENSE)列有 NetEase Youdao 版权。README 同时说明 Cowork 是产品和会话层，OpenClaw 是底层运行时与网关，后者执行 Agent 任务。本文研究技能管理和协议桥接，不把 OpenClaw、第三方插件及内置衍生技能的能力全部算作网易原创。

**输入与上下文，源码可见。** [技能管理器](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/main/skills/skillManager.ts)解析技能目录，分别保存名称、描述、正文、路径、启用状态和加载问题。自动路由提示只列出已启用技能的名称、描述和位置，要求先读取最相关的一份正文，再沿正文引用继续读取；相对路径以技能目录为基准。[会话提示构造器](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/renderer/components/cowork/skillSystemPrompt.ts)将技能提示与基础提示拼接，并对继续会话时是否存在技能提示做分支处理。这些是进入引擎前的产品层准备，不等于完整模型请求已经在此处可见。

**执行与状态，源码可见。** 安装路径会先尝试扫描技能；发现风险时保存待确认记录并设置过期清理，安装完成后通知界面和运行时同步方。[批准协议桥](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/main/libs/agentEngine/openclawApprovalBridge.ts)把执行或插件请求转成统一权限请求，并把用户决策映射为一次允许、持续允许或拒绝，保留请求、会话及工具调用关联。这里的产物是可供运行时使用的技能状态与批准决策；真实工作文件和任务成功条件还要进入 OpenClaw 及具体工具继续追踪。

**必须保留的实现边界。** 该安装路径捕获扫描异常后会继续安装，所以“提供扫描器”不能写成“任何扫描失败都会阻断”。批准解析也存在自动批准分支，不能宣称每条命令都会人工确认。技能的 isOfficial 字段来自头部元数据，只是包内声明，不能代替本仓库对公司归属的外部核实。这些判断都来自上述固定实现，不是对整个产品安全性的评定。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [SkillManager](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/main/skills/skillManager.ts)：安装、启用、元数据、按需目录与失败策略 |
| 2 | [提示词拼接](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/renderer/components/cowork/skillSystemPrompt.ts)：技能与基础规则如何组合 |
| 3 | [运行时批准桥](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/main/libs/agentEngine/openclawApprovalBridge.ts)：产品决策如何关联到具体调用 |

**迁移建议与未验证事项。** 把“已安装”“已启用”“能加载”“已获执行批准”作为不同状态记录，并在界面说明失败原因。决定扫描器不可用时采用何种策略，应明确写在实现和测试条件里。本轮未安装桌面应用、启动网关、连接 IM/MCP 或完整审计内置技能，不能宣称已验证完整任务链。

## 上海人工智能实验室 Lagent：消息、记忆、解析与执行分别建模

**来源与版本。** [上海人工智能实验室官方公告](https://www.shlab.org.cn/news/5443477)直接介绍并链接 Lagent；[InternLM 官方组织页面](https://github.com/InternLM)也明确研究机构身份。[Lagent](https://github.com/InternLM/lagent)固定提交为 `0ab2e2f550477884743cd63fbca7bc4aa7b00290`，使用 [Apache-2.0](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/LICENSE)。研究机构案例用来比较工程方法，不计入互联网大厂项目。

**输入与上下文，源码可见。** [基础 Agent](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/agents/agent.py)以 AgentMessage（统一消息对象）接收输入，在调用前后更新按 session_id（会话编号）区分的记忆。聚合器把历史、系统模板和输出格式要求转换为模型请求，解析器再把返回文本转成格式化结果。[ReAct 实现](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/agents/react.py)把工具说明放入选择动作的模板，使模型的选择范围与执行器拥有的能力保持对应。

**执行、错误与停止，源码可见。** [动作执行器](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/actions/action_executor.py)按工具名及方法名分派；[动作前后处理钩子](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/hooks/action_preprocessor.py)负责把模型格式转成工具参数，再把成功结果或错误信息转换回消息文本。ReAct 在“选择动作—执行动作”之间循环，默认检查消息正文或格式化结果中是否出现 conclusion；达到最大轮数也会返回最后消息。因此，消息协议、工具成功状态、循环结束条件与业务验收仍是四层不同问题。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [Agent](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/agents/agent.py)：会话记忆、模型输入聚合、输出解析 |
| 2 | [ReAct](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/agents/react.py)：选择与执行循环 |
| 3 | [ActionExecutor](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/actions/action_executor.py)、[处理钩子](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/hooks/action_preprocessor.py)：接口适配与错误回传 |

**迁移建议与未验证事项。** 如果一个 Agent 函数同时做历史管理、提示词、解析、工具调用和重试，可先拆出统一消息对象与动作执行器，再给停止条件单独命名。这更容易判断失败发生在模型、格式还是工具一层。本轮未运行教程、验证中断恢复或覆盖全部 Agent 类型；钩子存在也不意味着业务幂等、重试与回滚已经实现。

## 上海人工智能实验室 MindSearch：并发搜索需要统一引用与可检查的图状态

**来源与版本。** [InternLM/MindSearch](https://github.com/InternLM/MindSearch)由同一研究机构的官方组织发布，[Apache-2.0 许可](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/LICENSE)明确 Shanghai AI Laboratory 版权。固定提交为 `7952c5f8a956fe6a44228a6a7d528a35340e7c87`。[中文 README](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/README_zh-CN.md)注明展示评测的实验完成于 2024 年 7 月 7 日之前，本条不把这组历史结果写成今天的搜索质量比较。

**输入与上下文，源码可见。** [提示词文件](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/mindsearch_prompt.py)分开规定搜索器、规划器和汇总器的职责：搜索器回答单一子问题并标引用，规划器构造搜索图，汇总器根据已有问答整理结果。[图实现](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/graph.py)为子搜索器构造当前子问题、主问题等输入，并为任务保存独立会话状态。父节点历史有对应输入模板，但其实际传递还存在下述静态疑点。

**执行、结果与完成，源码可见。** 规划器生成图操作代码，ExecutionAction（图操作执行器）执行后把搜索任务提交给线程池或异步事件循环；队列逐步返回节点回答、记忆和状态。[主搜索 Agent](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/mindsearch_agent.py)汇集各节点结果，把节点内部引用重新编号，保存 ref2url（引用编号到来源地址的映射），避免不同子任务都使用“1号来源”而发生混淆。出现回复节点时再触发最终汇总；没有工具调用也有结束路径。源码保存的是可检查的搜索轨迹，不是自动证明回答事实正确。

**阅读调用链发现的两个边界。** 首先，图执行器在当前 Python 进程直接 exec 模型生成的代码，本文件没有隔离沙箱。其次，add_edge 将邻接边保存为字典，而 add_node 查找父节点时把节点名与整个边对象比较；仅凭“带历史”参数和图示，不能认定父节点答案已正确进入子搜索器。引用合并还依赖节点记忆中特定位置的工具消息。这些是固定快照的静态观察，需专门实验才能确认运行影响；本轮没有替上游修改或运行验证。

| 阅读顺序 | 具体文件与用途 |
| --- | --- |
| 1 | [角色提示词](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/mindsearch_prompt.py)：单一子问题、图操作与引用要求 |
| 2 | [图与搜索任务](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/graph.py)：并发、节点状态、异常传播与父信息传递 |
| 3 | [结果汇合](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/mindsearch_agent.py)：引用重排、图状态与最终回答 |

**迁移建议与未验证事项。** 构建研究 Agent 时，可以先为子任务结果设计“问题、回答、来源映射、执行状态”的稳定结构，再合并引用。若选择执行模型生成的程序，还需要独立设计执行边界。父子任务依赖、引用正确性和异常恢复应作为具体实验问题；本文没有运行搜索引擎、模型或图执行器，也不承诺并发一定提升回答质量。

## 跨项目可以带走的四个检查问题

1. **上下文的哪个部分是常驻，哪个部分按需加载？** Kimi CLI 与 LobsterAI 都展示了技能索引和正文的分工；MiniMax Skills 本身只提供知识包，加载行为取决于宿主。
2. **模型输出是怎样变成实际动作的？** Open-AutoGLM 走有限动作与设备适配，Lagent 走解析器和动作执行器，MiniMax MCP 走参数化 API；这些路径的错误反馈方式并不一样。
3. **什么事件只代表流程结束，什么证据代表目标达成？** 无工具调用、计划全 completed、finish、最大轮数、API 已受理，都不应未经检查便当成业务成功。
4. **公开材料承诺了什么，当前源码又实现了什么？** 归档状态、Lite 版本、依赖上游、扫描失败策略和参数结构差异，都是研究结论的一部分。

这些问题是本文的迁移建议，具体依据在各项目章节。后续实验应保存任务输入、固定版本、实际消息、工具返回及产物验收证据，再讨论收益。

## 后续线索：有官方入口，但本轮未拆解实现

| 线索 | 已确认的出处 | 本轮边界 |
| --- | --- | --- |
| 后继 Kimi Code CLI | [归档 README](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/README.md)指向 [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | 未读取后继实现，不以旧 Python 版代替 |
| MiniMax CLI | [官方 MCP README](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/README-CN.md)指向 [MiniMax-AI/cli](https://github.com/MiniMax-AI/cli) | 只确认官方推荐与链接，未作为新增源码证据计数 |

本轮正式来源均有可读实现与归属依据；没有把第三方目录中的公司名称或只有新闻宣传的项目充当正式源码证据。完整来源记录供主目录合并时使用，包含九项固定提交、五十个已读材料入口、分类、许可与未验证范围。

