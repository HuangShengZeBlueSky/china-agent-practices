# 十二类工程问题与方法对照

这些方法来自公开实现与技能文件的静态阅读。每项将观察到的机制、我们建议做的练习和未验证边界分别记录。效果需要在自己的任务上验证。

| 工程问题 | 首先看哪些项目 |
| --- | --- |
| 提示词与真实能力一起装配 | 飞书 Lark CLI、Qwen Code、Coze Studio |
| 技能目录先到，正文按需加载 | Eino 技能中间件、AgentScope、华为 openJiuwen、Kimi CLI · 历史 Python 版 |
| 把业务 Skill 写成执行契约 | 飞书官方 Skills、豆包 Base 技能归档、MiniMax Skills |
| 工具描述要解释实际执行语义 | 小米 mimoagent、美团 VitaBench 1.0、百度 AppBuilder SDK |
| 异步任务先查状态，再决定重试 | OpenSandbox、MiniMax MCP、飞书官方 Skills |
| 长结果外置，但保留状态和回读入口 | DeerFlow 2.x、小米 mimoagent、AWorld CLI |
| 任务交接要有输入、状态与责任 | Eino 技能中间件、JoyAgent-JDGenie、Tencent RTC Skills、归档采集与代表技能 |
| 界面变化后更新观察与操作目标 | BrowserSkill、UI-TARS Desktop、Open-AutoGLM |
| 结束信号、格式正确与业务完成分别验 | Trae Agent、美团 VitaBench 1.0、Coze Loop、Tencent RTC Skills、SkillHub 官方 Skills |
| 沿消息与轨迹理解框架 | Qwen-Agent、Lagent、Coze Loop、MindSearch |
| 文件变化与知识更新分别维护 | 归档采集与代表技能、CloudBase AI Toolkit、BrowserSkill |
| 把版本与协议差异留下来 | 飞书官方 Skills、豆包 Base 技能归档、华为 openJiuwen、归档采集与代表技能 |

## 1. 提示词与真实能力一起装配

**要解决的问题。** 提示词提到了工具，当前运行环境却没有这个工具；同一段指令被多个入口重复维护。

**观察到的机制。** 飞书把参数结构、适用指引、Skill 和参考资料分工；Qwen Code 按会话工具声明快照筛选相关指引；Coze Studio 在前置数据到齐后渲染模板，并按工具配置选择执行分支。

**迁移练习。** 为自己的 Agent 画一张“哪段上下文从哪里来”的表，把工具可用条件与调用示例的装配放在同一位置维护。

**证据边界。** 公开实现中仍可能有例外；这里没有测量幻觉或成功率变化。

阅读来源：

