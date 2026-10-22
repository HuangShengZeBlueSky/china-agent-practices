# 第三方技能归档：作者怎样采集、整理，以及我们能学到什么

> 核对日期：2026-10-21。研究快照：`ahang1598/doubao-workbuddy-qwenwork-skills@1c9239cc90585f57d9e06d32deffc017bbff5802`，提交时间为 2026-10-20 10:03:16 UTC。本文是对既有第三方来源的展开研究，不增加独立上游仓库数量。源码静态核对，未安装或执行其中的技能、同步脚本和业务工具。

## 结论

这个仓库的核心方法是：**从作者本机各产品的技能和插件缓存采集文件，按平台保存，用文件差异保留更新历史，再生成目录导航。** 作者把持续采集与阅读入口做成了工程流程。它为我们提供了大量值得逐份研究的材料；材料能证明归档文本如何规定行为，不能单独证明厂商线上系统的完整提示词、实际调用上下文或运行效果。[根 README][root] 和 [同步脚本][sync] 是理解这个仓库的第一组材料。

最值得迁移的有三项。第一，把来源、当前路径、历史删除和版本线索留下来，后续才能解释内容为何变化。第二，把目录盘点与深入学习分开，不能因为列出了几千份文件就标记为已经掌握。第三，研究技能如何交接事实、约束工具、恢复失败和验收产物；这些行为契约比单独收集一句角色提示词更有工程价值。

### 证据分别能说明什么

| 层次 | 本次可以确认的内容 | 仍然不能确认的内容 |
| --- | --- | --- |
| 作者自述 | 根 README 称归档本机已安装的技能、专家与插件市场；各平台 README 给出本地来源路径 | 作者设备之外的产品覆盖范围、每个文件最初如何获得 |
| 同步源码 | 本地路径映射、文件哈希比较、删除归档、索引生成、计划任务及 Git 提交流程 | 计划任务是否每天成功，作者本机原文件是否与每次提交完全一致 |
| Git 树与提交 | 固定提交中的文件路径、blob 标识、增删改记录；一个删除归档实例 | 文件作者身份、未提交的文件、服务端动态提示或工具配置 |
| 代表文件深读 | 六份技能怎样描述输入、上下文、执行分工、失败恢复和验收 | 宿主是否强制执行这些声明，实际业务调用是否成功 |
| 我们的迁移建议 | 如何建立自己的证据目录、语义学习记录和看板状态 | 建议尚未经过的运行实验 |

根目录未发现许可证，GitHub 仓库许可元数据为 `null`；本次六个代表包目录也未发现独立的 LICENSE/COPYING 文件。因此本仓库保存原创分析、元数据和原文链接，不镜像这些技能全文，也不据此推断其可再分发或商用范围。

## 一、采集对象：产品目录与实际来源要一起看

[四份产品 README][doubao-readme] 与 [SourceSpec 配置][sync] 可以互相核对。下表将作者个人 Windows 用户目录统一写成 `%USERPROFILE%`，保留产品路径结构。

| 仓库平台 | 本机来源范围 | 仓库中的主要分组 | 应怎样理解 |
| --- | --- | --- | --- |
| Doubao | `AppData/Local/Doubao/User Data/Default/.doubao/agent_mode/workspace/.skills` | `doubao/skills` | 作者本机豆包办公相关技能目录的快照 |
| WorkBuddy | `.workbuddy/plugins/marketplaces`、`.workbuddy/skills`、连接器市场及默认注册表 | `experts`、`official_experts`、`cb_teams_experts`、`skills`、`connectors` | 混合了多个市场、专家包、连接器和技能，包含包内嵌套技能 |
| QwenWork | `.qwenworkcn/plugins`、`.qwenworkcn/skills`、MCP 注册表与市场元数据缓存 | `experts`、`skills`、`connectors` | 插件、技能和连接器登记信息采用不同索引方式 |
| ChatGPT | `.codex/skills/.system`、`.codex/plugins/cache` | `skills`、带版本的 `plugins` | 仓库以 ChatGPT 命名，采集路径具体指向本机 Codex；在本项目中仅作非中国公司的对照 |

