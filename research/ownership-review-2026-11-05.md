# 国内来源复核：百度AppBuilder与小米mimoagent

日期2026-11-05，P1-01继续。此次核查两个既有来源，不增加冻结31仓分母，也不宣称完成所有归属/迁移核查。

| 项目 | 当前入口与版本 | 归属与许可原文 | 仍需保留的边界 |
| --- | --- | --- | --- |
| 百度AppBuilder SDK | master，76a7316c0671900b698f9e955afb432ec9a93183；本日API archived=false，与10-26记录相同 | [百度云新闻](https://cloud.baidu.com/news/news_4accd301-fabc-4c67-b79f-05e2932a3a8e)正文“产品使用入口”直接链接baidubce/app-builder；[安装说明](https://ai.baidu.com/ai-doc/AppBuilder/Nly5mrifk)的Go路径再次指向同仓；固定LICENSE为Apache-2.0，保留Baidu版权 | SDK客户端公开不等于云端系统提示、模型编排与业务验证器公开；旧新闻的功能/收益不能升级为本日实测 |
| 小米mimoagent | mimo-oss，c3df8469f250b15e7906487a6d52be4c1827a509；本日API archived=false，与10-26相同 | 固定LICENSE.md与NOTICE明确Xiaomi Corporation版权，并保留mini-swe-agent作者；MIT，NOTICE说明分叉自1.9.0及后续扩展 | 本日官网检索未取得直达mimoagent的反向链接；不能把MiMo Code博客当成mimoagent的实现证明。归属有仓库版权证据，官网直链仍列缺口 |

README、许可证、NOTICE、实现与测试的规范快照及SHA256见[原文清单](evidence/2026-11-05/source-manifest.json)。两仓已有固定版本完整源码归档；本轮复用展开文件，未重新下载或重复计数完整包。未运行安装器、上游测试、模型、业务接口或训练。

## 可见范围的具体收紧

AppBuilder README的AppBuilderClient示例是app_id→create_conversation→run→answer，需云端应用与凭据；本轮读事件处理器得知success是循环结束依据，done/error本身不终止，未知工具返回空output，普通本地函数异常会传播。只检查回调输出首项不能描述成所有工具结果都完成校验。下游序列化仍待读。

mimoagent README把Agent、Model、Environment和Dataset分层。NOTICE区分原生重实现的工具目录与黑盒安装运行第三方CLI；各自上游许可独立，不能把MIT根许可覆盖到运行时下载的所有组件。其白盒工具名/描述相似也不等于拥有第三方内部实现。BaseAgent/DefaultAgent的实际退出包含InfraError，超过文件开头列举的三种状态；并行批次并不保证立即取消。详见[两实现调用链与反例](solutions/tool-outcome-and-termination.md)。

这些是静态源码结论和有条件推导，不是线上故障、漏洞复现或效果比较。README的轨迹/评分能力仍为作者描述，本轮没有读取数据集评分器，未给出性能结论。

## 归档与增量

12份已存在的完整文件原文读回一致：百度4、小米5、飞书3。全部核对Git blob及既有manifest的SHA256/字节数。新展开原文0，完整归档新增0；其中飞书3份为新读依赖，其他文件为归属/控制链的本轮复核。历史大归档本次没有重新下载复验。

网页只保留URL、日期、已读范围和原创解释，未确认再分发许可，不将网页链接计为全文备份。检索偶遇MiMo Code官方文章与MiMo-V2.6论文，分别记为官方片段发现/搜索片段候选，见[增量发现](evidence/2026-11-05/discovery.json)；均不计全文研究或冻结范围。

P1仍待其他来源归属许可、10个当前版本备份影响、Kimi转换/目标宿主、AgentScope2.0映射，以及第三方归档字段矛盾。两仓本日HEAD未变化不意味着31仓全部本日复核。下次继续未闭合来源，优先完成广度清单，再进入P1-02。
