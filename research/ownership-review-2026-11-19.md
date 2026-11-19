# UI-TARS Desktop 归属、归档状态与两套 SDK

2026-11-19，P1-01。中文检索“字节 UI TARS Desktop SDK 官方 GUIAgent”，英文检索“UI TARS SDK GUIAgent finish status screenshot”。ByteDance Seed 的 2025-04-17 文章链接 UI-TARS 模型仓，模型仓 README 再链接 UI-TARS-desktop，配合字节组织仓、固定版权和 Apache-2.0 根许可构成来源链。[Seed 公告](https://seed.bytedance.com/en/blog/%E5%AD%97%E8%8A%82-seed-%E6%99%BA%E8%83%BD%E4%BD%93%E6%A8%A1%E5%9E%8B-ui-tars-1-5-%E5%BC%80%E6%BA%90-%E5%A4%9A%E9%A1%B9-benchmark-%E5%8F%96%E5%BE%97-sota-%E8%A1%A8%E7%8E%B0) · [模型仓到 Desktop](https://github.com/bytedance/UI-TARS) · [固定许可](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/LICENSE)

Desktop 默认分支 main，HEAD 仍为 `3ac2cb8d946d78d5ff92ad17b318eaafa18c178c`，与 10-26 相同。然而今日 API 返回 archived=true，旧审计的 archived=false 只保留为历史记录，具体归档日期未核。主仓已有该版本整包，本轮只读清单和指定文件哈希，不重新验证整包。

同一提交同时存在 packages/ui-tars/sdk（package.json 版本 1.2.3，README 标注 Experimental）和 multimodal/gui-agent/agent-sdk。早期案例读后者，本轮重点读前者的公开导出、run 循环、上下文和错误回调。两套实现的调用链分别记录，当前默认 Desktop 的实际接线尚待核。[1.2.3 包入口](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/packages/ui-tars/sdk/package.json) · [另一套 GUIAgent](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/multimodal/gui-agent/agent-sdk/src/GUIAgent.ts) · [方案卡](solutions/ui-tars-sdk-terminal-status.md)
