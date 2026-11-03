# AgentScope Runtime 迁移核查：能力承诺与状态兼容不是一回事

日期：2026-11-03。P1-01 子单元；静态阅读，不是部署或迁移成功报告。延续 [31 仓版本审计](repository-audit-2026-10-26.md)，没有把旧 HEAD 写成今日重新审计的 HEAD。

## 本次确认

旧 Runtime 固定版本 22072fd7075ce0c6f43cb39509d6a14b0e60ddb5 的 README 公告建议迁移 AgentScope 2.0，并称沙箱、AaaS 与可观测性已集成。这是维护者的迁移方向与能力声明；不证明旧接口、状态文件、取消时序和依赖环境可直接复用。

同版本 cookbook/en/CHANGELOG.md 的 v1.1.0 章节给出了更具体的断点：Runtime 自定义 Session/Memory 服务与适配器移除；应用改用 Agent 框架自身持久化；AgentApp 从工厂模式改为继承 FastAPI；推荐 lifespan；init/shutdown 装饰器弃用。这是旧 Runtime 内部 v1.0→v1.1 迁移，不能误写成 Runtime→AgentScope 2.0 的完整指南。

目标仓库 agentscope-ai/agentscope @ bdad647d2fee7d66597681ecd89e086b7800dd2a 的 README 已读正文。它明确要求 Python 3.11+，提供 Agent、Toolkit、Credential 和 Agent Service 入口；旧 Runtime README 的前提是 Python 3.10+。版本门槛与示例 API 已有差异，故“换包名即可迁移”缺乏依据。目标 README 展示的多租户、持久化、调度等仍是官方功能说明；本轮未追目标源码验证等价。

根许可全文核对：Runtime 为 Apache-2.0，含 Copyright 2025 Alibaba；目标为 Apache-2.0，含 Copyright 2024 Alibaba，并明确列出部分前端资源的 MIT 与字体 OFL 归属。保留完整 LICENSE，不能用根许可标签覆盖所有资产。版权署名加官方组织的迁移链接是本轮可见归属证据；并未重新核验全部公司官网链。

## 源码子链带来的实质修订

[启动互斥与中断方案](solutions/agentscope-runtime-interruption.md)追到了 AgentApp→InterruptMixin→Local/Redis 后端，包含两类图、测试断言边界和失败时序。Runtime 的任务状态仅记录 RUNNING/STOPPED 等控制标记，Agent 上下文持久化由应用接框架 Session。CAS 能防止有效状态期间同后端的重复启动，但已读路径的 TTL 与无代次写回不足以支持永久单执行者或外部副作用恰好一次保证。

这不是已复现漏洞报告，也不说明 2.0 延续了旧问题。对照表是后续迁移验收的具体起点：

| 旧入口/契约 | 目标入口证据 | 迁移验收还缺什么 |
| --- | --- | --- |
| AgentApp query、SSE | README 的 Agent Service | 请求 schema、事件格式、异常与取消的逐字段映射 |
| Runtime JSONSession 示例 | README 的 SQL/NoSQL 会话持久化说明 | state schema、版本升级、历史会话加载及失败回滚 |
| Local/Redis InterruptMixin | README 的中断、会话隔离和后台任务说明 | owner/代次、锁期限、取消确认、订阅时序与重启恢复 |
| Python 3.10+ | Python 3.11+ | 依赖锁文件及宿主升级影响 |
| 根 Apache-2.0 | Apache-2.0 加第三方资源通知 | 新版本整包资产/许可证完整清单 |

## 原文与备份

全部使用固定 GitHub 文件；[来源清单](evidence/2026-11-03/source-manifest.json)有路径、版本、阅读范围、字节数、Git blob、SHA256。原文落在 snapshots/{owner}/{repo}/{commit}/files/{path}，相应 manifest 同步依赖与范围。

本轮核对 24 份原文：Lark 13、Runtime 9、目标 AgentScope 2。6 份复用既有展开文件；16 份补充既有版本的展开文件，另 2 份建立目标版本的指定文件节选。目标 AgentScope 版本仍没有完整归档；只存 README/LICENSE 不会消除 10 个完整版本备份缺口。未修改 31 仓/40 版本的既有完整归档基线，也不扩大 6235 路径/3085 组。

## 检索与纳入标准

本轮中英文查询：飞书 CLI docs revision-id 版本 冲突 重试；larksuite cli revision conflict retry docs update；AgentScope Runtime migration 2.0 archive deployment official；site.agentscope.io AgentScope 2.0 Runtime 迁移 部署；site.github.com/agentscope-ai/agentscope runtime migration 2.0。

检索发现官方 Runtime README 与 CHANGELOG 后，回到固定源码读取。Go 包镜像、技能市场、社区博客只用于发现，不作为结论依据。搜索到 larksuite/cli issue 1093 的并发覆盖报告标题，尚未读 issue 正文与维护者回复，登记为候选反证，不把摘要中的“隐藏参数”等说法套到本次固定版本（已读参数定义没有 Hidden 字段）。同名 AgentScope 论文也不据名称当同项目证据。

## 剩余与恢复入口

P1-01 继续进行：其他官方来源链与许可、Kimi 新实现、十个版本缺口、第三方归档元数据一致性。AgentScope 后续先按上表取目标源码并对照，暂不承诺迁移兼容。当前文件不是 P3 全架构验收，也不是 2.0 完整方案卡。
