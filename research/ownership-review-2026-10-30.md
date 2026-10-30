# P1-01：Qwen-Agent归属与公开范围
检查日期2026-10-30；本次是既有来源核查，不是新增项目验收。

英文检索“Qwen Agent official QwenLM repository license”定位[Qwen官方文档的v2.0页面](https://qwen.readthedocs.io/en/v2.0/framework/qwen_agent.html)，全文明确链接QwenLM/Qwen-Agent并展示Assistant和自定义工具。它是旧版文档，不能当2026年完整能力清单。中文查询“飞书 CLI 文件路径 @file 官方”用于定位输入研究入口，第三方技能市场页未用于关键结论。

全文读取[固定README](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md)及[LICENSE](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/LICENSE)。README版权署名Qwen team、Alibaba Group，与官方文档链接相互支持；根许可为Apache-2.0。Git blob分别为 7d41fe4e7c78fa62d59b03ce4bd444fcdb75eb58、d645695673349e3947e8e5ae42332d0ac3164cd7。沿用既有版本档案，本轮未新镜像、未计新增完整备份；官网页面未确认镜像许可，只留原创核查与原文入口。

README称框架作为Qwen Chat后端，这是作者陈述，不足以证明开源仓等于产品全部后端。同一README历史新闻提示数学示例执行器未沙箱化，而当前FAQ描述Docker代码解释器；它们对应不同时间/入口，不能选择其中一句推广为所有工具的执行保证。本轮未读二者具体执行链，不判定真实隔离强度，也未运行任何例子。

本来源归属与根许可子单元完成，P1-01其余来源、Kimi/AgentScope迁移及10个HEAD备份缺口继续保留。模型权重与第三方依赖许可不由根代码许可自动覆盖；未更改冻结范围。
