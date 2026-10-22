/*
 * 中国 Agent 工程研究台。
 * 输入为已审阅的 ATLAS_DATA；提供本地检索、原文导航与浏览器内学习记录。
 * 此界面不连接业务账号、不运行上游 Agent，也不在后台自动采集资料。
 */
"use strict";

const DATA = window.ATLAS_DATA;
const STORAGE_KEY = "china-agent-atlas-learning-v2";
const TYPES = { official_code: "官方源码", official_docs: "官方文档", third_party_archive: "第三方归档" };
const STATUS = { unread: "未读", reading: "阅读中", read: "已读", practiced: "已实践" };
const VIEWS = { library: "资料库", methods: "方法地图", paths: "学习路线", archive: "归档作者怎么做", learning: "我的学习" };
const state = { view: "library", query: "", company: "", category: "", type: "", progress: "", layout: "cards", myFilter: "saved", archiveQuery: "", archivePlatform: "", archiveScope: "active", archivePage: 1 };
let learning = loadLearning();
let activeSource = null;
let activeDocument = "README.md";
let toastTimer;
let noteTimer;

/** 输入任意文本；转义 HTML 特殊字符；输出可安全插入模板的字符串。 */
function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]));
}

/** 读取浏览器本地学习记录；仅接收普通对象字段；异常时返回空记录。 */
function loadLearning() {
  try {
    const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    return { saved: parsed.saved && typeof parsed.saved === "object" ? parsed.saved : {}, status: parsed.status && typeof parsed.status === "object" ? parsed.status : {}, notes: parsed.notes && typeof parsed.notes === "object" ? parsed.notes : {}, paths: parsed.paths && typeof parsed.paths === "object" ? parsed.paths : {} };
  } catch { return { saved: {}, status: {}, notes: {}, paths: {} }; }
}

/** 将当前学习记录写入本地存储；失败时通知用户；不上传或同步任何笔记。 */
function persistLearning() {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(learning)); }
  catch { toast("浏览器未允许保存，请导出学习记录备份。"); }
}

