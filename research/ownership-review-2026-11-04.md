# Kimi 新旧入口、许可与迁移边界

2026-11-04，P1-01子单元，未完成整阶段。已从远端规则和11-03日志恢复。

旧MoonshotAI/kimi-cli固定9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82的[README](https://github.com/MoonshotAI/kimi-cli/blob/9ab1286b8fe4e6bcd116949a27ce5e0ac3389c82/README.md)明确归档、不再维护并指向新仓库；PyPI的kimi-code是旧别名，不是新实现。旧声明原文已读，保留既有快照，不执行安装脚本。

本日读取新仓库API：MoonshotAI/kimi-code，默认main，archived=false；固定HEAD 444c609e8e6629d43fb7fd571a8db48ce5a41570。新README及根LICENSE全文核对为MIT、Copyright 2026 Moonshot AI。旧README声明Apache-2.0，因此不能把旧许可沿用到新仓库。此结论只覆盖所选文件，未完成新仓库全部第三方依赖许可审计。

[迁移源码方案](solutions/kimi-migration-state-boundaries.md)追清调度、Skill/Plan复制、报告、标记，10份原文完整节选已哈希校验。最重要的边界：复制Skill不核验同名内容等价；Plan只是文件未接入Plan模式；完成标记会写旧source目录。原文中的“不改动旧数据”不应扩大为目录没有任何写入。会话与配置转换器仍待读，不能宣称迁移功能全量验证。

固定新迁移指南仍写旧CLI可照常使用，旧仓库公告却说现有安装不再支持并将停止工作。两个文本的维护措辞存在张力，本轮保留版本与原文，不承诺旧客户端当前可用。新README区分直接二进制安装无需Node与开发环境Node≥24.15.0，不能混成所有用户都需安装Node。

检索：中文“Kimi CLI Python 归档 kimi-code 迁移 官方”；英文“site.github.com/MoonshotAI/kimi-code migration Python license”。检索仅定位官方入口，实际结论取自固定README、指南和源码。镜像站、论坛与搜索摘要不作实现依据。

这是已有Kimi迁移待办的新目标增量；原31仓/40版本、6235路径/3085组不变。新仓库只备份10份指定文件，未计完整归档；原31仓内10个完整版本缺口仍保留，新Kimi整仓备份另列增量缺口。未执行脚本、登录、业务API或模型调用，网站未部署。

后续：配置/MCP/session转换器与目标扫描器；其余国内来源归属与许可；AgentScope目标映射和既有版本备份缺口。
