/* Bind the existing workbench to the saved archive. No model or SQL execution. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function present(value) {
    if (Array.isArray(value)) return value.map(present);
    if (value && typeof value === 'object') {
      const internal = /^(method_id|method_revision|generator_condition|asset_condition|revision|ontology_revision|composition_revision|consumer_contract_version|compiler|format_version|source_commit|release_label|provider|system_fingerprint|.*sha256|.*_hash)$/;
      return Object.fromEntries(Object.entries(value).filter(([key]) => !internal.test(key)).map(([key, item]) => [key, present(item)]));
    }
    return value;
  }
  const jsonText = value => JSON.stringify(present(value), null, 2) ?? '';
  const code = value => `<pre class="mono text-[11px] text-slate-300 whitespace-pre-wrap break-words">${esc(typeof value === 'string' ? value : jsonText(value))}</pre>`;
  const detail = (title, value, open = false) => `<details class="p-2 rounded border border-slate-800 bg-slate-950/50" ${open ? 'open' : ''}><summary class="text-xs text-indigo-300 cursor-pointer">${esc(title)}</summary>${code(value)}</details>`;
  const note = text => `<div class="p-3 text-xs text-slate-400">${esc(text)}</div>`;
  const S = {index:null, entry:null, db:null, case:null, caseMeta:null, filter:'success', epoch:0, queryEpoch:0, timer:null, frames:[], cursor:0, history:[], historyPage:0, cache:new Map(), error:null, updateIndex:0};
  const statusLabel = status => ({success:'成功', failure:'失败', unknown:'未评分'}[status] || '未评分');
  const group = () => S.index?.datasets.find(x => x.id === currentDatasetKey);
  const visibleCases = () => (S.entry?.cases || []).filter(x => S.filter === 'all' || (x.result_status || 'unknown') === S.filter);
  const activeClass = 'ds-tab-btn flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-semibold bg-indigo-600 text-white shadow-sm transition';
  const idleClass = 'ds-tab-btn flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-semibold text-slate-400 hover:text-white hover:bg-slate-800 transition';
  function stop() { clearTimeout(S.timer); S.timer = null; }
  function fail(error) { S.error = String(error.message || error); $('inspector-content').innerHTML = note(S.error); console.error(error); }
  async function get(path) {
    if (!/^(data\/|history-sql\/|explanations\/|archive-index\.json$)/.test(path) || path.includes('..')) throw new Error('Invalid archive path');
    const response = await fetch(path);
    if (!response.ok) throw new Error(`归档文件读取失败：${path} (${response.status})`);
    return response.json();
  }
  async function cached(path) {
    if (S.cache.has(path)) return S.cache.get(path);
    const data = await get(path); S.cache.set(path, data);
    if (S.cache.size > 6) S.cache.delete(S.cache.keys().next().value);
    return data;
  }
  function showInspector(title, payload) {
    $('inspect-target-type').textContent = title;
    $('inspector-content').innerHTML = code(payload);
  }
  function clearAnswer(message = '选择一道归档问题') {
    for (const id of ['answer-subgraph-render','answer-families-render','contract-clauses-body','answer-result-table-container','answer-sql-code']) $(id).innerHTML = note(message);
    $('contract-status-badge').textContent = '归档记录';
  }
  function resetView(message) {
    stop(); S.case = null; S.caseMeta = null; S.frames = []; S.cursor = 0;
    $('left-content-tables').innerHTML = note(message);
    $('left-content-history').innerHTML = note(message);
    $('construct-graph-container').innerHTML = note(message);
    $('drawer-trajectory-steps').innerHTML = note(message);
    $('inspector-content').innerHTML = note(message);
    $('construct-done-banner').classList.add('hidden');
    clearAnswer(message);
  }
  window.renderDatasetTabs = function() {
    if (!S.index) return;
    const host = document.querySelector('.ds-tab-btn')?.parentElement;
    if (!host) return;
    host.style.maxWidth = '36vw'; host.style.overflowX = 'auto';
    host.innerHTML = S.index.datasets.map(d => `<button class="${d.id === currentDatasetKey ? activeClass : idleClass}" style="flex-shrink:0" data-dataset="${esc(d.id)}">${esc(d.label === 'Spider2-Lite' ? 'Spider 2.0-Lite' : d.label)} (${d.question_count})</button>`).join('');
    host.querySelectorAll('[data-dataset]').forEach(b => b.onclick = () => selectDataset(b.dataset.dataset).catch(fail));
  };
  window.renderDbList = function() {
    if (!group()) return;
    const entries = group().databases;
    $('db-count-badge').textContent = `${entries.length} 个 DB/schema`;
    $('db-list-container').innerHTML = entries.map((d, i) => `<button type="button" data-db-index="${i}" class="p-2 rounded-lg border cursor-pointer transition text-left ${d.id === currentDbKey ? 'bg-indigo-950/40 border-indigo-500/80 shadow-md' : 'bg-[var(--surface)] border-[var(--border)] hover:border-slate-700'}"><div class="font-mono text-xs font-bold text-indigo-300 truncate">${esc(d.id)}</div><div class="text-[10px] text-slate-400">${d.table_count} 表 · ${d.object_count} 对象 · ${d.history_sql_count} SQL · ${d.cases.length} 题</div></button>`).join('');
    $('db-list-container').querySelectorAll('[data-db-index]').forEach(b => b.onclick = () => selectDatabase(entries[Number(b.dataset.dbIndex)].id).catch(fail));
  };
  window.selectDataset = async function(key) {
    if (!S.index) return;
    const selected = S.index.datasets.find(d => d.id === key);
    if (!selected) throw new Error('Unknown dataset');
    currentDatasetKey = key; S.filter = 'success'; renderDatasetTabs();
    return selectDatabase(selected.databases.find(d => d.result_counts.success)?.id || selected.databases[0].id);
  };
  window.selectDatabase = async function(key) {
    if (!group()) return;
    const entry = group().databases.find(d => d.id === key);
    if (!entry) throw new Error('Unknown database');
    const ticket = ++S.epoch; ++S.queryEpoch;
    currentDbKey = key; S.entry = entry; S.db = null; S.history = []; S.historyPage = 0; S.updateIndex = 0;
    resetView('正在加载本库归档…'); renderDbList(); renderQuestionSelector();
    const raw = await cached(entry.path);
    if (ticket !== S.epoch) return;
    S.db = raw;
    // The old global functions still receive the same dataset/DB object shape.
    DATASETS[currentDatasetKey].databases[key].constructed = true;
    $('tab-table-count').textContent = `(${raw.ontology?.tables?.length || 0})`;
    renderTables(); renderConstructGraphForDb(); renderUpdate();
    $('construct-status-tag').textContent = `${entry.source_count} 来源记录 · ${entry.object_count} 语义对象 · 点击 Run 回放`;
    $('construct-done-title').textContent = `本库归档 · ${entry.table_count} 表 · ${entry.object_count} 对象`;
    const historyPromise = raw.history_sql_path ? cached(raw.history_sql_path) : Promise.resolve({records:[]});
    const first = visibleCases()[0];
    const casePromise = first ? selectCase(first.id) : Promise.resolve(clearAnswer('当前筛选下没有问题；可切换为“全部”'));
    const history = await historyPromise;
    if (ticket !== S.epoch) return;
    S.history = history.records || []; $('tab-sql-count').textContent = `(${S.history.length})`;
    renderHistory(); await casePromise;
    if (ticket !== S.epoch) return;
    if (currentStage !== 'answer') renderTrajectoryForDb();
  };
  window.loadActiveDbView = function() { /* Navigation is asynchronous in this adapter. */ };

  function columnAliases(table, column) {
    const recovery = S.db?.ontology?.recovery?.find(r => r.prediction?.physical_table === table)?.prediction;
    const rc = recovery?.columns?.find(c => c.physical_column === column);
    const objects = (S.db?.ontology?.objects || []).filter(o => (o.physical_identifiers || []).includes(`${table}.${column}`) && o.kind === 'column');
    return {aliases:[...new Set([...(rc?.aliases || []), ...objects.flatMap(o => o.aliases || [])])], recovery:rc, objects};
  }
  function renderTables() {
    const tables = S.db?.ontology?.tables || [];
    $('left-content-tables').innerHTML = tables.map((t, i) => `<details class="rounded border border-[var(--border)] bg-[var(--surface)]" ${i === 0 ? 'open' : ''}><summary class="p-2 font-mono text-xs text-indigo-300 cursor-pointer">${esc(t.physical_table)} <span class="text-slate-400">${t.columns?.length || 0} 列</span></summary><div class="px-2.5 pb-2 flex flex-col gap-1">${(t.columns || []).map(c => { const aliases = columnAliases(t.physical_table, c.physical_column).aliases; return `<button class="text-left text-[11px] text-slate-300 hover:text-white" data-column="${esc(t.physical_table + '.' + c.physical_column)}">${esc(c.physical_column)} <span class="text-green-300">${esc(aliases[0] || '')}</span><span class="text-slate-500"> ${esc(c.declared_type || '')}</span></button>`; }).join('')}</div></details>`).join('') || note('本库没有保存物理 schema');
    $('left-content-tables').querySelectorAll('[data-column]').forEach(b => b.onclick = () => inspectColumn(b.dataset.column));
    const docs = document.createElement('div'); docs.className = 'flex gap-2 text-xs p-2';
    docs.innerHTML = '<button data-guide="zh" class="text-indigo-300">本库解析 · 中文</button><button data-guide="en" class="text-indigo-300">English</button>';
    docs.querySelectorAll('[data-guide]').forEach(b => b.onclick = () => loadGuide(b.dataset.guide).catch(fail));
    $('left-content-tables').prepend(docs);
  }
  async function loadGuide(language) {
    const ticket = S.epoch, path = S.db?.explanations;
    if (!path) return showInspector('本库解析', '归档未保存解释文档');
    const guide = await cached(path);
    if (ticket !== S.epoch) return;
    const doc = guide.documents[language]; $('inspect-target-type').textContent = language === 'zh' ? '本库 Schema 与业务口径' : 'Schema & business semantics';
    $('inspector-content').innerHTML = `<a class="text-indigo-300 text-xs" href="${esc(doc.markdown)}" download>↓ ${language === 'zh' ? '下载文档' : 'Download guide'}</a><article class="text-slate-300 text-xs leading-relaxed" style="user-select:text">${doc.html}</article>`;
  }
  function inspectColumn(identifier) {
    if (!S.db) return;
    const tables = S.db.ontology.tables || [];
    const table = tables.find(t => (t.columns || []).some(c => `${t.physical_table}.${c.physical_column}` === identifier));
    const physical = table?.columns?.find(c => `${table.physical_table}.${c.physical_column}` === identifier);
    const recovered = physical ? columnAliases(table.physical_table, physical.physical_column) : {};
    const sources = S.history.filter(h => (h.supported_physical_identifiers || h.explicit_physical_identifiers || []).includes(identifier));
    $('inspect-target-type').textContent = identifier;
    $('inspector-content').innerHTML = detail('物理列与恢复名称', {physical, ...recovered}, true) + sources.map(h => detail(h.history_id, h.sql)).join('');
  }
  window.inspectElement = (_type, id) => inspectColumn(id);
  function renderHistory() {
    const pageSize = 20, start = S.historyPage * pageSize, pages = Math.max(1, Math.ceil(S.history.length / pageSize));
    $('left-content-history').innerHTML = `<div class="text-[11px] text-slate-400">${S.history.length} 条已保存 SQL</div><div class="flex justify-between text-xs text-indigo-300"><button id="history-prev">←</button><span>${S.historyPage + 1} / ${pages}</span><button id="history-next">→</button></div>` + S.history.slice(start, start + pageSize).map((h, i) => `<button data-history-index="${start + i}" class="text-left p-2 rounded border border-[var(--border)] bg-[var(--surface)] hover:border-indigo-400"><div class="mono text-xs text-indigo-300">${esc(h.history_id)}</div><div class="mono text-[10px] text-slate-300 line-clamp-2">${esc(h.sql)}</div></button>`).join('');
    $('history-prev').disabled = S.historyPage === 0; $('history-next').disabled = S.historyPage + 1 >= pages;
    $('history-prev').onclick = () => { S.historyPage--; renderHistory(); };
    $('history-next').onclick = () => { S.historyPage++; renderHistory(); };
    $('left-content-history').querySelectorAll('[data-history-index]').forEach(b => b.onclick = () => showHistory(Number(b.dataset.historyIndex)));
  }
  function showHistory(index) {
    const h = S.history[index]; if (!h) return;
    const objects = (S.db.ontology.objects || []).filter(o => (h.supported_object_ids || []).includes(o.id));
    const edges = (h.supported_edge_indices || []).map(i => S.db.ontology.edges[i]).filter(Boolean);
    $('inspect-target-type').textContent = h.history_id;
    $('inspector-content').innerHTML = code(h.sql) + detail('恢复的列、语义对象与连接路径', {identifiers:h.supported_physical_identifiers, objects, edges}) + detail('来源记录', h);
  }
  window.highlightFromSql = id => { const i = S.history.findIndex(h => h.history_id === id); if (i >= 0) showHistory(i); };

  function tableCards(objects) {
    const tables = S.db?.ontology?.tables || [];
    const byTable = new Map();
    for (const object of objects) for (const table of object.physical_tables || []) { if (!byTable.has(table)) byTable.set(table, []); byTable.get(table).push(object); }
    return tables.filter(t => byTable.has(t.physical_table)).map(t => {
      const items = byTable.get(t.physical_table), identifiers = new Set(items.flatMap(o => o.physical_identifiers || []));
      return `<div class="bg-slate-900/90 border border-indigo-500/40 rounded-xl p-3 shadow-lg"><div class="text-xs font-bold text-indigo-300 border-b border-slate-800 pb-2">${esc(t.physical_table)} <span class="text-slate-400">${items.length} 对象</span></div><div class="flex flex-col gap-1 mt-2">${(t.columns || []).filter(c => identifiers.has(`${t.physical_table}.${c.physical_column}`)).map(c => {
        const found = items.find(o => o.kind === 'column' && (o.physical_identifiers || []).includes(`${t.physical_table}.${c.physical_column}`));
        return `<button data-column="${esc(t.physical_table + '.' + c.physical_column)}" class="text-left mono text-[11px] text-slate-300 hover:text-white">${esc(c.physical_column)} <span class="text-green-300">${esc(found?.aliases?.[0] || '')}</span></button>`;
      }).join('')}</div></div>`;
    }).join('');
  }
  window.renderConstructGraphForDb = function(objects) {
    if (!S.db) return;
    const container = $('construct-graph-container');
    container.style.overflow = 'auto'; container.style.display = 'block'; container.style.userSelect = 'text';
    if (!objects) { container.innerHTML = note('点击 Run Construct，按保存的 SQL 来源和恢复记录回放本体构建'); return; }
    const business = objects.filter(o => !['column','table'].includes(o.kind));
    container.innerHTML = `<div class="grid grid-cols-3 gap-3">${tableCards(objects)}</div><details class="mt-3 p-3 rounded border border-slate-700"><summary class="text-xs text-purple-300 cursor-pointer">业务口径与语义对象 · ${business.length}</summary>${business.map(o => detail((o.aliases?.[0] || o.expression || o.id), o)).join('')}</details>`;
    container.querySelectorAll('[data-column]').forEach(b => b.onclick = () => inspectColumn(b.dataset.column));
  };
  function buildFrames() {
    const o = S.db.ontology, sources = o.sources || [], size = Math.max(1, Math.ceil(sources.length / 8)), frames = [];
    for (let i = 0; i < sources.length; i += size) {
      const end = Math.min(sources.length, i + size);
      frames.push({kind:'construct', title:`历史 SQL 来源 ${i + 1}–${end}`, count:end, data:sources.slice(i, end)});
    }
    for (const record of o.construct || []) frames.push({kind:'family', title:`列族约束 · ${record.table || record.family_id}`, count:sources.length, data:record});
    frames.push({kind:'ontology', title:'恢复名称、业务口径与连接路径', count:sources.length, data:{tables:o.recovery || [], edges:o.edges || [], object_count:o.objects?.length || 0}});
    return frames;
  }
  function setReplay(frames, step) {
    stop(); S.frames = frames; S.cursor = 0; S.replayStep = step; renderTrajectoryForDb();
  }
  function advance() {
    if (S.cursor >= S.frames.length || !S.replayStep) return false;
    const frame = S.frames[S.cursor++]; S.replayStep(frame); renderTrajectoryForDb(); return S.cursor < S.frames.length;
  }
  function play() { if (advance()) S.timer = setTimeout(play, 350); }
  window.runConstructAnimation = function() {
    if (!S.db) return;
    const epoch = S.epoch;
    setReplay(buildFrames(), frame => {
      if (epoch !== S.epoch) return;
      const ids = new Set((S.db.ontology.sources || []).slice(0, frame.count).map(s => s.evidence_id));
      const objects = (S.db.ontology.objects || []).filter(o => frame.kind === 'ontology' || (o.evidence_ids || []).some(id => ids.has(id)));
      renderConstructGraphForDb(objects);
      $('construct-status-tag').textContent = `归档回放 ${S.cursor}/${S.frames.length} · ${objects.length} 语义对象`;
      if (S.cursor === S.frames.length) $('construct-done-banner').classList.remove('hidden');
    }); play();
  };
  window.resetConstructCanvas = function() { stop(); S.frames = []; S.cursor = 0; renderConstructGraphForDb(); $('construct-done-banner').classList.add('hidden'); renderTrajectoryForDb(); };

  function renderQuestionSelector() {
    let select = $('archive-question');
    if (!select) {
      const old = $('answer-question-text'); select = document.createElement('select'); select.id = 'archive-question';
      select.className = old.className; select.style.minWidth = '0'; select.setAttribute('aria-label','归档问题'); old.replaceWith(select);
      select.onchange = () => selectCase(select.value).catch(fail);
      const filter = document.createElement('select'); filter.id = 'archive-result-filter'; filter.setAttribute('aria-label','结果筛选'); filter.className = 'text-xs bg-slate-800 border border-slate-700 rounded p-1';
      filter.innerHTML = '<option value="success">成功</option><option value="all">全部</option><option value="failure">失败</option><option value="unknown">未评分</option>';
      select.before(filter); filter.onchange = () => setFilter(filter.value).catch(fail);
      const buttons = [...$('answer-constructed-view').querySelectorAll('button[onclick^="loadPresetQuestion"]')];
      buttons.forEach((b,i) => {b.removeAttribute('onclick'); b.textContent = i ? '下一题 →' : '← 上一题'; b.onclick = () => moveCase(i ? 1 : -1).catch(fail);});
    }
    $('archive-result-filter').value = S.filter;
    const cases = visibleCases();
    select.innerHTML = cases.map(c => `<option value="${esc(c.id)}">[${statusLabel(c.result_status)}] ${esc(c.id)} · ${esc(c.question)}</option>`).join('') || '<option>当前筛选下没有归档问题</option>';
    select.disabled = !cases.length;
    if (S.caseMeta && cases.some(c => c.id === S.caseMeta.id)) select.value = S.caseMeta.id;
  }
  async function setFilter(value) { S.filter = value; renderQuestionSelector(); const first = visibleCases()[0]; if (first) await selectCase(first.id); else { ++S.queryEpoch; stop(); S.case = S.caseMeta = null; S.frames = []; S.cursor = 0; clearAnswer('当前筛选下没有问题；可切换为“全部”'); renderTrajectoryForDb(); } }
  async function moveCase(delta) { const cases = visibleCases(); const i = cases.findIndex(c => c.id === S.caseMeta?.id); if (cases.length) await selectCase(cases[(i + delta + cases.length) % cases.length].id); }
  window.loadPresetQuestion = id => moveCase(id === 1 ? -1 : 1).catch(fail);
  async function selectCase(id) {
    const meta = S.entry?.cases.find(c => c.id === id); if (!meta) throw new Error('Unknown question');
    stop(); const ticket = ++S.queryEpoch, epoch = S.epoch; S.case = null; S.caseMeta = meta; S.frames = []; S.cursor = 0;
    clearAnswer('正在读取该题保存的轨迹…'); renderQuestionSelector();
    const saved = await cached(meta.path); if (ticket !== S.queryEpoch || epoch !== S.epoch) return;
    S.case = saved; renderAnswerStageForDb(); if (currentStage === 'answer') setReplay(queryFrames(), applyQueryFrame);
  }
  function nativeTrace() { return S.case?.saved_native_trace || S.case?.prediction || {}; }
  function queryFrames() {
    if (!S.case) return [];
    const p = S.case.prediction || {}, t = nativeTrace(), r = t.react || {}, frames = [{kind:'question', title:'输入问题', data:{question:S.case.question, database:S.case.database}}];
    if (r.initial_search) frames.push({kind:'retrieval', title:'语义层检索', data:r.initial_search});
    if (r.graph_evo_program_context || r.query_contract || r.scope_contract_validation) frames.push({kind:'context', title:'绑定列族与证据上下文', data:{context:r.graph_evo_program_context, query_contract:r.query_contract, validation:r.scope_contract_validation}});
    if (r.compiled_semantic_plan) frames.push({kind:'plan', title:'编译的语义计划', data:r.compiled_semantic_plan});
    for (const [i, usage] of (t.audit?.usage || []).entries()) frames.push({kind:'model', title:`保存的模型调用 ${i + 1}`, data:usage});
    for (const action of r.trajectory || []) frames.push({kind:'tool', title:`${action.tool || '工具调用'} · ${action.status || '归档'}`, data:action});
    for (const action of p.access_trace || []) frames.push({kind:'tool', title:'保存的数据库访问', data:action});
    frames.push({kind:'final', title:'保存的最终 SQL 与评分', data:{sql:p.sql ?? '', status:p.status || p.decision, error:p.error, execution_probe:p.execution_probe, result_status:S.caseMeta.result_status, official_score:S.caseMeta.official_score, evaluation_reason:S.caseMeta.evaluation_reason}});
    return frames;
  }
  function exactExecution() {
    const p = S.case?.prediction || {}, direct = p.execution_probe || {};
    if (Array.isArray(direct.columns) && Array.isArray(direct.rows)) return direct;
    const normalize = sql => String(sql || '').trim().replace(/;$/, '').trim();
    return [...(nativeTrace().react?.trajectory || [])].reverse().find(a => normalize(a.arguments?.sql) === normalize(p.sql) && Array.isArray(a.observation?.rows))?.observation;
  }
  function renderExecution() {
    const observation = exactExecution();
    if (!observation) { $('answer-result-table-container').innerHTML = note('最终 SQL 的执行行未保存；可查看右侧执行记录'); return; }
    $('answer-result-table-container').innerHTML = `<table class="w-full text-left text-xs font-mono"><thead class="bg-slate-900 text-slate-400"><tr>${(observation.columns || []).map(c => `<th class="p-2">${esc(c)}</th>`).join('')}</tr></thead><tbody>${observation.rows.map(row => `<tr>${row.map(c => `<td class="p-2 text-emerald-300">${esc(typeof c === 'object' ? jsonText(c) : c)}</td>`).join('')}</tr>`).join('')}</tbody></table>` + (observation.truncated ? note('归档记录标记：结果行已截断') : '');
  }
  window.renderAnswerStageForDb = function() {
    $('answer-unconstructed-view').classList.add('hidden'); $('answer-constructed-view').classList.remove('hidden');
    $('answer-guard-pill').textContent = '归档回放';
    if (!S.case) return;
    const t = nativeTrace(), r = t.react || {}, p = S.case.prediction || {}, meta = S.caseMeta;
    $('answer-subgraph-render').innerHTML = detail('检索到的本体子图与证据', r.initial_search || {}, true);
    $('answer-families-render').innerHTML = detail('物理列绑定 / 列族上下文', r.graph_evo_program_context || r.compiled_semantic_plan?.role_bindings || {}, true);
    $('contract-clauses-body').innerHTML = detail('保存的 Query Contract', r.scope_contract_validation || r.query_contract || {}, true) + detail('编译的语义计划', r.compiled_semantic_plan || {});
    $('contract-status-badge').textContent = statusLabel(meta.result_status);
    $('contract-status-badge').className = `pill ${meta.result_status === 'success' ? 'pill-green' : meta.result_status === 'failure' ? 'pill-red' : 'pill-amber'} text-[10px]`;
    $('answer-sql-code').innerHTML = code(p.sql || '保存的 SQL 为空'); renderExecution();
    const badge = $('answer-sql-code').parentElement.querySelector('.pill'); if (badge) badge.textContent = `归档评分 · ${statusLabel(meta.result_status)}`;
    const time = $('answer-result-table-container').parentElement.querySelector('.text-slate-500'); if (time) { const seconds = p.latency_seconds ?? p.wall_seconds ?? p.seconds; time.textContent = Number.isFinite(seconds) ? `归档总耗时 ${seconds.toFixed(2)}s` : '归档执行结果'; }
  };
  function applyQueryFrame(frame) {
    const ids = ['step-subgraph','step-linking','step-contract','step-sql'];
    const stage = ({question:0, retrieval:0, context:1, plan:2, model:2, tool:3, final:3})[frame.kind] ?? 0;
    ids.forEach((id, i) => { $(id).className = `px-2 py-0.5 rounded ${i <= stage ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40' : 'bg-slate-800 text-slate-400 border border-slate-700'}`; });
    showInspector(frame.title, frame.data);
  }
  window.runAnswerPipeline = function() { if (!S.case) return; setReplay(queryFrames(), applyQueryFrame); play(); };

  function renderUpdate() {
    if (!S.db) return;
    const section = $('stage-update'), events = S.db.maintenance || [];
    const area = section.querySelector('.grid-cols-3');
    const toolbar = section.firstElementChild;
    const oldVersion = toolbar.querySelector('.pill'); if (oldVersion) oldVersion.textContent = `${events.length} 条归档更新`;
    const ev = events[S.updateIndex];
    const options = events.map((e,i) => `<option value="${i}">${esc(e.title || e.event_type)}</option>`).join('');
    const changes = ev?.column_changes || [];
    area.innerHTML = `<div class="col-span-2 bg-[var(--card)] border border-[var(--border)] rounded-xl p-4 flex flex-col overflow-auto"><div class="flex gap-2 mb-3"><select id="archive-update-event" class="min-w-0 flex-1 bg-slate-900 text-xs p-2 border border-slate-700 rounded" aria-label="增量更新记录">${options || '<option>本库无归档更新事件</option>'}</select><button id="archive-update-run" class="bg-indigo-600 text-white text-xs px-3 py-1 rounded">▶ Run Update</button></div><div id="archive-update-canvas">${ev ? note('点击 Run Update 回放保存的增量闭包与名称变更') : note('本库没有保存增量更新事件')}</div></div><div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-4 flex flex-col overflow-auto"><div class="text-xs font-bold text-slate-300 mb-3">前后口径对比</div>${changes.map(c => `<div class="p-2 mb-2 rounded border border-amber-500/40 text-xs"><div class="text-indigo-300">${esc((c.physical_identifiers || []).join(', '))}</div><div class="text-slate-400">${esc(jsonText(c.before))}</div><div class="text-emerald-300">→ ${esc(jsonText(c.after))}</div></div>`).join('') || note(ev ? '该事件未保存列名变化；可查看完整闭包记录' : '—')}</div>`;
    $('archive-update-event').disabled = !events.length; $('archive-update-run').disabled = !events.length;
    $('archive-update-event').onchange = () => { stop(); S.updateIndex = Number($('archive-update-event').value); renderUpdate(); };
    $('archive-update-run').onclick = runUpdate;
  }
  function runUpdate() {
    const e = S.db?.maintenance?.[S.updateIndex]; if (!e) return;
    const r = e.receipt || {};
    const frames = [
      {kind:'update', title:'读取增量来源与名称修正', data:{source:e.source, event_type:e.event_type, column_changes:e.column_changes}},
      {kind:'update', title:'标记变化种子', data:{delta_ids:r.delta_ids, delta_size:r.delta_size}},
      {kind:'update', title:'展开依赖闭包', data:{affected_ids:r.affected_ids, affected_size:r.affected_size, unchanged_object_count:r.unchanged_object_count}},
      {kind:'update', title:'应用名称变化与保留未受影响对象', data:{column_changes:e.column_changes, ontology_diff:r.ontology_diff, before_hash:r.before_hash, after_hash:r.after_hash}},
    ];
    $('archive-update-canvas').innerHTML = '';
    setReplay(frames, f => { $('archive-update-canvas').insertAdjacentHTML('beforeend', detail(f.title, f.data, true)); showInspector(f.title, f.data); }); play();
  }
  window.renderTrajectoryForDb = function() {
    if (!S.db) return;
    const frames = S.frames.length ? S.frames : currentStage === 'answer' ? queryFrames() : currentStage === 'construct' ? buildFrames() : [];
    $('drawer-trajectory-steps').innerHTML = `<div class="flex gap-2 text-xs text-indigo-300 mb-2"><button id="archive-next">下一步 →</button><button id="archive-stop">停止</button><span class="text-slate-400">${S.cursor} / ${frames.length}</span></div>` + frames.map((f, i) => `<button data-frame="${i}" class="text-left p-2 rounded border ${i < S.cursor ? 'border-emerald-500/40' : 'border-slate-800'} bg-[var(--surface)]"><span class="text-xs ${i < S.cursor ? 'text-emerald-300' : 'text-slate-300'}">${i + 1}. ${esc(f.title)}</span></button>`).join('');
    $('archive-stop').onclick = stop;
    $('archive-next').onclick = () => { stop(); if (!S.frames.length) { if (currentStage === 'answer') setReplay(queryFrames(), applyQueryFrame); else if (currentStage === 'construct') { runConstructAnimation(); stop(); return; } } advance(); };
    $('drawer-trajectory-steps').querySelectorAll('[data-frame]').forEach(b => b.onclick = () => { stop(); const f = frames[Number(b.dataset.frame)]; showInspector(f.title, f.data); });
  };
  window.switchStage = function(stage) {
    stop(); currentStage = stage; S.frames = []; S.cursor = 0;
    ['construct','answer','update'].forEach(name => { $('stage-' + name).classList.toggle('hidden', name !== stage); $('nav-' + name).className = name === stage ? 'stage-nav-btn flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-indigo-600 text-white shadow-sm transition-all' : 'stage-nav-btn flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold text-slate-400 hover:text-white transition-all'; });
    if (stage === 'answer') { renderAnswerStageForDb(); if (S.case) setReplay(queryFrames(), applyQueryFrame); }
    if (stage === 'update') renderUpdate();
    renderTrajectoryForDb();
  };
  async function init() {
    resetView('正在加载全量归档索引…');
    // Clear prototype examples before exposing archive navigation.
    for (const key of Object.keys(DATASETS)) delete DATASETS[key];
    S.index = await get('archive-index.json');
    for (const d of S.index.datasets) DATASETS[d.id] = {id:d.id, name:d.label, databases:Object.fromEntries(d.databases.map(db => [db.id, {id:db.id, name:db.id, constructed:true}]))};
    const brandVersion = document.querySelector('header .pill'); if (brandVersion) brandVersion.textContent = '归档';
    const panel = $('answer-sql-code').parentElement.querySelector('.pill'); if (panel) panel.textContent = '归档评分';
    currentDatasetKey = S.index.datasets[0].id; renderDatasetTabs(); switchStage('construct');
    await selectDatabase(group().databases.find(d => d.id === 'formula_1')?.id || group().databases[0].id);
    S.error = null; return {datasets:S.index.datasets.length, databases:S.index.database_count, questions:S.index.question_count};
  }
  window.SRArchive = {state:S, selectCase, setFilter, stop, advance, loadGuide, runUpdate, visibleCases};
  SRArchive.ready = new Promise((resolve, reject) => {
    const start = () => init().then(resolve, error => {fail(error); reject(error);});
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, {once:true}); else start();
  });
})();
