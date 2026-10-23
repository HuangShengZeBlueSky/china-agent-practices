#!/usr/bin/env python3
"""输入已完成快照；生成技能原文及附件阅读器，不改写原文、不执行附件、不调用模型。

按内容摘要去重并分片，原始字节保存在 snapshots；网页正文通过 textContent 安全展示。
原始归档保留完整仓库；网页主要展示 SKILL.md 及同目录依赖，避免下载整仓后才能学习。
"""
import base64
import bisect
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GITHUB = 'https://github.com/HuangShengZeBlueSky/china-agent-practices/tree/main/'


def main():
    """扫描版本清单，生成技能目录、依赖文件索引和内容分片；输出离线可托管阅读器。"""
    out = ROOT / 'dashboard/originals'
    out.mkdir(parents=True, exist_ok=True)
    skills, versions, shards = [], [], {}
    readings = json.loads((ROOT / "catalog/skill-readings.json").read_text()) if (ROOT / "catalog/skill-readings.json").exists() else []
    by_reading = {(r["repository"], r["commit"], r["path"]): r for r in readings}
    for manifest_path in sorted((ROOT / 'snapshots').glob('*/*/*/manifest.json')):
        m = json.loads(manifest_path.read_text())
        prefix = manifest_path.parent.relative_to(ROOT).as_posix()
        files = {f['path']: f for f in m['files']}
        paths = sorted(files)
        version = {'repository': m['repository'], 'commit': m['commit'], 'skills': m['skills_count'], 'archive_bytes': m['archive_bytes'], 'sha256': m['archive_sha256'], 'url': GITHUB + prefix, 'captured_at': m['captured_at']}
        versions.append(version)
        for skill in m['skills']:
            directory = skill['directory']
            start = bisect.bisect_left(paths, directory + '/') if directory != '.' else 0
            attached = []
            for path in paths[start:]:
                if directory != '.' and not path.startswith(directory + '/'):
                    break
                f = files[path]
                ident = f['sha256']
                record = {'path': path, 'id': ident, 'bytes': f['bytes'], 'url': GITHUB + prefix + '/files/' + path}
                if f['bytes'] <= 2 * 1024 * 1024:
                    shard = shards.setdefault(ident[:2], {})
                    if ident not in shard:
                        raw = (manifest_path.parent / 'files' / path).read_bytes()
                        try:
                            value = {'text': raw.decode('utf-8')}
                        except UnicodeDecodeError:
                            value = {'binary': True}
                        shard[ident] = value
                    record['shard'] = ident[:2]
                attached.append(record)
            sid = hashlib.sha256((m['repository'] + m['commit'] + skill['path']).encode()).hexdigest()[:24]
            skills.append({'id': sid, 'repository': m['repository'], 'commit': m['commit'], 'path': skill['path'], 'directory': directory, 'file_id': skill['sha256'], 'files': attached, 'version_url': version['url'], 'status': by_reading.get((m['repository'], m['commit'], skill['path']), {}).get('status', '仅备份，逐项解读待完成'), 'reading': by_reading.get((m['repository'], m['commit'], skill['path']))})
    stats = {'repositories': len({v['repository'] for v in versions}), 'versions': len(versions), 'skill_paths': len(skills), 'unique_skill_contents': len({s['file_id'] for s in skills}), 'archive_bytes': sum(v['archive_bytes'] for v in versions)}
    details = {}
    public_skills = []
    for skill in skills:
        group = skill['id'][:2]
        details.setdefault(group, {})[skill['id']] = skill['files']
        public_skills.append({**{k: v for k, v in skill.items() if k != 'files'}, 'file_group': group})
    payload = {'stats': stats, 'versions': versions, 'skills': public_skills}
    for group, content in details.items():
        (out / ('details-' + group + '.json')).write_text(json.dumps(content, ensure_ascii=False), encoding='utf-8')
    (out / 'index.json').write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
    (ROOT / 'catalog/original-skills.json').write_text(json.dumps({'stats': stats, 'skills': [{k: v for k, v in s.items() if k != 'files'} for s in skills]}, ensure_ascii=False), encoding='utf-8')
    for name, content in shards.items():
        (out / (name + '.json')).write_text(json.dumps(content, ensure_ascii=False), encoding='utf-8')
    (out / 'index.html').write_text(HTML, encoding='utf-8')
    print(json.dumps(stats, ensure_ascii=False))