/** 输入短消息；在页面底部短暂展示；返回无。 */
function toast(message) {
  const target = document.getElementById("toast");
  target.textContent = message;
  target.classList.add("visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => target.classList.remove("visible"), 2800);
}

/** 输入来源标识；在已审阅目录中查找并返回对应来源对象。 */
function sourceById(id) { return DATA.sources.find(source => source.id === id); }

/** 输入来源对象；选择中文分组名；返回界面使用的组织名称。 */
function groupOf(source) { return source.company_group || source.company; }

/** 输入来源对象；优先使用人工简称；返回适合紧凑卡片的标题。 */
function titleOf(source) { return source.short_title || source.project; }

/** 输入来源标识；验证本地状态值；返回已知阅读状态。 */
function progressOf(id) { return Object.hasOwn(STATUS, learning.status[id]) ? learning.status[id] : "unread"; }

/** 输入来源对象；根据类型生成来源标记；返回转义后的 HTML。 */
function typeBadge(source) {
  const style = source.source_type === "third_party_archive" ? "archive" : source.source_type === "official_docs" ? "docs" : "";
  return `<span class="source-type ${style}">${esc(TYPES[source.source_type] || source.source_type)}</span>`;
}

/** 输入来源标识列表；生成可打开拆解的按钮；未知标识不会显示。 */
function sourcePills(ids) {
  return `<div class="source-pills">${ids.map(sourceById).filter(Boolean).map(source => `<button class="source-pill" data-source="${esc(source.id)}">${esc(titleOf(source))} ↗</button>`).join("")}</div>`;
}

/** 输入标题、说明和可选标记；输出统一页面导语。 */
function pageIntro(eyebrow, title, description, badge = "") {
  return `<section class="page-intro"><div><p class="eyebrow">${esc(eyebrow)}</p><h1>${esc(title)}</h1><p>${esc(description)}</p></div>${badge ? `<span class="intro-badge">${esc(badge)}</span>` : ""}</section>`;
}

/** 根据当前资料筛选条件匹配文本和标签；返回新的来源数组，不修改原目录。 */
function filteredSources() {
  const needle = state.query.trim().toLocaleLowerCase();
  return DATA.sources.filter(source => {
    const haystack = [source.project, source.company, groupOf(source), source.summary, source.learning_value, ...(source.methods || []), ...(source.categories || []).map(category => DATA.categories[category]), ...source.inspected_files.map(file => file.path)].join(" ").toLocaleLowerCase();
    return (!needle || haystack.includes(needle)) && (!state.company || groupOf(source) === state.company) && (!state.category || (source.categories || []).includes(state.category)) && (!state.type || source.source_type === state.type) && (!state.progress || (state.progress === "saved" ? learning.saved[source.id] : progressOf(source.id) === state.progress));
  });
}

/** 输入来源对象；生成浏览卡片，包含证据类型、方法摘要与学习状态。 */
function sourceCard(source) {
  const status = progressOf(source.id);
  const saved = !!learning.saved[source.id];
  return `<article class="source-card"><div class="source-card-top"><span class="company-mark" aria-hidden="true">${esc(groupOf(source).slice(0, 1))}</span><span class="company-label">${esc(groupOf(source))}</span>${typeBadge(source)}<button class="save-button" data-save="${esc(source.id)}" aria-label="${saved ? "取消收藏" : "收藏"} ${esc(titleOf(source))}" aria-pressed="${saved}">${saved ? "★" : "☆"}</button></div><h3><button data-source="${esc(source.id)}">${esc(titleOf(source))}</button></h3>${source.lifecycle_note ? `<div class="historical">◷ ${esc(source.lifecycle_note)}</div>` : ""}<p class="summary">${esc(source.summary || source.methods.slice(0, 2).join("；"))}</p><div class="tag-list">${(source.categories || []).slice(0, 4).map(category => `<span class="chip">${esc(DATA.categories[category])}</span>`).join("")}</div><div class="source-card-footer"><span class="reading-status ${status === "reading" ? "reading" : status !== "unread" ? "read" : ""}">${status === "read" || status === "practiced" ? "✓ " : ""}${STATUS[status]}</span><span class="actions"><button class="link-button" data-source="${esc(source.id)}">查看拆解</button><a href="${esc(source.url)}" target="_blank" rel="noopener noreferrer">原文 ↗</a></span></div></article>`;
}

/** 输入已筛选的来源列表；生成可横向滚动的紧凑表格。 */
function sourceTable(sources) {
  return `<div class="source-table-wrap"><table class="source-table"><thead><tr><th scope="col">项目与组织</th><th scope="col">从这里学什么</th><th scope="col">来源</th><th scope="col">学习状态</th><th scope="col">阅读</th></tr></thead><tbody>${sources.map(source => `<tr><td class="project-cell"><button class="link-button" data-source="${esc(source.id)}">${esc(titleOf(source))}</button><small>${esc(groupOf(source))}${source.lifecycle_note ? ` · ${esc(source.lifecycle_note)}` : ""}</small></td><td class="summary-cell">${esc(source.summary || source.methods.join("；"))}</td><td>${typeBadge(source)}</td><td><span class="reading-status">${STATUS[progressOf(source.id)]}</span></td><td><div class="table-actions"><button class="save-button" data-save="${esc(source.id)}" aria-label="${learning.saved[source.id] ? "取消收藏" : "收藏"} ${esc(titleOf(source))}" aria-pressed="${!!learning.saved[source.id]}">${learning.saved[source.id] ? "★" : "☆"}</button><button class="link-button" data-source="${esc(source.id)}">拆解 ↗</button></div></td></tr>`).join("")}</tbody></table></div>`;
}

/** 输入空状态说明与可选按钮；输出占位说明，不制造虚假的资料卡。 */
function emptyState(title, message, action = "") {
  return `<div class="empty-state"><div class="empty-symbol" aria-hidden="true">◇</div><h3>${esc(title)}</h3><p>${esc(message)}</p>${action}</div>`;
}

/** 输入选项字典和当前选中值；生成下拉框选项。 */
function options(mapping, selected) {
  return Object.entries(mapping).map(([key, label]) => `<option value="${esc(key)}"${selected === key ? " selected" : ""}>${esc(label)}</option>`).join("");
}

/** 渲染资料库外框和筛选器；随后渲染结果，保留用户既有筛选条件。 */
function renderLibrary() {
  const companies = Object.fromEntries([...new Set(DATA.sources.map(groupOf))].map(company => [company, company]));
  document.getElementById("page-content").innerHTML = `${pageIntro("公开实现 · 可追溯的工程经验", "把大厂的 Agent 经验，拆成自己的方法。", "从提示词、技能与工具接口，一直读到执行循环、错误恢复和验收。每条结论都能回到具体文件与固定版本。", "源码与文档静态核对")}
  <section class="metrics" aria-label="研究覆盖"><div class="metric"><strong>${DATA.stats.sources}</strong><span>已建档研究条目</span><small>含官方材料与第三方归档</small></div><div class="metric"><strong>${DATA.stats.organizations}</strong><span>公司与研究机构</span><small>大厂为主，扩展项目另标身份</small></div><div class="metric"><strong>${DATA.stats.materials}</strong><span>已核对材料入口</span><small>按具体文件与文档 URL 去重</small></div><div class="metric"><strong>${DATA.methods.length}</strong><span>可迁移的工程方法</span><small>附问题、机制和实践建议</small></div></section>
  <section class="guide-banner"><div><h2>先读飞书，再走完一个 Agent 的工作过程。</h2><p>业务技能 → CLI 契约 → 上下文加载 → 工具执行 → 完成验收</p></div><button class="button" data-view="paths">选择学习路线 <span>↗</span></button></section>
  <section aria-labelledby="library-heading"><div class="section-heading"><h2 id="library-heading">资料库</h2><span class="hint">快照更新于 ${esc(DATA.updated_at)}</span></div><div class="filter-panel"><div class="filter-row"><label class="search-box"><span aria-hidden="true">⌕</span><input id="library-search" type="search" placeholder="搜索项目、公司、方法或文件名…" aria-label="搜索资料库" value="${esc(state.query)}"></label><select id="company-filter" class="filter-select" aria-label="按公司筛选">${options({ "": "全部公司 / 机构", ...companies }, state.company)}</select><select id="category-filter" class="filter-select" aria-label="按工程主题筛选">${options({ "": "全部工程主题", ...DATA.categories }, state.category)}</select><select id="type-filter" class="filter-select" aria-label="按来源类型筛选">${options({ "": "全部来源", ...TYPES }, state.type)}</select><select id="progress-filter" class="filter-select" aria-label="按学习状态筛选">${options({ "": "全部学习状态", saved: "已收藏", ...STATUS }, state.progress)}</select></div><div class="filter-bottom"><span id="result-count" class="result-count" role="status" aria-live="polite"></span><div class="filter-bottom-actions"><button class="text-button" id="clear-filters">重置筛选</button><div class="layout-switch" role="group" aria-label="浏览方式"><button data-layout="cards" class="${state.layout === "cards" ? "active" : ""}" aria-pressed="${state.layout === "cards"}">卡片</button><button data-layout="table" class="${state.layout === "table" ? "active" : ""}" aria-pressed="${state.layout === "table"}">表格</button></div></div></div></div><div id="library-results"></div></section>`;
  renderLibraryResults();
}

/** 仅更新搜索结果与数量，避免每次输入重建筛选器而丢失焦点。 */
function renderLibraryResults() {
  const sources = filteredSources();
  document.getElementById("result-count").innerHTML = `显示 <strong>${sources.length}</strong> / ${DATA.sources.length} 条 · 研究条目数与仓库数分别统计`;
  document.getElementById("library-results").innerHTML = sources.length ? state.layout === "cards" ? `<div class="source-grid">${sources.map(sourceCard).join("")}</div>` : sourceTable(sources) : emptyState("没有匹配的资料", "试试缩短关键词，或清除公司、主题和学习状态筛选。", '<button class="button" id="reset-empty">重置筛选</button>');
}

/** 从方法目录生成问题、证据与练习对照，方法卡本身不代表实测效果。 */
function renderMethods() {
  document.getElementById("page-content").innerHTML = `${pageIntro("从收藏走向理解", "先找问题，再看别人怎样解决。", "把不同项目放在同一个工程问题下比较。来源事实与迁移建议分开写，看到适用条件之后，再用自己的任务验证。", `${DATA.methods.length} 个方法主题`)}<div class="method-grid">${DATA.methods.map((method, index) => `<article class="method-card"><span class="method-number">METHOD ${String(index + 1).padStart(2, "0")}</span><h3>${esc(method.title)}</h3><p><span class="method-label">要解决的问题</span>${esc(method.problem)}</p><p><span class="method-label">观察到的机制</span>${esc(method.mechanism)}</p><div class="practice"><span class="method-label">可以怎样学</span>${esc(method.practice)}</div>${sourcePills(method.source_ids)}${method.boundary ? `<p class="boundary">边界：${esc(method.boundary)}</p>` : ""}</article>`).join("")}</div>`;
}

/** 按预设顺序展示阅读路线与练习交付物，记录的完成状态由用户自行勾选。 */
function renderPaths() {
  document.getElementById("page-content").innerHTML = `${pageIntro("带着一个产物去读", "四条路线，把经验用起来。", "选一个与你当前项目最接近的目标。每一步都给出阅读对象、观察重点，以及最终应当留下的可检查产物。", "按目标学习")}<div class="path-grid">${DATA.learning_paths.map((path, index) => `<article class="path-card"><div class="path-top"><span>路线 ${String(index + 1).padStart(2, "0")}</span><span>${path.steps.length} 个步骤</span></div><h2>${esc(path.title)}</h2><p>${esc(path.description)}</p><div class="path-output"><strong>完成后留下：</strong>${esc(path.output)}</div>${path.steps.map((step, stepIndex) => `<div class="path-step"><span class="step-number">${stepIndex + 1}</span><div><h4>${esc(step.title)}</h4><p>${esc(step.task)}</p>${sourcePills(step.source_ids || [])}${step.doc ? `<button class="source-pill" data-doc="${esc(step.doc)}">阅读中文方法说明 ↗</button>` : ""}</div></div>`).join("")}<label class="path-check"><input type="checkbox" data-path="${esc(path.id)}" ${learning.paths[path.id] ? "checked" : ""}>我已完成这条路线的阅读与练习</label></article>`).join("")}</div><p class="local-note">路线完成状态仅保存在当前浏览器，可以在“我的学习”导出备份。</p>`;
}

/** 生成第三方归档研究页面，分别呈现作者工作流、统计口径、样本和路径索引。 */
function renderArchive() {
  const archive = DATA.archive;
  document.getElementById("page-content").innerHTML = `${pageIntro("一个收藏者的工作方法", "他把本机材料，变成了持续更新的归档。", "阅读 ahang1598 的采集脚本、目录树与代表性技能。以下是对第三方归档的观察，目录名不构成厂商认证，完整路径索引也不等于已深读全部正文。", "第三方归档 · 单独标识")}
  <div class="detail-actions"><a class="button primary" href="${esc(archive.repository_url || "https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills")}" target="_blank" rel="noopener noreferrer">打开原仓库 ↗</a><button class="button" data-doc="cases/archive-collection-method.md">阅读完整拆解</button></div>
  <div class="archive-lead"><section class="panel"><p class="eyebrow">采集与学习分两步</p><h2>文件自动同步，知识另行归纳。</h2><ol class="pipeline">${(archive.pipeline || []).map(step => `<li><strong>${esc(step.title)}</strong><p>${esc(step.description)}</p></li>`).join("")}</ol></section><section class="panel"><p class="eyebrow">固定提交下的目录统计</p><h3>按 SKILL.md 路径计数</h3><table class="mini-table"><thead><tr><th scope="col">归档产品</th><th scope="col">当前路径</th><th scope="col">删除历史</th></tr></thead><tbody>${(archive.platforms || []).map(platform => `<tr><td>${esc(platform.label)}</td><td>${platform.active}</td><td>${platform.historical}</td></tr>`).join("")}<tr><td><strong>合计</strong></td><td><strong>${archive.active_paths ?? "—"}</strong></td><td><strong>${archive.historical_paths ?? "—"}</strong></td></tr></tbody></table><div class="callout">${esc(archive.counting_note || "技能路径、内容去重数、插件条目数采用不同口径；不要把这些数字当成独立技能数量。")}</div><p>索引仅包含路径与原文链接。部分路径来自插件缓存和历史版本，ChatGPT / Codex 作为归档方法的对照材料。</p><a class="link-button" href="${esc(archive.commit_url || archive.repository_url || "https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills")}" target="_blank" rel="noopener noreferrer">固定快照 ${esc((archive.commit || "").slice(0, 10))} ↗</a></section></div>
  <div class="section-heading"><h2>抽读这些，学具体写法</h2><span class="hint">样本阅读与完整索引分开</span></div><div class="archive-sample-grid">${(archive.samples || []).map(sample => `<article class="archive-sample"><p class="eyebrow">${esc(sample.platform_label || sample.platform || "归档样本")}</p><h4>${esc(sample.title)}</h4><p>${esc(sample.lesson)}</p><a class="link-button" href="${esc(sample.url)}" target="_blank" rel="noopener noreferrer">查看固定版本原文 ↗</a></article>`).join("")}</div>
  <section class="archive-index" aria-labelledby="archive-index-title"><div class="section-heading"><h2 id="archive-index-title">完整技能路径索引</h2><span class="hint">元数据建档，非逐项深读</span></div><div class="archive-controls"><label class="search-box"><span aria-hidden="true">⌕</span><input id="archive-search" type="search" placeholder="搜索目录名，例如 lark、qa、research…" aria-label="搜索归档技能路径" value="${esc(state.archiveQuery)}"></label><select class="filter-select" id="archive-platform" aria-label="归档产品">${options({ "": "全部归档产品", ...Object.fromEntries((archive.platforms || []).map(p => [p.id, p.label])) }, state.archivePlatform)}</select><select class="filter-select" id="archive-scope" aria-label="归档路径状态">${options({ active: "当前路径", historical: "删除历史", all: "全部路径" }, state.archiveScope)}</select></div><div id="archive-results"></div></section>`;
  renderArchiveResults();
}

/** 对归档路径索引作字面匹配与分页；一次最多呈现 60 条，避免长列表阻塞浏览。 */
function renderArchiveResults() {
  const needle = state.archiveQuery.trim().toLocaleLowerCase();
  const records = (DATA.archive.inventory || []).filter(item => (!needle || item.path.toLocaleLowerCase().includes(needle)) && (!state.archivePlatform || item.platform === state.archivePlatform) && (state.archiveScope === "all" || (state.archiveScope === "historical") === !!item.historical));
  const perPage = 60;
  const pages = Math.max(1, Math.ceil(records.length / perPage));
  state.archivePage = Math.min(Math.max(1, state.archivePage), pages);
  const pageRecords = records.slice((state.archivePage - 1) * perPage, state.archivePage * perPage);
  const labels = Object.fromEntries((DATA.archive.platforms || []).map(p => [p.id, p.label]));
  document.getElementById("archive-results").innerHTML = `<p class="archive-count" role="status" aria-live="polite">匹配 ${records.length.toLocaleString()} 个路径 · 第 ${state.archivePage} / ${pages} 页 · 每页最多 60 项</p>${records.length ? `<div class="archive-list">${pageRecords.map(item => `<div class="archive-row"><strong>${esc(labels[item.platform] || item.platform)}${item.historical ? '<br><span class="source-type archive">历史</span>' : ""}</strong><code>${esc(item.path)}</code><a href="${esc(item.url)}" target="_blank" rel="noopener noreferrer">原文 ↗</a></div>`).join("")}</div><div class="detail-actions"><button class="button small" data-archive-page="prev" ${state.archivePage === 1 ? "disabled" : ""}>上一页</button><button class="button small" data-archive-page="next" ${state.archivePage === pages ? "disabled" : ""}>下一页</button></div>` : emptyState("没有匹配的技能路径", "试试其他目录关键词，或切换当前路径与删除历史。")}`;
}

/** 汇总浏览器内收藏、阅读与实践记录，按用户选择展示相应来源卡片。 */
function renderLearning() {
  const counts = { saved: DATA.sources.filter(s => learning.saved[s.id]).length, reading: DATA.sources.filter(s => progressOf(s.id) === "reading").length, read: DATA.sources.filter(s => progressOf(s.id) === "read").length, practiced: DATA.sources.filter(s => progressOf(s.id) === "practiced").length, notes: DATA.sources.filter(s => String(learning.notes[s.id] || "").trim()).length };
  const labels = { saved: "已收藏", reading: "阅读中", read: "已读", practiced: "已实践", notes: "有笔记" };
  const sources = DATA.sources.filter(source => state.myFilter === "saved" ? learning.saved[source.id] : state.myFilter === "notes" ? String(learning.notes[source.id] || "").trim() : progressOf(source.id) === state.myFilter);
  document.getElementById("page-content").innerHTML = `${pageIntro("留下自己的理解", "从“看过”，走到“会用”。", "收藏想研究的材料，记录读到的机制和适用条件。阅读与实践状态由你自己标记，与本仓的源码核查状态分别记录。", "仅保存在当前浏览器")}<div class="detail-actions"><button class="button primary" id="export-learning">导出学习记录 ↓</button><button class="button" data-view="library">继续浏览资料库 ↗</button></div><div class="my-learning-summary">${Object.entries(labels).map(([key, label]) => `<button data-my-filter="${key}" class="${state.myFilter === key ? "active" : ""}" aria-pressed="${state.myFilter === key}"><strong>${counts[key]}</strong>${label}</button>`).join("")}</div><p class="local-note">笔记不会跨设备自动同步。清理浏览器数据前，请导出备份；导出文件包含收藏、状态、笔记与原文地址。</p>${sources.length ? `<div class="source-grid">${sources.map(sourceCard).join("")}</div>` : emptyState("这里还没有学习记录", "在资料卡右上角点星标，或打开拆解设置阅读状态、写下笔记。", '<button class="button" data-view="library">去资料库选一条</button>')}`;
}

/** 输入页面名称；更新导航、URL 与主体；页面内容均来自同一份固定数据。 */
function setView(view, scroll = true) {
  state.view = Object.hasOwn(VIEWS, view) ? view : "library";
  document.querySelectorAll(".nav-item").forEach(button => {
    const selected = button.dataset.view === state.view;
    button.classList.toggle("active", selected);
    if (selected) button.setAttribute("aria-current", "page"); else button.removeAttribute("aria-current");
  });
  document.getElementById("current-location").textContent = VIEWS[state.view];
  history.replaceState(null, "", `#${state.view}`);
  ({ library: renderLibrary, methods: renderMethods, paths: renderPaths, archive: renderArchive, learning: renderLearning })[state.view]();
  if (scroll) window.scrollTo({ top: 0, behavior: "instant" });
}

/** 输入来源标识；生成右侧证据面板，提供原文、方法、边界和本地笔记。 */
function openSource(id) {
  const source = sourceById(id);
  if (!source) return;
  activeSource = id;
  const status = progressOf(id);
  const inspection = source.inspection_level === "documentation_review" ? "官方文档核对，未实跑" : source.inspection_level === "repository_review" ? "目录与文档初筛，未实跑" : "源码 / 文件静态核对，未实跑";
  const organization = { major_company: "科技公司", model_company: "模型公司 · 扩展对照", research_org: "研究机构 · 扩展对照", community: "社区 / 第三方" }[source.organization_kind] || "公开工程项目";
  document.getElementById("source-content").innerHTML = `<header class="detail-header"><div class="detail-top"><span class="company-label">${esc(source.company)}</span>${typeBadge(source)}<button class="icon-button" id="close-source" aria-label="关闭资料拆解">×</button></div><h2 id="source-title">${esc(source.project)}</h2><p>${esc(source.summary || source.methods.join("；"))}</p><div class="detail-actions"><a class="button primary small" href="${esc(source.url)}" target="_blank" rel="noopener noreferrer">打开项目原文 ↗</a><button class="button small" data-doc="${esc(source.case_file)}" data-focus="${esc(source.case_heading || "")}">阅读中文拆解</button><button class="button small" data-save="${esc(id)}" aria-pressed="${!!learning.saved[id]}">${learning.saved[id] ? "★ 已收藏" : "☆ 收藏"}</button></div></header><div class="detail-body"><dl class="detail-meta"><div><dt>核对程度</dt><dd>${esc(inspection)}</dd></div><div><dt>检查日期</dt><dd>${esc(source.checked_at)}</dd></div><div><dt>组织身份</dt><dd>${esc(organization)}</dd></div><div><dt>固定提交</dt><dd>${source.commit ? esc(source.commit.slice(0, 12)) : "文档页面，无提交号"}</dd></div><div><dt>上游许可</dt><dd>${esc(source.license)}</dd></div><div><dt>材料数</dt><dd>${source.inspected_files.length} 个已核对入口</dd></div></dl>${source.lifecycle_note ? `<div class="callout">${esc(source.lifecycle_note)}</div>` : ""}<section class="detail-section"><h3>值得学什么</h3><ul>${source.methods.map(method => `<li>${esc(method)}</li>`).join("")}</ul>${source.learning_value ? `<p class="callout">迁移思路：${esc(source.learning_value)}</p>` : ""}</section><section class="detail-section"><h3>从这些具体文件读起</h3>${source.inspected_files.map(file => `<a class="detail-material" href="${esc(file.url)}" target="_blank" rel="noopener noreferrer"><code>${esc(file.path)} ↗</code><span>${esc(file.purpose)}</span></a>`).join("")}</section><section class="detail-section limits"><h3>证据能支持到哪里</h3><ul>${source.evidence_limits.map(limit => `<li>${esc(limit)}</li>`).join("")}</ul></section>${source.ownership_evidence?.length ? `<section class="detail-section"><h3>归属与出处依据</h3>${source.ownership_evidence.map((url, index) => `<a class="detail-material" href="${esc(url)}" target="_blank" rel="noopener noreferrer"><span>依据 ${index + 1} · ${esc(new URL(url).hostname)} ↗</span></a>`).join("")}</section>` : ""}<section class="detail-section"><h3>我的学习记录</h3><div class="learning-controls"><label for="detail-progress">阅读状态</label><select id="detail-progress" class="filter-select">${options(STATUS, status)}</select></div><label class="notes-label" for="source-notes">这条经验解决什么问题？我准备怎样验证？</label><textarea class="notes-box" id="source-notes" placeholder="写下机制、适用条件，以及准备在自己项目里做的实验…">${esc(learning.notes[id] || "")}</textarea><p class="local-note">自动保存到当前浏览器，可在“我的学习”导出。</p></section></div>`;
  const dialog = document.getElementById("source-dialog");
  if (!dialog.open) dialog.showModal();
  dialog.scrollTop = 0;
}

/** 输入本仓文档相对路径；用本地 Markdown 渲染器呈现，屏蔽原始 HTML 和危险链接。 */
function openDocument(path, focus = "") {
  const documentData = DATA.documents[path];
  if (!documentData) { toast("这份材料请从研究包或原文链接阅读。"); return; }
  activeDocument = path;
  const renderer = new marked.Renderer();
  renderer.html = token => esc(token.text);
  const article = document.getElementById("reader-content");
  article.innerHTML = marked.parse(documentData.markdown, { renderer, gfm: true, breaks: false });
  article.querySelectorAll("a").forEach(link => {
    const href = link.getAttribute("href") || "";
    if (/^https?:\/\//i.test(href)) { link.target = "_blank"; link.rel = "noopener noreferrer"; return; }
    if (/^[a-z][a-z0-9+.-]*:/i.test(href)) { link.removeAttribute("href"); return; }
    const resolved = new URL(href, `https://atlas.invalid/${activeDocument}`);
    const target = decodeURIComponent(resolved.pathname.slice(1));
    if (DATA.documents[target]) { link.dataset.doc = target; link.href = `#doc/${encodeURIComponent(target)}`; }
    else if (target === "catalog/sources.json") { link.dataset.exportCatalog = "1"; link.href = "#catalog"; }
    else { link.removeAttribute("href"); link.title = "此相对路径可在完整研究包中打开"; }
  });
  document.getElementById("reader-title").textContent = documentData.title;
  const dialog = document.getElementById("reader-dialog");
  if (!dialog.open) dialog.showModal();
  dialog.scrollTop = 0;
  if (focus) {
    const heading = [...article.querySelectorAll("h2, h3")].find(item => item.textContent.toLocaleLowerCase().includes(focus.toLocaleLowerCase()));
    if (heading) { heading.style.scrollMarginTop = "110px"; heading.scrollIntoView({ block: "start" }); }
  }
}

/** 输入文件名与 JSON 对象；创建临时下载链接后回收 URL，导出不经过服务器。 */
function downloadJSON(filename, value) {
  const url = URL.createObjectURL(new Blob([JSON.stringify(value, null, 2)], { type: "application/json;charset=utf-8" }));
  const link = document.createElement("a");
  link.href = url; link.download = filename; document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

/** 输入来源标识；切换收藏并同步当前页与已打开的面板按钮。 */
function toggleSave(id) {
  learning.saved[id] = !learning.saved[id];
  persistLearning();
  document.querySelectorAll(`[data-save="${CSS.escape(id)}"]`).forEach(button => {
    const saved = learning.saved[id];
    button.setAttribute("aria-pressed", String(saved));
    if (button.classList.contains("save-button")) { button.textContent = saved ? "★" : "☆"; button.setAttribute("aria-label", `${saved ? "取消收藏" : "收藏"} ${titleOf(sourceById(id))}`); }
    else button.textContent = saved ? "★ 已收藏" : "☆ 收藏";
  });
  if (state.view === "learning") renderLearning();
  if (state.view === "library" && state.progress === "saved") renderLibraryResults();
  toast(learning.saved[id] ? "已加入收藏" : "已取消收藏");
}

/** 清除资料筛选条件并重建资料库；保留收藏、笔记和浏览方式。 */
function resetFilters() {
  Object.assign(state, { query: "", company: "", category: "", type: "", progress: "" });
  renderLibrary();
}

/** 输入界面点击事件；统一分派导航、阅读、下载和分页，避免重复绑定动态节点。 */
function handleClick(event) {
  const target = event.target.closest("button,a");
  if (!target || target.disabled) return;
  if (target.dataset.view) { event.preventDefault(); setView(target.dataset.view); }
  else if (target.dataset.source) openSource(target.dataset.source);
  else if (target.dataset.save) toggleSave(target.dataset.save);
  else if (target.dataset.doc) { event.preventDefault(); openDocument(target.dataset.doc, target.dataset.focus || ""); }
  else if (target.dataset.layout) { state.layout = target.dataset.layout; renderLibrary(); }
  else if (target.dataset.myFilter) { state.myFilter = target.dataset.myFilter; renderLearning(); }
  else if (target.dataset.archivePage) { state.archivePage += target.dataset.archivePage === "next" ? 1 : -1; renderArchiveResults(); }
  else if (target.id === "close-source") document.getElementById("source-dialog").close();
  else if (target.id === "close-reader") document.getElementById("reader-dialog").close();
  else if (target.id === "clear-filters" || target.id === "reset-empty") resetFilters();
  else if (target.id === "export-catalog" || target.dataset.exportCatalog) { event.preventDefault(); downloadJSON("agent-research-sources.json", { updated_at: DATA.updated_at, verification_note: DATA.verification_note, sources: DATA.sources }); }
  else if (target.id === "export-learning") downloadJSON("agent-research-learning.json", { schema_version: "1.0", exported_at: new Date().toISOString(), catalog_snapshot: DATA.updated_at, local_only: true, ...learning, references: DATA.sources.filter(s => learning.saved[s.id] || learning.status[s.id] || learning.notes[s.id]).map(s => ({ id: s.id, project: s.project, url: s.url })) });
}

/** 输入文本事件；即时更新检索结果，笔记延迟写入并使用输入时捕获的来源标识。 */
function handleInput(event) {
  if (event.target.id === "library-search") { state.query = event.target.value; renderLibraryResults(); }
  else if (event.target.id === "archive-search") { state.archiveQuery = event.target.value; state.archivePage = 1; renderArchiveResults(); }
  else if (event.target.id === "source-notes" && activeSource) {
    const id = activeSource;
    learning.notes[id] = event.target.value;
    clearTimeout(noteTimer);
    noteTimer = setTimeout(persistLearning, 250);
  }
}

/** 输入选择框或复选框事件；更新筛选、阅读状态或路线完成状态并保存。 */
function handleChange(event) {
  const filterMap = { "company-filter": "company", "category-filter": "category", "type-filter": "type", "progress-filter": "progress" };
  if (filterMap[event.target.id]) { state[filterMap[event.target.id]] = event.target.value; renderLibraryResults(); }
  else if (event.target.id === "archive-platform") { state.archivePlatform = event.target.value; state.archivePage = 1; renderArchiveResults(); }
  else if (event.target.id === "archive-scope") { state.archiveScope = event.target.value; state.archivePage = 1; renderArchiveResults(); }
  else if (event.target.id === "detail-progress" && activeSource) { learning.status[activeSource] = event.target.value; persistLearning(); if (state.view === "learning") renderLearning(); if (state.view === "library") renderLibraryResults(); }
  else if (event.target.dataset.path) { learning.paths[event.target.dataset.path] = event.target.checked; persistLearning(); }
}

/** 初始化导航、数据统计与事件绑定；根据已知 hash 打开对应页面。 */
function initialize() {
  if (!DATA || !Array.isArray(DATA.sources)) { document.getElementById("page-content").textContent = "数据未生成，请先运行 python3 scripts/build_dashboard.py。"; return; }
  document.getElementById("nav-count").textContent = DATA.sources.length;
  document.getElementById("snapshot-date").textContent = DATA.updated_at;
  if (DATA.download_url) { const link = document.getElementById("download-pack"); link.href = DATA.download_url; link.hidden = false; }
  document.addEventListener("click", handleClick);
  document.addEventListener("input", handleInput);
  document.addEventListener("change", handleChange);
  document.getElementById("source-dialog").addEventListener("close", () => { persistLearning(); if (state.view === "learning") renderLearning(); });
  window.addEventListener("pagehide", persistLearning);
  setView(location.hash.slice(1), false);
}

initialize();
