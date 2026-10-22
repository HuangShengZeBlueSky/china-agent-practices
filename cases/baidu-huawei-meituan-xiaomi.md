# 百度、华为、美团、小米：四种可以读到实现的 Agent 工程方法

核查日期：2026-10-21。本页研究公开源码、官方示例与官方说明。没有调用收费模型、连接企业业务账号或实跑上游系统；下述运行流是源码阅读结论，不能据此声称已经复现效果，也不能代表这些公司的全部内部生产方案。所有分析均为本仓库原创，原始材料通过固定版本链接阅读。

## 先选择自己要学的部分

| 学习问题 | 案例 | 最值得看的实现 |
| --- | --- | --- |
| 我有现成业务函数，怎样交给 Agent 调用？ | 百度 AppBuilder | 工具说明、参数约束、云端暂停、本地执行、按调用编号回传 |
| 有很多 Skill，怎样让模型知道何时读哪份？ | 华为 openJiuwen | 元数据注册、技能清单提示词、按需读取正文、读取工具依赖检查 |
| 怎样把业务规则写进工具，并验证任务真的完成？ | 美团 VitaBench 1.0 | 工具前置条件与后置条件、可执行环境、独立评分提示词 |
| 怎样比较不同提示词、工具和执行环境的真实表现？ | 小米 mimoagent | Agent、模型、环境、数据集分层；工具错误反馈；轨迹与评分留存 |

## 百度 AppBuilder：让业务函数成为可调用工具

