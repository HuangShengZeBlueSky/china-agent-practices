# openJiuwen 与 VitaBench 版本证据

2026-11-17，P1-01。中英文检索分别使用“openJiuwen 智能体框架 官方 中断 恢复”和“openJiuwen agent-core workflow interrupt resume checkpoint”。openJiuwen 官网的 Agent Core 跳到 AtomGit，华为云将 openJiuwen 列在 AgentArts 生态。GitHub 同名组织仓核得 develop、未归档，固定 README 和关键源码保有华为版权，根许可为 Apache-2.0。两托管端具体提交一致性未核，商业 AgentArts 功能只按公开文档登记。[社区官网](https://www.openjiuwen.com/) · [官网指向的 AtomGit](https://atomgit.com/openJiuwen/agent-core) · [华为云](https://www.huaweicloud.com/product/agentarts/openJiuwen.html) · [GitHub 固定许可](https://github.com/openJiuwen-ai/agent-core/blob/5c7c2662b7bcf3998cef975e59f75a07d3b27b22/LICENSE)

GitHub HEAD `5c7c2662b7bcf3998cef975e59f75a07d3b27b22` 更新于 11-16 UTC，与 10-26 的 `046a869101cb895f1ac0ce6d2220111046fdea61` 不同。本批只核当前取消链，未逐条比较两版，不把旧版技能调用结论迁移到新版本。当前 HEAD 保存 9 份指定文件，整仓待补。[固定清单](../snapshots/openJiuwen-ai/agent-core/5c7c2662b7bcf3998cef975e59f75a07d3b27b22/manifest.json) · [技术方案](solutions/openjiuwen-workflow-cancel-checkpoint.md)

VitaBench 1.0 的项目页署名美团 LongCat。仓库默认 main、未归档，当前 `742e240855bf8686a0842360749d5ea970ea3987` 与历史归档版本一致。复读固定 MIT 许可和 README，评分器指定文件另留固定入口。本轮恢复关键结论与证据记录，先前 6 份评分器展开文件及飞书 SDK 方案暂未恢复发布，既有 VitaBench 整包也未重验。[作者项目页](https://vitabench.github.io/) · [固定许可](https://github.com/meituan-longcat/vitabench/blob/742e240855bf8686a0842360749d5ea970ea3987/LICENSE) · [评分方案](solutions/vitabench-window-reward.md)
