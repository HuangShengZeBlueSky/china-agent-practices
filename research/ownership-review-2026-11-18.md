# BrowserSkill 归属、版本与公开范围

2026-11-18，P1-01。中英文检索分别使用“腾讯 BrowserSkill 官方 浏览器 安全”和“Tencent BrowserSkill official extension authorization”。Tencent 组织仓库与固定 MIT 许可均指向腾讯。README 给出的官网是 browserskill.weixin.qq.com，本次网页读取失败，归属证据使用官方组织仓、根版权及官方维护的扩展隐私说明。[固定许可](https://github.com/Tencent/BrowserSkill/blob/3d4c1bb3b1a29908a299c1ccac1d55bdd54a0a62/LICENSE) · [扩展隐私说明](https://github.com/Tencent/BrowserSkill/blob/3d4c1bb3b1a29908a299c1ccac1d55bdd54a0a62/apps/extension/PRIVACY.md)

GitHub 默认分支 main，未归档。HEAD `3d4c1bb3b1a29908a299c1ccac1d55bdd54a0a62` 日期为 2026-11-17 UTC，与 10-26 的 `c0b8e5704a69aa93f6cdd40bbb286a9dd485d42b` 不同。历史 `6214e3d` 有完整归档清单，本次没有重新验算。10-26 和当前 HEAD 整仓仍欠缺，当前仅展开 11 份指定文件，不作跨版本等价判断。[原文清单](../snapshots/Tencent/BrowserSkill/3d4c1bb3b1a29908a299c1ccac1d55bdd54a0a62/manifest.json)

README 将 Agent/模型、CLI/daemon 和浏览器扩展分开。技能更新后还要求开启新 Agent 会话加载新指令，说明磁盘交付与模型实际上下文存在独立验证点。[固定中文 README](https://github.com/Tencent/BrowserSkill/blob/3d4c1bb3b1a29908a299c1ccac1d55bdd54a0a62/README.zh-CN.md) · [受管理技能更新方案](solutions/browserskill-managed-skill-update.md)

新头含 browser-skill 入口，仅作为当前分发依赖补读；冻结的 6235 路径、3085 组仍按原索引逐项学习。
