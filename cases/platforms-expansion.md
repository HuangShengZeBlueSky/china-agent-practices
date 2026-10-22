# 平台与工具扩展：把 Agent 运行过程变成可读、可检查的工程

核查日期：2026-10-21。本轮新增 **10 个项目级来源记录**，对应 **32 个实现、提示或技能文件**，另读各项目 README 与许可证共 20 个文件。52 是文件条目数，不是 52 个独立项目。各文件均固定到同一项目的 commit；大文件只核查本文涉及的函数与段落，结构化清单记录了阅读范围。

本页覆盖构图、上下文、界面操作、服务封装、沙箱命令、技能分流及评估。所有案例都是**源码静态核对，未实跑**：没有安装上游依赖、运行其脚本、连接业务账号或调用在线模型。Skill 中的命令与操作要求是研究对象，不是本次任务的执行指令。官方仓库说明公开代码的来源；它不能单独证明闭源产品全部采用同样实现，也不能证明每段代码或提示措辞首次由该公司发明。

这里的 **schema** 指字段与类型契约；**middleware** 指在模型或工具调用前后处理请求的中间件；**checkpoint** 指供恢复使用的状态快照；**trace/span** 指一次执行及其中子步骤的观测记录。

## 阅读入口

| 项目 | 本次具体切口 | 先学什么 |
| --- | --- | --- |
| Coze Studio | 单 Agent 构图与 Jinja2 系统提示 | 提示装配与工具分支如何相互约束 |
| Coze Loop | 提示评估器执行与输出解析 | 评估版本、实际输入和错误能否回查 |
| DeerFlow 2.x | 技能入口与工具输出预算 | 什么时候只给索引，什么时候读正文 |
| UI-TARS Desktop | GUI Agent SDK 的动作循环 | 截图、动作语法、解析器和执行器的边界 |
| AgentScope Runtime | AgentApp 与沙箱结果适配器 | 推理逻辑如何获得服务生命周期 |
| OpenSandbox | 命令 Skill、接口与 SSE adapter | 后台句柄、日志、超时和重试的语义 |
| AWorld CLI | 技能选择与会话压缩 | 恢复时需要哪些显式状态和证据 |
| BrowserSkill | 浏览器 Skill 与元素引用实现 | 观察、操作、错误恢复如何闭环 |
| Tencent RTC Agent Skills | 路由、session 工具与评估提示 | 技能不能独自承担哪些状态管理责任 |
| SkillHub | 官方检索/评估 Skill 与校验器 | 质量判断与格式合规分别由谁保证 |

## 1. Coze Studio：提示词是构图结果的一部分

**证据版本：** `fefb05ff27be1da939612fbf9faf5db62583b8ae`；[Apache-2.0 许可](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/LICENSE-APACHE)；源码静态核对，未实跑。

