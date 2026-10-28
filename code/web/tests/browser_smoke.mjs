// Browser smoke test using Chrome's built-in debugging protocol; no npm dependencies.
// Start a dedicated headless Chrome with --remote-debugging-port=9223 and a temporary profile.
// Run the app on 8765, then: node code/web/tests/browser_smoke.mjs
import {writeFile} from 'node:fs/promises';
import assert from 'node:assert/strict';
const base = process.env.UI_BASE_URL || 'http://127.0.0.1:8765';
const targets = await (await fetch('http://127.0.0.1:9223/json')).json();
const ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
await new Promise((resolve, reject) => { ws.onopen = resolve; ws.onerror = reject; });
let id = 0; const pending = new Map(); const errors = [];
ws.onmessage = event => {
  const msg = JSON.parse(event.data);
  if (msg.id) { const p = pending.get(msg.id); if (p) { pending.delete(msg.id); clearTimeout(p.timer); msg.error ? p.reject(msg.error) : p.resolve(msg.result); } }
  if (msg.method === 'Runtime.exceptionThrown') errors.push(msg.params.exceptionDetails.text);
};
function call(method, params = {}) { return new Promise((resolve, reject) => { const key = ++id; const timer = setTimeout(() => { pending.delete(key); reject(new Error('Timed out: ' + method)); }, 15000); pending.set(key, {resolve, reject, timer}); ws.send(JSON.stringify({id:key, method, params})); }); }
async function evaluate(expression) { const r = await call('Runtime.evaluate', {expression, returnByValue:true, awaitPromise:true}); if(r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails)); return r.result.value; }
async function until(expression) { for(let i=0;i<60;i++){ if(await evaluate(expression)) return; await new Promise(r=>setTimeout(r,100)); } throw new Error('Condition not met: '+expression); }
async function screenshot(name) {
  await evaluate(`new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))`);
  const {cssContentSize} = await call('Page.getLayoutMetrics');
  const result = await call('Page.captureScreenshot', {format:'png', captureBeyondViewport:true, clip:{x:0,y:0,width:cssContentSize.width,height:cssContentSize.height,scale:1}});
  await writeFile('docs/ui/'+name+'.png',Buffer.from(result.data,'base64'));
}
try {
  await call('Runtime.enable'); await call('Page.enable');
  await call('Emulation.setDeviceMetricsOverride',{width:1440,height:1120,deviceScaleFactor:1,mobile:false});
  await call('Page.navigate',{url:base});
  await until(`document.querySelector('#overview-results') && !document.querySelector('#overview-results').hidden`);
  assert.equal(await evaluate(`document.querySelectorAll('#overview-results .report-link').length`),30);
  await until(`document.querySelector('#overview-results').textContent.includes('30 repositories present in both model runs')`);
  await screenshot('overview');
  await evaluate(`document.querySelector('#saved-model').value='Qwen3.6-35B-A3B-MLX-8bit'; document.querySelector('#saved-model').dispatchEvent(new Event('change'))`);
  await until(`!document.querySelector('#overview-results').hidden && document.querySelector('.report-link')?.hash.includes('Qwen')`);
  assert.equal(await evaluate(`document.querySelectorAll('.compare-link').length`),30);
  await evaluate(`document.querySelector('[aria-label="Comparison annotator"]').value='2'; document.querySelector('[aria-label="Comparison annotator"]').dispatchEvent(new Event('change')); document.querySelector('[aria-label="Comparison subset"]').value='holdout'; document.querySelector('[aria-label="Comparison subset"]').dispatchEvent(new Event('change'))`);
  await until(`document.querySelector('#overview-results').textContent.includes('20 repositories present in both model runs')`);
  await evaluate(`location.hash='compare/astropy_astropy'`);
  await until(`document.querySelector('#report-results').textContent.includes('SAVED MODEL COMPARISON')`);
  assert.equal(await evaluate(`document.querySelectorAll('#report-results tbody tr').length`),6);
  assert.match(await evaluate(`document.querySelector('#report-results').textContent`), /Models differ/);
  await screenshot('model-comparison');
  await call('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  assert.equal(await evaluate(`document.documentElement.scrollWidth <= innerWidth`),true,'Mobile comparison should not overflow');
  await evaluate(`Array.from(document.querySelectorAll('#report-results a')).find(a=>a.hash.includes('Qwen')).click()`);
  await until(`document.querySelector('#report-results .report-panels')`);
  assert.deepEqual(await evaluate(`Array.from(document.querySelectorAll('#report-results .big-score')).map(n=>n.textContent)`),['6 / 6','5 / 12']);
  assert.match(await evaluate(`location.hash`), /Qwen/);
  await evaluate(`location.hash='overview'; document.querySelector('#saved-model').value='llama3.1:8b'; document.querySelector('#saved-model').dispatchEvent(new Event('change'))`);
  await until(`!document.querySelector('#overview-results').hidden && document.querySelector('.report-link')?.hash.includes('llama')`);
  await call('Emulation.setDeviceMetricsOverride',{width:1440,height:1120,deviceScaleFactor:1,mobile:false});
  await evaluate(`document.querySelector('input[type=search]').value='astropy'; document.querySelector('input[type=search]').dispatchEvent(new Event('input'))`);
  assert.equal(await evaluate(`document.querySelectorAll('.report-link').length`),1);
  await evaluate(`document.querySelector('.report-link').click()`);
  await until(`document.querySelector('#report-results h1')?.textContent === 'astropy/astropy'`);
  assert.deepEqual(await evaluate(`Array.from(document.querySelectorAll('#report-results .big-score')).map(n=>n.textContent)`),['6 / 6','4 / 12']);
  await evaluate(`document.querySelector('#report-results .report-panels details').open=true`);
  await screenshot('repository-report');
  await call('Emulation.setEmulatedMedia', {media:'print'});
  assert.equal(await evaluate(`Array.from(document.querySelectorAll('#report-results .report-panels details')).filter(n=>getComputedStyle(n).display!=='none').length`),6,'Printed report retains every documentation score');
  await call('Emulation.setEmulatedMedia', {media:''});
  await call('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  assert.equal(await evaluate(`document.documentElement.scrollWidth <= innerWidth`),true,'Mobile report should not overflow');
  await evaluate(`location.hash='overview'`); await until(`!document.querySelector('#view-overview').hidden`);
  assert.equal(await evaluate(`document.documentElement.scrollWidth <= innerWidth`),true,'Mobile overview should not overflow');
  await evaluate(`document.querySelector('input[type=search]').value=''; document.querySelector('#saved-cohort').value='full'; document.querySelector('#saved-cohort').dispatchEvent(new Event('change'))`);
  assert.equal(await evaluate(`document.querySelectorAll('.report-link').length`),188);
  await evaluate(`document.querySelector('.report-link').click()`);
  await until(`document.querySelector('#report-results .big-score') && document.querySelector('#report-results').textContent.includes('FULL DATASET')`);
  assert.equal(await evaluate(`document.querySelectorAll('#report-results .big-score')[1].textContent`),'Not assessed');
  await call('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
  await evaluate(`location.hash='assess'`); await until(`!document.querySelector('#view-assess').hidden`);
  await evaluate(`document.querySelector('#live-model').value='Qwen3.6-35B-A3B-MLX-8bit'; document.querySelector('#live-model').dispatchEvent(new Event('change'))`);
  assert.match(await evaluate(`document.querySelector('#model-service-note').textContent`), /university KISTE/);
  await screenshot('assess-repository');
  await evaluate(`document.querySelector('#repo-input').value='invalid'; document.querySelector('#assess-form').requestSubmit()`);
  await until(`document.querySelector('#assess-status').classList.contains('error')`);
  assert.match(await evaluate(`document.querySelector('#assess-status').textContent`), /Enter a GitHub/);
  assert.equal(await evaluate(`document.querySelector('#assess-submit').disabled`),false);
  // Exercise client behavior for unavailable inference without accessing GitHub/Ollama.
  await evaluate(`window.originalFetch=window.fetch; window.fetch=async ()=>new Response(JSON.stringify({repo:'demo/repo',source:'live',metadata:{html_url:'https://github.com/demo/repo'},rule_based:{F1_persistent_id:0,F2_metadata_file:0,A1_license:1,I1_dependency_file:0,R1_readme_present:1,R2_citation:0,rule_based_total:2},llm:{error:'Documentation service unavailable. Please retry.'},readme:'Example',readme_limit:12000}),{status:200}); document.querySelector('#repo-input').value='demo/repo'; document.querySelector('#assess-form').requestSubmit()`);
  await until(`!document.querySelector('#assess-results').hidden`);
  assert.deepEqual(await evaluate(`Array.from(document.querySelectorAll('#assess-results .big-score')).map(n=>n.textContent)`),['2 / 6','Not assessed']);
  await evaluate(`window.fetch=async ()=>new Response('unreadable',{status:502}); document.querySelector('#assess-form').requestSubmit()`);
  await until(`document.querySelector('#assess-status').classList.contains('error')`);
  assert.match(await evaluate(`document.querySelector('#assess-status').textContent`), /unreadable response/);
  await evaluate(`window.fetch=window.originalFetch; location.hash='overview'`);
  assert.deepEqual(errors,[],'No browser JavaScript exceptions');
  console.log('PASS: model switching, comparison, annotator/holdout filters, saved provenance, cohort search, 390px layout, invalid input, unavailable LLM, unreadable response; screenshots saved in docs/ui.');
} finally { ws.close(); }
