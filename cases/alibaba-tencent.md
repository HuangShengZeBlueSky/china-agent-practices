# 阿里与腾讯：从提示词装配到技能维护

核对日期：2026-10-21。本文包含 **5 个项目案例**，其中 4 个阅读了官方仓库的相关实现，1 个只核对了官方产品文档；均未安装、调用付费模型或实跑云端任务。仓库公开实现能说明这些版本怎样工作，不能直接证明公司所有线上产品都采用相同实现，也不能证明某项设计提高了多少成功率。

| 项目 | 主要学习对象 | 证据状态 | 固定版本与许可 |
| --- | --- | --- | --- |
| Qwen Code，阿里终端智能体 | 系统提示词装配、工具可用性、技能加载与缓存 | 已读官方源码及设计文档 | `461be87304c7b3b5d64b701207c49f236515d5fd`；Apache-2.0 |
| Qwen-Agent，阿里智能体框架 | 知识注入、工具描述、消息转换、调用循环 | 已读官方源码 | `31a4d36d123688581a9e9744427272b33ce940e0`；Apache-2.0 |
| AgentScope，阿里开源智能体框架 | 工具分组、技能摘要、模型请求组装 | 已读官方源码 | `b2a084799bf883a5a8d0f56e44f205f78a83f0fe`；Apache-2.0 |
| CloudBase AI Toolkit，腾讯云开发工具包 | 业务技能、命令行回退、工具返回、审查与同步维护 | 已读官方技能与实现 | `f49b8d481373937b3c39012deef6cf5da829ef6e`；MIT |
| CodeBuddy / WorkBuddy，腾讯开发与办公助手 | 技能配置、独立子代理、企业分发 | 仅官方产品文档 | 核对当日页面；未找到对应公开实现提交，文档转载许可未确认 |

上述四个开源仓库的根许可证均已打开核对。CloudBase 的技能文件也声明 MIT。本文只保存原创分析与原文入口，不搬运上游全文。

## 1. Qwen Code：提示词要和当前会话的真实能力一致

