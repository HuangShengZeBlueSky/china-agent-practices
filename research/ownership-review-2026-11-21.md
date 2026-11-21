# Tencent RTC 来源与停止边界专项

2026-11-21；P1-01 继续。本日读取远端最新规则、方法、排期、台账、上次日志及16个技能分片。国内专项26/31，剩5条；专项记录不代替版本归档和阶段验收。

[官网](https://trtc.io/agent-skills)的 View on Github 实际指向 Tencent-RTC/agent-skills；固定根 MIT LICENSE 保留2026 Tencent RTC版权，闭合官网到源码归属链。该仓是公开集成技能，不能扩展为 CodeBuddy 等产品内部完整实现。产品“自动构建与验证”是官方承诺，本批只核 Stop 子链。

本日 main `f0a4b394cc1e2a1a5a5eef8313dab8c43e533ac5`、archived=false，分支引用与提交搜索互证。最初 `55a6bcf643acb4104105359ed0a1d194bdee7696`、10-26 `ec0afda9a277c2f9fd5ab00bebbffbe49c1b3a8f` 均保留，新旧整版差异未全核。[停止方案卡](solutions/trtc-stop-gate-boundaries.md)分清 Python exit 2、包装器 exit 0/block、缺依赖放行，以及 YAML 精确子串识别的边界。安装器实际宿主接线、apply 验证强度待核。

同时恢复 [AWorld 冻结协议保存](solutions/aworld-protocol-persistence-boundary.md)，不是新 HEAD 的替代解读。11份原文字节核对通过，10份新增展开、1份旧许可复用；腾讯新版8份节选、AWorld旧版补2份，整仓未下载重验。见[来源证据](evidence/2026-11-21/source-review.json)。网页仅保存来源入口与原创解读，未镜像正文。

未执行上游脚本、安装器、上报、模型或业务API；未部署网站。余5条为第三方技能归档、MiniMax skills、Open-AutoGLM、JoyAgent-JDGenie、LobsterAI。VitaBench与飞书SDK旧未发布批仍是恢复待办。
