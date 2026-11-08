# OpenSandbox 归属、固定许可与版本变化

2026-11-08，P1-01。AAIF 在 2026-10-22 公告明确 OpenSandbox 由阿里巴巴贡献。项目官网与源码 README 互指，当前 GitHub 组织为 opensandbox-group，默认分支 main，未归档。项目保留 Alibaba 命名空间的 SDK；证据支持阿里来源及 AAIF 项目身份，商业托管服务与部署版本需另核。[AAIF 公告](https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects) · [项目官网](https://open-sandbox.ai/) · [固定 README](https://github.com/opensandbox-group/OpenSandbox/blob/1f3ec4f27432ea2386cb8b357d70d2036c11f81c/README.md)

10-26 审计提交 `dc96a4698cefc59d0c7e8b393a44f1c795457f26` 与 11-08 核对的 `1f3ec4f27432ea2386cb8b357d70d2036c11f81c`（上游 11-07 UTC 提交）使用字节相同的 Apache-2.0 根许可；第三方依赖许可另核。GitHub 比较返回领先 604 个提交，落后 0 个，文件列表上限内只用于定位。旧版命令适配器直接去掉 SSE 请求的通用重试包装；新版保留网关唤醒超时这一种有条件的重发路径。两版均只新增指定文件快照，整包仍待，旧案例和原基线保留。[旧适配器](https://github.com/opensandbox-group/OpenSandbox/blob/dc96a4698cefc59d0c7e8b393a44f1c795457f26/sdks/sandbox/python/src/opensandbox/adapters/command_adapter.py) · [新适配器](https://github.com/opensandbox-group/OpenSandbox/blob/1f3ec4f27432ea2386cb8b357d70d2036c11f81c/sdks/sandbox/python/src/opensandbox/adapters/command_adapter.py) · [固定对比](https://github.com/opensandbox-group/OpenSandbox/compare/dc96a4698cefc59d0c7e8b393a44f1c795457f26...1f3ec4f27432ea2386cb8b357d70d2036c11f81c)

本次 HEAD 提交修改 OSEP-0025。提案整体处于 implementing，专门的 HTTPS resolver 调用者 JWT 认证标为已设计、未实现。凭据库路由存在不能证明该认证落地；代码入口和提案状态分别记录。公告、官网和研究提案都没有用来证明当前服务部署或安全实测。[固定提案](https://github.com/opensandbox-group/OpenSandbox/blob/1f3ec4f27432ea2386cb8b357d70d2036c11f81c/oseps/0025-credential-vault-provider-spi.md)

中英文检索使用“阿里 OpenSandbox 官方 开源 Agent 沙箱 生命周期 网络 GitHub”和“Alibaba official OpenSandbox sandbox isolation egress lifecycle”。官方网页保留链接，源码与提案保留完整所选文件和哈希。未运行上游代码。
