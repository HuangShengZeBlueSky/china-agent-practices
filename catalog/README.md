# 来源目录

检查日期：2026-10-21。共 35 条研究记录。每条按研究主题组织，同一仓库可支持多个主题，因此条目数不等于独立仓库数。

全部为静态阅读；具体覆盖范围见文件记录。完整第三方技能路径索引在 [archive-skill-index.json](archive-skill-index.json)，不计入逐篇深读数量。

| 项目 | 组织 / 来源 | 重点 | 中文拆解 |
| --- | --- | --- | --- |
| [飞书 Lark CLI](https://github.com/larksuite/cli) | 字节跳动 · 官方源码 | 把业务快捷命令、标准 API 与通用调用分层，配合权限、风险和结果契约。 | [阅读](../cases/bytedance-lark.md) |
| [飞书官方 Skills](https://github.com/larksuite/cli/tree/017b19a793ad71794a02887ede04757f3d82e10d/skills) | 字节跳动 · 官方源码 | 先解析真实业务对象，再按依赖执行；把技能路由与详细操作参考分开。 | [阅读](../cases/bytedance-lark.md) |
| [Eino 技能中间件](https://github.com/cloudwego/eino) | 字节跳动 · 官方源码 | 先提供技能目录，再按需读取正文；子任务可选择独立或继承父上下文。 | [阅读](../cases/bytedance-lark.md) |
| [Trae Agent](https://github.com/bytedance/trae-agent) | 字节跳动 · 官方源码 | 公开编码 Agent 的任务提示、工具循环、轨迹记录和结束信号。 | [阅读](../cases/bytedance-lark.md) |
| [豆包 Base 技能归档](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/tree/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base) | 跨平台第三方归档 · 第三方归档 | 第三方保存的 Base 1.5.1：从业务建模、字段设计到写入和回读验收。 | [阅读](../cases/bytedance-lark.md) |
| [豆包企业搜索归档](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/doubao-enterprise-search/SKILL.md) | 跨平台第三方归档 · 第三方归档 | 保留搜索的主体、时间与比较条件，并区分知识检索和已知对象操作。 | [阅读](../cases/bytedance-lark.md) |
| [Qwen Code](https://github.com/QwenLM/qwen-code) | 阿里巴巴 · 官方源码 | 依据会话工具声明快照筛选相关指引，技能目录与正文采用不同加载策略。 | [阅读](../cases/alibaba-tencent.md) |
| [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | 阿里巴巴 · 官方源码 | 把检索、模型适配、函数调用协议和工具执行连接到消息列表。 | [阅读](../cases/alibaba-tencent.md) |
| [AgentScope](https://github.com/agentscope-ai/agentscope) | 阿里巴巴 · 官方源码 | 让工具组与技能一起受能力启用状态约束，再装配说明、记忆和历史。 | [阅读](../cases/alibaba-tencent.md) |
| [CloudBase AI Toolkit](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) | 腾讯 · 官方源码 | 业务技能逐层路由到参考资料，CLI 与 MCP 互补，并维护经验规则的入库门槛。 | [阅读](../cases/alibaba-tencent.md) |
| [CodeBuddy / WorkBuddy 文档](https://www.codebuddy.cn/docs/cli/skills) | 腾讯 · 官方文档 | 官方文档说明技能描述、工具限制、子上下文和分发方式。 | [阅读](../cases/alibaba-tencent.md) |
| [百度 AppBuilder SDK](https://github.com/baidubce/app-builder) | 百度 · 官方源码 | 云端发出工具调用后暂停，本地执行函数，再按调用编号回传继续运行。 | [阅读](../cases/baidu-huawei-meituan-xiaomi.md) |
| [华为 openJiuwen](https://github.com/openJiuwen-ai/agent-core) | 华为 · 官方源码 | 用技能元数据建立入口，正文通过读取工具加载；文档与实际代码存在接口差异。 | [阅读](../cases/baidu-huawei-meituan-xiaomi.md) |
| [美团 VitaBench 1.0](https://github.com/meituan-longcat/vitabench) | 美团 · 官方源码 | 工具声明前后条件与读写类型，并用独立评分提示评价完整任务轨迹。 | [阅读](../cases/baidu-huawei-meituan-xiaomi.md) |
| [小米 mimoagent](https://github.com/XiaomiMiMo/mimoagent) | 小米 · 官方源码 | 把模型、Agent、环境和评分拆开，工具说明明确子进程、并发、超时和退出码。 | [阅读](../cases/baidu-huawei-meituan-xiaomi.md) |
| [Coze Studio](https://github.com/coze-dev/coze-studio) | 字节跳动 · 官方源码 | 把人设、变量、检索结果和工具配置装配成可执行 Agent 图。 | [阅读](../cases/platforms-expansion.md) |
| [Coze Loop](https://github.com/coze-dev/coze-loop) | 字节跳动 · 官方源码 | 把提示词评估拆成输入校验、模板渲染、模型调用、结果解析和可追踪版本。 | [阅读](../cases/platforms-expansion.md) |
| [DeerFlow 2.x](https://github.com/bytedance/deer-flow) | 字节跳动 · 官方源码 | 按运行配置拼装提示词与技能入口，并对工具大结果建立外置文件和上下文预算。 | [阅读](../cases/platforms-expansion.md) |
| [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop) | 字节跳动 · 官方源码 | 用明确的 GUI 动作语法把模型输出转成操作，再将新截图作为下一轮观察。 | [阅读](../cases/platforms-expansion.md) |
| [AgentScope Runtime](https://github.com/agentscope-ai/agentscope-runtime) | 阿里巴巴 · 官方源码 | 将 Agent 查询函数包装成带生命周期、流式响应、中断和协议适配的服务。 | [阅读](../cases/platforms-expansion.md) |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 阿里巴巴 · 官方源码 | 将沙箱命令执行划分为前台、后台与持久会话，并显式处理状态、日志和重试语义。 | [阅读](../cases/platforms-expansion.md) |
| [AWorld CLI](https://github.com/inclusionAI/AWorld) | 蚂蚁集团 · 官方源码 | 用显式规则选择技能，并把会话压缩、工作区信息和检查点状态纳入 CLI 上下文管理。 | [阅读](../cases/platforms-expansion.md) |
| [BrowserSkill](https://github.com/Tencent/BrowserSkill) | 腾讯 · 官方源码 | 把浏览器任务组织成观察、引用元素、操作、再观察的流程，并维护 Skill 安装来源。 | [阅读](../cases/platforms-expansion.md) |
| [Tencent RTC Skills](https://github.com/Tencent-RTC/agent-skills) | 腾讯 · 官方源码 | 以路由 Skill、产品 Skill、会话状态工具和独立评估提示组织 SDK 集成知识。 | [阅读](../cases/platforms-expansion.md) |
| [SkillHub 官方 Skills](https://github.com/Tencent/skillhub) | 腾讯 · 官方源码 | 公开技能发现流程和包质量评估模板，用程序检查报告格式与分数字段。 | [阅读](../cases/platforms-expansion.md) |
| [Kimi CLI · 历史 Python 版](https://github.com/MoonshotAI/kimi-cli) | 月之暗面 · 官方源码 | 用带作用域的技能索引、项目说明和工具集合组装 CLI 上下文，并在可观察的多步循环中持久化消息与停止原因。 | [阅读](../cases/ecosystem-expansion.md) |
| [MiniMax Skills](https://github.com/MiniMax-AI/skills) | MiniMax · 官方源码 | 把全栈开发拆成需求、架构、实施、验证与交接流程，并用独立脚本检查技能元数据和部分凭据模式。 | [阅读](../cases/ecosystem-expansion.md) |
| [MiniMax MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | MiniMax · 官方源码 | 把多模态服务包装为 MCP 工具，视频任务以 task_id 连接提交、查询、结果下载，并区分 API 与文件处理错误。 | [阅读](../cases/ecosystem-expansion.md) |
| [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | 智谱 · 官方源码 | 手机界面与任务组成多模态输入，模型给出有限动作，设备适配层执行，再用新截图继续观察。 | [阅读](../cases/ecosystem-expansion.md) |
| [JoyAgent-JDGenie](https://github.com/jd-opensource/joyagent-jdgenie) | 京东 · 官方源码 | 规划 Agent 管理结构化计划，执行 Agent 使用业务工具；两者根据真实工具列表、任务、日期、SOP 和已有产物组装提示词。 | [阅读](../cases/ecosystem-expansion.md) |
| [KwaiAgents Lite](https://github.com/KwaiKEG/KwaiAgents) | 快手 · 官方源码 | 以单任务规划—工具执行—结果记录循环完成信息检索；评测代码分别核对工具名、参数和规划文本。 | [阅读](../cases/ecosystem-expansion.md) |
| [LobsterAI](https://github.com/netease-youdao/LobsterAI) | 网易 · 官方源码 | 桌面产品层维护技能启用、路径和安装状态，生成按需读取目录，并把授权请求转换为 OpenClaw 运行时可处理的决策。 | [阅读](../cases/ecosystem-expansion.md) |
| [Lagent](https://github.com/InternLM/lagent) | 上海人工智能实验室 · 官方源码 | 把 Agent 封装为统一消息接口，用独立会话记忆、消息聚合器、格式解析器与动作执行器连接模型和工具。 | [阅读](../cases/ecosystem-expansion.md) |
| [MindSearch](https://github.com/InternLM/MindSearch) | 上海人工智能实验室 · 官方源码 | 规划器生成搜索图操作，子搜索器并发搜集并留下节点状态与记忆，最后统一引用编号并汇总回答。 | [阅读](../cases/ecosystem-expansion.md) |
| [归档采集与代表技能](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills) | 跨平台第三方归档 · 第三方归档 | 拆开本地文件同步、索引生成、变更归档与模型学习总结，并比较六个技能样本。 | [阅读](../cases/archive-collection-method.md) |

## Lark CLI（飞书命令行工具）

来源类型：官方源码。检查日：2026-10-21。固定提交：`017b19a793ad71794a02887ede04757f3d82e10d`。

许可：MIT

**学习重点：** 设计 CLI 时一起写适用场景、参数结构、返回语义与失败后的下一步。

具体阅读材料：

- [README.zh.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/README.zh.md)：项目定位与三层命令入口
- [AGENTS.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/AGENTS.md)：参数结构、适用指引、Skill 与参考资料的知识分工
- [affordance/contact.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/affordance/contact.md)：联系人相关命令何时使用与怎样选择
- [internal/schema/types.go](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/internal/schema/types.go)：工具参数、身份、权限与风险契约的数据结构
- [extension/command/definition.go](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/extension/command/definition.go)：扩展命令如何注册与提供元数据
- [extension/command/result_protocol.go](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/extension/command/result_protocol.go)：成功、失败和批处理部分成功的返回协议
- [errs/ERROR_CONTRACT.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/errs/ERROR_CONTRACT.md)：类型化错误、退出码与恢复信息约定

证据边界：

- 固定代码快照；官方身份由飞书官网与开放平台交叉确认。未执行 CLI 或验证任务成功率。

## Lark CLI 官方技能与技能创建指南

来源类型：官方源码。检查日：2026-10-21。固定提交：`017b19a793ad71794a02887ede04757f3d82e10d`。

许可：MIT

**学习重点：** 按触发条件、职责范围、对象解析、执行与回读验收写一个业务技能。

具体阅读材料：

- [skills/lark-base/SKILL.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/skills/lark-base/SKILL.md)：Base 1.2.23 的职责、对象解析、操作与验证流程
- [skills/lark-skill-maker/SKILL.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/skills/lark-skill-maker/SKILL.md)：怎样写技能路由、依赖和参考资料
- [skills/lark-workflow-standup-report/SKILL.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/skills/lark-workflow-standup-report/SKILL.md)：小型站会工作流如何串联真实业务对象

证据边界：

- 官方 Base 技能在此提交为 1.2.23，不是第三方归档 1.5.1；技能文件规定的行为不保证所有宿主都会遵守。

## Eino Skill Middleware（技能加载中间件）

来源类型：官方源码。检查日：2026-10-21。固定提交：`0a5ca53b9d3bf7b661dccc863465ec568a421eea`。

许可：Apache-2.0

**学习重点：** 记录一次技能激活前后具体增加的模型消息，验证子任务拿到的信息是否足够。

具体阅读材料：

- [adk/middlewares/skill/skill.go](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/adk/middlewares/skill/skill.go)：元数据列表、正文加载与子任务上下文分支
- [adk/middlewares/skill/prompt.go](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/adk/middlewares/skill/prompt.go)：目录和加载结果怎样进入模型可见文本
- [adk/middlewares/skill/filesystem_backend.go](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/adk/middlewares/skill/filesystem_backend.go)：文件系统技能后端的索引与正文读取

证据边界：

- 公开框架实现，不代表豆包等闭源产品当前完整架构。默认独立子任务不自动携带父任务全部信息；尚未运行例程。

## Trae Agent（公开软件工程智能体）

来源类型：官方源码。检查日：2026-10-21。固定提交：`e839e559ac61bdd0e057c375dd1dee391fee797d`。

许可：MIT

**学习重点：** 把“模型说完成”和“产物通过验证”拆成两个可观察状态。

具体阅读材料：

- [trae_agent/prompt/agent_prompt.py](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/prompt/agent_prompt.py)：编码任务的系统提示与工作要求
- [trae_agent/agent/trae_agent.py](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/agent/trae_agent.py)：任务、项目根目录和工具如何加入 Agent
- [trae_agent/agent/base_agent.py](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/agent/base_agent.py)：模型与工具循环、消息历史和轨迹
- [trae_agent/tools/base.py](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/tools/base.py)：工具定义与执行接口
- [trae_agent/tools/task_done_tool.py](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/tools/task_done_tool.py)：任务结束工具的实现和验证边界
- [trae_agent/utils/llm_clients/llm_client.py](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/utils/llm_clients/llm_client.py)：模型客户端的请求和响应适配

证据边界：

- 不是 Trae 商业客户端或 SOLO 完整源码。完成工具描述要求验证，但函数本身并不校验所有测试通过。未运行模型或评测。

## lark-base 1.5.1 与 Base 系统搭建指引

来源类型：第三方归档。检查日：2026-10-21。固定提交：`1c9239cc90585f57d9e06d32deffc017bbff5802`。

许可：未发现根目录许可；GitHub 许可元数据为空；不镜像原文

**学习重点：** 比较官方与归档的职责差异，学习业务设计流程，不按版本号猜测线上部署。

具体阅读材料：

- [README-doubao.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-doubao.md)：作者对豆包材料本地来源的说明
- [doubao/skills/lark-base/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base/SKILL.md)：第三方归档 Base 1.5.1 的职责与依赖
- [doubao/skills/lark-base/references/lark-base-solution-design.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base/references/lark-base-solution-design.md)：从业务建模到字段、公式与验收的设计流程

证据边界：

- 归档作者自述从本地豆包目录同步，无法独立证明官方发行来源、完整性或当前在用。与官方 Base Skill 的版本及应用模式边界不同。

## doubao-enterprise-search（企业搜索技能归档）

来源类型：第三方归档。检查日：2026-10-21。固定提交：`1c9239cc90585f57d9e06d32deffc017bbff5802`。

许可：未发现根目录许可；GitHub 许可元数据为空；不镜像原文

**学习重点：** 把检索约束显式写入任务表示；搜索无结果时记录范围而非推断事实不存在。

具体阅读材料：

- [doubao/skills/doubao-enterprise-search/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/doubao-enterprise-search/SKILL.md)：企业检索的范围保留、路由和无结果解释

证据边界：

- 仅证实公开归档文本存在，无法确认与用户此前执行轨迹同版，也未获得服务端系统提示词与检索实现。

## Qwen Code

来源类型：官方源码。检查日：2026-10-21。固定提交：`461be87304c7b3b5d64b701207c49f236515d5fd`。

许可：Apache-2.0

**学习重点：** 画出系统提示、启动消息、增量技能消息与工具返回的实际装配位置。

具体阅读材料：

- [packages/core/src/core/prompts.ts](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/packages/core/src/core/prompts.ts)：提示词装配与会话工具声明快照门控
- [packages/core/src/tools/skill.ts](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/packages/core/src/tools/skill.ts)：技能正文加载工具与激活结果
- [packages/core/src/tools/skill-utils.ts](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/packages/core/src/tools/skill-utils.ts)：技能发现、目录与元数据辅助逻辑
- [docs/design/2026-09-18-resident-tool-prompt-assembly.zh-CN.md](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/docs/design/2026-09-18-resident-tool-prompt-assembly.zh-CN.md)：静态工具声明、消息与缓存的设计边界

证据边界：

- 已读相关源码和设计文档，未安装或执行。
- 项目最初基于 Gemini CLI，不能把全部设计归为阿里原创。
- 设计稿含历史版本与待决事项，不能一概视为已部署机制。
- 未实测缓存、费用或成功率收益。

## Qwen-Agent

来源类型：官方源码。检查日：2026-10-21。固定提交：`31a4d36d123688581a9e9744427272b33ce940e0`。

许可：Apache-2.0

**学习重点：** 分别追踪谁执行检索，以及检索结果被插入哪一种消息。

具体阅读材料：

- [qwen_agent/agents/assistant.py](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/agents/assistant.py)：检索模块调用与参考内容注入位置
- [qwen_agent/agents/fncall_agent.py](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/agents/fncall_agent.py)：函数调用循环与工具结果写回
- [qwen_agent/tools/base.py](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/tools/base.py)：工具 schema 与参数校验基类
- [qwen_agent/llm/function_calling.py](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/llm/function_calling.py)：模型函数调用协议适配
- [qwen_agent/llm/fncall_prompts/nous_fncall_prompt.py](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/llm/fncall_prompts/nous_fncall_prompt.py)：Nous 函数调用提示与格式约定
- [qwen_agent/agent.py](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/agent.py)：基础消息、会话与工具调用接口

证据边界：

- 已读相关源码，未实跑检索或模型调用。
- 固定提交默认函数调用格式为 nous，不应把 qwen_fncall_prompt.py 误称为默认。
- 原始接口模式可以跳过提示词适配。
- 工具基类的校验辅助方法需被具体工具正确使用。

## AgentScope

来源类型：官方源码。检查日：2026-10-21。固定提交：`b2a084799bf883a5a8d0f56e44f205f78a83f0fe`。

许可：Apache-2.0

**学习重点：** 把可见、可调用与已启用能力统一建模，避免提示词与执行器各自维护名单。

具体阅读材料：

- [src/agentscope/tool/_toolkit.py](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/tool/_toolkit.py)：工具组和技能的启用、注册与筛选
- [src/agentscope/tool/_builtin/_skill.py](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/tool/_builtin/_skill.py)：读取技能的内置工具
- [src/agentscope/skill/_local_loader.py](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/skill/_local_loader.py)：本地技能元数据加载与同名处理
- [src/agentscope/agent/_agent.py](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/agent/_agent.py)：系统说明、技能目录、记忆与历史的装配

证据边界：

- 已读相关函数与上下文，未穷尽大型 Agent 类。
- 固定提交使用新一代接口，不把旧版 ReActAgent 教程当成当前实现。
- 未实测分组带来的准确率、延迟或费用变化。
- 阿里官方归属文档讨论 Java 接入；本文实现分析对象为同项目的 Python 主仓。

## CloudBase AI Toolkit

来源类型：官方源码。检查日：2026-10-21。固定提交：`f49b8d481373937b3c39012deef6cf5da829ef6e`。

许可：MIT

**学习重点：** 把一次错误写成有证据、适用条件和恢复方式的候选规则，再决定是否长期保留。

具体阅读材料：

- [config/source/guideline/cloudbase/SKILL.md](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/config/source/guideline/cloudbase/SKILL.md)：总技能如何选择业务领域和能力入口
- [config/source/skills/cloudbase-cli/SKILL.md](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/config/source/skills/cloudbase-cli/SKILL.md)：CLI 指引与领域参考的按需读取
- [mcp/src/tools/databasePG.ts](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/mcp/src/tools/databasePG.ts)：数据库工具的结构化返回、错误与后续行动
- [config/source/skills/cloudbase-code-review/SKILL.md](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/config/source/skills/cloudbase-code-review/SKILL.md)：经验何时可以进入长期规则
- [scripts/check-prompts-sync.mjs](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/scripts/check-prompts-sync.mjs)：多个分发位置的提示与技能同步检查

证据边界：

- 已读官方技能及相关实现，未登录腾讯云或执行资源操作。
- 技能指令不等于宿主运行时强制校验。
- 文档承认单独安装技能的自动选用并不一定稳定。
- 未运行同步脚本，未验证真实部署成功率。

## CodeBuddy / WorkBuddy

来源类型：官方文档。检查日：2026-10-21。固定提交：`文档页面，无提交号`。

许可：文档转载许可未确认；只保存原创摘要与链接

**学习重点：** 用文档建立功能入口，再追踪可公开核对的实现；保留文档与运行保证的区别。

具体阅读材料：

- [/docs/cli/skills](https://www.codebuddy.cn/docs/cli/skills)：CLI 技能结构、触发、工具约束与子上下文的官方说明
- [/document/product/1316/84533](https://www.tencentcloud.com/document/product/1316/84533)：企业技能分发与 WorkBuddy 相关官方说明

证据边界：

- 仅核对官方产品文档，没有对应内部实现提交。
- 没有安装或实跑 CodeBuddy / WorkBuddy。
- 不构成 WorkBuddy 全部内置技能或内部系统提示词已开源的证据。
- 网页会更新，当前内容以核对日期为界。

## AppBuilder SDK（应用开发工具包）

来源类型：官方源码。检查日：2026-10-21。固定提交：`76a7316c0671900b698f9e955afb432ec9a93183`。

许可：Apache-2.0

**学习重点：** 为每个工具写清参数语义、执行位置及结果对应的调用编号。

具体阅读材料：

- [LICENSE](https://github.com/baidubce/app-builder/blob/76a7316c0671900b698f9e955afb432ec9a93183/LICENSE)：用途与对应证据见关联案例的阅读说明
- [python/tests/test_appbuilder_client_toolcall.py](https://github.com/baidubce/app-builder/blob/76a7316c0671900b698f9e955afb432ec9a93183/python/tests/test_appbuilder_client_toolcall.py)：用途与对应证据见关联案例的阅读说明
- [python/core/console/appbuilder_client/event_handler.py](https://github.com/baidubce/app-builder/blob/76a7316c0671900b698f9e955afb432ec9a93183/python/core/console/appbuilder_client/event_handler.py)：用途与对应证据见关联案例的阅读说明
- [python/tests/test_appbuilder_client_toolcall_event_handler_error.py](https://github.com/baidubce/app-builder/blob/76a7316c0671900b698f9e955afb432ec9a93183/python/tests/test_appbuilder_client_toolcall_event_handler_error.py)：用途与对应证据见关联案例的阅读说明

证据边界：

- 仅公开 SDK 与示例，平台服务端系统提示词和完整上下文编排不可见
- 天气示例返回固定演示值，未调用真实天气服务
- 本轮只读源码，未配置账号或运行云端接口
- 框架接口不自动提供业务重试、幂等与回滚

## openJiuwen agent-core（智能体开发核心框架）

来源类型：官方源码。检查日：2026-10-21。固定提交：`4170e756504d70d8324c2ac18a5afdd770a99dc9`。

许可：Apache-2.0

**学习重点：** 同一提交同时核对技能说明、读取工具和调用者，发现文档漂移时保留两份证据。

具体阅读材料：

- [LICENSE](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/LICENSE)：用途与对应证据见关联案例的阅读说明
- [openjiuwen/core/single_agent/skills/skill_util.py](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/openjiuwen/core/single_agent/skills/skill_util.py)：用途与对应证据见关联案例的阅读说明
- [openjiuwen/core/single_agent/skills/skill_manager.py](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/openjiuwen/core/single_agent/skills/skill_manager.py)：用途与对应证据见关联案例的阅读说明
- [openjiuwen/core/single_agent/agents/react_agent.py](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/openjiuwen/core/single_agent/agents/react_agent.py)：用途与对应证据见关联案例的阅读说明
- [examples/mobile_gui/skills/scheduling/SKILL.md](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/examples/mobile_gui/skills/scheduling/SKILL.md)：用途与对应证据见关联案例的阅读说明
- [docs/zh/2.开发指南/API文档/openjiuwen.core/skills/openjiuwen_skills.md](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/docs/zh/2.%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/API%E6%96%87%E6%A1%A3/openjiuwen.core/skills/openjiuwen_skills.md)：用途与对应证据见关联案例的阅读说明

证据边界：

- 当前源码与中文技能 API 文档存在接口差异，分析以固定提交源码为准
- 技能注册不等于自动安装读取与执行工具
- 示例手机流程不代表所有设备界面或华为全部生产应用
- 本轮未执行技能或测量触发准确率

## VitaBench 1.0（交互任务评测基准）

来源类型：官方源码。检查日：2026-10-21。固定提交：`742e240855bf8686a0842360749d5ea970ea3987`。

许可：MIT；保留 Sierra Research 与 Meituan 版权

**学习重点：** 选一个业务任务，先列产物验收条件，再评估模型是否真的完成。

具体阅读材料：

- [LICENSE](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/LICENSE)：用途与对应证据见关联案例的阅读说明
- [src/vita/agent/llm_agent.py](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/agent/llm_agent.py)：用途与对应证据见关联案例的阅读说明
- [src/vita/environment/environment.py](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/environment/environment.py)：用途与对应证据见关联案例的阅读说明
- [src/vita/environment/tool.py](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/environment/tool.py)：用途与对应证据见关联案例的阅读说明
- [src/vita/domains/delivery/tools_schema.py](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/domains/delivery/tools_schema.py)：用途与对应证据见关联案例的阅读说明
- [src/vita/prompts/agent_system_prompt.yaml](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/prompts/agent_system_prompt.yaml)：用途与对应证据见关联案例的阅读说明
- [src/vita/prompts/full_trajectory_eval_template.yaml](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/prompts/full_trajectory_eval_template.yaml)：用途与对应证据见关联案例的阅读说明

证据边界：

- 评测基准的模拟业务不是美团真实生产订单 API
- 此记录为 VitaBench 1.0，不混用 VitaBench 2.0 的统计与实现
- 提示词中的业务条件不能代替执行权限控制
- 本轮未运行基准，未验证任何排行榜或性能提升

## mimoagent（智能体运行、轨迹采集与评分框架）

来源类型：官方源码。检查日：2026-10-21。固定提交：`c3df8469f250b15e7906487a6d52be4c1827a509`。

许可：MIT；NOTICE 列明上游与第三方工具的独立许可

**学习重点：** 让工具描述对应执行器真实语义，并在压缩结果时保留成功失败信息。

具体阅读材料：

- [LICENSE.md](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/LICENSE.md)：用途与对应证据见关联案例的阅读说明
- [NOTICE](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/NOTICE)：用途与对应证据见关联案例的阅读说明
- [README.md](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/README.md)：用途与对应证据见关联案例的阅读说明
- [src/mimoagent/agents/base.py](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/src/mimoagent/agents/base.py)：用途与对应证据见关联案例的阅读说明
- [src/mimoagent/agents/default.py](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/src/mimoagent/agents/default.py)：用途与对应证据见关联案例的阅读说明
- [src/mimoagent/tools/bash.py](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/src/mimoagent/tools/bash.py)：用途与对应证据见关联案例的阅读说明
- [example_configs/default-bash-only.yaml](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/example_configs/default-bash-only.yaml)：用途与对应证据见关联案例的阅读说明

证据边界：

- 明确由 mini-swe-agent 1.9.0 分叉并扩展，不是全部原创
- 接入第三方 CLI 不代表拥有其内部提示词或生产实现
- 公开运行框架不等于完整生产强化学习训练系统
- 配置级比较不自动满足严格配对实验与统计显著性
- 本轮未运行任务或复现性能结果

## Coze Studio

来源类型：官方源码。检查日：2026-10-21。固定提交：`fefb05ff27be1da939612fbf9faf5db62583b8ae`。

许可：Apache-2.0

**学习重点：** 学习提示词装配与程序分支如何协作，避免把整个 Agent 简化成一段系统提示。

具体阅读材料：

- [README.md](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE-APACHE](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/LICENSE-APACHE)：固定版本许可证正文
- [backend/domain/agent/singleagent/internal/agentflow/node_chat_prompt.go](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/agent/singleagent/internal/agentflow/node_chat_prompt.go)：系统模板、历史消息与用户输入的顺序
- [backend/domain/agent/singleagent/internal/agentflow/agent_flow_builder.go](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/agent/singleagent/internal/agentflow/agent_flow_builder.go)：BuildAgent 的前置节点、工具分支和编译选项
- [backend/domain/agent/singleagent/internal/agentflow/system_prompt.go](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/agent/singleagent/internal/agentflow/system_prompt.go)：公开 Jinja2 系统提示的占位字段与知识段落

证据边界：

- 仅核查开源单 Agent 的构图与模板；未运行工作流、验证断点恢复或对比商业扣子实现。
- 系统提示中的内容约束属于提示文本，不能证明模型必然遵循；Eino、FlowGram 等上游框架另有贡献，不能全部归作扣子原创。

## Coze Loop

来源类型：官方源码。检查日：2026-10-21。固定提交：`95dc2eebbc100b929c102d90111bb94fad41e500`。

许可：Apache-2.0

**学习重点：** 学习为评估器记录版本、实际输入与解析错误，使提示词改动可以被复查。

具体阅读材料：

- [README.md](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/LICENSE)：固定版本许可证正文
- [backend/modules/evaluation/domain/service/evaluator_source_prompt_impl.go](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/backend/modules/evaluation/domain/service/evaluator_source_prompt_impl.go)：Run、chat、renderTemplate、parseOutput 和 span 上报实现
- [backend/modules/evaluation/domain/entity/evaluator_version_prompt.go](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/backend/modules/evaluation/domain/entity/evaluator_version_prompt.go)：评估器版本字段与输入内容/schema 校验

证据边界：

- 静态核对提示词评估器路径，未运行实验、校准评委模型或验证评分有效性。
- JSON 修复与分数提取只解决格式兼容，不证明评分正确；开源版为公开核心模块，不能等同商业服务全貌。

## DeerFlow 2.x

来源类型：官方源码。检查日：2026-10-21。固定提交：`d4012c4b24f9b5ee14236a8214c82815de5b5214`。

许可：MIT

**学习重点：** 学习把技能发现、技能正文和大工具结果分层处理，同时保留回读路径与执行状态。

具体阅读材料：

- [README.md](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/LICENSE)：固定版本许可证正文
- [backend/packages/harness/deerflow/agents/lead_agent/prompt.py](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/backend/packages/harness/deerflow/agents/lead_agent/prompt.py)：技能索引/元数据两种路径及 apply_prompt_template 拼装
- [backend/packages/harness/deerflow/agents/middlewares/skill_activation_middleware.py](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/backend/packages/harness/deerflow/agents/middlewares/skill_activation_middleware.py)：显式斜杠技能激活、授权与正文注入的相关函数
- [backend/packages/harness/deerflow/agents/middlewares/tool_output_budget_middleware.py](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/backend/packages/harness/deerflow/agents/middlewares/tool_output_budget_middleware.py)：工具结果外置、失败截断、退出码与历史请求副本处理

证据边界：

- 只核查选定提示词和 middleware 函数，未运行 2.x 全链路或证明所有可选分支默认启用。
- 2.x README 声明其为重写版本，不能混用 1.x 架构；依赖 LangChain/LangGraph 等社区项目，不将框架通用能力归作字节独创。
- 上下文节省与任务效果未测量；外置或截断机制仍需验证信息可回读与完成证据。

## UI-TARS Desktop：GUI Agent SDK

来源类型：官方源码。检查日：2026-10-21。固定提交：`3ac2cb8d946d78d5ff92ad17b318eaafa18c178c`。

许可：Apache-2.0

**学习重点：** 学习模型动作、解析器、坐标转换、执行器和观察事件之间的接口边界。

具体阅读材料：

- [README.md](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/LICENSE)：固定版本许可证正文
- [multimodal/gui-agent/agent-sdk/src/GUIAgent.ts](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/multimodal/gui-agent/agent-sdk/src/GUIAgent.ts)：prompt 配置、坐标归一化、operator 执行与操作后截图事件
- [multimodal/gui-agent/agent-sdk/src/prompts.ts](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/multimodal/gui-agent/agent-sdk/src/prompts.ts)：选读动作空间、输出语法和终止动作模板
- [multimodal/gui-agent/agent-sdk/src/ToolCallEngine.ts](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/multimodal/gui-agent/agent-sdk/src/ToolCallEngine.ts)：流式累积、动作解析、错误转换和历史消息格式

证据边界：

- 本案针对仓库中的 GUI Agent SDK，未核查 Desktop 全部入口、模型版本兼容或执行真实界面。
- 模型生成 finished 仅是循环终止信号，不能独立证明用户目标已达成；本案未复现成功率。

## AgentScope Runtime（历史架构参考）

来源类型：官方源码。检查日：2026-10-21。固定提交：`22072fd7075ce0c6f43cb39509d6a14b0e60ddb5`。

许可：Apache-2.0

**学习重点：** 学习把 Agent 推理逻辑与服务运行契约分开，并记录项目迁移状态。

具体阅读材料：

- [README.md](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/LICENSE)：固定版本许可证正文
- [src/agentscope_runtime/engine/app/agent_app.py](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/src/agentscope_runtime/engine/app/agent_app.py)：query、生命周期、协议 schema、SSE 与中断封装相关函数
- [src/agentscope_runtime/adapters/agentscope/tool/sandbox_tool.py](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/src/agentscope_runtime/adapters/agentscope/tool/sandbox_tool.py)：签名保留、MCP 内容转换与文本回退

证据边界：

- README 已公告能力迁入 AgentScope 2.0、将归档；检查时 archived 为 false，不能写成已正式归档，也不作为当前独立主线推荐。
- 静态核对 AgentApp 与结果适配器，未运行服务或验证沙箱隔离、协议互操作；依赖 FastAPI、MCP、A2A 等上游。

## OpenSandbox

来源类型：官方源码。检查日：2026-10-21。固定提交：`62d3e59d10796154b88510f39fca8438eb99dd58`。

许可：Apache-2.0

**学习重点：** 学习副作用工具如何设计可追踪句柄、增量日志与不重复执行的传输规则。

具体阅读材料：

- [README.md](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/LICENSE)：固定版本许可证正文
- [cli/src/opensandbox_cli/skills/opensandbox-command-execution.md](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/cli/src/opensandbox_cli/skills/opensandbox-command-execution.md)：命令三种模式、状态/日志/中断、失败语义的使用契约
- [sdks/sandbox/python/src/opensandbox/services/command.py](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/sdks/sandbox/python/src/opensandbox/services/command.py)：Commands 协议及 execution/session 标识、增量日志接口
- [sdks/sandbox/python/src/opensandbox/adapters/command_adapter.py](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/sdks/sandbox/python/src/opensandbox/adapters/command_adapter.py)：SSE 客户端、重试绕开、事件消费与 run/interrupt 相关实现

证据边界：

- 原 alibaba/OpenSandbox API 重定向到当前 opensandbox-group；阿里来源依据保留，当前组织名称本身不证明治理关系。
- 本案只读命令 Skill、协议与 Python adapter，未部署沙箱、验证隔离强度或执行 CLI；后台启动响应不等于后台任务完成。

## AWorld CLI

来源类型：官方源码。检查日：2026-10-21。固定提交：`82af4062e29e128910afa8622c866f4b99a4d23d`。

许可：MIT

**学习重点：** 学习将技能候选、激活结果和摘要持久化分别记录，避免恢复时靠模型猜状态。

具体阅读材料：

- [README.md](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/LICENSE)：固定版本许可证正文
- [aworld-cli/src/aworld_cli/core/compact_history_prompt.txt](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/compact_history_prompt.txt)：会话压缩模板要求保留的任务与工作状态字段
- [aworld-cli/src/aworld_cli/core/skill_activation_resolver.py](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/skill_activation_resolver.py)：候选过滤、显式/关键词选择和激活指纹证据
- [aworld-cli/src/aworld_cli/core/runtime_skill_registry.py](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/runtime_skill_registry.py)：插件、兼容目录、内置 provider 的组合与来源路径
- [aworld-cli/src/aworld_cli/core/context.py](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/context.py)：token 检查、工作区摘要输入、摘要保存与检查点失败语义

证据边界：

- 本案只覆盖 CLI 技能路由与压缩路径，未验证全部多 Agent、训练或自进化能力，也未复现榜单。
- 关键词匹配、摘要质量与指纹证据的实际效果未测；仓库收录的提示文本不自动证明措辞首次由蚂蚁原创。

## BrowserSkill

来源类型：官方源码。检查日：2026-10-21。固定提交：`6214e3d6a3d74eaf39c0202c4f182b5755974da9`。

许可：MIT

**学习重点：** 学习让元素引用受会话/标签页约束，让恢复步骤依据当前状态而非盲目重试。

具体阅读材料：

- [README.md](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/LICENSE)：固定版本许可证正文
- [crates/bsk-cli/skill/SKILL.md](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/crates/bsk-cli/skill/SKILL.md)：触发说明、观察/动作循环和按需参考文件
- [crates/bsk-cli/skill/references/help-and-recovery.md](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/crates/bsk-cli/skill/references/help-and-recovery.md)：按错误/帮助结果选择恢复动作的契约
- [crates/bsk-cli/src/skill_install/provenance.rs](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/crates/bsk-cli/src/skill_install/provenance.rs)：版本化来源标记、文件摘要与更新前状态
- [apps/extension/src/tools/snapshot-ref.ts](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/apps/extension/src/tools/snapshot-ref.ts)：session/tab 归属与 DOM/视觉引用区分

证据边界：

- 流程与恢复规则来自官方 Skill 文本；引用归属检查与安装标记有实现证据，但未启动真实浏览器或验证所有流程强制执行。
- 使用现有登录会话与用户标签页的权限边界需由宿主落实；本案不将 Skill 提示视为安全隔离证明。

## Tencent RTC Agent Skills

来源类型：官方源码。检查日：2026-10-21。固定提交：`55a6bcf643acb4104105359ed0a1d194bdee7696`。

许可：MIT

**学习重点：** 学习把分流、执行状态与验收拆开，并区分知识失败、环境失败及真实运行效果。

具体阅读材料：

- [README.md](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/LICENSE)：固定版本许可证正文
- [skills/trtc/SKILL.md](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/skills/trtc/SKILL.md)：根路由、session 恢复、owner 交接及产品/意图分流
- [skills/trtc-ai-service/SKILL.md](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/skills/trtc-ai-service/SKILL.md)：选读双根路径、接口验收、交付与工具约束
- [skills/trtc/tools/session.py](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/skills/trtc/tools/session.py)：transaction、_atomic_write、_flock、schema 与迁移相关实现
- [.claude/skills/trtc-eval/scripts/evaluator.py](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/.claude/skills/trtc-eval/scripts/evaluator.py)：基于固定字符串约束的静态计分实现
- [.claude/skills/trtc-eval/prompts/ai_driver_system_prompt.md](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/.claude/skills/trtc-eval/prompts/ai_driver_system_prompt.md)：评估专用输出契约和知识不可读失败分类

证据边界：

- 只核查选定 Skill、会话工具和评估文件，未实跑 SDK、上报流程或基准；评估模式提示有专用假设，不能当普通产品默认交互。
- 静态字符串命中不能证明可编译或业务成功；AI 客服 Skill 自述的验收包含控制面与样例交付，真实语音质量仍需另验。
- Windows 无 fcntl 时锁降级，不能笼统宣称全部平台有相同并发保证；未把公开包推广成 CodeBuddy/WorkBuddy 内部实现。

## SkillHub 官方 Skills 与 TRACE 校验器

来源类型：官方源码。检查日：2026-10-21。固定提交：`a051f06f7944d24ade04bea27735f430b19a8298`。

许可：MIT

**学习重点：** 学习把候选召回、意图匹配、证据评分和机器可检查的报告分开。

具体阅读材料：

- [README.md](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/README.md)：项目定位、公开范围、归属线索与维护状态
- [LICENSE](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/LICENSE)：固定版本许可证正文
- [skills/find-skill-skillhub/SKILL.md](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/skills/find-skill-skillhub/SKILL.md)：多关键词召回、意图重排与渐进引用
- [skills/skillhub-trace-evaluator/SKILL.md](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/skills/skillhub-trace-evaluator/SKILL.md)：基于已读包的评分流程与跳过扫描约定
- [skills/skillhub-trace-evaluator/scripts/validate_trace_scores.py](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/skills/skillhub-trace-evaluator/scripts/validate_trace_scores.py)：分数字段、维度、说明和 scan 分支的校验实现

证据边界：

- 官方仓库只公开 API 文档、插件和部分官方 Skills；平台聚合的第三方 Skills 不能一概标为腾讯原创。
- 本案未调用在线 API 或运行评分；校验器只能证明结构/数值合规，不能证明证据真实、评分准确或已做安全扫描。
- GitHub license 元数据为 NOASSERTION，但已读 LICENSE 明确声明 MIT；以该固定版本正文登记。

## Kimi CLI（已归档 Python 版的技能与执行循环）

来源类型：官方源码。检查日：2026-10-21。固定提交：`9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82`。

许可：Apache-2.0；NOTICE 标明 skill-creator 复用了 OpenAI Codex 的 Apache-2.0 材料

**学习重点：** 适合学习技能发现与正文加载如何接入真实模型循环，以及为何必须区分正常回答、工具拒绝、重复调用和步数耗尽。

具体阅读材料：

- [README.md](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/README.md)：核对归档状态、后继 Kimi Code 与当前来源边界
- [LICENSE](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/LICENSE)：主许可证
- [NOTICE](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/NOTICE)：Moonshot AI 版权与第三方来源
- [src/kimi_cli/skill/__init__.py](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/skill/__init__.py)：作用域、重名处理、技能清单格式与正文读取
- [src/kimi_cli/soul/agent.py](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/soul/agent.py)：工作目录、AGENTS.md、技能清单、工具与 MCP 装配
- [src/kimi_cli/agents/default/system.md](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/agents/default/system.md)：项目规则与技能目录的提示词插入位置
- [src/kimi_cli/soul/kimisoul.py](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/src/kimi_cli/soul/kimisoul.py)：模型调用、工具结果回写、检查点、压缩和停止原因

证据边界：

- 检查时该仓库已归档；固定快照是历史 Python 版，不代表后继 MoonshotAI/kimi-code 的当前实现。
- 未安装 CLI、调用模型或连接 MCP；未实测恢复、压缩与技能选用成功率。
- 只读调用边界，未完整审计所有工具、授权实现及模型服务端。
- 正常无工具调用只意味着本轮结束，不是工作产物通过独立验收。

## MiniMax Skills（全栈开发技能与技能校验器）

来源类型：官方源码。检查日：2026-10-21。固定提交：`60aaae52bb2af8162732751a4332f62a5fef518b`。

许可：主许可证 MIT；CREDITS 列出 Anthropic Apache-2.0、Expo MIT 等衍生材料，具体资产另看各自许可

**学习重点：** 适合学习如何把工程知识写成有触发边界、有证据要求的技能，并分清技能包结构通过与实际业务产物通过。

具体阅读材料：

- [README.md](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/README.md)：官方与社区技能标记、Beta 状态和分发方式
- [LICENSE](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/LICENSE)：MiniMax 版权与主许可证
- [CREDITS.md](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/CREDITS.md)：区分官方维护、社区贡献与衍生来源
- [skills/fullstack-dev/SKILL.md](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/fullstack-dev/SKILL.md)：触发与排除条件、需求到交接流程、验证要求
- [skills/fullstack-dev/references/release-checklist.md](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/fullstack-dev/references/release-checklist.md)：发布阶段与需求—测试证据对应表
- [.claude/skills/pr-review/scripts/validate_skills.py](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/.claude/skills/pr-review/scripts/validate_skills.py)：元数据、目录名称和凭据模式检查的实际范围

证据边界：

- 本条只拆解 fullstack-dev 及校验器，不代表已审查仓库每个技能。
- README 同时包含 Official 与 Community 条目；官方组织托管不等于每个条目都由 MiniMax 原创。
- 校验脚本只做有限格式和模式扫描，不能证明语义质量或程序安全。
- 技能中的必须执行属于宿主应遵守的指令；不是运行时已经强制执行的证据。
- 未执行校验器、技能或任何生成任务。

## MiniMax MCP（多模态 API 适配与异步任务状态）

来源类型：官方源码。检查日：2026-10-21。固定提交：`0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a`。

许可：MIT

**学习重点：** 适合学习长耗时工具如何向 Agent 表达已提交、处理中、失败和结果可取，避免将受理成功误当产物完成。

具体阅读材料：

- [README-CN.md](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/README-CN.md)：MCP 能力范围、配置及资源返回模式
- [LICENSE](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/LICENSE)：MiniMax AI 版权与主许可证
- [minimax_mcp/server.py](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/minimax_mcp/server.py)：generate_video 与 query_video_generation 的提交、轮询、下载和错误分支
- [minimax_mcp/client.py](https://github.com/MiniMax-AI/MiniMax-MCP/blob/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a/minimax_mcp/client.py)：API 鉴权、HTTP 与业务错误、Trace-Id

证据边界：

- 这是 MCP 服务适配层，不含宿主 Agent 的系统提示词、技能选择与完整会话循环。
- 本次未调用 MiniMax API、生成媒体、配置账号或执行文件下载流程。
- 所读视频路径以 TextContent 返回失败文字；不应据此假定宿主总能收到统一的机器可读错误状态。
- 同步轮询有次数上限，但客户端未统一设置请求超时；轮询次数并不等于严格总耗时上限。
- 检查日官方指南推荐优先使用 MiniMax CLI；本条保留 MCP 实现的学习价值，不作为当前安装优先级建议。

## Open-AutoGLM（手机 GUI Agent 的截图—动作循环）

来源类型：官方源码。检查日：2026-10-21。固定提交：`86f55382982fb054e8fc98ca80609dff8a2cdc3c`。

许可：Apache-2.0；README 另链接 resources/privacy_policy.txt 使用规范，模型与第三方组件须分别核对

**学习重点：** 适合学习视觉 Agent 的上下文保留策略、动作解析与设备接口分层，尤其是完成信号与真实任务成功之间的差别。

具体阅读材料：

- [README.md](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/README.md)：智谱产品关联、Phone Agent 范围和模型/设备依赖
- [LICENSE](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/LICENSE)：源码主许可证
- [resources/privacy_policy.txt](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/resources/privacy_policy.txt)：部署数据流说明及另行声明的使用规范
- [phone_agent/agent.py](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/agent.py)：任务与截图输入、历史图像移除、异常和终止条件
- [phone_agent/actions/handler.py](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/actions/handler.py)：动作分派、坐标转换、确认与人工接管、AST 参数解析

证据边界：

- 仅静态核对 Android/HarmonyOS 共享入口的主要流程；未接手机、执行 ADB/HDC 或测试 iOS。
- 主 Agent 循环主要靠下一张截图观察动作结果，没有统一把每个 ActionResult 作为工具消息回填。
- 动作解析失败会转为 finish；模型异常也会结束循环，因此 finished 不能作为业务成功证据。
- 点击确认依赖动作中携带 message；未证明运行时能独立识别所有敏感业务行为。
- 开源框架不等于智谱闭源产品的完整生产实现。

## JoyAgent-JDGenie（规划、执行和产物状态）

来源类型：官方源码。检查日：2026-10-21。固定提交：`2417e0b8b636d941ad5fb14c59b20dddfef5375d`。

许可：Apache-2.0

**学习重点：** 适合学习多 Agent 的状态交接、原生工具调用与文本解析模式的不同回传形式，以及并发工具结果怎样按调用编号对齐。

具体阅读材料：

- [README.md](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/README.md)：所属京东团队、产品范围与源码架构
- [LICENSE](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/LICENSE)：主许可证
- [genie-backend/src/main/java/com/jd/genie/agent/agent/PlanningAgent.java](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/PlanningAgent.java)：规划上下文、计划工具、下一任务与完成状态
- [genie-backend/src/main/java/com/jd/genie/agent/agent/ExecutorAgent.java](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/ExecutorAgent.java)：执行上下文、并发工具结果回填、截断和任务摘要
- [genie-backend/src/main/java/com/jd/genie/agent/agent/BaseAgent.java](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/agent/BaseAgent.java)：循环步数、工具异常与按调用 ID 汇集结果
- [genie-backend/src/main/java/com/jd/genie/agent/tool/common/PlanningTool.java](https://github.com/jd-opensource/joyagent-jdgenie/blob/2417e0b8b636d941ad5fb14c59b20dddfef5375d/genie-backend/src/main/java/com/jd/genie/agent/tool/common/PlanningTool.java)：计划创建、修改、状态标记与 finish 行为

证据边界：

- 固定的是默认 data_agent 分支；未把其他分支、报告版系统或线上 JoyAgent 平台当成同一实现。
- 未安装 Java/Python/前端依赖、调用模型或运行报告生成。
- 规划状态由工具更新，finish 可把步骤置 completed；未看到此处独立校验产物内容。
- 工具输出可按字符截断，截断后是否仍足以完成任务需单独评估。
- 没有据 README 排行榜宣传推断本快照的实测效果。

## KwaiAgents / KAgentSys-Lite（规划循环与细粒度评测）

来源类型：官方源码。检查日：2026-10-21。固定提交：`3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c`。

许可：CC-BY-NC-SA-4.0（主 LICENSE.txt，含非商业与相同方式共享条件）

**学习重点：** 适合学习低复杂度 Agent 如何把角色、时间、工具与短期历史拼成提示，以及离线文本/动作匹配评测为何不能代替端到端任务验收。

具体阅读材料：

- [README.md](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/README.md)：Kuaishou Technology 归属、Lite 与论文完整版的明确差异
- [LICENSE.txt](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/LICENSE.txt)：CC-BY-NC-SA-4.0 许可证
- [kwaiagents/agents/kagent.py](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/agents/kagent.py)：最近对话、已完成任务、工具执行、异常与终止
- [kwaiagents/agents/prompts.py](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/agents/prompts.py)：角色/时间/工具/记忆拼装与 token 截断
- [kwaiagents/utils/function_utils.py](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/kwaiagents/utils/function_utils.py)：从函数说明生成工具参数描述
- [benchmark/benchmark_eval.py](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/benchmark/benchmark_eval.py)：工具名精确匹配、参数 ROUGE 与规划指标

证据边界：

- 公开的是 Lite 代码，README 明确工具更少、缺少完整版记忆机制，且源自 BabyAGI/Auto-GPT 等项目的演进。
- 代码仍会拼入最近三轮对话和已完成任务；不能把缺少专门记忆机制误写成完全没有历史上下文。
- 主许可证含非商业条件，不宜称为可无条件商用的 MIT/Apache 项目。
- 工具异常常返回空字符串，停止条件也包括无工具、未知工具与迭代上限，均非独立任务成功证明。
- 评测包含文本相似度与工具名/参数匹配，不等同于在真实业务环境中完成任务。
- 未运行旧依赖、模型服务、搜索或评测，未验证今日外部接口可用性。

## LobsterAI（桌面产品层的技能管理与运行时桥接）

来源类型：官方源码。检查日：2026-10-21。固定提交：`b649d5c80f25887e6d0c1ff04024150f7476da5d`。

许可：主许可证 MIT；内置技能、OpenClaw 及其他依赖分别保留上游许可

**学习重点：** 适合学习产品状态、技能上下文和 Agent 运行时怎样解耦，也能看清官方标记、扫描结果和运行期批准并非同一层保障。

具体阅读材料：

- [README_zh.md](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/README_zh.md)：网易有道归属、Cowork 与 OpenClaw 的分工
- [LICENSE](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/LICENSE)：NetEase Youdao 版权与主许可证
- [src/main/skills/skillManager.ts](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/main/skills/skillManager.ts)：技能解析/启用/目录提示、安装审查与失败策略
- [src/renderer/components/cowork/skillSystemPrompt.ts](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/renderer/components/cowork/skillSystemPrompt.ts)：技能提示与基础提示拼接、继续对话的注入条件
- [src/main/libs/agentEngine/openclawApprovalBridge.ts](https://github.com/netease-youdao/LobsterAI/blob/b649d5c80f25887e6d0c1ff04024150f7476da5d/src/main/libs/agentEngine/openclawApprovalBridge.ts)：执行/插件批准请求解析、调用关联与决策映射

证据边界：

- 本轮研究产品层和桥接代码，不是完整审计 OpenClaw 引擎、全部插件或所有内置技能。
- README 明确底层任务由 OpenClaw 执行，不能把依赖能力全部称为网易原创。
- 技能安全扫描异常在此安装路径中不会阻断安装；有扫描器不代表扫描失败时默认拒绝。
- 执行批准解析存在自动批准分支，不能概括为每个命令都先人工批准。
- isOfficial 从技能头部字段读取，属于包元数据，不构成外部官方身份认证。
- 未安装桌面应用、启动网关、连接 IM/MCP 或运行工作任务。

## Lagent（统一消息、会话记忆与动作执行）

来源类型：官方源码。检查日：2026-10-21。固定提交：`0ab2e2f550477884743cd63fbca7bc4aa7b00290`。

许可：Apache-2.0

**学习重点：** 适合学习一个小型 ReAct Agent 必须有哪些清晰边界，而不是把提示词、解析、执行和历史管理混在一个函数里。

具体阅读材料：

- [README.md](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/README.md)：消息层、会话记忆与可组合 Agent 的官方用法
- [LICENSE](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/LICENSE)：主许可证
- [lagent/agents/agent.py](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/agents/agent.py)：消息入出记忆、聚合、解析与会话状态
- [lagent/agents/react.py](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/agents/react.py)：工具描述进入模板、循环与完成条件
- [lagent/actions/action_executor.py](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/actions/action_executor.py)：工具命名、动作分派和前后钩子
- [lagent/hooks/action_preprocessor.py](https://github.com/InternLM/lagent/blob/0ab2e2f550477884743cd63fbca7bc4aa7b00290/lagent/hooks/action_preprocessor.py)：模型动作格式转换与成功/错误结果文本化

证据边界：

- 上海人工智能实验室是研究机构，不计作互联网大厂。
- 只读当前快照中的基础 Agent/ReAct/执行器，未运行教程或逐项覆盖全部代理类型。
- ReAct 默认检查消息正文或格式化结果中是否出现 conclusion，循环耗尽也会返回最后一条消息；它没有提供独立业务成功证明。
- 动作层的状态和错误回传不自动提供业务重试、幂等或回滚。

## MindSearch（搜索规划图、并发子任务与引用合并）

来源类型：官方源码。检查日：2026-10-21。固定提交：`7952c5f8a956fe6a44228a6a7d528a35340e7c87`。

许可：Apache-2.0；LICENSE 明列 Shanghai AI Laboratory 版权

**学习重点：** 适合学习深度研究任务怎样拆分、并行和汇合，尤其是跨子任务引用冲突与图状态展示；也展示阅读调用链发现版本细节的必要性。

具体阅读材料：

- [README_zh-CN.md](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/README_zh-CN.md)：框架范围、历史评测日期和相关项目
- [LICENSE](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/LICENSE)：Shanghai AI Laboratory 版权与许可
- [mindsearch/agent/graph.py](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/graph.py)：子搜索输入、线程/异步任务、状态队列与图执行
- [mindsearch/agent/mindsearch_agent.py](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/mindsearch_agent.py)：规划循环、引用编号重排、图状态与最终汇总
- [mindsearch/agent/mindsearch_prompt.py](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/mindsearch/agent/mindsearch_prompt.py)：搜索器/规划器/汇总器的上下文模板和引用要求

证据边界：

- 研究机构的公开研究项目，不能当作大厂商业产品生产架构。
- graph.py 直接 exec 模型生成的图操作代码；本文件未提供隔离沙箱。
- add_edge 保存邻接边字典，而 add_node 的父节点筛选把节点名与整个边对象比较；仅静态发现，父回答自动传递需专门验证。
- 引用合并读取节点记忆中特定位置的工具消息，属于与既定搜索流程耦合的实现。
- 中文 README 评测注明实验完成于 2024-07-07 前，不把历史数字写成当前效果。
- 未运行模型、搜索引擎、图执行器或评测；未验证多线程异常恢复与引用准确率。

## 跨产品归档的采集流程与六个代表技能

来源类型：第三方归档。检查日：2026-10-21。固定提交：`1c9239cc90585f57d9e06d32deffc017bbff5802`。

许可：根目录未见许可证且 GitHub license 元数据为 null；六个代表包目录未发现独立 LICENSE/COPYING 文件。本分析只保存原创摘要与链接，不作再分发许可推断。

**学习重点：** 借鉴可追溯的采集流水线，在其上增加人工审阅的方法、适用条件、差异与实践记录。

具体阅读材料：

- [README.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [README-doubao.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-doubao.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [README-workbuddy.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-workbuddy.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [README-qwenwork.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-qwenwork.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [README-chatgpt.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-chatgpt.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [scripts/sync_platform.py](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/scripts/sync_platform.py)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [scripts/register-windows-task.ps1](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/scripts/register-windows-task.ps1)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [scripts/sync_doubao_skills.py](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/scripts/sync_doubao_skills.py)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [.gitignore](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/.gitignore)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [doubao/change-logs/2026-10-20-180008.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/change-logs/2026-10-20-180008.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [workbuddy/experts/ai-expert-studio/skills/ai-expert-studio-orchestrator/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/workbuddy/experts/ai-expert-studio/skills/ai-expert-studio-orchestrator/SKILL.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [workbuddy/connectors/marketplace/connectors/databuddy/skills/data-task-planner/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/workbuddy/connectors/marketplace/connectors/databuddy/skills/data-task-planner/SKILL.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [qwenwork/skills/dingtalk-chat-to-todo/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/qwenwork/skills/dingtalk-chat-to-todo/SKILL.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [qwenwork/experts/product-design/skills/qa/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/qwenwork/experts/product-design/skills/qa/SKILL.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [doubao/skills/app-builder-orchestration/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/app-builder-orchestration/SKILL.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [chatgpt/skills/review-agent/SKILL.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/chatgpt/skills/review-agent/SKILL.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [workbuddy/experts/ai-expert-studio/.codebuddy-plugin/plugin.json](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/workbuddy/experts/ai-expert-studio/.codebuddy-plugin/plugin.json)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解
- [qwenwork/experts/product-design/chain-protocol.md](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/qwenwork/experts/product-design/chain-protocol.md)：采集流程、统计口径或代表性技能正文，具体对应关系见中文拆解

证据边界：

- 作者的个人设备样本不代表厂商全量发布目录。
- 归档内容不等于各产品完整系统提示词；宿主系统指令、动态工具 schema、账户状态、服务端编排可能不可见。
- marketplace、official_experts、install_source 等目录/字段不构成作者身份和来源认证。
- 文本要求、运行时执行和有效性实验分开；本次为静态核对。
- 未证明作者怎样首次得到每个插件、是否编辑过个别副本、厂商是否认可再发布。
- 没有对全部 2,792 份 SKILL 正文做深读或语义去重。
- 2,792 个 SKILL.md 仅完成路径元数据索引，本轮代表正文深读另计；不新增 2,792 条已审阅研究来源。