WorkBuddy 的 `official_experts` 目录名、QwenWork 技能中的 `install_source: official` 都是归档内的路径或字段，不能代替独立的官方来源认证。例如本次读取的 WorkBuddy AI 专家团 [plugin.json][team-manifest] 把作者标为 AI-HIVE Team；它可以作为市场插件设计样本，不应改写成“腾讯内部团队的官方提示词”。[WorkBuddy 索引][workbuddy-readme]、[QwenWork 索引][qwen-readme] 和 [ChatGPT 索引][chatgpt-readme] 提供各自的采集范围。

### 目录总量：两套统计口径并列保留

我们通过 GitHub 连接器读取固定提交的完整产品树；较大的 WorkBuddy 树按七个子树分段读取，递归返回均为 `truncated=false`，再合并计数。[固定根树 API][tree] 可回查产品子树标识。**活跃路径**指仍位于产品主目录、排除产品根下 `archive/` 和 `change-logs/` 的文件；这个词不表示客户端正在启用。文件只计 Git tree 中的 blob，不计目录。

| 平台 | 活跃文件数 | 活跃 SKILL.md 路径 | 历史删除 SKILL.md 路径 | 活跃 SKILL 内容按 blob 去重 |
| --- | ---: | ---: | ---: | ---: |
| Doubao | 4,397 | 305 | 32 | 305 |
| WorkBuddy | 17,915 | 1,858 | 114 | 1,830 |
| QwenWork | 4,447 | 380 | 23 | 380 |
| ChatGPT / Codex 对照 | 957 | 38 | 42 | 38 |
| **合计** | **27,716** | **2,581** | **211** | **2,553** |

完整元数据索引包含 **2,792 个 SKILL.md 路径**。其中 211 个历史路径都位于 `archive/deleted/`。Git blob 去重只合并字节相同的内容；2,553 不能称为“互不重复的独立技能”，因为语义相近、不同版本、引用副本和宿主依赖还需要逐项判断。本文新增深读六份代表文件，其余目录项不标为已读。

WorkBuddy 的 1,858 个活跃路径分散在连接器 695、专家 560、官方市场目录 437、团队市场目录 139、顶层技能目录 27；只数 `workbuddy/skills` 会遗漏主体。QwenWork 的 380 个路径中，专家包内有 201 个，技能目录内有 179 个。ChatGPT/Codex 的 38 个路径中，33 个来自带版本的插件缓存，5 个来自系统技能目录。支持文件同样重要：四平台活跃路径中，以 `references/` 路径段计有 10,915 个文件，以 `scripts/` 路径段计有 4,092 个文件；这些是目录存在性统计，不表示每份都已阅读或运行。

作者各产品 README 使用另一套“索引条目”口径：

| 平台 | 作者 README 的索引条目 | 作者 README 的索引文件 |
| --- | ---: | ---: |
| Doubao | 280 | 4,885 |
| WorkBuddy | 634 | 17,602 |
| QwenWork | 265 | 4,761 |
| ChatGPT / Codex | 20 | 949 |
| **合计** | **1,199** | **28,197** |

这里的条目可能是一个完整插件包、专家包、单个技能、连接器登记项或某个缓存版本。脚本还会把 QwenWork 同一注册文件中的多个连接器分别列为条目。**1,199 不是官方技能数量，也不是我们已经学习的数量。** README 文件数与 Git 已提交文件口径存在差额，本次没有逐项完成差额归因；看板应显示自己采用的统计定义，保留作者声明作为独立证据，不能偷偷把两套数混用。

## 二、作者的采集与维护流程

### 1. 读取明确的本地源，按文件内容比较变化

[sync_platform.py][sync] 用平台配置连接“源路径”和“仓库目标路径”。程序按相对路径判断新增和删除，对同路径文件计算 SHA-256 判断内容是否修改；新增和修改文件复制到目标，删除文件移动到带同步时间的 `archive/deleted/`。若整个配置源路径不存在，程序会报错，不会直接把它当作空目录并清空归档目标。

这使“产品删除了一个技能”和“研究者没找到它”具有不同记录。固定提交中，`student-discount-application` 的 13 个文件被移到 2026-10-20 的删除目录；[变更日志][latest-log] 逐项列出原路径和归档路径，[提交记录][latest-commit] 中对应文件为重命名且内容改动为零。我们核对的是这个具体实例，不把它扩展成所有历史都已验证的承诺。

### 2. 分平台防重入，Git 写入统一串行

[Windows 任务注册脚本][schedule] 为四个平台配置每日 18:00 的任务，经 WSL 调用同步脚本。同步器有平台锁，提交阶段再获取共享 Git 锁，避免各平台同时操作同一工作区索引。运行依赖包含 Windows 计划任务、WSL、Python、Git；选择推送时还依赖 `gh` 和既有认证。