**来源与归属。** [官方产品页](https://qwen.ai/qwencode)与[官方仓库](https://github.com/QwenLM/qwen-code)相互对应。项目承认最初基于 Google Gemini CLI，因此不能把仓库中所有设计都归为阿里原创；研究对象是阿里维护的这个具体版本及其可复用实现。

| 阅读入口 | 关注点 |
| --- | --- |
| [提示词构造器 `prompts.ts`](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/packages/core/src/core/prompts.ts) | 系统提示词分层、交互模式、按真实工具集合筛选指引和调用示例 |
| [技能工具 `skill.ts`](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/packages/core/src/tools/skill.ts) | 静态工具描述、运行时技能集合、首次加载和重复加载 |
| [技能上下文辅助函数 `skill-utils.ts`](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/packages/core/src/tools/skill-utils.ts) | 技能正文与技能根目录如何一起交给模型 |
| [按常驻工具集装配提示词：中文设计文档](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/docs/design/2026-09-18-resident-tool-prompt-assembly.zh-CN.md) | 为什么出现“提示词要求调用的工具并不存在”，以及设计约束和已知残留 |

**调用前的上下文。** `assembleSystemPrompt`（系统提示词装配函数）把基础行为规则、媒体指引、项目上下文、追加指令、自动记忆放在明确的顺序中。交互式命令行、无人交互运行、由宿主中转问答三种模式会得到不同的问询规则。工具相关指引接收 `declaredTools`（实际声明的工具集合）；示例涉及当前不可调用的工具时，可以整块移除。这里的关键是把“模型被告知能做什么”和“请求真的提供什么”对齐，而不是继续加长提示词。

**技能如何进入模型。** 技能工具自身的描述保持不变；可用技能目录通过会话开始的提示消息及后续增量消息更新。模型按准确名称调用技能工具后，工具返回正文并附技能所在目录，供模型定位脚本和参考资料。已经驻留在上下文中的技能再次调用时，通常只返回简短确认，避免重复注入；实现也处理技能内容变化等失效情况。[技能实现](https://github.com/QwenLM/qwen-code/blob/461be87304c7b3b5d64b701207c49f236515d5fd/packages/core/src/tools/skill.ts)把保持工具声明稳定与提示词缓存关联起来，但本文未测量实际节省。

**最值得迁移的方法。** 在自己的 Agent 中，先记录“实际发给模型的系统提示词、工具声明和技能目录”，再分析选错工具的原因。单看某份提示词文件，容易漏掉工具不可用、模式不匹配、重复上下文这三类工程问题。需要借鉴的最小单元是“提示词构造器＋工具集合快照＋技能正文加载器”，无需复制整个终端产品。

**证据边界。** 中文设计文档自称方案稿，含历史代码版本和待决问题；本文用当前固定提交的实现核对主要机制，没有把文档里的计划全部视作已经上线。其源码还明确保留部分例外，所以不能表述为“提示词绝不会提到任何未声明工具”。

## 2. Qwen-Agent：把一次工具调用前后的消息变化读清楚

**来源与归属。** [QwenLM 官方仓库](https://github.com/QwenLM/Qwen-Agent)的实现文件标有 Qwen 团队、Alibaba Group 的版权信息。这个案例适合学习一个小而完整的调用链，不必先理解大型产品的全部功能。

| 阅读入口 | 关注点 |
| --- | --- |
| [助手与知识注入 `assistant.py`](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/agents/assistant.py) | 将检索片段整理为“来源＋内容”，加入系统消息 |
| [工具调用循环 `fncall_agent.py`](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/agents/fncall_agent.py) | 模型输出、工具执行、结果回填以及调用轮数上限 |
| [工具基础接口 `tools/base.py`](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/tools/base.py) | 名称、描述、参数结构、实际执行函数、参数验证辅助方法 |
| [函数调用适配器 `function_calling.py`](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/llm/function_calling.py) | 根据配置选择模型需要的调用格式 |
| [默认 Nous 格式的提示词与解析实现](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/llm/fncall_prompts/nous_fncall_prompt.py) | 工具说明写入系统消息、调用与返回的格式转换 |
| [基础 Agent 的工具执行 `agent.py`](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/agent.py) | 普通异常怎样作为可读错误返回；哪些异常继续抛出 |

**调用前后到底发生什么。** 用户消息和文件先进入助手；如果没有直接提供知识文本，助手调用其记忆／检索模块获得片段。片段整理为带来源的知识段落，追加到首条系统消息；原本没有系统消息时则新建一条。随后工具调用 Agent 将各工具的 `name`（名称）、`description`（用途说明）、`parameters`（参数结构）交给模型适配层。模型返回工具调用后，程序执行实际工具，将结果附到消息列表，再请求下一轮，直到不再调用工具或达到轮数上限。

**值得特别核对的细节。** 固定提交里的 `fncall_prompt_type`（函数调用提示词类型）默认值是 `nous`，不能因为文件名里有 `qwen_fncall_prompt.py`，就断言所有调用都使用后者。Nous 适配层会把工具声明组织为模型可读的提示内容，并把历史调用、工具结果转换为对应格式；使用原始接口的路径可以跳过这一步。所谓“同一个工具定义”，在不同模型接口前仍可能需要不同的上下文表示。[适配器](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/qwen_agent/llm/function_calling.py)

**可迁移的方法。** 把业务规则、外部知识、工具接口、模型格式适配分开维护。调试时至少保留“适配前的消息”“适配后的模型请求”“工具返回”三份证据，才能区分选错工具、参数错误和格式不兼容。工具基类提供参数校验辅助方法，但具体工具仍需正确调用和实现它；普通执行异常可返回模型继续处理，也有异常会向上抛出，不能一概称为自动修复。

**证据边界。** 这里描述的是源码控制流；没有实际执行模型与检索任务，也没有据此证明检索结果质量或工具调用成功率。

## 3. AgentScope：技能目录与工具集合要一起随任务收缩

**来源与归属。** [阿里云官方接入文档](https://www.alibabacloud.com/help/en/agentloop/integrating-the-agentscope-java-application)明确说明 AgentScope 是阿里开源的智能体框架。本文阅读的是 [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) 的 Python 主仓固定提交；该仓已使用新一代接口，不能直接把旧版 `ReActAgent`（推理与行动交替的智能体）教程当成当前源码说明。

| 阅读入口 | 关注点 |
| --- | --- |
| [工具集合管理 `_toolkit.py`](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/tool/_toolkit.py) | 按激活组收集工具与技能；生成技能摘要提示词 |
| [技能读取工具 `_skill.py`](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/tool/_builtin/_skill.py) | 模型按名选择后，返回完整正文；未找到则返回明确错误 |
| [本地技能加载器 `_local_loader.py`](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/skill/_local_loader.py) | 校验名称与描述、读取正文、按文件修改时间缓存 |
| [Agent 请求装配 `_agent.py`](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/agent/_agent.py) | 系统指令、摘要、对话、工具声明进入模型的具体顺序 |

**模型看到的内容。** `get_skill_instructions`（技能目录提示词生成方法）列出可用技能的名称、描述、目录，并说明先用技能读取工具获得正文，再照正文调用实际工具。它接收当前已激活的工具组；基础组始终存在，其他组按状态参与。模型选中某个技能后，技能读取工具只从当前可用集合找对应正文，因此“目录里看得到”和“读取时取得到”使用同一组状态。

**一次模型请求。** `_prepare_model_input`（模型输入准备方法）先建立系统消息，再放压缩摘要和当前对话；工具声明也根据当前激活组生成。系统消息由基础指令、技能目录、工作区／结果外置说明组成，随后允许中间件依次加工。这里可以直接看见“摘要放在哪”“技能放在哪”，而非只听到上下文管理的抽象说法。[请求装配实现](https://github.com/agentscope-ai/agentscope/blob/b2a084799bf883a5a8d0f56e44f205f78a83f0fe/src/agentscope/agent/_agent.py)

**可迁移的方法。** 当工具越来越多，按任务激活一组互相配套的工具和技能，比仅隐藏工具名更完整。对于自己的多业务 Agent，可以把“题库操作工具＋出题技能”或“订单工具＋退款技能”放进同一能力组。这个分组例子是本仓的迁移建议，不是 AgentScope 官方案例。还应检查重名技能行为：当前收集代码会记录警告并以后者覆盖，不能默认所有名称冲突都会阻止运行。

**证据边界。** 本文阅读了上述函数及相邻逻辑，未穷尽整个 Agent 类，也未测量分组后的选择准确率、延迟或费用。

## 4. 腾讯 CloudBase：把业务踩坑写成可执行的技能体系

**来源与归属。** [腾讯云开发官方文档](https://docs.cloudbase.net/ai/cloudbase-ai-toolkit/prompts/how-to-use)直接链接腾讯 CloudBase 工具包，并区分 MCP（工具连接与调用协议）提供实际工具、Skill（技能）提供开发规则与经验。这是一组能公开读取的官方技能，不需要借助第三方归档来推定来源。

| 阅读入口 | 关注点 |
| --- | --- |
| [总入口技能 `cloudbase/SKILL.md`](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/config/source/guideline/cloudbase/SKILL.md) | 场景路由、先决条件、技能边界、常见错误 |
| [命令行技能 `cloudbase-cli/SKILL.md`](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/config/source/skills/cloudbase-cli/SKILL.md) | 先读基础参考，再按业务读取；命令失败的诊断和接口回退 |
| [PostgreSQL 工具 `databasePG.ts`](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/mcp/src/tools/databasePG.ts) | 查询与修改接口、任务状态、结构化后续动作 |
| [代码审查技能 `cloudbase-code-review/SKILL.md`](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/config/source/skills/cloudbase-code-review/SKILL.md) | 业务规则、模型语义审查、错误经验进入规则的门槛 |
| [技能文档同步检查 `check-prompts-sync.mjs`](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/scripts/check-prompts-sync.mjs) | 技能覆盖、生成物漂移、参考文件与文档链接一致性 |

**上下文和执行顺序。** 总入口先判断业务属于登录、数据库、云函数还是部署，再要求读取对应技能。命令行技能要求先加载基础参考，之后只读取当前任务需要的业务文件，并在足够完成当前任务时停止继续加载。MCP 工具在本轮尚不可用时，有明确的命令行替代路径，同时留下后续接入配置。这些都是写给模型的工作指引；是否准确触发仍取决于宿主和模型，官方文档也承认单独安装技能的自动选用并不总是稳定。

**经验写得具体在哪里。** 命令行技能解释“帮助命令报错”不等于“该命令不存在”，给出继续确认语法和查询文档的路径；区分国内站与国际站；要求操作后用查询确认效果；多次失败后重新检查接口、环境和权限。这类内容把真实失败模式写成“症状—核对项—下一步”，比空泛要求模型谨慎更可操作。具体平台规则只适用于相应版本，不宜直接搬到其他云厂商。

**接口也在教模型继续工作。** 数据库工具使用 `success`（是否成功）、`data`（业务结果）、`message`（说明）、`errorCode`（错误类别）、`nextActions`（建议下一步）组织返回。迁移任务可以处于待完成或超时状态，并提供任务标识和后续查询路径。这里能学到：异步任务的返回应明确区分“尚未完成”和“操作失败”，避免模型看到超时便重新执行修改。[数据库工具实现](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/blob/f49b8d481373937b3c39012deef6cf5da829ef6e/mcp/src/tools/databasePG.ts)

**经验怎样维护。** 审查技能明确要求，单次失败和个案绕法不能直接升格为硬规则；应有稳定接口文档、重复失败或确定行为支持。规则文件包含适用模块、严重程度、阶段、模型语义检查和修复指引。另有同步脚本检查技能源、生成文档和链接目标是否一致。对研究仓库最有价值的迁移是：每条经验保存适用条件和证据；改技能时同时维护目录、参考文件和对外文档，避免“文件写好了但 Agent 永远发现不了”。

**证据边界。** 技能正文表示官方提供给 Agent 的指令，不等于运行时已强制执行；工具代码才说明程序真正做了哪些校验。本文没有登录腾讯云、执行部署或运行其同步脚本，也不把指令中的目标表述当成实测收益。

## 5. CodeBuddy / WorkBuddy：公开扩展契约也值得收集

**来源与证据。** [CodeBuddy 官方技能文档](https://www.codebuddy.cn/docs/cli/skills)描述项目级、用户级技能目录，以及 `description`（用途与触发描述）、`allowed-tools`（工具白名单）、`context: fork`（独立子代理上下文）等配置。本文只核对文档，未取得相应内部实现和系统提示词。

**可学习的契约。** 文档将模型是否可自动调用、用户是否能从菜单调用、是否需要独立上下文分开配置。独立子代理模式将技能内容作为任务提示交给子代理，再把结果交回主会话；相应钩子可绑定子代理生命周期。由此得到的迁移建议是：写技能时同时明确触发者、所需工具和结果返回位置，不能只写一段“你是专家”的角色描述。该建议是对公开契约的分析，并未复现 CodeBuddy 行为。

[腾讯企业技能管理文档](https://www.tencentcloud.com/document/product/1316/84533)还区分企业统一分发与成员自定义来源，管理可见范围和使用权限。这提供另一条研究线：多人共用技能时，内容版本、谁能看到、谁能更新也属于技能工程。它不构成“WorkBuddy 内置技能原文已经完整开源”的证据。

## 阅读与复用建议

想先搞懂最基础调用过程，读 Qwen-Agent 的助手、调用循环和模型适配器；想看终端产品如何工程化提示词，读 Qwen Code 的提示词构造器与技能工具；想学习多能力管理，读 AgentScope 的工具集合与请求装配；想学习业务技能怎么写、怎么维护，优先读腾讯 CloudBase 的入口、命令行技能和审查规则。CodeBuddy 文档适合核对扩展接口，研究其内部实现时应继续寻找公开代码或可复核运行轨迹。

以上阅读顺序是本仓建议。所有“可迁移的方法”都需要在自己的任务、模型和工具条件下验证，不代表上游已为这些迁移场景提供效果证明。
