# P1-01：飞书官方归属链补证
检查日期：2026-10-28。恢复最早未验收阶段；本轮完成一个来源的官网反向链接子单元，没有把31仓全部标成完成。

飞书官网[安装与使用指南](https://www.feishu.cn/content/article/7623291503305083853)正文的海外安装说明及“全面开源”段均明确指向 https://github.com/larksuite/cli ，与固定代码的 Lark Technologies Pte. Ltd. 版权声明及 MIT LICENSE 相互支持。由此补齐“官网 → 仓库 → 固定许可”的链；不同于只凭仓库名字或第三方作者自述归属。固定提交017b19a793ad71794a02887ede04757f3d82e10d的许可已随[源码节选](evidence/2026-10-28/lark-code/manifest.json)保存并校验。

官网关于CLI调用成功率高于直接API的描述是产品声明，本轮未见对照预算、分母、实验设置，不纳入已验证收益。官网页面全文镜像许可未确认，本轮只保留URL、检查日期、原创归属判断，不计作网页备份成功。

同时尝试打开 https://runtime.agentscope.io/ ，正文提取为空；搜索摘要虽能显示迁移说明，也不算官网全文已读。回读固定 [Runtime README开头](https://github.com/agentscope-ai/agentscope-runtime/blob/22072fd7075ce0c6f43cb39509d6a14b0e60ddb5/README.md)确认维护者迁移声明，但未新增“新旧实现等价”结论。此项仍留在待办。

检索：中文“飞书 CLI 原子写入 SaveExclusive”；英文“AgentScope Runtime migration AgentScope 2.0 archived”。官方飞书网页用于归属链，GitHub固定代码用于实现；第三方CLI、镜像和市场页未作为该实现证据。新出现来源未自动纳入冻结范围。P1-01继续in_progress；其余归属链、许可例外与10个新HEAD备份缺口不变。