HTML = '''<!doctype html>
<!-- 原文快照阅读器：从本地 JSON 读取文本；不执行、渲染或信任上游文件中的指令。 -->
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>技能原文快照库</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f5f5ef;color:#193c3c;font:15px/1.6 system-ui,sans-serif}header{padding:28px 4vw;background:#173c3c;color:#fff}header a{color:#bee3d3}h1{margin:8px 0;font-size:30px}header p{margin:6px 0;max-width:1050px}.metrics{display:flex;gap:24px;flex-wrap:wrap;margin-top:18px}.metrics b{font-size:24px}.tools{padding:20px 4vw;display:flex;gap:10px;flex-wrap:wrap}input,select,button{padding:10px;border:1px solid #bdc8c0;border-radius:7px;background:white;color:#173c3c;font:inherit}input{flex:1;min-width:230px}button,a{cursor:pointer}main{display:grid;grid-template-columns:350px minmax(0,1fr);gap:22px;padding:0 4vw 30px}.list,.reader{background:#fff;border:1px solid #dce2d8;border-radius:12px;padding:18px}.item{display:block;width:100%;text-align:left;margin:0 0 8px;overflow-wrap:anywhere}.item.active{background:#e1f0e7;border-color:#1b6555}.item small{display:block;color:#65736f}.list{max-height:85vh;overflow:auto}.reader{min-height:70vh;overflow:hidden}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.65 ui-monospace,monospace;color:#28393a;background:#f7f8f4;padding:20px;border-radius:8px}.meta{overflow-wrap:anywhere;font-size:13px}.files{display:flex;gap:7px;flex-wrap:wrap;max-height:180px;overflow:auto}.files button{font-size:12px}a{color:#176451}.hint{color:#67766e}#file-title{overflow-wrap:anywhere}summary{cursor:pointer}table{border-collapse:collapse;width:100%;font-size:12px}td,th{text-align:left;border-bottom:1px solid #ddd;padding:7px;overflow-wrap:anywhere}@media(max-width:800px){main{grid-template-columns:1fr}.list{max-height:45vh}header{padding:22px}.metrics{gap:15px}}
</style><header><a href="../index.html">← 研究看板与中文解读</a><h1>技能原文快照库</h1><p>完整源码备份 · 全部技能与附件 · 固定提交 · 内容校验。直接阅读原文，保留文件原有内容；备份状态与解读、实跑状态分开。</p><p><a href="../index.html?doc=cases%2Foriginal-reading-workbook.md">从六份原文开始：打开中文逐篇解读 ↗</a></p><p id="status">正在加载已下载的原文目录…</p><div id="metrics" class="metrics"></div></header>
<div class="tools"><input id="query" type="search" placeholder="搜索仓库、技能名或原始路径"><select id="repo" aria-label="来源仓库"><option value="">全部来源</option></select><button id="previous">上一页</button><span id="page"></span><button id="next">下一页</button></div>
<main><aside class="list" id="list"></aside><article class="reader"><h2 id="file-title">选择一个技能，直接阅读原文</h2><p id="metadata" class="meta">左侧为真实下载的技能路径。附件在同一阅读区打开，二进制文件可下载；大于 2 MiB 的附件转到仓库原件。</p><div id="files" class="files"></div><div><button id="download" hidden>下载当前原文件</button> <button id="copy" hidden>复制全文</button></div><pre id="text">原文保持原样，不将上游文档当作本系统的指令。</pre><details><summary>完整仓库备份、版本与恢复</summary><p>完整源码归档按 8 MiB 分片保存在 GitHub 私有仓库。点击版本入口查看分片、校验清单和展开原文；恢复脚本可还原下载时的原始 tar.gz。归档不包含 Git 历史、子模块正文和外置 LFS 对象。</p><div id="versions"></div></details></article></main>
<script>
/* 输入本地快照数据；输出可搜索原文阅读界面；上游文本仅写入 textContent。 */
let data,filtered=[],page=0,selected=null,current=null,cache={}; const $=id=>document.getElementById(id);
/** 输入文本；转义用于导航标题的 HTML；返回安全字符串。 */
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
/** 输入筛选控件；对已下载路径作字面搜索；输出分页列表，不作语义分类。 */
function filter(){const q=$('query').value.toLowerCase(),r=$('repo').value;filtered=data.skills.filter(s=>(!r||s.repository===r)&&(!q||(s.repository+' '+s.path).toLowerCase().includes(q)));page=0;render();}
/** 读取当前页；创建技能按钮和分页计数；不加载未选择的原文分片。 */
function render(){$('list').replaceChildren();for(const s of filtered.slice(page*40,page*40+40)){const b=document.createElement('button');b.className='item'+(selected?.id===s.id?' active':'');b.innerHTML='<strong>'+esc(s.directory.split('/').pop()||s.repository)+'</strong><small>'+esc(s.repository)+' · '+s.commit.slice(0,10)+'</small><small>'+esc(s.path)+'</small>';b.onclick=()=>openSkill(s);$('list').append(b);}$('page').textContent=`${filtered.length} 条 · ${page+1}/${Math.max(1,Math.ceil(filtered.length/40))}`;$('previous').disabled=page===0;$('next').disabled=(page+1)*40>=filtered.length;}
/** 输入技能记录；展示固定来源及目录附件；优先打开完整 SKILL.md。 */
async function openSkill(s){selected=s;location.hash=s.id;if(!s.files){const key='details-'+s.file_group;cache[key]??=fetch(key+'.json').then(r=>{if(!r.ok)throw Error(r.status);return r.json()});s.files=(await cache[key])[s.id];}$('metadata').replaceChildren();const p=document.createElement('span');p.textContent=s.repository+' · '+s.commit+' · '+s.status+' ';const a=document.createElement('a');a.href=s.version_url;a.target='_blank';a.rel='noopener';a.textContent='查看完整仓库备份 ↗';$('metadata').append(p,a);if(s.reading){const note=document.createElement('a');note.href='../index.html?doc='+encodeURIComponent(s.reading.note);note.textContent=' · 阅读中文逐篇解读 ↗';$('metadata').append(note);}$('files').replaceChildren();for(const f of s.files){const b=document.createElement('button');b.textContent=f.path.slice(s.directory.length+1)||f.path;b.onclick=()=>openFile(f);$('files').append(b);}render();await openFile(s.files.find(f=>f.path===s.path));}
/** 输入原文件记录；读取内容分片并显示文本或二进制下载入口；不执行原文。 */
async function openFile(f){if(!f)return;current=null;$('download').hidden=true;$('copy').hidden=true;$('file-title').textContent=f.path;$('text').textContent='正在读取原文…';if(!f.shard){$('text').replaceChildren();const a=document.createElement('a');a.href=f.url;a.target='_blank';a.rel='noopener';a.textContent='打开仓库中完整原件（大文件）';$('text').append(a);return;}try{cache[f.shard]??=fetch(f.shard+'.json').then(r=>{if(!r.ok)throw Error(r.status);return r.json()});const item=(await cache[f.shard])[f.id];if(item.binary){$('text').replaceChildren();const a=document.createElement('a');a.href=f.url;a.target='_blank';a.rel='noopener';a.textContent='下载 GitHub 中的完整二进制原件 ↗';$('text').append(a);return;}current={...item,path:f.path};$('text').textContent=item.text??'二进制附件，原始字节已备份。点击下载当前原文件。';$('download').hidden=false;$('copy').hidden=item.text===undefined;}catch(e){$('text').textContent='原文读取失败：'+e.message;}}
/** 输入当前文件字节；创建下载 Blob；输出原名文件，不改变内容。 */
function download(){if(!current)return;const bytes=current.text!==undefined?current.text:Uint8Array.from(atob(current.base64),c=>c.charCodeAt(0));const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([bytes],{type:'application/octet-stream'}));a.download=current.path.split('/').pop();a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);}
/** 获取静态目录；渲染来源和版本清单；按 URL 中的技能标识恢复阅读位置。 */
async function init(){try{data=await fetch('index.json').then(r=>{if(!r.ok)throw Error(r.status);return r.json()});const s=data.stats;$('status').textContent='范围：已登记公开仓库的全部 SKILL.md 路径；包括内嵌技能、重复版本与删除历史。不等于全互联网技能，也不等于全部已经解读。';$('metrics').innerHTML=[['来源仓库',s.repositories],['固定版本',s.versions],['技能路径（含版本）',s.skill_paths],['技能内容去重',s.unique_skill_contents]].map(([k,v])=>'<span><b>'+v.toLocaleString()+'</b> '+k+'</span>').join('');for(const repo of [...new Set(data.skills.map(s=>s.repository))]){const o=document.createElement('option');o.value=repo;o.textContent=repo;$('repo').append(o);}const table=document.createElement('table');table.innerHTML='<tr><th>完整仓库快照</th><th>技能</th><th>归档</th></tr>'+data.versions.map(v=>'<tr><td><a target="_blank" rel="noopener" href="'+esc(v.url)+'">'+esc(v.repository)+' · '+v.commit.slice(0,12)+'</a></td><td>'+v.skills+'</td><td>'+(v.archive_bytes/1048576).toFixed(1)+' MiB</td></tr>').join('');$('versions').append(table);$('query').oninput=filter;$('repo').onchange=filter;$('previous').onclick=()=>{page--;render()};$('next').onclick=()=>{page++;render()};$('download').onclick=download;$('copy').onclick=()=>navigator.clipboard.writeText(current.text);filter();const wanted=new URLSearchParams(location.search).get('file');const selected=data.skills.find(s=>s.id===location.hash.slice(1))||data.skills.filter(s=>wanted&&wanted.startsWith('snapshots/'+s.repository+'/'+s.commit+'/files/'+(s.directory==='.'?'':s.directory+'/'))).sort((a,b)=>b.directory.length-a.directory.length)[0];if(selected){await openSkill(selected);if(wanted){const f=selected.files.find(f=>'snapshots/'+selected.repository+'/'+selected.commit+'/files/'+f.path===wanted);if(f)await openFile(f);}}}catch(e){$('status').textContent='目录加载失败：'+e.message;}}
init();
</script></html>'''


if __name__ == '__main__':
    main()

