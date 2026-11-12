# MindSearch 官方归属、版本与依赖

2026-11-12，P1-01。上海人工智能实验室官方发布材料将 MindSearch 列为书生工具链的一部分，作者论文直接链接 InternLM/MindSearch；固定根许可证 Apache-2.0 标注 Shanghai AI Laboratory。默认分支 main、仓库未归档，所查最新提交仍为 `7952c5f8a956fe6a44228a6a7d528a35340e7c87`（2025-07-04 UTC），与 10-26 审计一致。[实验室发布](https://www.shlab.org.cn/news/5443966) · [作者论文](https://arxiv.org/html/2407.20183) · [固定许可](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/LICENSE)

源码依赖锁定 `lagent==0.5.0rc2`。11-11 研究的 Lagent 仓库 HEAD 是另一提交，不能替代这个依赖版本的实际运行证据。已对照固定原文与旧 manifest，新增展开入口和依赖清单两份，完整压缩包沿用既有记录，未重验。产品部署、服务配置及运行版本未核。[依赖清单](https://github.com/InternLM/MindSearch/blob/7952c5f8a956fe6a44228a6a7d528a35340e7c87/requirements.txt) · [引用方案](solutions/mindsearch-citation-integrity.md)

检索使用“上海人工智能实验室 MindSearch 思维搜索 开源”和“MindSearch InternLM official WebPlanner graph”。读作者正文的方法与实验相关段落，论文完整精读、附录和评测器复现留在原计划，未将作者报告计为本轮效果验证。