- [飞书 Lark CLI](https://github.com/larksuite/cli) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `017b19a793ad71794a02887ede04757f3d82e10d`
- [Qwen Code](https://github.com/QwenLM/qwen-code) · [中文拆解](../cases/alibaba-tencent.md) · 固定提交 `461be87304c7b3b5d64b701207c49f236515d5fd`
- [Coze Studio](https://github.com/coze-dev/coze-studio) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `fefb05ff27be1da939612fbf9faf5db62583b8ae`

## 2. 技能目录先到，正文按需加载

**要解决的问题。** 一次塞入所有技能正文会占用上下文，也让模型难以选对内容。

**观察到的机制。** Eino 将 List 元数据与 Get 正文分开；AgentScope 让技能随工具组启用；openJiuwen 依赖外部读取工具；历史 Kimi CLI 保留技能作用域和路径。

**迁移练习。** 先记录技能名称、触发描述、作用域与正文路径，再抓一条实际请求验证正文在何时进入模型上下文。

**证据边界。** 读到文件并不等于已经具备依赖工具；不同宿主加载通道不同。

阅读来源：

- [Eino 技能中间件](https://github.com/cloudwego/eino) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `0a5ca53b9d3bf7b661dccc863465ec568a421eea`
- [AgentScope](https://github.com/agentscope-ai/agentscope) · [中文拆解](../cases/alibaba-tencent.md) · 固定提交 `b2a084799bf883a5a8d0f56e44f205f78a83f0fe`
- [华为 openJiuwen](https://github.com/openJiuwen-ai/agent-core) · [中文拆解](../cases/baidu-huawei-meituan-xiaomi.md) · 固定提交 `4170e756504d70d8324c2ac18a5afdd770a99dc9`
- [Kimi CLI · 历史 Python 版](https://github.com/MoonshotAI/kimi-cli) · [中文拆解](../cases/ecosystem-expansion.md) · 固定提交 `9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82`

## 3. 把业务 Skill 写成执行契约

**要解决的问题。** 技能只有角色和目标，没有对象解析、前提、输出或验收，模型难以知道下一步。

**观察到的机制。** 飞书技能先确认真实对象和字段；归档 Base 指引从业务结构推到数据模型；MiniMax fullstack-dev 将需求、实施、验证与交接分开。

**迁移练习。** 用一个小任务写出触发条件、职责范围、输入、依赖、执行顺序、失败处理和可检查的交付物。

**证据边界。** 技能文本表达意图；哪些约束由程序强制执行需要另查执行器。

阅读来源：

- [飞书官方 Skills](https://github.com/larksuite/cli/tree/017b19a793ad71794a02887ede04757f3d82e10d/skills) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `017b19a793ad71794a02887ede04757f3d82e10d`
- [豆包 Base 技能归档](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/tree/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `1c9239cc90585f57d9e06d32deffc017bbff5802`
- [MiniMax Skills](https://github.com/MiniMax-AI/skills) · [中文拆解](../cases/ecosystem-expansion.md) · 固定提交 `60aaae52bb2af8162732751a4332f62a5fef518b`

## 4. 工具描述要解释实际执行语义

**要解决的问题。** 参数格式正确，但模型误解了子进程、并发、时间、分页或状态，仍然会做错事。

**观察到的机制。** mimoagent 的 Bash 说明进程与并发语义；VitaBench 声明工具前后条件；AppBuilder 用调用编号连接云端请求与本地结果。

**迁移练习。** 挑最常失败的工具，把状态变化、前置条件、结果判定和副作用写进描述，再对照执行代码检查是否一致。

**证据边界。** 接口说明的完善不能代替真实任务测试。

阅读来源：

- [小米 mimoagent](https://github.com/XiaomiMiMo/mimoagent) · [中文拆解](../cases/baidu-huawei-meituan-xiaomi.md) · 固定提交 `c3df8469f250b15e7906487a6d52be4c1827a509`
- [美团 VitaBench 1.0](https://github.com/meituan-longcat/vitabench) · [中文拆解](../cases/baidu-huawei-meituan-xiaomi.md) · 固定提交 `742e240855bf8686a0842360749d5ea970ea3987`
- [百度 AppBuilder SDK](https://github.com/baidubce/app-builder) · [中文拆解](../cases/baidu-huawei-meituan-xiaomi.md) · 固定提交 `76a7316c0671900b698f9e955afb432ec9a93183`

## 5. 异步任务先查状态，再决定重试

**要解决的问题。** 响应超时或暂时查不到结果时再次提交，可能重复创建资源或重复运行任务。

**观察到的机制。** OpenSandbox 的非幂等 SSE 启动请求绕开自动重试；MiniMax MCP 将视频提交与查询分离；飞书技能明确区分异步写入与失败。

**迁移练习。** 让提交返回任务编号，查询返回明确终态；对“效果未知”的错误先查原任务，只有幂等语义明确的操作才自动重试。

**证据边界。** 客户端返回次数上限不一定等于严格总超时；不同 API 的幂等保证要逐项核对。

阅读来源：

- [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `62d3e59d10796154b88510f39fca8438eb99dd58`
- [MiniMax MCP](https://github.com/MiniMax-AI/MiniMax-MCP) · [中文拆解](../cases/ecosystem-expansion.md) · 固定提交 `0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a`
- [飞书官方 Skills](https://github.com/larksuite/cli/tree/017b19a793ad71794a02887ede04757f3d82e10d/skills) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `017b19a793ad71794a02887ede04757f3d82e10d`

## 6. 长结果外置，但保留状态和回读入口

**要解决的问题。** 长日志、网页和文件挤占上下文；直接截断又可能丢失失败证据。

**观察到的机制。** DeerFlow 在输出预算中间件启用且结果超过阈值时，将大工具结果外置为文件并提供回读路径，持久化失败时降级截断；mimoagent 截断正文后保留退出码；AWorld 的压缩提示要求摘要保留待办、错误与当前工作。

**迁移练习。** 为大结果保存原始产物、简要类型、退出状态和可回读位置；测试一次失败时模型是否还能找到决定性的原文。

**证据边界。** 这里包含提示约定和代码处理机制；关键内容是否实际保留，以及上下文与任务效果变化，仍需运行验证。

阅读来源：

- [DeerFlow 2.x](https://github.com/bytedance/deer-flow) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `d4012c4b24f9b5ee14236a8214c82815de5b5214`
- [小米 mimoagent](https://github.com/XiaomiMiMo/mimoagent) · [中文拆解](../cases/baidu-huawei-meituan-xiaomi.md) · 固定提交 `c3df8469f250b15e7906487a6d52be4c1827a509`
- [AWorld CLI](https://github.com/inclusionAI/AWorld) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `82af4062e29e128910afa8622c866f4b99a4d23d`

## 7. 任务交接要有输入、状态与责任

**要解决的问题。** 拆了很多角色，却没有完整任务输入、产物引用、状态版本和清楚的完成条件。

**观察到的机制。** Eino 区分独立与继承上下文子任务；JoyAgent 分离计划与执行；TRTC 的技能与工具通过会话工具的版本检查和原子替换更新共享状态；归档团队技能明确交接字段。

**迁移练习。** 把任务目标、已有事实、约束、产物路径、未完成项与验证责任写进交接记录，按实际依赖决定是否共享历史。

**证据边界。** TRTC 在缺少 fcntl 的平台有无锁降级；文本协议与程序保证不能混写。

阅读来源：

- [Eino 技能中间件](https://github.com/cloudwego/eino) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `0a5ca53b9d3bf7b661dccc863465ec568a421eea`
- [JoyAgent-JDGenie](https://github.com/jd-opensource/joyagent-jdgenie) · [中文拆解](../cases/ecosystem-expansion.md) · 固定提交 `2417e0b8b636d941ad5fb14c59b20dddfef5375d`
- [Tencent RTC Skills](https://github.com/Tencent-RTC/agent-skills) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `55a6bcf643acb4104105359ed0a1d194bdee7696`
- [归档采集与代表技能](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills) · [中文拆解](../cases/archive-collection-method.md) · 固定提交 `1c9239cc90585f57d9e06d32deffc017bbff5802`

## 8. 界面变化后更新观察与操作目标

**要解决的问题。** 界面变化后仍用旧元素引用或旧坐标，动作能执行却作用到错误对象。

**观察到的机制。** BrowserSkill 用 session 和 tab 约束引用并规定失效后的恢复；UI-TARS 与 Open-AutoGLM 在动作之后取得新截图继续推理。

**迁移练习。** 把观察、动作解析、执行结果和下一次观察分别记录；超时但效果未知时先重新观察，不连续重复点击。

**证据边界。** 模型发出的 finished 与真实任务成功不同；本轮没有操作设备或浏览器验证上游能力。

阅读来源：

- [BrowserSkill](https://github.com/Tencent/BrowserSkill) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `6214e3d6a3d74eaf39c0202c4f182b5755974da9`
- [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `3ac2cb8d946d78d5ff92ad17b318eaafa18c178c`
- [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) · [中文拆解](../cases/ecosystem-expansion.md) · 固定提交 `86f55382982fb054e8fc98ca80609dff8a2cdc3c`

## 9. 结束信号、格式正确与业务完成分别验

**要解决的问题。** 模型说完成、状态字段是 completed，或者 JSON 能解析，就被当成任务成功。

**观察到的机制。** Trae 暴露任务结束工具；VitaBench 用独立提示评估轨迹；Coze Loop 拆分模板、调用与解析；TRTC 的代码静态约束检查与 SkillHub 的报告字段校验，分别展示了静态检查和格式合规的边界。

**迁移练习。** 为同一任务单独记录：循环是否结束、输出格式是否通过、产物是否存在、需求是否满足。把最后一项落实到可观察证据。

**证据边界。** 评委模型本身需要校准；静态字符串命中与评分字段合法都不证明质量。

阅读来源：

- [Trae Agent](https://github.com/bytedance/trae-agent) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `e839e559ac61bdd0e057c375dd1dee391fee797d`
- [美团 VitaBench 1.0](https://github.com/meituan-longcat/vitabench) · [中文拆解](../cases/baidu-huawei-meituan-xiaomi.md) · 固定提交 `742e240855bf8686a0842360749d5ea970ea3987`
- [Coze Loop](https://github.com/coze-dev/coze-loop) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `95dc2eebbc100b929c102d90111bb94fad41e500`
- [Tencent RTC Skills](https://github.com/Tencent-RTC/agent-skills) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `55a6bcf643acb4104105359ed0a1d194bdee7696`
- [SkillHub 官方 Skills](https://github.com/Tencent/skillhub) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `a051f06f7944d24ade04bea27735f430b19a8298`

## 10. 沿消息与轨迹理解框架

**要解决的问题。** 只读系统提示词，遗漏检索发生的位置、工具输出的角色及状态写回顺序。

**观察到的机制。** Qwen-Agent 把检索所得资料装入系统消息；Lagent 分离消息聚合、动作解析与执行；Coze Loop 分阶段留 trace；MindSearch 合并子搜索的引用映射。

**迁移练习。** 记录一次模型调用前后的消息序列，标出检索执行者、注入角色、调用编号和可追溯引用。

**证据边界。** MindSearch 的图执行与父节点传递有已记录的实现边界，不能把设计图当成运行验证。

阅读来源：

- [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) · [中文拆解](../cases/alibaba-tencent.md) · 固定提交 `31a4d36d123688581a9e9744427272b33ce940e0`
- [Lagent](https://github.com/InternLM/lagent) · [中文拆解](../cases/ecosystem-expansion.md) · 固定提交 `0ab2e2f550477884743cd63fbca7bc4aa7b00290`
- [Coze Loop](https://github.com/coze-dev/coze-loop) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `95dc2eebbc100b929c102d90111bb94fad41e500`
- [MindSearch](https://github.com/InternLM/MindSearch) · [中文拆解](../cases/ecosystem-expansion.md) · 固定提交 `7952c5f8a956fe6a44228a6a7d528a35340e7c87`

## 11. 文件变化与知识更新分别维护

**要解决的问题。** 收藏越来越多，但缺少适用条件、变化原因和读完后的实践结论。

**观察到的机制。** 第三方归档将文件同步、变更日志与根目录模型总结分开；CloudBase 对长期规则的证据设门槛；BrowserSkill 记录包来源和文件指纹。

**迁移练习。** 每次新增记录至少补一条“解决什么问题、证据在哪、何时适用、怎样验证”；文件没变不制造提交，结论变了写清原因。

**证据边界。** 本仓没有设置定时采集任务；归档作者的关键词分类不等于语义学习。

阅读来源：

- [归档采集与代表技能](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills) · [中文拆解](../cases/archive-collection-method.md) · 固定提交 `1c9239cc90585f57d9e06d32deffc017bbff5802`
- [CloudBase AI Toolkit](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) · [中文拆解](../cases/alibaba-tencent.md) · 固定提交 `f49b8d481373937b3c39012deef6cf5da829ef6e`
- [BrowserSkill](https://github.com/Tencent/BrowserSkill) · [中文拆解](../cases/platforms-expansion.md) · 固定提交 `6214e3d6a3d74eaf39c0202c4f182b5755974da9`

## 12. 把版本与协议差异留下来

**要解决的问题。** 同名技能来自不同渠道；文档、主技能和引用协议并不总是一致。

**观察到的机制。** 飞书官方与豆包归档的 Base 职责存在差异；openJiuwen 文档与实现的读取工具不同；QwenWork 归档 QA 的路径和状态标记出现漂移。

**迁移练习。** 按来源、提交、路径和检查日保存结论。发现冲突时同时记录两份证据，说明采用哪个实现作为解释依据。

**证据边界。** 版本号大小不代表渠道间的先后关系，也不能证明全量生产部署。

阅读来源：

- [飞书官方 Skills](https://github.com/larksuite/cli/tree/017b19a793ad71794a02887ede04757f3d82e10d/skills) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `017b19a793ad71794a02887ede04757f3d82e10d`
- [豆包 Base 技能归档](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/tree/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/lark-base) · [中文拆解](../cases/bytedance-lark.md) · 固定提交 `1c9239cc90585f57d9e06d32deffc017bbff5802`
- [华为 openJiuwen](https://github.com/openJiuwen-ai/agent-core) · [中文拆解](../cases/baidu-huawei-meituan-xiaomi.md) · 固定提交 `4170e756504d70d8324c2ac18a5afdd770a99dc9`
- [归档采集与代表技能](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills) · [中文拆解](../cases/archive-collection-method.md) · 固定提交 `1c9239cc90585f57d9e06d32deffc017bbff5802`
