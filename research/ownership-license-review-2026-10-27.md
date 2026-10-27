# P1-01：归属、许可例外与公开边界复核
日期：2026-10-27。完成两个固定来源的许可正文复核及公开范围核对；不是31仓全部验收，P1-01继续进行。

|来源与固定版本|实读证据|本轮判断|
|---|---|---|
|Tencent/skillhub @ a051f06f7944d24ade04bea27735f430b19a8298|README全文、LICENSE全文；产品站点正文提取不足|腾讯组织仓库与版权声明、tencent.com 联系邮箱形成相互支持证据；根许可正文明确MIT|
|KwaiKEG/KwaiAgents @ 3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c|README开头项目归属与Lite范围段、LICENSE.txt全文|README自述为快手团队；根许可为CC-BY-NC-SA-4.0；并未重新核验全部官网反向链接|

## 固定原文和复核凭据
- [SkillHub LICENSE](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/LICENSE)，Git blob：dbbab6c2a989e436545a481e20553b17023d4832。
- [SkillHub README](https://github.com/Tencent/skillhub/blob/a051f06f7944d24ade04bea27735f430b19a8298/README.md)，说明开源范围为API文档与示例、DSH插件、官方Skills三部分。
- [KwaiAgents LICENSE.txt](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/LICENSE.txt)，Git blob：bfef380bf7d9cb74ec9ba533b37c3fbeef3bdc09。
- [KwaiAgents README](https://github.com/KwaiKEG/KwaiAgents/blob/3504ab8a00a3c3f5e5a4ccbd12dee64997f9561c/README.md)，已读开头归属与Lite差异段；并未把论文摘要登记升级为全文精读。

复用已有版本归档，本轮未重下整仓；原文许可与现有catalog记录一致。上一轮API检测NOASSERTION不否定正文已明确给出的许可证；因此以后台账分别记录机器检测与人工正文核对，不能覆盖成“无许可”。

## 为什么这影响工程学习
SkillHub开源插件、文档和官方技能，不意味着公开了平台全部后端，也不意味着平台聚合的全部技能都由腾讯编写或采用同一许可。固定README中的13万+等统计只是该版本产品自述，本轮不作为已验证的当前数量，也不扩大本仓6235路径的冻结分母。

KwaiAgents README主动区分论文系统与开源Lite：工具更少、缺少记忆机制、代码基于BabyAGI与Auto-GPT等项目演化。读Lite调用链不能据此声称复现论文完整版；论文的效果数字也不能直接贴到Lite。许可复核仅记录源文件文本的标识与条件，不作整个依赖树的授权结论。

旧目录中第三方归档写“不镜像原文”，后续实际已有备份；这是历史目录描述与当前状态的不一致，需在全量来源/备份审计时纠正。不能因为文件已备份就反推已得到上游许可。本轮不删除已有历史、不改变访问权限，也不新增该来源的全文镜像。

## 检索轨迹与剩余工作
中文查询“腾讯 SkillHub github Tencent 官方”；英文查询“KwaiAgents github license Kuaishou”。搜索结果只用于定位官方仓库；关键判断使用固定源码正文。访问 https://skillhub.cn/ 的正文抽取不足，没有把搜索摘要当官网全文备份。社区转载、市场目录未作为结论依据。

剩余：其余来源逐家官网归属链、第三方许可与备份记录一致性、10个新HEAD备份差异、Kimi新实现与AgentScope迁移等价性。P1-02尚不启动验收；不因10月27日原排期而跳过P1-01。
