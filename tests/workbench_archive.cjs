const fs = require('fs');
const path = require('path');
const assert = require('node:assert/strict');
const {JSDOM, ResourceLoader, VirtualConsole} = require('../.qa/node_modules/jsdom');
const root = path.resolve(__dirname, '../dist');
let delayed = '';
const errors = [];
const virtualConsole = new VirtualConsole();
virtualConsole.on('jsdomError', e => errors.push(e.message));
class LocalResources extends ResourceLoader {
  fetch(url) {
    if (new URL(url).hostname === 'www.gstatic.com') return Promise.resolve(Buffer.from(''));
    const name = path.join(root, decodeURIComponent(new URL(url).pathname));
    return Promise.resolve(fs.readFileSync(name));
  }
}
let html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
if (!html.includes('src="archive-adapter.js"')) html = html.replace('</body>', '<script src="archive-adapter.js"></script></body>');
const dom = new JSDOM(html, {
  url:'http://127.0.0.1:8766/', runScripts:'dangerously', resources:new LocalResources(), virtualConsole,
  beforeParse(window) {
    window.fetch = async value => {
      const name = String(value);
      if (name === delayed) await new Promise(resolve => setTimeout(resolve, 35));
      const file = path.resolve(root, name);
      assert(file.startsWith(root + path.sep));
      return {ok:fs.existsSync(file), status:fs.existsSync(file) ? 200 : 404, json:async() => JSON.parse(fs.readFileSync(file, 'utf8'))};
    };
    window.addEventListener('error', e => errors.push(e.message));
  },
});
const window = dom.window;
const $ = id => window.document.getElementById(id);
const tick = () => new Promise(resolve => setImmediate(resolve));
async function main() {
  await tick();
  const counts = await window.SRArchive.ready;
  assert.deepEqual(JSON.parse(JSON.stringify(counts)), {datasets:8, databases:370, questions:4394});
  assert.equal(window.document.querySelectorAll('[data-dataset]').length, 8);
  assert.equal(window.SRArchive.state.filter, 'success');
  const coverage = [];
  for (const dataset of window.SRArchive.state.index.datasets) {
    await window.selectDataset(dataset.id);
    const s = window.SRArchive.state;
    assert.equal(s.db.database, s.entry.id);
    assert.equal(window.document.querySelectorAll('[data-db-index]').length, dataset.databases.length);
    assert.equal(s.case.dataset, dataset.id);
    assert.equal(s.caseMeta.result_status, 'success');
    assert.equal($('answer-sql-code').textContent, s.case.prediction.sql || '保存的 SQL 为空');
    window.switchStage('answer'); window.runAnswerPipeline(); window.SRArchive.stop();
    while (window.SRArchive.advance()) {}
    assert.equal(window.SRArchive.state.cursor, window.SRArchive.state.frames.length);
    assert.equal($('contract-status-badge').textContent, '成功');
    await window.SRArchive.setFilter('all');
    const last = window.SRArchive.visibleCases().at(-1);
    await window.SRArchive.selectCase(last.id);
    assert.equal($('contract-status-badge').textContent, ({success:'成功',failure:'失败',unknown:'未评分'})[last.result_status || 'unknown']);
    coverage.push({dataset:dataset.id, databases:dataset.databases.length, questions:dataset.question_count});
  }
  await window.selectDataset('BIRD-History');
  await window.selectDatabase('formula_1');
  window.switchStage('construct'); window.runConstructAnimation(); window.SRArchive.stop();
  while (window.SRArchive.advance()) {}
  assert($('construct-graph-container').textContent.includes('race_name'));
  assert(!$('construct-done-banner').classList.contains('hidden'));
  window.switchStage('update'); window.SRArchive.runUpdate(); window.SRArchive.stop();
  while (window.SRArchive.advance()) {}
  assert($('archive-update-canvas').textContent.includes('race_name'));
  await window.SRArchive.loadGuide('zh'); assert($('inspector-content').querySelector('article'));
  await window.SRArchive.loadGuide('en'); assert($('inspector-content').querySelector('article'));
  await window.selectDataset('EvoSchema'); window.switchStage('update');
  assert.equal($('archive-update-run').disabled, true);
  assert(!$('stage-update').textContent.includes('Starting Grid'));
  // A slow previous DB response cannot replace the newly selected DB.
  await window.selectDataset('KaggleDBQA');
  const entries = window.SRArchive.state.index.datasets.find(x => x.id === 'KaggleDBQA').databases;
  window.SRArchive.state.cache.clear(); delayed = entries[0].path;
  await Promise.all([window.selectDatabase(entries[0].id), window.selectDatabase(entries[1].id)]);
  assert.equal(window.SRArchive.state.db.database, entries[1].id);
  assert.equal(window.SRArchive.state.entry.id, entries[1].id);
  delayed = '';
  // Archive SQL remains text even when it contains HTML.
  const s = window.SRArchive.state, original = s.case.prediction.sql;
  s.case.prediction.sql = '<img src=x onerror=alert(1)>'; window.renderAnswerStageForDb();
  assert.equal($('answer-sql-code').querySelector('img'), null);
  assert.equal($('answer-sql-code').textContent, '<img src=x onerror=alert(1)>'); s.case.prediction.sql = original;
  assert.deepEqual(errors, []);
  console.log(JSON.stringify({status:'PASS', counts, coverage, checks:['archive SQL/score binding','success/all filters','saved construction/update playback','bilingual per-DB guides','DB navigation race','HTML escaping','all eight datasets']}, null, 2));
}
main().then(() => {window.SRArchive?.stop(); dom.window.close();}, error => {console.error(error); window.SRArchive?.stop(); dom.window.close(); process.exitCode = 1;});
