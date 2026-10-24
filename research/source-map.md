# 国内外来源与论文地图

检查日：2026-10-25。现有材料、这次核对和待发现目标分别标识；每条的证据深度见结构化台账。论文摘要不算全文研究。

| 来源 | 组织/地区 | 当前深度 | 下一步核心问题 |
| --- | --- | --- | --- |
| [Lark CLI（飞书命令行工具）](https://github.com/larksuite/cli) | 字节跳动 / 飞书 / 既有中国项目及对照材料 | 继承既有静态阅读 | 把业务快捷命令、标准 API 与通用调用分层，配合权限、风险和结果契约。 |
| [Lark CLI 官方技能与技能创建指南](https://github.com/larksuite/cli/tree/017b19a793ad71794a02887ede04757f3d82e10d/skills) | 字节跳动 / 飞书 / 既有中国项目及对照材料 | 继承既有静态阅读 | 先解析真实业务对象，再按依赖执行；把技能路由与详细操作参考分开。 |
| [Eino Skill Middleware（技能加载中间件）](https://github.com/cloudwego/eino) | 字节跳动 / CloudWeGo / 既有中国项目及对照材料 | 继承既有静态阅读 | 先提供技能目录，再按需读取正文；子任务可选择独立或继承父上下文。 |
| [Trae Agent（公开软件工程智能体）](https://github.com/bytedance/trae-agent) | 字节跳动 / 既有中国项目及对照材料 | 继承既有静态阅读 | 公开编码 Agent 的任务提示、工具循环、轨迹记录和结束信号。 |
| [lark-base 1.5.1 与 Base 系统搭建指引](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/tree/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base) | 豆包相关第三方归档 / 既有中国项目及对照材料 | 继承既有静态阅读 | 第三方保存的 Base 1.5.1：从业务建模、字段设计到写入和回读验收。 |
| [doubao-enterprise-search（企业搜索技能归档）](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/doubao-enterprise-search/SKILL.md) | 豆包相关第三方归档 / 既有中国项目及对照材料 | 继承既有静态阅读 | 保留搜索的主体、时间与比较条件，并区分知识检索和已知对象操作。 |
| [Qwen Code](https://github.com/QwenLM/qwen-code) | 阿里 / 既有中国项目及对照材料 | 继承既有静态阅读 | 依据会话工具声明快照筛选相关指引，技能目录与正文采用不同加载策略。 |
| [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | 阿里 / 既有中国项目及对照材料 | 继承既有静态阅读 | 把检索、模型适配、函数调用协议和工具执行连接到消息列表。 |
| [AgentScope](https://github.com/agentscope-ai/agentscope) | 阿里 / 既有中国项目及对照材料 | 继承既有静态阅读 | 让工具组与技能一起受能力启用状态约束，再装配说明、记忆和历史。 |
| [CloudBase AI Toolkit](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) | 腾讯 / 既有中国项目及对照材料 | 继承既有静态阅读 | 业务技能逐层路由到参考资料，CLI 与 MCP 互补，并维护经验规则的入库门槛。 |
| [CodeBuddy / WorkBuddy](https://www.codebuddy.cn/docs/cli/skills) | 腾讯 / 既有中国项目及对照材料 | 继承既有静态阅读 | 官方文档说明技能描述、工具限制、子上下文和分发方式。 |
| [AppBuilder SDK（应用开发工具包）](https://github.com/baidubce/app-builder) | 百度 / 既有中国项目及对照材料 | 继承既有静态阅读 | 云端发出工具调用后暂停，本地执行函数，再按调用编号回传继续运行。 |
| [openJiuwen agent-core（智能体开发核心框架）](https://github.com/openJiuwen-ai/agent-core) | 华为 / 既有中国项目及对照材料 | 继承既有静态阅读 | 用技能元数据建立入口，正文通过读取工具加载；文档与实际代码存在接口差异。 |
| [VitaBench 1.0（交互任务评测基准）](https://github.com/meituan-longcat/vitabench) | 美团 / 既有中国项目及对照材料 | 继承既有静态阅读 | 工具声明前后条件与读写类型，并用独立评分提示评价完整任务轨迹。 |
| [mimoagent（智能体运行、轨迹采集与评分框架）](https://github.com/XiaomiMiMo/mimoagent) | 小米 / 既有中国项目及对照材料 | 继承既有静态阅读 | 把模型、Agent、环境和评分拆开，工具说明明确子进程、并发、超时和退出码。 |
| [Coze Studio](https://github.com/coze-dev/coze-studio) | 字节跳动 / 扣子 / 既有中国项目及对照材料 | 继承既有静态阅读 | 把人设、变量、检索结果和工具配置装配成可执行 Agent 图。 |
| [Coze Loop](https://github.com/coze-dev/coze-loop) | 字节跳动 / 扣子 / 既有中国项目及对照材料 | 继承既有静态阅读 | 把提示词评估拆成输入校验、模板渲染、模型调用、结果解析和可追踪版本。 |
| [DeerFlow 2.x](https://github.com/bytedance/deer-flow) | 字节跳动 / DeerFlow 社区 / 既有中国项目及对照材料 | 继承既有静态阅读 | 按运行配置拼装提示词与技能入口，并对工具大结果建立外置文件和上下文预算。 |
| [UI-TARS Desktop：GUI Agent SDK](https://github.com/bytedance/UI-TARS-desktop) | 字节跳动 / 既有中国项目及对照材料 | 继承既有静态阅读 | 用明确的 GUI 动作语法把模型输出转成操作，再将新截图作为下一轮观察。 |
| [AgentScope Runtime（历史架构参考）](https://github.com/agentscope-ai/agentscope-runtime) | 阿里巴巴 / AgentScope / 既有中国项目及对照材料 | 继承既有静态阅读 | 将 Agent 查询函数包装成带生命周期、流式响应、中断和协议适配的服务。 |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 阿里巴巴来源 / OpenSandbox 社区 / 既有中国项目及对照材料 | 继承既有静态阅读 | 将沙箱命令执行划分为前台、后台与持久会话，并显式处理状态、日志和重试语义。 |
| [AWorld CLI](https://github.com/inclusionAI/AWorld) | 蚂蚁集团 / inclusionAI / 既有中国项目及对照材料 | 继承既有静态阅读 | 用显式规则选择技能，并把会话压缩、工作区信息和检查点状态纳入 CLI 上下文管理。 |
| [BrowserSkill](https://github.com/Tencent/BrowserSkill) | 腾讯 / 既有中国项目及对照材料 | 继承既有静态阅读 | 把浏览器任务组织成观察、引用元素、操作、再观察的流程，并维护 Skill 安装来源。 |
| [Tencent RTC Agent Skills](https://github.com/Tencent-RTC/agent-skills) | 腾讯 / Tencent RTC / 既有中国项目及对照材料 | 继承既有静态阅读 | 以路由 Skill、产品 Skill、会话状态工具和独立评估提示组织 SDK 集成知识。 |
| [SkillHub 官方 Skills 与 TRACE 校验器](https://github.com/Tencent/skillhub) | 腾讯 / SkillHub / 既有中国项目及对照材料 | 继承既有静态阅读 | 公开技能发现流程和包质量评估模板，用程序检查报告格式与分数字段。 |
| [Kimi CLI（已归档 Python 版的技能与执行循环）](https://github.com/MoonshotAI/kimi-cli) | 月之暗面 / Moonshot AI / 既有中国项目及对照材料 | 继承既有静态阅读 | 用带作用域的技能索引、项目说明和工具集合组装 CLI 上下文，并在可观察的多步循环中持久化消息与停止原因。 |
| [MiniMax Skills（全栈开发技能与技能校验器）](https://github.com/MiniMax-AI/skills) | MiniMax / 既有中国项目及对照材料 | 继承既有静态阅读 | 把全栈开发拆成需求、架构、实施、验证与交接流程，并用独立脚本检查技能元数据和部分凭据模式。 |
| [MiniMax MCP（多模态 API 适配与异步任务状态）](https://github.com/MiniMax-AI/MiniMax-MCP) | MiniMax / 既有中国项目及对照材料 | 继承既有静态阅读 | 把多模态服务包装为 MCP 工具，视频任务以 task_id 连接提交、查询、结果下载，并区分 API 与文件处理错误。 |
| [Open-AutoGLM（手机 GUI Agent 的截图—动作循环）](https://github.com/zai-org/Open-AutoGLM) | 智谱 / Z.ai / 既有中国项目及对照材料 | 继承既有静态阅读 | 手机界面与任务组成多模态输入，模型给出有限动作，设备适配层执行，再用新截图继续观察。 |
| [JoyAgent-JDGenie（规划、执行和产物状态）](https://github.com/jd-opensource/joyagent-jdgenie) | 京东 / 既有中国项目及对照材料 | 继承既有静态阅读 | 规划 Agent 管理结构化计划，执行 Agent 使用业务工具；两者根据真实工具列表、任务、日期、SOP 和已有产物组装提示词。 |
| [KwaiAgents / KAgentSys-Lite（规划循环与细粒度评测）](https://github.com/KwaiKEG/KwaiAgents) | 快手 / KwaiKEG / 既有中国项目及对照材料 | 继承既有静态阅读 | 以单任务规划—工具执行—结果记录循环完成信息检索；评测代码分别核对工具名、参数和规划文本。 |
| [LobsterAI（桌面产品层的技能管理与运行时桥接）](https://github.com/netease-youdao/LobsterAI) | 网易 / 网易有道 / 既有中国项目及对照材料 | 继承既有静态阅读 | 桌面产品层维护技能启用、路径和安装状态，生成按需读取目录，并把授权请求转换为 OpenClaw 运行时可处理的决策。 |
| [Lagent（统一消息、会话记忆与动作执行）](https://github.com/InternLM/lagent) | 上海人工智能实验室 / InternLM / 既有中国项目及对照材料 | 继承既有静态阅读 | 把 Agent 封装为统一消息接口，用独立会话记忆、消息聚合器、格式解析器与动作执行器连接模型和工具。 |
| [MindSearch（搜索规划图、并发子任务与引用合并）](https://github.com/InternLM/MindSearch) | 上海人工智能实验室 / InternLM / 既有中国项目及对照材料 | 继承既有静态阅读 | 规划器生成搜索图操作，子搜索器并发搜集并留下节点状态与记忆，最后统一引用编号并汇总回答。 |
| [跨产品归档的采集流程与六个代表技能](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills) | ahang1598 的跨产品第三方归档 / 既有中国项目及对照材料 | 继承既有静态阅读 | 拆开本地文件同步、索引生成、变更归档与模型学习总结，并比较六个技能样本。 |
| [Agent Skills 规范与参考实现](https://github.com/agentskills/agentskills) | Agent Skills / 跨国标准 | 指定规范/源码已读 | 发现、加载与校验究竟由哪一层保证？ |
| [MCP 2026-07-28 架构与版本](https://github.com/modelcontextprotocol/modelcontextprotocol) | MCP / 跨国标准 | 指定规范/源码已读 | 当前与旧协议怎样兼容，哪些状态在 Host？ |
| [OpenAI Multi-agent 文档](https://developers.openai.com/api/docs/guides/agents-api/multi-agent) | OpenAI / 海外 | 相关正文已读 | 独立上下文、委派与共享文件协调的边界？ |
| [OpenAI Skills 文档](https://developers.openai.com/api/docs/guides/tools-skills) | OpenAI / 海外 | 相关正文已读 | 技能目录、上传与宿主发现有哪些差别？ |
| [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | Anthropic / 海外 | 文章已读 | 初始化、增量工作与跨会话交接怎样设计？ |
| [Agent Framework Checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) | Microsoft / 海外 | 相关正文已读 | 断点保存了什么，和摘要及业务状态有何区别？ |
| [Agent Development Kit 官方入口](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk) | Google / 海外 | 入口已打开，待深读 | 工作流、模型 Agent 和部署如何衔接？ |
| [Open Protocols with Strands Agents SDK](https://aws.amazon.com/blogs/opensource/open-protocols-with-the-strands-agents-sdk/) | AWS / 海外 | 入口已打开，待深读 | 协议互操作与 Harness 运行职责怎样分开？ |
| [Agent Planning Benchmark](https://arxiv.org/abs/2606.04874v3) | 作者论文，机构待全文核对 / 论文 | 仅摘要 | 怎样把规划问题与执行问题分开评估？ |
| [OneDayAgent](https://arxiv.org/abs/2608.05013v1) | 作者论文，机构待全文核对 / 论文 | 仅摘要 | 分解、执行记忆、产物验证和修复如何组合？ |
| [EvoHarnessBench](https://arxiv.org/abs/2609.04280v3) | 作者论文，机构待全文核对 / 论文 | 仅摘要 | 新增工具、技能和 Agent 后，旧能力是否退化？ |
| [Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI](https://arxiv.org/abs/2609.38143v2) | 作者论文，机构待全文核对 / 论文 | 仅摘要 | 构造执行环境的经验怎样学习与迁移？ |
| [Doc2Harness](https://arxiv.org/abs/2610.20344v1) | 作者论文，机构待全文核对 / 论文 | 仅摘要 | 怎样直接验证 Harness 实现符合行为契约？ |
| [SHarP](https://arxiv.org/abs/2610.04178v1) | 作者论文，机构待全文核对 / 论文 | 仅摘要 | 哪些 Harness 组件可以删掉，怎样测代价和贡献？ |
| Codex、Agents SDK、公开 Harness 与技能评估 | OpenAI / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Claude Agent SDK、Claude Code、Skills、团队协作 | Anthropic / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Gemini CLI、ADK、A2A 与研究 Agent | Google / DeepMind / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Agent Framework、AutoGen、Semantic Kernel 的演进 | Microsoft / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Strands、AgentCore、长期任务恢复 | AWS / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| NeMo Agent Toolkit 与评估 | NVIDIA / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| BeeAI、Agent Stack 与工作流 | IBM / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Agentforce、公开研究与评测 | Salesforce / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| 公开 Agent 工具与研究 | Meta / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| 工具环境与 Agent 评测公开研究 | Apple / 海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| smolagents、工具执行与代码 Agent | Hugging Face / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| LangGraph、Deep Agents | LangChain / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Workflows、检索与数据 Agent | LlamaIndex / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Role、Task、Crew 与流程 | CrewAI / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| PydanticAI 类型化 Agent | Pydantic / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| 持久记忆与上下文 | Letta / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| 编程 Agent 执行架构 | OpenHands / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Team、Workflow 与状态 | Agno / 社区/海外 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| 应用工作流与插件 | Dify / 社区/跨国 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| 浏览器任务与状态 | Browser Use / 社区/跨国 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| 协议、任务与能力发现 | A2A 项目 / 跨国标准 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| OPPO、vivo、360、商汤公开工程材料 | 中国厂商补充 / 中国 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| Kimi、MiniMax、AgentScope 当前入口变化 | 中国厂商迁移 / 中国 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| ReAct、Toolformer、Reflexion、Voyager | 经典论文 / 论文 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| AutoGen、MetaGPT 与多 Agent 负面/同预算比较 | 协作论文 / 论文 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| SWE-bench、WebArena、OSWorld、GAIA、tau-bench、ToolSandbox | 评测论文 / 论文 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| SkillsBench 与生态规模技能发现 | 技能论文 / 论文 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |
| MobilePA-Bench | 最新线索 / 论文 | 待确认入口 | 先确认公开入口、归属、版本与可读实现，再确定具体问题 |

候选公司、项目和论文主题是检索范围，不保证它们所有功能均公开；官方、社区、第三方归档分别归因。

## 信息源与发现机制

官方开发者文档、官网指向的 GitHub 组织、固定源码、release 与迁移记录；arXiv、OpenReview、ACL Anthology、会议论文页与作者项目页；官方工程博客；具体实现 issue 和失败轨迹。社区文章与社交平台仅用于发现线索，关键事实回到一手材料。

采用关键词检索、代码符号/文件检索、引用链回溯和近 30/90 天增量扫描。每周复核覆盖矩阵：不能让编程 Agent 的材料挤掉办公、数据、服务和其他垂类。
