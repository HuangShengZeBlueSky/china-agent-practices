# 全球 Agent 工程学习计划

建立日期：2026-10-25。时区：Asia/Shanghai。目标：从中国、海外大厂、开源实现和前沿论文中，学会设计 Skill、MCP、CLI、Harness，以及 Subagent、Team、Goal、Plan 等组件，并能解释它们如何组合成垂类 Agent。

[研究方法](method.md) · [阶段排期](schedule.md) · [进度台账](progress.json) · [具体任务](backlog.json) · [来源地图](source-map.md) · [完整技能阅读队列](../catalog/skill-study/README.md) · [运行规则](automation.md)

## 学到什么才算完成

每个独立技术方案都交付一份中文方案卡：问题、适用条件、真实输入输出、流程图、架构图、模型与普通程序的职责、状态与上下文、失败恢复、验收方法、替代方案、迁移练习，以及固定原文证据。图必须对应已读材料，推测部分明确标识。每篇重点论文另拆数据、算法、实验设置、消融、局限和可复用部件。

本计划以理解和学习为中心。广泛收集后先比较再判断；不以厂商名气、星标、宣传数字或资料数量代替结论。关键设计至少对照另一种实现，并主动寻找失败案例和相反证据。

## 已有基础与本次启动

继承现有 31 仓库、40 版本、6,235 个技能路径、3,085 份按入口字节去重的内容，以及完整源码备份。此统计是 2026-10-23 的固定基线，不包含本次新增的协议节选快照。原文已备份不等于逐项解读；已有 5 个技能入口的阅读记录保留原等级。

本次新增：
- 可接续的阶段计划、任务清单、证据标准和调研日志。
- 全部 6,235 个路径的阅读归属，按 3,085 个入口内容组建队列；依赖差异仍按路径分别核对。
- [八类组件如何组合](solutions/component-map.md)：教学架构与职责边界。
- [Skill 规范与参考实现](solutions/skills-spec.md)：规范、元数据生成、静态检查的实际边界。
- [MCP 的版本化架构](solutions/mcp-versioned.md)：2026-07-28 规范与旧握手版本的区别。
- 两个协议项目共 7 份指定原文文件，保留许可证、固定提交、Git blob 与 SHA256 校验。它们是节选快照，不是新增两仓库的完整备份。
- 最新论文进入分级阅读池，摘要登记不冒充全文精读。

## 如何接续

每次从 progress.json 与 backlog.json 读取最早未完成且依赖满足的任务。完成一个可核查的小单元，保存证据与结论，更新状态，再继续下一个。技能队列同步推进，新增线索进入单独增量池，不能偷偷扩大本轮“全部”的分母。

主线首轮预计 24 周，2026-10-26 至 2027-04-11。此日期是阶段规划，不承诺届时读完数千个技能及其依赖。每周用真实完成量更新剩余时间。没有完成的任务继续保留，不能为赶进度把“索引”“摘要”改成“精读”。

GitHub 是本轮排期、证据和研究进度的持久入口。研究看板保留现有内容；仓库新增文档不会自动出现在已部署网站中，网站更新应另记实际部署结果。


## 2026-10-26 更新

[31 仓维护与版本复核](repository-audit-2026-10-26.md)完成元数据子单元，P1-01 仍待归属与许可复核。[飞书文档技能方案卡](solutions/lark-doc-routing-and-validation.md)新增两类图和失败边界；仅入口及部分依赖已读，整包未验收。当前版本缺失的10个快照已单列增量记录，没有改变技能基线分母。

## 2026-10-27 更新

[归属与许可例外复核](ownership-license-review-2026-10-27.md)完成两来源子单元，P1-01仍在进行。[文件后端与草稿契约](solutions/lark-fileio-and-draft-contract.md)追到注入、回退、清理和验收边界；lark-doc目录累计读6/44，整包未验收。新增7份固定代码节选并验证Git blob，2份既有原文SHA256核对通过。未实跑，网站未部署。

## 2026-10-28 更新

[飞书官网归属链补证](ownership-review-2026-10-28.md)完成一个来源子单元。[原子发布](solutions/lark-atomic-publication.md)追到VFS和OS调用，复核上游测试断言不足；[白板子任务与扩展块](solutions/lark-whiteboard-subagent-contract.md)区分技能分工、宿主调度、读写数据模型。两卡各有两类图。目录累计8/44；新增8份指定文件（含许可）校验通过；未实跑，未部署网站。P1继续进行。

## 2026-10-29 更新

[异步回滚与正文恢复](solutions/lark-history-recovery.md)补齐两类图、真实API适配、状态机归属、上游测试边界与失败练习；命令无错误不代表业务成功。目录累计10/44；5份完整文件节选含许可通过Git blob与既有依赖哈希校验。[Eino归属补证](ownership-review-2026-10-29.md)读官网反向链和固定许可。P1-01继续，未实跑、未部署网站。

