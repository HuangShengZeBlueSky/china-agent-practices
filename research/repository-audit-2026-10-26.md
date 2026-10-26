# 31 个既有仓库的维护与版本复核

检查日期：2026-10-26。属于 P1-01 的可复核子单元：全部仓库元数据和默认分支 HEAD 已读；不是 31 仓源码重新精读，也未完成所有官方归属链复核。详细提交、时间、历史版本和字段见[证据表](evidence/2026-10-26/repository-audit.json)。原始快照保持不变。

31 个入口均可访问。20 个当前 HEAD 等于旧研究版本，11 个不同；对照实际 snapshots.versions，21 个当前 HEAD 已有备份，10 个尚无该版本备份。两种分母差别来自第三方归档：它的当前版本已经备份，但旧研究来源仍指向更早版本。不能把 11 次版本差异都说成 11 个新备份缺口。

|仓库|默认分支|归档标志|当前 HEAD|当前版本已备份|
|---|---|---|---|---|
|[larksuite/cli](https://github.com/larksuite/cli)|main|false|[017b19a793](https://github.com/larksuite/cli/commit/017b19a793ad71794a02887ede04757f3d82e10d)|是|
|[cloudwego/eino](https://github.com/cloudwego/eino)|main|false|[0a5ca53b9d](https://github.com/cloudwego/eino/commit/0a5ca53b9d3bf7b661dccc863465ec568a421eea)|是|
|[bytedance/trae-agent](https://github.com/bytedance/trae-agent)|main|false|[e839e559ac](https://github.com/bytedance/trae-agent/commit/e839e559ac61bdd0e057c375dd1dee391fee797d)|是|
|[ahang1598/doubao-workbuddy-qwenwork-skills](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills)|main|false|[4e60dd8977](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/commit/4e60dd8977eee1d770dd22de4780a4b54385adb8)|是|
|[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)|main|false|[338f13366c](https://github.com/QwenLM/qwen-code/commit/338f13366c1d86e586f7e0785942740da3503887)|否|
|[QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)|main|false|[31a4d36d12](https://github.com/QwenLM/Qwen-Agent/commit/31a4d36d123688581a9e9744427272b33ce940e0)|是|
|[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)|main|false|[bdad647d2f](https://github.com/agentscope-ai/agentscope/commit/bdad647d2fee7d66597681ecd89e086b7800dd2a)|否|
|[TencentCloudBase/CloudBase-AI-Toolkit](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit)|main|false|[4f68e9060c](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit/commit/4f68e9060c94327c1a39aa282ad17a03a4d7dfe5)|否|
|[baidubce/app-builder](https://github.com/baidubce/app-builder)|master|false|[76a7316c06](https://github.com/baidubce/app-builder/commit/76a7316c0671900b698f9e955afb432ec9a93183)|是|
|[openJiuwen-ai/agent-core](https://github.com/openJiuwen-ai/agent-core)|develop|false|[046a869101](https://github.com/openJiuwen-ai/agent-core/commit/046a869101cb895f1ac0ce6d2220111046fdea61)|否|
|[meituan-longcat/vitabench](https://github.com/meituan-longcat/vitabench)|main|false|[742e240855](https://github.com/meituan-longcat/vitabench/commit/742e240855bf8686a0842360749d5ea970ea3987)|是|
|[XiaomiMiMo/mimoagent](https://github.com/XiaomiMiMo/mimoagent)|mimo-oss|false|[c3df8469f2](https://github.com/XiaomiMiMo/mimoagent/commit/c3df8469f250b15e7906487a6d52be4c1827a509)|是|
|[coze-dev/coze-studio](https://github.com/coze-dev/coze-studio)|main|false|[fefb05ff27](https://github.com/coze-dev/coze-studio/commit/fefb05ff27be1da939612fbf9faf5db62583b8ae)|是|
|[coze-dev/coze-loop](https://github.com/coze-dev/coze-loop)|main|false|[434767e7da](https://github.com/coze-dev/coze-loop/commit/434767e7da1c82aa7c34e7abee31a7293bd42861)|否|
|[bytedance/deer-flow](https://github.com/bytedance/deer-flow)|main|false|[ce0fa4c114](https://github.com/bytedance/deer-flow/commit/ce0fa4c114226213e5e5799cc2fea43687dc4aba)|否|
|[bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)|main|false|[3ac2cb8d94](https://github.com/bytedance/UI-TARS-desktop/commit/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c)|是|
|[agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)|main|false|[22072fd707](https://github.com/agentscope-ai/agentscope-runtime/commit/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5)|是|
|[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)|main|false|[dc96a4698c](https://github.com/opensandbox-group/OpenSandbox/commit/dc96a4698cefc59d0c7e8b393a44f1c795457f26)|否|
|[inclusionAI/AWorld](https://github.com/inclusionAI/AWorld)|main|false|[82af4062e2](https://github.com/inclusionAI/AWorld/commit/82af4062e29e128910afa8622c866f4b99a4d23d)|是|
|[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)|main|false|[c0b8e5704a](https://github.com/Tencent/BrowserSkill/commit/c0b8e5704a69aa93f6cdd40bbb286a9dd485d42b)|否|
|[Tencent-RTC/agent-skills](https://github.com/Tencent-RTC/agent-skills)|main|false|[ec0afda9a2](https://github.com/Tencent-RTC/agent-skills/commit/ec0afda9a277c2f9fd5ab00bebbffbe49c1b3a8f)|否|
|[Tencent/skillhub](https://github.com/Tencent/skillhub)|main|false|[a051f06f79](https://github.com/Tencent/skillhub/commit/a051f06f7944d24ade04bea27735f430b19a8298)|是|
|[MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli)|main|true|[9ab1286b8f](https://github.com/MoonshotAI/kimi-cli/commit/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82)|是|
|[MiniMax-AI/skills](https://github.com/MiniMax-AI/skills)|main|false|[60aaae52bb](https://github.com/MiniMax-AI/skills/commit/60aaae52bb2af8162732751a4332f62a5fef518b)|是|
|[MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)|main|false|[0856b9aef8](https://github.com/MiniMax-AI/MiniMax-MCP/commit/0856b9aef8a9d676bb63bdd6b6426d7b640a3b7a)|是|
|[zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)|main|false|[86f5538298](https://github.com/zai-org/Open-AutoGLM/commit/86f55382982fb054e8fc98ca80609dff8a2cdc3c)|是|
|[jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie)|data_agent|false|[2417e0b8b6](https://github.com/jd-opensource/joyagent-jdgenie/commit/2417e0b8b636d941ad5fb14c59b20dddfef5375d)|是|
|[KwaiKEG/KwaiAgents](https://github.com/KwaiKEG/KwaiAgents)|main|false|[3504ab8a00](https://github.com/KwaiKEG/KwaiAgents/commit/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c)|是|
|[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)|main|false|[cbbe6492a0](https://github.com/netease-youdao/LobsterAI/commit/cbbe6492a02684218376102f383569affeac4b2b)|否|
|[InternLM/lagent](https://github.com/InternLM/lagent)|main|false|[0ab2e2f550](https://github.com/InternLM/lagent/commit/0ab2e2f550477884743cd63fbca7bc4aa7b00290)|是|
|[InternLM/MindSearch](https://github.com/InternLM/MindSearch)|main|false|[7952c5f8a9](https://github.com/InternLM/MindSearch/commit/7952c5f8a956fe6a44228a6a7d528a35340e7c87)|是|

## 维护状态需要两种证据

Kimi Python 仓库 API 的 archived=true，固定 README 明确不再维护并指向 MoonshotAI/kimi-code，旧 PyPI kimi-code 名称也不等于新 CLI。新入口仅登记到增量池，不把它混入 31 仓冻结范围。

AgentScope Runtime 的 archived=false，但固定 README 已公告能力迁入 AgentScope 2.0、将归档。二者并不矛盾：一个是平台当前标志，一个是维护者迁移声明。不能只用 archived=false 就推荐继续在旧架构扩展。源码：[Kimi README](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/README.md)、[Runtime README](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/README.md)。本次读了公告及迁移部分，没有验证新实现的功能等价性。

默认分支也不统一：openJiuwen 为 develop，mimoagent 为 mimo-oss，百度为 master，京东为 data_agent；固定 main 采集会遗漏或读错版本。pushed_at 是仓库活动线索，不是稳定性、主分支变更或“仍维护”的充分证据；故同时读取默认分支提交。

## 来源性质和剩余差距

公司/机构归属继承 catalog/sources.json 的既有 ownership_evidence，本次没有重新逐家验明官网链。ahang1598 是第三方归档；不能把其目录中的产品名当官方发布证明。KwaiAgents、SkillHub 的 API 许可证识别为 NOASSERTION，第三方归档为未识别；这是检测结果，不能推论“没有版权限制”。需要继续核对具体文件许可。

本轮没有下载十个新 HEAD 的大归档。它们均进入增量记录，先判断变更影响，再单独固定版本备份；原来 6235 路径、3085 内容组分母不变。P1-01 继续 in_progress，下一步补齐官网归属、许可例外、迁移后的公开边界；之后才验收并进入海外主线。

## 检索记录

中文：飞书 CLI lark-doc 创建 工作流 官方；英文：AgentScope Runtime archived migration 2.0 Kimi CLI Python archived。补充核验：官方 GitHub lark-shared 绝对路径、AgentScope Runtime Archive Notice。搜索仅作发现，维护结论使用固定 README 和 GitHub API 原值，技能结论使用固定源码。社区镜像及技能市场页没有作为主要证据。
