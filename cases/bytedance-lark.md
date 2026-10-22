# 字节跳动与飞书：把经验写进模型能执行的接口

核验日期：2026-10-21。本文包含五个拆解案例，区分官方代码、官方维护规范与第三方归档。所列提交是本次分析固定的快照，不承诺等于当前主分支最新提交。结论来自静态阅读；本次没有登录飞书、运行 CLI、调用付费模型或验证真实任务成功率。

## 一、飞书 CLI：把底层接口变成适合 Agent 调用的产品

**原文入口与来源。** [飞书官网 CLI 页面](https://www.feishu.cn/feishu-cli)和[开放平台说明](https://open.feishu.cn/document/mcp_open_tools/feishu-cli-let-ai-actually-do-your-work-in-feishu)指向 [larksuite/cli](https://github.com/larksuite/cli)。它是飞书官方维护的命令行工具，采用 MIT 许可。本次核验的提交是 `017b19a793ad71794a02887ede04757f3d82e10d`，提交日期为 2026-10-14。名称带“飞书 CLI”的其他仓库可能是独立实现，也可能是复制该项目的分支，不能仅凭介绍里的“官方”判断身份。

**最值得学的设计是三层命令。** [中文说明](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/README.zh.md)把执行入口分成业务快捷命令、已注册 API 命令、通用 API 请求。快捷命令可以合并高频步骤、补默认值、改善参数；已注册命令覆盖标准平台接口；通用入口处理前两层未覆盖的能力。模型优先选高层入口，需要时逐层向下，而不是从每个任务都手工拼 HTTP 请求开始。

**提示词与代码有明确分工。** [维护规范 AGENTS.md](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/AGENTS.md)把信息分为四个所有者：代码元数据与参数模式负责“能做什么、输入输出是什么”；`affordance`（命令使用指引）负责“什么时候用、什么时候避免”；`SKILL.md`（技能主文件）负责领域路由、概念、风险和跨命令流程；`references`（按需读取的参考资料）负责详细操作。这是可以直接迁移到自建 Agent 的维护方法：同一个字段定义只维护一次，Skill 不再复制整份 API 手册。

这不是抽象口号。[联系人命令指引](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/affordance/contact.md)分别说明按姓名找人、按已知标识读取资料、查机器人、批量查个人状态的适用边界，并指向对应 Skill。模型可以由任务语义决定路径，代码再验证参数与身份。`has_more`（是否还有结果）也被解释为结果完整性信号，避免把当前返回集当成全部事实。

**接口本身帮助模型减少误用。** [参数模式实现](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/internal/schema/types.go)除了字段类型，还包含必填项、默认值、枚举含义、输入承载参数、权限范围、身份和风险。已存在类型化命令时，模式不暴露底层 HTTP 路径，代码注释明确说明这是为了减少模型绕回通用请求。这里的设计经验是：接口不仅描述能力，也塑造模型会选择的执行路径。

执行结果同样有稳定约定：普通成功数据进入标准输出，普通错误进入标准错误；`ok`（成功标记）和进程退出码判断成功，不能照搬原始 API 的 `code == 0` 判断。还要读[错误契约](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/errs/ERROR_CONTRACT.md)中的例外：批处理部分失败仍把完整结果放在标准输出，返回失败标记、逐项数据和非零退出码，不能把有标准输出等同成功。开发新命令时，[扩展定义](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/extension/command/definition.go)集中声明读写风险、授权身份、参数、校验、预演和执行；[结果协议校验](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/extension/command/result_protocol.go)检查成功结果与分页信息，防止测试环境误认成功而实际 CLI 拒绝结果。

**模型调用前的上下文。** 飞书 CLI 是工具，不是大模型调用器。外部 Agent 把用户任务、所需 Skill、命令帮助或参数模式、历史工具结果组织成模型上下文；模型生成命令，CLI 执行后返回结构化结果，再由 Agent 决定下一步。不能从 CLI 仓库推断豆包或其他产品的完整系统提示词。

**可复用的方法。** 如果要做教学、报表或业务台账 Agent，可以先设计少量高频业务命令，再保留底层通用入口；把命令适用边界写成语义说明，把参数合法性留在代码里，统一结果协议。需另行用真实任务评测调用成功率，不能把官方“更适合 Agent”的定位当成本仓库已复现的效果。

## 二、官方 Skill：路由、操作依赖和数据口径都写清楚

**可直接阅读官方原文。** [官方 lark-base 技能](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/skills/lark-base/SKILL.md)在本次提交中声明版本 `1.2.23`。用户提供的归档版本是 `1.5.1`，两者是不同来源的快照，不能按版本号大小推断哪一个就是面向所有用户的当前生产版本。

这个官方技能先解释资源层次，再要求解析真实目标：链接通过解析命令取得真实标识，标题搜索出现多个候选时进行消歧，不能把一个 URL、知识库标识或任意字符串直接充当表格标识。后续按资源种类选择命令，写入、筛选、关联等需要字段类型的任务再补读字段结构。说明中还区分异步写入成功与最终状态可读，避免每写一项就立即读取造成误判。这里的经验是把**对象定位和依赖关系**写进技能，而不只写“你擅长多维表格”。

**一个更容易学的最小例子是日程待办摘要。** [官方站会摘要技能](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/skills/lark-workflow-standup-report/SKILL.md)先读共享认证说明，再读取日程和未完成任务，最后由模型结合时间、状态和截止日期形成摘要。它明确指出待办查询必须显式过滤未完成项，默认返回页不代表全部数据；日期参数必须转换成接口接受的时间格式，不能把“明天”原样传入。这样的规则对应真实失败模式：完成任务被列为待办、时区错位、分页遗漏。

**技能应该怎么写，也有官方示范。** [lark-skill-maker 技能创建说明](https://github.com/larksuite/cli/blob/017b19a793ad71794a02887ede04757f3d82e10d/skills/lark-skill-maker/SKILL.md)强调触发描述、所需权限，以及多步操作间的返回标识传递、失败回滚和可并行步骤。它把已有快捷命令作为首选，必要时查接口模式，再走底层接口。可学的是“先找现有执行能力，再写编排经验”，而非先堆一个大提示词，再让模型猜底层操作。

**模型调用前的上下文与流程。** 外部 Agent 先看到技能名称和触发描述；命中后读取正文；遇到复杂字段、图表或工作流才继续读参考资料；工具结果中的真实标识和状态加入后续上下文。以上是技能文件要求的行为，不等于所有宿主 Agent 都会严格执行，也不证明安装技能即可获得账号权限。

## 三、Eino：技能怎样实际进入模型上下文

**原文入口与来源。** [CloudWeGo 官方开源介绍](https://www.cloudwego.io/zh/docs/eino/overview/eino_open_source/)说明 Eino 来自字节跳动内部的模型应用开发实践。官方仓库 [cloudwego/eino](https://github.com/cloudwego/eino)采用 Apache-2.0 许可；核验提交为 `0a5ca53b9d3bf7b661dccc863465ec568a421eea`，日期 2026-10-19。这里研究的是公开框架，不推断所有内部产品都使用相同配置。

**最核心的实现只有“列目录”和“取正文”两步。** [文件后端](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/adk/middlewares/skill/filesystem_backend.go)负责读取技能文件；[技能中间件](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/adk/middlewares/skill/skill.go)中的 `Info`（生成工具说明）先调用 `List`（获取元信息），把名称和描述放进技能工具的说明。模型选中某技能后，`InvokableRun`（执行工具调用）才通过 `Get`（读取指定技能）取得正文。模型不需要在第一轮就携带所有技能全文。

[默认提示词](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/adk/middlewares/skill/prompt.go)进一步告诉模型：先判断适用性，读取完整技能，再按需读支持文件；工具结果包含技能的绝对目录，便于定位相对引用。可复用的方法是“技能目录提供选择依据，完整说明提供执行方法，工具返回负责把资料送进上下文”。

当前实现还把上下文继承变成可配置行为：

| 模式 | 调用前送入模型的内容 | 适合学习的问题 |
| --- | --- | --- |
| 默认内联 | 技能正文作为工具结果返回当前会话 | 如何让同一个 Agent 临时获得专项操作说明 |
| `fork`（独立子任务） | 新子 Agent 默认以包含技能内容的用户消息开始，不继承父会话历史 | 如何隔离上下文；业务任务信息需要另行明确提供 |
| `fork_with_context`（继承上下文的子任务） | 父会话历史加上与技能调用关联的工具结果 | 如何把已查到的上下文交给专长 Agent |

这些差异直接存在于 `runAgentMode`（执行子 Agent 模式）的消息构造代码中；`BuildContent`（构建本次技能内容）与 `BuildForkMessages`（构建子 Agent 初始消息）允许宿主补充本轮任务信息。不能把“不继承父历史”理解成子 Agent 会自动知道父任务，也不能把技能文本加载等同于工具权限已经具备。

**可复用的方法。** 在自己的 Harness（智能体运行框架）里，至少把技能索引、正文加载、参考文件定位、上下文继承四项分开。这样才能分别评估选错技能、没读正文、丢了任务条件、带入无关历史等错误。上述是从公开实现提炼的设计建议，尚未在本仓库做对照实验。

## 四、Trae Agent：完整系统提示词与循环代码可以对照阅读

**原文入口与来源。** [bytedance/trae-agent](https://github.com/bytedance/trae-agent)是字节跳动公开的软件工程 Agent 项目，MIT 许可；本次核验的提交是 `e839e559ac61bdd0e057c375dd1dee391fee797d`，日期 2026-02-05。它不能被等同于 Trae 商业客户端或 SOLO 模式的完整实现。

[系统提示词](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/prompt/agent_prompt.py)把修复任务展开为理解问题、定位代码、复现问题、诊断、定点修复、验证和说明结果，并给出绝对路径要求。其价值在于明确过程中的中间产物：先有复现，再有补丁，再有验证结果；同时也说明提示词的任务假设偏向 GitHub 问题修复，不能不加调整地用于所有日常编码任务。

[任务初始化代码](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/agent/trae_agent.py)实际构造两部分：系统消息放固定操作规范，用户消息放项目根路径和问题正文。工具通过注册表与配置装配，工具名称、描述、参数由[工具基类](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/tools/base.py)定义。这样可以区分哪些信息来自提示词，哪些来自工具接口，哪些是本轮任务数据。

[基础循环](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/agent/base_agent.py)将消息、模型配置和工具交给模型客户端；模型请求工具后，执行器返回结果，再继续下一轮，并记录轨迹与步数。[模型客户端入口](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/utils/llm_clients/llm_client.py)默认复用历史；具体格式由各供应商适配器处理。读代码时不能只看循环中本轮消息列表，就断言历史被清空。

**一个很值得保留的边界。** [task_done 工具](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/trae_agent/tools/task_done_tool.py)的描述要求先验证再报告完成，但工具函数本身只返回完成结果；任务类在特定配置下额外检查补丁非空。这里并没有一个通用机制证明“所有测试已通过”。因此，研究提示词必须同时找执行侧门控：写了“必须验证”与程序真正检查了什么，是两层证据。

**可复用的方法。** 研究一个 Agent，按“系统提示词 → 本轮消息构造 → 工具模式 → 循环 → 完成判定 → 轨迹记录”连起来读。这样才能复现它，而不是只收藏一个漂亮的角色提示词。

## 五、第三方豆包归档：可以学细节，但要把版本与出处钉住

**来源核验。** 用户提供的 [ahang1598/doubao-workbuddy-qwenwork-skills](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills)由个人账号维护。[豆包索引说明](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-doubao.md)自述从本地豆包工作目录同步文件。本次核验提交是 `1c9239cc90585f57d9e06d32deffc017bbff5802`，日期 2026-10-20；仓库根目录未见许可证文件，GitHub 许可证元数据为空。这只能证实该快照公开存在，不能独立证明文件来自哪个官方发行版、是否完整、是否仍在生产中使用。本文只写原创分析和链接，不镜像技能全文。

| 用户给出的材料 | 本次核验结果 | 研究时的用法 |
| --- | --- | --- |
| [lark-base 技能](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base/SKILL.md) | 文件存在，声明 `version: 1.5.1`，依赖 `lark-cli` | 当作第三方保存的版本快照；可与官方文件比较 |
| [Base 系统搭建指引](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base/references/lark-base-solution-design.md) | 文件可读，包含建模、功能组合和回读验收规则 | 学“如何把模糊需求翻译成可交付系统” |
| [企业搜索技能](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/doubao-enterprise-search/SKILL.md) | 文件可读，包含路由、查询构造、多轮继承与来源引用规则 | 学搜索与对象操作边界；不能证明与用户之前轨迹的版本完全一致 |

**归档与官方存在实质差异。** 归档的 Base 技能明确排除应用模式，而本次官方 `1.2.23` 文件包含应用模式路由。这已经足以说明“同名技能”不等于“同一套能力与约束”。任何复用都应同时记录宿主、CLI 版本和技能提交，不能把两份文件随意拼在一起后声称还原官方。

**搭建指引里值得学习的是交付定义。** 它先判断业务对象与重复事件是否需要分表，再按需求选择字段、视图和计算；持续变化的结论应由公式表达；只有确有提醒等需求时才配置自动化；创建后需读回相应配置或结果。这给出一个可迁移思路：把用户可见的完成条件写进技能，使 Agent 交付能持续使用的成果。本仓库不把指引中的功能丰富度下限机械推广到其他产品。

**企业搜索指引里值得学习的是查询语义保护。** 文件把“了解项目背景、讨论与结论”和“读取或修改一个明确对象”分开路由；构造查询时尽量保留用户问题中的主体、比较关系、时间与来源限制；多轮追问可以继承主题，但不能继承一次显式命令的特殊入口条件。检索无结果也不能证明事实不存在。这些规则可以作为搜索 Agent 的测试题来源，例如“上一轮查项目 A，本轮只说 B 团队呢”是否丢失项目主题。

**模型调用前的上下文。** 从公开文字只能重建它要求 Agent 使用的技能、参考资料、查询文本和工具结果，无法得知豆包服务端最终拼接的系统消息、模型配置或隐含检索逻辑。企业搜索工具名是这个宿主的能力标识，不代表复制技能到别的 Agent 就会获得同名工具。

## 建议的学习顺序

先读官方“日程待办摘要”感受一个小技能如何编排两个真实命令，再读 CLI 的四层信息分工，接着读 Eino 的技能加载实现，最后对照 Trae 的完整模型循环和第三方归档的交付规则。每次迁移只提取一种方法，并给它配一组实际任务：例如是否能保留查询限定、是否能区分同名对象、是否把分页结果误当全部。源码存在、设计合理与实际任务有效，应分别记录。