配置证明“设计为每天运行”。最近 15 个提交样本显示数日的同步记录，不能证明没有中断。脚本在没有源文件变化且未要求刷新文档时提前退出；即使刷新，内容相同也可以不提交。因此，缺少某天的提交并不等于当天任务失败。

### 3. 自动生成的是目录导航，根 README 保留编辑性总结

程序优先从插件清单 `plugin.json` 读取名称、说明、分类和关键词；找不到时读取 `SKILL.md` 的头部字段，再回退到 README 摘要。之后生成各平台 README 和来源目录的 SUMMARY，包含场景导航、条目目录和文件数。头部解析是有限的文本解析器，不应据此假定任意复杂 YAML 都能被完整识别。

默认场景分类由有序关键词规则完成；QwenWork 的分类还使用已有分类元数据、目录前缀，团队市场可以读取既有分析 Markdown。**本次核对的自动同步代码没有调用大模型完成分类。** 根 README 的“最近同步”栏则明确自述由模型按需总结变更日志，不随计划任务自动刷新；`write_root_readme` 在根 README 已存在时不覆盖它。[相关提交][readme-commit] 也记录了根 README 的重建。

这给我们的启发是把工作分开：程序负责文件盘点、哈希和差异；模型负责阅读全文后提炼任务语义与设计方法。目录关键词适合搜索入口，不能直接充当“这个技能解决什么问题、为什么这样设计”的结论。

### 4. 复用前需要补齐采集范围与内容审核

源码会复制配置源文件，未观察到自动脱敏步骤。它还会采集本机连接器登记文件。借鉴时应先限定允许收集的路径和字段，排除凭据及个人业务数据，再生成可审查的差异。这里说的是复用方案需要的边界，不是在断言已发现仓库泄露了凭据。

公开材料尚未解释每个插件如何首次进入作者设备、哪些是厂商自带、哪些是市场安装、作者是否调整过个别副本，以及再发布授权。我们可以确认采集脚本的输入位置与处理方式；这些未知项应一直保留在来源记录中。

## 三、六份值得深读的代表文件

以下均为**第三方归档中的行为说明**。表述“要求读取”“应传递”“负责执行”指文本规定的流程；我们没有拿到宿主拼装最终模型请求的轨迹，也没有运行这些工具。除本文列出的主文件、团队清单和链路协议外，链接到的参考目录只核对了存在性，不宣称已经全文验证。

### 1. WorkBuddy：用交接契约组织五角色团队

原文：[ai-expert-studio-orchestrator/SKILL.md][team]，归档版本字段为 1.1.1；配套 [plugin.json][team-manifest] 给出五个角色和插件作者标签。

输入是创作需求、素材、产物规格与确认信息。技能分别规定负责人、需求策划、模型选择、生成执行、质检交付的职责：策划不代替选模，选模不擅改提示词，执行者不擅自换模型或重新生成，质检者未实际预览就不能下视觉质量结论。模型调用前预期交接的内容包括事实、素材角色、提示词、参数、任务数量、模型与价格快照、确认记录，而不只是“请帮忙生成”。

工具返回应带任务 ID、状态、结果与失败原因。未进入终态时继续查询原任务；提示词、参数、数量或模型发生变化时，按新生成意图处理。可学的方法是**把分工、交接字段、原任务续查和验收能力写成明确契约**。代价与权限边界需要宿主配合，文本中的 `allowed-tools` 列表本身不能证明工具权限已经强制落实。

### 2. WorkBuddy：规划器先组织业务问题，再交给执行器

原文：[DataBuddy data-task-planner/SKILL.md][planner]。它接收分析问题和工作空间，先理解目标、指标、时间、维度、比较基线与假设，再按需要查看实体元数据。文本允许有限的 `wedatacli` 探查，禁止规划阶段调用实际数据查询、预测、相关性计算等命令。

输出是可以独立回答的业务任务和依赖关系；任务文本不点名底层工具。随后将同样的文本、数量与顺序登记到宿主 To-dos 任务列表，规划阶段结束。依赖包括工作空间、`wedatacli` 与宿主任务列表能力；工具名称可以随宿主而变。

