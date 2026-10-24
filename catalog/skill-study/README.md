# 全量技能学习队列

基线：2026-10-23 的原文库；2026-10-25 建立阅读台账。全部 **6,235 个路径**，按入口字节内容组成 **3,085 组**，分成 16 个小分片供后续研究逐批读取。

[机器索引](index.json) · [原文总索引](../original-skills.json) · [研究方法](../../research/method.md) · [阶段排期](../../research/schedule.md)

## 当前状态

5 组有历史入口阅读记录；3,080 组尚未逐项解读。新台账的整包依赖核对、完整研究验收、真实业务执行均尚未完成。既有局部阅读证据保留在 prior_reading，不因为生成台账就升级状态。

## 记录结构

content_id 表示入口内容组。occurrences 保留每个 source_id、仓库、提交和路径；dependency_status、host_status、review_status、execution_status 分别记录依赖核对、宿主条件、研究验收与实际运行。analysis_file 指向中文解读；solution_file 指向有流程图和架构图的方案卡。

入口相同只允许复用入口解读。整包结论复用必须对照依赖清单和宿主，并填写 equivalence_evidence。不能把一个代表样本读完后批量标记所有副本完成。

## 批次工作

先按主题选择官方技能，再扩展相近变体和历史。每次读取一个可消化分片，选择少量未完成组；从固定快照读完整入口和关键依赖，写中文笔记、方案图或已有方案的有据引用，并逐路径核对差异。需要跨次阅读的内容保存精确断点。

脚本 scripts/build_skill_study_queue.py 只负责从冻结基线生成/合并台账，保留人工状态；不会生成学习结论。新增技能另入增量池，只有显式升级范围才改变当前分母。

研究完成与实跑完成分开统计。格式验证成功、下载成功、模型读过摘要都不足以把 review_status 改为完成。

## 分片

- [内容组 0](groups-0.json)
- [内容组 1](groups-1.json)
- [内容组 2](groups-2.json)
- [内容组 3](groups-3.json)
- [内容组 4](groups-4.json)
- [内容组 5](groups-5.json)
- [内容组 6](groups-6.json)
- [内容组 7](groups-7.json)
- [内容组 8](groups-8.json)
- [内容组 9](groups-9.json)
- [内容组 a](groups-a.json)
- [内容组 b](groups-b.json)
- [内容组 c](groups-c.json)
- [内容组 d](groups-d.json)
- [内容组 e](groups-e.json)
- [内容组 f](groups-f.json)