**来源与版本。** [官方仓库](https://github.com/baidubce/app-builder)属于百度智能云组织；实现文件含百度版权与 Apache-2.0 许可声明。本次固定提交为 `76a7316c0671900b698f9e955afb432ec9a93183`，提交日期 2026-04-26。[许可原文](https://github.com/baidubce/app-builder/blob/76a7316c0671900b698f9e955afb432ec9a93183/LICENSE)。这是官方软件开发工具包，不等于平台服务端 Agent 的完整源码。

**具体怎么运转。** 官方[天气工具示例](https://github.com/baidubce/app-builder/blob/76a7316c0671900b698f9e955afb432ec9a93183/python/tests/test_appbuilder_client_toolcall.py)先创建会话，再把用户问题与工具定义一起交给 `run`（启动或继续运行）。工具定义不仅写用途，还明确支持的地区、参数类型、必填项、单位枚举和参数示例。服务端决定调用工具后，返回 `interrupt`（暂停等待工具结果）事件；客户端取得函数名和参数，执行对应本地函数，再把结果与 `tool_call_id`（本次工具调用编号）一起回传到原会话，模型继续生成回答。

这里可直接复用的经验是：**把业务函数的说明书做成模型能消费的接口契约。** 示例既演示手写工具参数结构，也演示 `Manifest.from_function`（从 Python 函数生成工具清单），还允许用装饰器补充函数与参数的语义。这样，改一个参数含义时可以靠近业务代码维护，不必另写一大段与代码脱节的系统提示词。该示例的天气结果是固定演示值，不能当作真实天气服务。

**调用模型之前有什么上下文。** 客户端能够确认的输入是 `conversation_id`（会话标识）、`query`（本轮问题）、`tools`（可调用工具定义），以及后续的 `tool_outputs`（工具执行结果）；有些调用还附带文件标识。平台服务端最终如何拼装系统提示词、检索内容和历史消息，不能从这个客户端示例完整得知。研究记录应把这一部分标为未公开，避免把 SDK 的入参冒充完整模型请求。

**错误怎样处理。** [事件处理器实现](https://github.com/baidubce/app-builder/blob/76a7316c0671900b698f9e955afb432ec9a93183/python/core/console/appbuilder_client/event_handler.py)把准备、运行、暂停、成功和错误分别交给回调处理；暂停回调必须返回工具结果列表，空列表或首项无法转换成规定的输出结构会报错。默认工具调用处理器按函数名称映射到本地实现。它没有因此自动获得业务重试、幂等或事务回滚能力；这些需要在业务工具实现中设计。

**建议学走什么。** 如果已有分期计算器、题库查询或企业检索函数，先为每个函数写清适用范围、必填参数和结果含义，再接入调用编号关联的执行回路。首先复用平台现成的会话与工具能力，就能形成一个最小业务 Agent；没有必要先自建完整框架。

## 华为 openJiuwen：Skill 的注册、提示与读取是不同步骤

**来源与版本。** [华为官方说明](https://www.huawei.com/en/news/2026/9/hc-ai-industry-adoption)明确介绍 openJiuwen；[项目仓库](https://github.com/openJiuwen-ai/agent-core)中的实现文件带华为版权声明。固定提交为 `4170e756504d70d8324c2ac18a5afdd770a99dc9`，提交日期 2026-10-21；[主许可](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/LICENSE)为 Apache-2.0。这里研究的是该版本的公开技能机制与示例。

**具体怎么运转。** [技能管理器](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/openjiuwen/core/single_agent/skills/skill_manager.py)扫描技能目录，读取 `SKILL.md`（技能说明文件）的头部元数据，保存名称、描述和目录；重复名称在没有显式允许覆盖时会报错。[技能辅助类](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/openjiuwen/core/single_agent/skills/skill_util.py)将这些信息生成技能清单，并提示模型先用 `read_file`（读取文件工具）打开相关技能正文。注册时为了解析元数据会读文件，但首轮技能清单没有把所有正文整篇塞给模型。

**调用模型之前有什么上下文。** [ReAct Agent 实现](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/openjiuwen/core/single_agent/agents/react_agent.py)在调用阶段更新系统提示词构造器中的技能分区。该分区含“有哪些技能、各自做什么、文件在哪”；模型再结合任务语义选择需要读取的正文。这个模块本身不是基于关键词的技能选择器，也没有证明每次都能选中正确技能；它提供的是模型选择所需的上下文与读取入口。

**为什么要同时读代码与文档。** 本次发现一个具体版本差异：同一提交下的[中文技能 API 文档](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/docs/zh/2.%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/API%E6%96%87%E6%A1%A3/openjiuwen.core/skills/openjiuwen_skills.md)仍描述 `view_file`（查看文件工具）与自动挂载工具的旧接口；当前 `skill_util.py` 则要求执行工具在外部添加，注册方法明确返回成功值。当前 Agent 发现缺少 `read_file` 时会记录警告。因此不能只照着旧文档假设“注册了 Skill，就自动有文件读取和执行工具”。

**一份具体 Skill 长什么样。** [手机日程技能原文](https://github.com/openJiuwen-ai/agent-core/blob/4170e756504d70d8324c2ac18a5afdd770a99dc9/examples/mobile_gui/skills/scheduling/SKILL.md)把任务拆成多个意图：查会议时间、在会议前设置闹钟、设置绝对时间闹钟、设置倒计时。它要求从日历界面读取真实开始时间，计算偏移，再到时钟应用创建并检查结果；配套图片用于帮助识别界面。值得学习的是“触发条件—步骤—歧义—完成检查”的写法，而不是将某个手机界面的位置当成通用事实。示例对同名会议的默认选择也不能直接替代实际产品的人物消歧策略。

**建议学走什么。** 为自己的技能保留一个简短而准确的用途描述；把长流程、参考资料与截图放在技能包里，让模型按需读取；同时核对运行环境真的提供读取、执行和结果验证工具。技能文件表达工作方法，框架提供执行能力，两者需要逐项接上。

## 美团 VitaBench：工具说明承担业务流程约束

**来源与版本。** [美团技术团队文章](https://tech.meituan.com/2025/11/02/LongCat-VitaBench-Agent.html)介绍并指向该基准；[官方仓库](https://github.com/meituan-longcat/vitabench)固定提交为 `742e240855bf8686a0842360749d5ea970ea3987`，提交日期 2026-02-22。[MIT 许可](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/LICENSE)同时保留 Sierra Research 与美团版权。此处分析 VitaBench 1.0 的公开实现；[VitaBench 2.0](https://tech.meituan.com/2026/06/29/LongCat-VitaBench-2.0.html)是后续独立版本，不能把两者的数据与实现混写。

**最有学习价值的原文。** [外卖工具说明](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/domains/delivery/tools_schema.py)为每个工具单列用途、前置条件、后置条件、参数、返回含义及读写类型。例如创建订单前要确定单一商家、商品及饮食限制；支付工具要求已经有订单且用户表达支付意愿；取消工具提示先查状态并避免重复取消。这些条件给模型可操作的业务顺序，比只写“创建订单”“取消订单”包含更多决策信息。

**调用模型之前有什么上下文。** [Agent 实现](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/agent/llm_agent.py)将带任务时间的系统规则与累计用户、助手、工具消息组合，同时提供工具定义。[系统提示词](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/prompts/agent_system_prompt.yaml)要求根据已知信息补齐参数、按工具条件行动并明确结束对话。模型选工具后，[环境层](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/environment/environment.py)执行对应函数，按原调用编号回传结果；工具异常会形成带错误标志的工具消息，供后续轮次处理。

**怎样判断真的做完。** [完整轨迹评分提示词](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/src/vita/prompts/full_trajectory_eval_template.yaml)给评审模型任务要求、完整交互轨迹和逐项评分点。它区分“工具查到了信息”“助手向用户做出推荐”“真正执行了订单操作”，要求结合证据更新评分点，并记录有关轮次。对订单数量与时间这类硬约束，不能因为对话中用户妥协就自动放宽原任务标准。这里是另一个用于评估的模型调用，不是给执行 Agent 看答案。

**建议学走什么。** 工具定义、执行环境、评估规则应该一起读。可以把题库发布、企业文档修改等任务也写成前后条件，并在评估时检查实际产物。业务流程约束写进工具描述有助于模型决策，但提示词不等于执行权限控制；基准的模拟业务也不是美团真实订单 API。

## 小米 mimoagent：把 Agent 做成可比较、可记录的实验对象

**来源与版本。** [小米 MiMo 组织仓库](https://github.com/XiaomiMiMo/mimoagent)的[许可](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/LICENSE.md)和[来源说明](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/NOTICE)均明确小米版权，也明确项目由 `mini-swe-agent`（极简软件工程智能体）1.9.0 分叉后扩展。固定提交为 `c3df8469f250b15e7906487a6d52be4c1827a509`，提交日期 2026-10-18。主项目使用 MIT 许可；接入的第三方命令行程序各有自己的许可，不能统称为小米原创或全部适用 MIT。

**具体怎么运转。** [项目说明](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/README.md)将系统分为 Agent 决策、模型协议、执行环境、数据集与评分器。白盒模式运行可修改的原生循环；黑盒模式在任务环境中运行指定版本的外部编程 CLI（命令行程序），由框架提供任务并评分。输出包括逐实例日志、交互轨迹、评分信息及汇总记录。它公开的是运行与采集框架，不能仅凭此认定完整生产强化学习训练系统已经公开。

**调用模型之前有什么上下文。** [基础循环](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/src/mimoagent/agents/base.py)在首轮渲染系统模板与任务模板，模板变量来自配置、环境、任务和模型信息；后续轮次继续追加用户输入与工具结果。[默认 Agent](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/src/mimoagent/agents/default.py)再把工具清单交给模型。模型发出工具调用时执行并回填工具消息，没有工具调用时结束当前轮。因而同一个实验可分别替换提示词、工具集合或环境，而不必重写所有层。

**真正细的工程经验在工具描述。** [Bash 工具](https://github.com/XiaomiMiMo/mimoagent/blob/c3df8469f250b15e7906487a6d52be4c1827a509/src/mimoagent/tools/bash.py)明确每次调用是新的子进程，目录与环境变量修改不会自然延续；要求非交互命令，给出超时参数及上限，并解释同一轮并发调用可能产生文件读写竞争。这些说明直接来自执行语义，会影响模型怎么安排动作。超时会回传部分输出与可操作的恢复提示；基础设施连接错误和普通工具错误采用不同的传播路径。

**长输出如何不丢关键信息。** 默认 Agent 先截断冗长工具正文，再附加退出码等元数据，避免决定成功或失败的信息被一起截掉。工具调用编号与名称也随结果保留；并发执行的结果按原调用顺序对应回填。这些做法使后续模型更容易判断要继续、重试还是收尾，也让研究者能追踪失败发生在哪一层。

**建议学走什么。** 为自己准备一个小的固定任务集，保留任务初始环境、待比较的提示词与工具版本、完整工具返回和最终产物。先验证评分链路能对参考解给出合理结果，再比较不同 Agent 方案。配置能拆分不同变量是实验便利条件，但并不自动构成严格的配对统计实验；预算、任务抽样和重复次数仍须另外控制。

## 本轮结论怎样复用

这四个案例互补：百度展示把现有函数接进业务 Agent 的最短路径；华为把技能元数据、技能正文与执行工具连接起来；美团让业务条件和真实完成标准显式化；小米让不同方案能在任务环境中留下可比较的轨迹。一个值得持续维护的研究条目，应同时保留“原文在哪里、这份版本实际做什么、我准备学走哪一点、有什么没有被公开证据支持”。

本轮新增本页与来源清单，没有改动或删除上游代码。核对了四个仓库的归属、许可、提交与所列源码；没有运行上游项目，没有得出性能提升结论。