可学的方法是**让计划表达业务目标，让执行阶段选择实现手段，并保持计划与看板逐条对应**。未知条件保留为假设或待澄清项。这里的“禁止执行”是归档提示中的职责约定，我们没有核对一个能够独立阻止越界调用的运行时门禁。

### 3. QwenWork：把对话证据、身份 ID 与外部写入串起来

原文：[dingtalk-chat-to-todo/SKILL.md][todo]，自带版本 1.0.0 和 `install_source: official` 字段。后一个字段只记录归档自述。

流程先明确群和时间范围，取得真实用户与群 ID，按绝对时间分页读消息，结合上下文识别待办。文本要求呈现候选和不采纳项理由，经过用户确认后再用 `dws` CLI 创建待办。身份、群、消息上下文与任务之间有明确传递关系，避免在后续调用中猜 ID。

访问失败需要报告；分页中断时标明结果不完整；创建失败核对执行人 ID。**“找到一条任务”和“待办已经创建”是不同完成状态。** 可学的是有来源的身份传递、完整性标记和语义判断后的写入确认。该能力依赖已登录 CLI 与联系人、群消息、待办权限；本次未验证实际 CLI 版本和执行结果。

### 4. QwenWork：结构化设计验收，同时暴露协议漂移

原文：[product-design/skills/qa/SKILL.md][qa]；补充全文：[chain-protocol.md][chain]。

QA 头部的 `chain.reads` 声明读取设计简报、流程、先前检查、站点结构和用户故事；写出 `qa` 状态。偏差记录包含设计源、实际实现、差异、修复建议、位置、严重性及与上游发现的关系。文件工具读取代码或截图，证据不足时降级为可执行清单；可选连接器与本地看板模板属于额外依赖。核心报告和状态应先成立，看板用于展示已有结果。

这套设计值得学的是**把上游产物变成结构化输入，把验收结论变成可追踪偏差**。同时要保留三个明确问题：QA 文件使用 `spark-output/context`，总协议使用 `.spark/context`；QA 前段要求完整 JSON 标记，后段又要求写盘后输出紧凑的 `ref` 标记；协议提到的 `dist/validate-chain.py` 在本固定提交的 product-design 子树中未找到。

因此，这一例同时展示了好设计与维护风险。归档足以让我们研究持久化状态、上下游接口及看板合并规则，不能据此宣称整个套件协议一致、已经通过验证。后续迁移要检查状态路径、字段模式、标记格式与失败时的行为是否真正对齐。

### 5. Doubao：给主技能增加复杂交接与验收能力

原文：[app-builder-orchestration/SKILL.md][builder]。

它把自己定位成基础 `doubao-app-builder` 的扩展：当任务包含复杂附件、全量表格导入、既有应用 ID 或失败续跑时，补上输入准备和验收控制。输入清单保留原始意图、真实 `app_id`、附件、允许变更和须保留项；表格交给 `sheet` 读取真实字段与行数，再形成编号变更单。

应用执行仍交给基础构建器或 `app_builder_agent`；需要附件 URL 时依赖 `FileBatchUpload`。返回后按字段、页面、数据量、默认状态、移动端和须保留项核对，发现差异则复用同一应用 ID 继续修正。

可学的方法是**主技能拥有入口与执行，扩展只负责特定复杂度的交接和验收**。它降低了多入口争抢任务与修改对象漂移的风险；“全量导入”必须由真实读取与条数核对支撑。这些专有宿主工具的实际接口和运行时仍未验证。

### 6. ChatGPT/Codex 对照：把审查证据门槛写清楚

原文：[review-agent/SKILL.md][review]。本例用于对照，不计入中国公司，也不代表 ChatGPT 网页产品完整系统提示。

输入是另一个 agent 委派的代码变更审查。文本要求读取适用的 AGENTS.md、完整差异、调用点和相关测试；分支审查先确定共同祖先，避免比较基准错误。执行保持只读；发现必须由代码证明，属于本次引入、可操作且作者可能修复的问题。输出按严重性列出位置和触发场景，没有合格发现可以直接报告无发现。

可学的方法是**同时规定发现的纳入标准、排除标准和零发现的合法性**。完成条件是覆盖完整变更并如实交代验证缺口，而不是一定产生若干条意见。运行依赖是可读代码、Git 和项目规则；归档文本不证明实际审查质量。

## 四、给我们自己的采集、学习和看板流程

可以沿用作者的文件版本管理思路，把研究工作组织成以下可检查的步骤。