## 2026-10-30 更新

[文件输入与基线](solutions/lark-input-provenance.md)闭合快捷命令@file、来源位、路径捕获及相邻决策静态子链；发现两个解析器空白/空文件/BOM语义不同。[素材预览与下载](solutions/lark-media-side-effects.md)区分read标记与本地写副作用、存在检查与排他保存。两卡均有两类图；14份原文节选含许可已校验。目录累计12/44。[Qwen-Agent归属核查](ownership-review-2026-10-30.md)补固定README与许可证据。仍在P1，未实跑、未部署网站。

## 2026-11-03 更新

[文档版本与重试边界](solutions/lark-update-conflict-contract.md)追到错误分类和SDK调用边界；[Runtime启动互斥与中断](solutions/agentscope-runtime-interruption.md)对照本地锁、Redis Lua与任务TTL，两卡各有流程和架构图。[AgentScope迁移核查](ownership-review-2026-11-03.md)区分旧Runtime内部迁移与2.0兼容性。24份原文校验，18份补存规范目录、6份复用；目录13/44，整包0、实跑0。[排期复核](review-2026-11-03.md)补登记缺失的周末检查，按依赖继续P1-01；网站未部署。

## 2026-11-04 更新

[Kimi迁移边界](solutions/kimi-migration-state-boundaries.md)补源码与许可核查，区分文件复制、目标运行和完成标记；10份固定原文节选已校验。[体裁与证据路由](solutions/lark-genre-evidence-routing.md)对照技术文档三模式与调研报告，提示契约不等于机器门禁。两卡均有两类图。目录15/44，P1-01继续，整包0、实跑0、未部署网站。

## 2026-11-05 更新

[百度与小米来源核查](ownership-review-2026-11-05.md)补官方归属、根许可、第三方边界及两仓本日HEAD；[工具结果与结束判定](solutions/tool-outcome-and-termination.md)用实际分支反证立即取消和结束即成功。[指标与决策证据契约](solutions/lark-quantitative-evidence-contract.md)新读3份依赖，目录18/44，剩26。两张方案各有两类图；12份既有原文读回和哈希核对，原文新增0。P1-01、整包与实验继续待办，未部署网站。

## 2026-11-06 更新

[提案与执行计划](solutions/lark-proposal-plan-contract.md)补路由、真实授权证据、依赖与退出条件，含流程图、架构图、反例及学习练习。[Coze官方归属补证](ownership-review-2026-11-06.md)区分开源与商业版、模板装配与实际执行。6份既有原文核对，技能目录21/44；P1继续，整包0、实跑0，网站未部署。

## 2026-11-07 更新

[SOP、PRD与周期报告](solutions/lark-operational-evidence-contract.md)完整解读3份依赖，区分操作证明、可观察需求和状态证据，含两类图、跨实现结束判定对照与未运行练习。三份既有原文逐字读回并哈希核对，目录24/44，整包0、实跑0。[周末复核](review-2026-11-07.md)归集31仓证据、79条来源状态及真实吞吐，明确P1剩余和下一批trae-agent/CloudBase；阶段未验收不按日期切换，网站未部署。

## 2026-11-08 更新

[Trae Agent 与 CloudBase](ownership-review-2026-11-08.md)补归属、许可及版本差异。CloudBase 两版新增指定原文节选，整包未发布。[会议纪要与复盘](solutions/lark-meeting-retrospective-evidence.md)含两类图、反例和练习，目录 26/44，整包与实跑均 0。[P1 复核](review-2026-11-08.md)确认未达验收，按依赖顺延。

[11-08 追加批次](log/2026-11-08-b.md)补 Qwen Code 归属、权限与恢复，飞书目录 28/44。

[11-08 OpenSandbox 与体裁路由批次](log/2026-11-08-c.md)补归属、唤醒重发和三份路由，目录 31/44。

## 2026-11-09 更新

[MiniMax MCP 整包与归属](ownership-review-2026-11-09.md)已核归档和固定文件，[查询与交付](solutions/minimax-mcp-video-delivery.md)追到副作用及异常差异。[飞书三类路由](solutions/lark-creative-media-marketing-routing.md)推进目录至 34/44。

## 2026-11-10

[DeerFlow 归属](ownership-review-2026-11-10.md)及[输入归一化](solutions/deerflow-model-input-normalization.md)已补。[平台叶](solutions/lark-platform-draft-boundaries.md)推进目录至37/44。

## 2026-11-11

[Lagent归属](ownership-review-2026-11-11.md)与[执行契约](solutions/lagent-action-status-and-hooks.md)已补。[飞书媒体补偿](solutions/lark-media-insert-recovery.md)发现同版Wiki入口文档与代码差异，目录40/44，整组未验收。
