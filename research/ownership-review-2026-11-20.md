# AWorld 官方归属与版本专项

2026-11-20；接续 P1-01。先重新读取远端 AGENTS、研究入口、方法、排期、progress、backlog、11-19日志和技能索引。基线提交 `212cee5ccacb4f2cd4ec22f338ce1fcadf39277a`，保留已有修改。不是 P1 验收或全项目研究完成。

## 归属、版本和许可

[官方文章](https://www.inclusion-ai.org/blog/aworld/)署名 Ant Group，发布日期2025-07-07，并指向 inclusionAI/AWorld。[组织公开资料](https://github.com/inclusionAI)说明 Ant Group 开源项目并列验证域名 inclusion-ai.org。归属据此闭合，不靠第三方转载或星标。文章榜单与训练效果仅是作者报告，本批未复现，未作为实现收益。

本日 API default_branch=main、archived=false；分支引用和最新提交搜索交叉核对 HEAD 为 `bef598fcfb60da988c2660cafcf0d45f0128e8bf`，最新提交记录日期2026-11-09。10-26审计固定版本 `82af4062e29e128910afa8622c866f4b99a4d23d` 保留，不静默覆盖。当前根 LICENSE 为 MIT，保留 Inclusion AI 版权及许可；README 的 Harness、演化与排行榜说明不自动构成已验证收益。

## 本次具体核对

[激活与证据方案](solutions/aworld-skill-activation-attestation.md)补来源优先级、确定选择、包指纹、Task 回执与正文分层展示。旧版指纹失败跳过证据；新版解析器要求每个激活技能具备证据并报错。旧版调用方是否另行拒绝需分开核，不能泛称旧版没有门禁。

[长任务技能方案](solutions/aworld-long-running-evidence-contract.md)完整读冻结入口及两份引用，区分模型计划、工具观察、复核建议和外部验收。新版 reviewer lease 变更单列版本增量；没有把新提示承诺当成冻结运行时事实，也没有把新入口替换进冻结技能队列。两张独立方案均有流程图和架构图、失败反例、同问题对照与未运行练习。

## 原文交付与缺口

26份固定原文读取/复用，全部核对 Git blob 和 SHA256；其中21份新展开、5份旧展开复用。新 HEAD 的17份仅为指定文件节选，旧版本补展开4份，整包分片与旧哈希记录保留，未重新下载验算。见[本批来源证据](evidence/2026-11-20/aworld-review.json)、[新版节选 manifest](../snapshots/inclusionAI/AWorld/bef598fcfb60da988c2660cafcf0d45f0128e8bf/manifest.json)、[旧版 manifest](../snapshots/inclusionAI/AWorld/82af4062e29e128910afa8622c866f4b99a4d23d/manifest.json)。

官方网页仅保存元数据、原文入口与原创解释，未镜像正文，网页再分发许可未确认；不把链接计为原文备份成功。完整新版归档、全部版本差异、模型请求/执行协议、动态激活后的身份、业务工具和崩溃恢复仍待核。

国内专项从24/31推进到25/31，余6条：第三方技能归档、Tencent-RTC/agent-skills、MiniMax-AI/skills、Open-AutoGLM、JoyAgent-JDGenie、LobsterAI。专项记录不等于所有维护状态、版本差异与备份缺口已验收。P1-01继续；VitaBench原文展开、飞书前次SDK未发布批次仍保留恢复待办。

本批只做源码静态核对、文本差分与字节校验；未运行上游脚本、CLI、模型、测试或业务 API，未部署网站。
