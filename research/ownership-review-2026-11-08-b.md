# Qwen Code 归属、许可和固定版本补核

2026-11-08，P1-01 静态核查。官方文档描述模型自行调用技能与用户通过斜杠命令显式调用两条入口。源码仓由 QwenLM 组织维护，默认分支 main，未归档。当前根许可为 Apache-2.0，保留源码各文件的版权和许可声明；不将根许可外推为所有依赖许可，也不推定任何云端产品采用相同部署。[官方技能文档](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/) · [固定 README](https://github.com/QwenLM/qwen-code/blob/53e3e3ac2a01c2c933075d4941d0d2ceb18b106e/README.md) · [固定许可](https://github.com/QwenLM/qwen-code/blob/53e3e3ac2a01c2c933075d4941d0d2ceb18b106e/LICENSE)

10-26 审计版本 `338f13366c1d86e586f7e0785942740da3503887` 的根包清单为 0.26.1；本次读取 `53e3e3ac2a01c2c933075d4941d0d2ceb18b106e`（2026-11-08 UTC），根包清单为 0.27.0。对比显示领先 613 个提交、落后 0 个，接口返回 300 个文件条目，不能据此推断全量变更规模。两版技能工具 Git blob 不同，需分别固定结论。当前保留六份指定文件，旧版保留三份（含同字节根许可）；两版整仓均未归档，既有 461be87、2050db8 的归档与案例保留。源码版本不能证明 npm 实发版本。[固定对比](https://github.com/QwenLM/qwen-code/compare/338f13366c1d86e586f7e0785942740da3503887...53e3e3ac2a01c2c933075d4941d0d2ceb18b106e) · [机器证据](evidence/2026-11-08-b/source-review.json)

中文与英文检索分别用“通义千问 Qwen Code 官方 开源 CLI 技能 加载”和“Qwen Code official docs QwenLM github skills activate_skill”。阅读官方技能说明及固定源码，社区和搜索摘要未作为结论。官方网页只存链接。本轮未验证模型调用或性能。
