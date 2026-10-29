# P1-01：Eino 官方归属与许可补证

检查日期：2026-10-29。仅完成 cloudwego/eino 的来源子单元，P1-01仍在进行；不是新技术方案验收。

[CloudWeGo About](https://www.cloudwego.io/about/)正文明确项目来自字节跳动基础架构团队，并将Eino列入项目列表。[官网Eino概述](https://www.cloudwego.io/docs/eino/overview/)的 Eino GitHub Repository Link 指向 cloudwego/eino。固定[README](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/README.md)反向链接官网并给出字节安全联系入口，形成官网与仓库相互支持的归属链。不是仅凭组织名称推断。

全文核对固定 README 与 [LICENSE-APACHE](https://github.com/cloudwego/eino/blob/0a5ca53b9d3bf7b661dccc863465ec568a421eea/LICENSE-APACHE)，Git blob 分别为 3f84ab00064b908791aead1ec46771486905bf0d 与 66a27ec5ff940d3a9652d2948746ebac4c9d0188。许可正文为 Apache-2.0；本轮最初请求 LICENSE 返回404，随后按README真实链接读取 LICENSE-APACHE。文件名猜错不能解释为没有许可证。本轮复用已登记固定版本归档，没有新增整仓镜像，也没有将依赖树整体许可视为已审计。

README区分核心Eino、eino-ext与eino-examples；读核心仓不等于读全组件实现或字节闭源业务系统。官网当前导航出现v0.9迁移与更多组件，只登记为后续版本对照线索，不把页面导航当功能实证或把当前页面能力直接套在固定提交上。

检索：中文“飞书 cli @file 参数”用于技能发现，结果未作为主证据；英文“CloudWeGo Eino official ByteDance github license”定位上述官方页面。两份官网正文已读取；未确认网页全文镜像许可，只保留原创核验说明与URL，固定仓库文件沿用已有原文档案。没有运行Eino、测试性能或审计新HEAD。下一步继续剩余来源归属及许可、Kimi/AgentScope迁移等价边界与10个版本备份缺口。