1. **登记一个上游身份。** 同一仓库只算一个独立项目，子文件是证据。记录固定提交、检查日期、许可状态、产品渠道、作者身份依据与未知项；官方材料和第三方归档保留独立来源链。
2. **机器建立路径清单。** 枚举文件、保存 Git blob 标识、识别当前路径、历史删除和缓存版本，产生增删改差异。这里只做确定性的结构处理，不替代内容理解。
3. **模型按任务语义深读。** 给模型主文件、必要参考文件及来源说明，要求逐项提炼输入、模型前上下文、工具执行者、返回契约、失败恢复、完成条件和可迁移方法；每项结论指向原文，缺证据填写未知。不能只用文件名、关键词命中或目录分类来生成工程结论。
4. **分别处理内容重复和能力相近。** 哈希只能发现完全相同内容。语义相近的技能交给模型比较其触发范围、工具依赖和验收差异，保留多来源关系；不因名称相同就合并。
5. **把研读与验证分开。** 状态至少区分“仅有目录”“已读原文”“已形成方法记录”“已有运行验证”。路径或协议不一致标为待验证；静态分析不能自动升级为实验成功。
6. **让看板反映证据进度。** 全目录提供产品、路径关键词、当前/历史状态筛选；六个代表案例单独展示学习结论。目录数量衡量覆盖范围，深读和验证状态衡量研究进展，两个指标分别呈现。
7. **更新先审差异，再修结论。** 保留旧快照和变更原因；删去的技能进入历史视图；没有变化时不制造更新记录。若以后配置定时收集，应单独落实采集范围与用户授权。

值得长期关注的是归档的演化：某个技能何时增加失败恢复，某个接口何时改成结构化输出，某套协议何时发生不一致。能回答这些问题，仓库就从链接收藏进展为可追溯的工程学习记录。

## 五、核对范围与仍待解决的问题

本次完整枚举了四个平台的 Git 文件树，读取根 README、四份平台 README、三份采集/任务脚本、近期 15 条提交元数据、具体删除变更日志、六份代表技能、团队插件清单和设计链路协议。完整 SKILL 路径索引仅保存元数据；没有全量复制或逐一阅读全文。

后续最有价值的补证是：对六份代表文件分别找到厂商或插件作者可认证的发布入口；核对宿主工具的实际 schema、权限和版本；对一个最小、无业务副作用的场景做适配实验；解释 README 文件数与 Git 树计数差额；验证 QwenWork 设计套件的协议漂移是否已在其他版本修复。每项完成后应另记证据，不把当前未知改写成默认成立。

[root]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README.md
[tree]: https://api.github.com/repos/ahang1598/doubao-workbuddy-qwenwork-skills/git/trees/c2da69d8d6c2b1d4f024bf82d38c1392aba5cc0d
[sync]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/scripts/sync_platform.py
[schedule]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/scripts/register-windows-task.ps1
[doubao-readme]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-doubao.md
[workbuddy-readme]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-workbuddy.md
[qwen-readme]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-qwenwork.md
[chatgpt-readme]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/README-chatgpt.md
[latest-log]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/change-logs/2026-10-20-180008.md
[latest-commit]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/commit/1c9239cc90585f57d9e06d32deffc017bbff5802
[readme-commit]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/commit/db7573b51f1024cbdbf52e629e6dc70bfbfd9b96
[team]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/workbuddy/experts/ai-expert-studio/skills/ai-expert-studio-orchestrator/SKILL.md
[team-manifest]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/workbuddy/experts/ai-expert-studio/.codebuddy-plugin/plugin.json
[planner]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/workbuddy/connectors/marketplace/connectors/databuddy/skills/data-task-planner/SKILL.md
[todo]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/qwenwork/skills/dingtalk-chat-to-todo/SKILL.md
[qa]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/qwenwork/experts/product-design/skills/qa/SKILL.md
[chain]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/qwenwork/experts/product-design/chain-protocol.md
[builder]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/doubao/skills/app-builder-orchestration/SKILL.md
[review]: https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/1c9239cc90585f57d9e06d32deffc017bbff5802/chatgpt/skills/review-agent/SKILL.md

## 本仓数据入口

详细研究记录见 [归档研究数据](../catalog/archive-research.json)，完整路径元数据见 [技能路径索引](../catalog/archive-skill-index.json)。这些数据仅含原创分析和元数据，不包含完整技能正文。