**来源。** [项目 Wiki](https://github.com/coze-dev/coze-studio/wiki/1.-What-is-Coze-Studio)明确把 Coze Studio 介绍为字节扣子平台的开源版本；[README](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md)链接扣子官网，并致谢 Eino 与 FlowGram。归属成立，但本案不把底层框架、前端画布和公开平台全部能力概括成扣子从零原创。

**输入到产物。** 输入是用户消息、Agent 配置和会话状态。程序先准备人设变量、知识检索和工具预取，将结果送入提示模板；模板的系统段含人设、时间、记忆变量和知识内容，再接聊天历史及当前输入。这里模型看到的内容不只是一段手写 persona，而是多条程序路径的汇合结果。[构图实现](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/agent/singleagent/internal/agentflow/agent_flow_builder.go)与[消息模板](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/agent/singleagent/internal/agentflow/node_chat_prompt.go)能够交叉核对这个顺序。

**程序与模型分工。** `BuildAgent` 先收集插件、工作流、数据库和变量工具；有工具时检查模型 Function Call 能力，建立 Eino ReAct 子图，并配置 checkpoint store 与允许直接返回的工作流工具；没有工具时使用 ChatModel 节点。模型负责在绑定的工具范围内生成请求或回答，程序负责工具集合、分支和图的连接。仅从这里能确认“恢复所需存储被配置”，还不能宣称任意工作流已成功恢复。[公开系统提示](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/backend/domain/agent/singleagent/internal/agentflow/system_prompt.go)中的内容约束也只是提示要求，不是强制执行的证据。

**迁移学习。** 拆一个 Agent 时，应同时找“提示文本在哪里”和“哪些节点生成它的变量”；把能力检查、工具有无、直接返回条件写成程序分支。可做的验证是固定输入，分别给无工具、有工具但模型不支持、可用工具三种配置，检查形成的模型请求和结束路径。本次未执行这组验证，也未比对商业扣子的实际请求。

## 2. Coze Loop：让评估器自己也有版本和执行记录

**证据版本：** `95dc2eebbc100b929c102d90111bb94fad41e500`；[Apache-2.0 许可](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/LICENSE)；源码静态核对，未实跑。

**来源。** [README](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/README.md)将开源版定义为基于商业版开放的核心模块，链接[扣子罗盘](https://www.coze.cn/loop)，并使用字节安全响应渠道。本案研究提示词评估器，未遍历整个实验平台。

**输入到产物。** 输入包括评估器版本、待评字段和模型配置。`PromptEvaluatorVersion` 保存消息、输入 schema、解析方式、工具与版本。运行路径依次做基础信息和输入校验、变量渲染、模型调用、结果解析，产出 score、reason、token 使用、状态及错误。模板渲染、模型调用和输出解析分别建立 span，根 span 带 evaluator ID 和 version，使同一评分可以回到实际使用的模板和模型请求。证据见[版本实体](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/backend/modules/evaluation/domain/entity/evaluator_version_prompt.go)及[执行实现](https://github.com/coze-dev/coze-loop/blob/95dc2eebbc100b929c102d90111bb94fad41e500/backend/modules/evaluation/domain/service/evaluator_source_prompt_impl.go)。

**失败是产物的一部分。** Function Call 模式要求工具调用并从参数提取分数和理由；正文模式按直接解析 JSON、修复 JSON、提取 JSON 片段、提取分数逐级尝试。调用失败、空响应和解析失败进入明确错误状态，而不是自动当成低质量答案。不同解析策略仍可能接受不完整或错误判断，格式修复不等于评分正确。

**迁移学习。** 给自己的评估器同时记录版本、输入映射、模型响应和解析方式，再把“被测任务答错”与“评估器没有正常运行”区分开。若准备采纳宽松解析，应保留原响应并检查每种回退是否改变分数含义。本次没有调用评委模型、运行实验或测量评分与人工判断的一致性。

## 3. DeerFlow 2.x：技能与工具结果都需要上下文预算

**证据版本：** `d4012c4b24f9b5ee14236a8214c82815de5b5214`；[MIT 许可](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/LICENSE)；源码静态核对，未实跑。

**来源与版本。** [README](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/README.md)明确说明 2.x 为重写版本，旧研究框架在 1.x 分支；本案使用当前 2.x 文件。源码直接依赖 LangChain/LangGraph，许可证同时列出 ByteDance 和 DeerFlow Authors，不能把社区框架机制或后续社区贡献都写成字节独创。

**模型调用前。** `apply_prompt_template` 根据子 Agent、技能、内存、延迟工具和 bash 可用性组装不同指引。技能入口有两种代码路径：传统完整元数据列表；调用方传入技能名集合时使用紧凑名称索引，让模型再通过 `describe_skill` 发现详情。传统路径要求先读主文件、再按需读支持资料；显式 `/skill-name` 由中间件注入正文，避免再次读取同一主文件。技能可见与是否获准激活另有检查。[提示构建](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/backend/packages/harness/deerflow/agents/lead_agent/prompt.py)和[激活中间件](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/backend/packages/harness/deerflow/agents/middlewares/skill_activation_middleware.py)证明存在这些分支，本次未确认所有部署的默认选项。

**工具返回后。** [输出预算中间件](https://github.com/bytedance/deer-flow/blob/d4012c4b24f9b5ee14236a8214c82815de5b5214/backend/packages/harness/deerflow/agents/middlewares/tool_output_budget_middleware.py)先看结果大小，超出阈值时把正文写到宿主映射目录或远端沙箱，模型侧收到摘要和回读路径；持久化不可用时保留头尾并提示省略，尽量把命令退出码留在结尾。它还可以在模型请求副本中省略被后续成功读写取代的旧 `write_file` 大参数，同时保留原消息和检查点。当前模型上下文与完整运行记录因此具有不同用途。

**迁移学习。** 技能发现可先给小索引，命中后再展开；工具大结果可先保存、再返回定位信息。真正要验证的是模型能否读回被省略的关键内容、退出状态是否还在、压缩后能否继续任务。本次未测 token 节省、延迟或成功率，不能据代码中的预算逻辑宣称这些指标已经改善。

## 4. UI-TARS Desktop：把动作语法与环境观察接起来

**证据版本：** `3ac2cb8d946d78d5ff92ad17b318eaafa18c178c`；[Apache-2.0 许可](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/LICENSE)；源码静态核对，未实跑。

**范围。** 本案读的是字节官方仓库内的 `multimodal/gui-agent/agent-sdk`，不是模型权重，也不是所有 Desktop 和 Agent TARS 入口。三个文件中的版权/许可标记与[README](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md)共同给出来源。

**输入到下一次输入。** 用户任务、历史动作和截图进入模型；[提示模板](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/multimodal/gui-agent/agent-sdk/src/prompts.ts)列出点击、拖动、输入、等待和完成等语法，并提示参数转义规则。构造器也支持用 operator 的动作集合装配模板。[ToolCallEngine](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/multimodal/gui-agent/agent-sdk/src/ToolCallEngine.ts)累积流式文本，在完整响应后交给自定义或默认解析器，再转换为统一工具调用。文件顶部有“无流式支持”的旧注释，但当前实现确实有流式累积函数；因此这里依据函数行为描述，未把注释当成全部事实。

**执行与恢复线索。** [GUIAgent](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/multimodal/gui-agent/agent-sdk/src/GUIAgent.ts)负责坐标归一化和 operator 执行，操作后重新截图并加入页面 URL，以 `environment_input` 事件供后续模型使用。解析失败产生带 `errorMessage` 的工具结果；历史保留模型原始动作文本，便于后续解释失败。模型输出 `finished` 会影响循环终止，但单凭这个词不能证明界面目标已实现。

**迁移学习。** GUI Agent 的可复用单元是“动作语法—解析—执行—新观察”契约。加入新动作时要同时检查提示、解析器与 operator；验收还要检查页面上的实际成功信号。这里未运行桌面、未验证模型与模板兼容性，也没有成功率结论。

## 5. AgentScope Runtime：把 Agent 查询变成可管理的服务

**证据版本：** `22072fd7075ce0c6f43cb39509d6a14b0e60ddb5`；[Apache-2.0 许可](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/LICENSE)；源码静态核对，未实跑。

**维护状态先于选型。** [README](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/README.md)已发布迁移公告，称能力整合进 AgentScope 2.0，并计划归档该仓库；核查时 GitHub `archived` 仍为 false。此处保留为历史架构案例，不能写成“已经归档”，也不把它推荐为新的独立主线。许可证标注 Alibaba，阿里云亦有[相关集成文档](https://www.alibabacloud.com/help/en/tablestore/memory-storage-service-sub-product-test/agentscope-runtime-with-tablestore)。

**输入到产物。** [AgentApp](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/src/agentscope_runtime/engine/app/agent_app.py)在 FastAPI 上登记查询函数，绑定 Runner，并在服务层处理启动/关闭生命周期、SSE 流式响应和按用户/会话的中断管理。A2A、Responses 与 AG-UI 协议适配在这里注册，相关 schema 被加入 OpenAPI。模型与业务上下文仍由被包装的 Agent/Runner 路径处理；服务封装不等于重新实现模型推理。

**工具接口。** [沙箱工具适配器](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/src/agentscope_runtime/adapters/agentscope/tool/sandbox_tool.py)保留函数签名和 docstring，便于 Toolkit 生成工具 schema；返回值若已是 ToolResponse 则直接使用，否则尝试把 MCP 内容块转换为 AgentScope 结构，失败时退回文本。这个文件解释了为什么工具接口不仅是函数名，还包括输入描述、内容块和错误情况下的可消费格式。

**迁移学习。** 在业务 Agent 外放一层清楚的运行契约：谁启动、谁清理、怎么停止、如何输出事件、外部协议如何映射。这里仅核查服务包装与工具返回适配，没有部署服务或验证协议互操作、沙箱隔离和所有并发场景；FastAPI、MCP 和 A2A 的上游贡献应单独归属。

## 6. OpenSandbox：命令不是“发出去就算完成”

**证据版本：** `62d3e59d10796154b88510f39fca8438eb99dd58`；[Apache-2.0 许可](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/LICENSE)；源码静态核对，未实跑。

**来源变化。** 原[alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox)的 API 已重定向到 `opensandbox-group/OpenSandbox`，当前[README](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/README.md)仍列出 Alibaba 命名空间的 SDK。这里标记“阿里来源 / OpenSandbox 社区”，不根据组织名推断现行治理或公司控制关系。

**输入到产物。** [命令 Skill](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/cli/src/opensandbox_cli/skills/opensandbox-command-execution.md)明确区分三条路径：前台命令直接读流；后台命令拿 execution ID，后续查 status 和增量 logs；需要工作目录或环境状态持续存在时创建 session。命令 payload 使用明确分隔符，超时、工作目录和 session 清理有各自语义。[Commands 协议](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/sdks/sandbox/python/src/opensandbox/services/command.py)则给出 run、interrupt、状态、日志及会话生命周期的接口。模型在宿主中选择调用；沙箱 SDK 本身不负责决定任务计划。

**重试边界。** [Python adapter](https://github.com/opensandbox-group/OpenSandbox/blob/62d3e59d10796154b88510f39fca8438eb99dd58/sdks/sandbox/python/src/opensandbox/adapters/command_adapter.py)把 SSE 执行流与简单控制 API 分开。SSE POST 明确绕开可重试 transport，因为重发会让非幂等命令重复执行。前台继续读取到流结束，以兼容结束事件后的尾部输出；后台在相应确认事件后结束该次响应，任务最终状态仍应另查。连接返回、执行启动和任务完成是不同证据。

**迁移学习。** 任何有副作用的 Agent 工具，都应说明重试是否会重复产生结果、何时返回句柄、怎样查询完成、日志游标怎样推进。可先在可控环境用无副作用命令测试断流和重试行为。本案未部署或执行沙箱，未验证隔离强度，也没有把启动响应当成执行成功。

## 7. AWorld CLI：技能选择与压缩恢复都留下状态

**证据版本：** `82af4062e29e128910afa8622c866f4b99a4d23d`；[MIT 许可](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/LICENSE)；源码静态核对，未实跑。

**来源。** [inclusionAI 官方文章](https://www.inclusion-ai.org/blog/aworld/)署名 Ant Group、Agent Team at inclusionAI，并链接仓库。本案仅研究当前 CLI 文件，不复述文章中的排行榜，也不把“自进化”产品目标当作已验证效果。

**技能路径。** [运行时 registry](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/runtime_skill_registry.py)合并插件、兼容目录和内置 provider；[激活解析器](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/skill_activation_resolver.py)先过滤可见性、禁用项、作用域与 Agent 匹配，再合并显式请求和默认技能。自动选择路径使用关键词出现次数评分并选择最高匹配项，未使用这里没有的语义向量检索。结果分成 available 与 active，并为激活包记录规范路径和指纹；包无法读取时不制造证据。

**压缩路径。** [压缩提示](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/compact_history_prompt.txt)要求保留用户意图、文件、错误、反馈、待办和正在做的工作；[context.py](https://github.com/inclusionAI/AWorld/blob/82af4062e29e128910afa8622c866f4b99a4d23d/aworld-cli/src/aworld_cli/core/context.py)检查 token 统计，提取有大小上限的工作区信息，把历史和工作区作为摘要输入，保存摘要后尝试创建 Context 检查点。若检查点失败，返回“摘要已保存、检查点失败”的结果，避免把部分完成笼统写成成功。

**迁移学习。** “能发现技能”“本轮选中了技能”“恢复时确实用了哪一包”应分别保存；压缩除了摘要文字，还需要记录检查点是否建立。这里未实跑路由或恢复，没有测摘要保真度，也没有追溯提示措辞的最初作者；官方仓库收录与原创归属是不同问题。

## 8. BrowserSkill：错误恢复应回到当前页面状态

**证据版本：** `6214e3d6a3d74eaf39c0202c4f182b5755974da9`；[MIT 许可](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/LICENSE)；源码静态核对，未实跑。

**来源与切口。** 腾讯官方组织仓库和[许可证](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/LICENSE)确认来源。这里同时读了面向模型的 Skill 与元素引用、安装来源标记的实现，避免只从产品介绍推断执行行为。

**任务路径。** [主 Skill](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/crates/bsk-cli/skill/SKILL.md)要求先定义成功条件，建立 session，observe 获取元素引用，再行动；导航或页面大幅变化后重新观察，完成后停止自有 session。细节按调试、截图、文件、标签页等任务分到引用文件。它是渐进加载的可读范例：主文件告诉模型何时加载哪份说明，未把所有命令细节一起塞入上下文。

**实现与契约互证。** [snapshot-ref.ts](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/apps/extension/src/tools/snapshot-ref.ts)从会话 ref store 查元素并核对 tab；未知或跨标签页引用返回结构化错误，视觉区域引用不会转为 DOM 目标。[恢复说明](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/crates/bsk-cli/skill/references/help-and-recovery.md)区分失效引用、未知会话、超时但效果未知、人工帮助取消等情况。超时后先检查当前状态很关键，因为操作可能已经发生，立即重试可能重复提交。

**包维护也是技能工程。** [provenance.rs](https://github.com/Tencent/BrowserSkill/blob/6214e3d6a3d74eaf39c0202c4f182b5755974da9/crates/bsk-cli/src/skill_install/provenance.rs)维护版本化标记、各文件 SHA-256 和更新前状态，为判断“用户改过”或“安装中断”提供依据。这个文件本身不是完整更新事务，本案不声称已验证整个升级过程。

**迁移学习与边界。** 把观察引用、动作目标和会话归属关联起来，让错误提示指导下一步观察；把技能升级也当作需要来源记录的文件更新。没有启动浏览器，没有测试真实页面；Skill 中的权限与恢复要求也不自动等于宿主已强制落实。

## 9. Tencent RTC Agent Skills：路由、状态与评估各有责任

**证据版本：** `55a6bcf643acb4104105359ed0a1d194bdee7696`；[MIT 许可](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/LICENSE)；源码静态核对，未实跑。

**来源。** [Tencent RTC 官方页面](https://trtc.io/agent-skills)提供 Agent Skills 介绍，仓库许可标明 Tencent RTC。它是公开 SDK 集成技能集合，不能据此声称发现了 CodeBuddy/WorkBuddy 的完整内部 Agent。

**从问题到交接。** [根 trtc Skill](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/skills/trtc/SKILL.md)读取已有 session，识别产品、平台与意图，路由到对应 owner Skill，并说明何时停止分发。[AI 客服 Skill](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/skills/trtc-ai-service/SKILL.md)把技能资源根目录与用户项目根目录分开，给出能力装配、接口、健康检查和交付约定。它在纯后端路径中的验收是健康、自建控制面返回任务/会话 ID、样例代码交付，真实语音质量仍由用户前端验证；不能把这组控制面检查扩大成全业务效果已验证。

**状态交给程序。** [session.py](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/skills/trtc/tools/session.py)的 transaction 在文件锁内重读磁盘版本，使用 state_version 比较交换（CAS）拒绝过时更新，校验 schema 后写临时文件并替换目标；迁移代码把旧 current_step 拆到会话状态与 flow 状态。函数也明确存在无 fcntl 时的无锁降级，因此不能宣称全部平台有同样并发保证。本文依据函数核对，未把文件头所有设计备忘和待办当成已经完成。

**评估不是普通交互。** [评估专用提示](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/.claude/skills/trtc-eval/prompts/ai_driver_system_prompt.md)覆盖正常引导流程，要求固定代码路径、依赖声明和 Web 自动运行入口；知识不可读时输出 `kb_unreachable`，让评估环境问题与知识质量问题分开。[静态 evaluator](https://github.com/Tencent-RTC/agent-skills/blob/55a6bcf643acb4104105359ed0a1d194bdee7696/.claude/skills/trtc-eval/scripts/evaluator.py)只按必须/禁止字符串计算命中和分数。静态分数既不证明可编译，也不证明 SDK 业务成功；本次未运行评估或在线上报流程。

**迁移学习。** 用小的根 Skill 负责路由，用专门工具管理可恢复状态，再以不同层次的证据验收代码与运行结果。尤其要记录评估模式改变了哪些正常假设，否则容易把测试提示的能力当成真实用户流程的效果。

## 10. SkillHub：报告能被解析，不代表结论已经成立

**证据版本：** `a051f06f7944d24ade04bea27735f430b19a8298`；[MIT 许可](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/LICENSE)；源码静态核对，未实跑。

**来源与许可。** [README](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/README.md)明确本仓库公开 API 文档、DeepSeek Harness 插件和官方 Skills，并说明平台聚合全球同步与用户上传内容。因此这里的“腾讯官方”只描述仓库及其官方维护文件，不能扩展成平台上全部技能均为腾讯原创。GitHub license 元数据返回 NOASSERTION，但[实际 LICENSE](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/LICENSE)明确写 MIT，登记以正文为准。

**发现流程。** [find-skill-skillhub](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/skills/find-skill-skillhub/SKILL.md)先将需求拆成场景、分类和中英文关键词，多次召回并按 slug 去重，再用名称和描述判断契合度。热度只是相近候选的排序线索，不能替代任务匹配。API 与分类细节放在 references，主文件保留工作流。该流程由 Skill 规定；本次没有在线查询 API 或验证推荐效果。

**评估流程。** [TRACE Skill](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/skills/skillhub-trace-evaluator/SKILL.md)先读取技能包，再分维加载细则，要求每项有面向开发者和普通用户的理由，最终输出 JSON。[校验器](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/skills/skillhub-trace-evaluator/scripts/validate_trace_scores.py)检查五维、子项、分数范围和非空文本。Skill 要求安全扫描项 `trust.scan` 为 skipped，但校验器也兼容平台式已评分 scan；这个差别说明文本要求与代码校验覆盖范围并不完全一致。

**迁移学习。** 把检索召回、任务重排、基于证据的评价与格式校验拆成不同环节，分别记录完成证据。校验通过只能证明结构和数值规则合规，不能证明理由来自真实阅读、分数准确或已完成安全扫描。没有实跑评价或验证任何包的质量。

## 如何把本页转成自己的学习任务

这些项目共同提示的是若干可检验的问题，而不是一套已经证明通用有效的模板：

1. **模型最终看到什么？** 同时追踪提示文件与组装函数，保存一次完整的模型请求快照。
2. **大结果还能找回来吗？** 若使用索引、外置文件或摘要，检查关键证据回读路径与失败回退。
3. **重复操作会怎样？** 对有副作用的工具明确句柄、状态、断流和重试语义。
4. **“完成”由谁宣布？** 区分模型终止标记、进程退出、接口成功、产物存在与用户目标达成。
5. **评估失败能解释吗？** 分开环境不可用、输入不合法、模型调用失败、解析失败和任务质量。
6. **来源和版本能复原吗？** 保留 commit、许可证、实际读过的文件、上游依赖与迁移状态。

以上是由所读实现推导的实验方向；尚无本仓库自己的运行结果支持效果比较。结构化记录见 `catalog/sources.json` 中同名来源；新增记录的整合由仓库维护流程完成。

