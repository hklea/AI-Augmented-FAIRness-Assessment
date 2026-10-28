const LLAMA = "llama3.1:8b", QWEN = "Qwen3.6-35B-A3B-MLX-8bit";
const modelLabel = model => model === QWEN ? "Qwen3.6 35B / University KISTE" : model === LLAMA ? "Llama 3.1 8B / Local Ollama" : model || "No model";
const number = value => Number.isFinite(value) ? value.toFixed(3) : "Unavailable";
﻿const INDICATORS = {
  F1_persistent_id: "Persistent identifier", F2_metadata_file: "Structured metadata",
  A1_license: "License", I1_dependency_file: "Dependency specification",
  R1_readme_present: "README presence", R2_citation: "Citation information",
};
const DIMENSIONS = {D1: "Installation clarity", D2: "Usage clarity", D3: "Purpose description", D4: "Dependency description", D5: "Examples and tutorials", D6: "Contribution information"};
const RUBRICS = {
  D1: "0: No installation instructions. 1: Incomplete instructions or external links. 2: Actionable steps and required prerequisites.",
  D2: "0: No usage information. 1: Linked documentation or tutorials without an inline example. 2: A concrete command, code snippet, workflow, or executable example.",
  D3: "0: No purpose description. 1: Vague or incomplete description. 2: Clear explanation of the software and intended domain or audience.",
  D4: "0: No meaningful dependency or environment information. 1: Partial information. 2: Required and/or optional dependencies explicitly listed in human-readable form.",
  D5: "0: No examples or tutorials mentioned. 1: An explicit reference to examples or tutorials whose content is not supplied. 2: A meaningful usage example in the supplied evidence. Generic documentation links do not count as examples.",
  D6: "0: Neither contribution nor support information. 1: Partial contribution or support information. 2: Contribution guidance and at least one support or community channel.",
};
const $ = id => document.getElementById(id);
function el(tag, attrs = {}, children = []) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
  for (const child of [].concat(children)) if (child != null) node.append(child.nodeType ? child : document.createTextNode(String(child)));
  return node;
}
function note(text) { return el("p", {class: "note"}, text); }
function card(title, children) { return el("section", {class: "card"}, [el("h2", {}, title), ...children]); }
function details(title, children) { return el("details", {}, [el("summary", {}, title), el("div", {class: "details-body"}, children)]); }
function button(text, action) { const b = el("button", {type: "button"}, text); b.addEventListener("click", action); return b; }
function showStatus(node, message, error = false) { node.hidden = !message; node.className = `status${error ? " error" : ""}`; node.textContent = message || ""; }
async function getJson(url, options) {
  const response = await fetch(url, options);
  let data;
  try { data = await response.json(); } catch { throw new Error("The server returned an unreadable response. Please retry."); }
  if (!response.ok) throw new Error(typeof data.detail === "string" ? data.detail : "The request failed. Please retry.");
  return data;
}
function scoreCard(label, value, max, caption, className = "") {
  return el("div", {class: `score-summary ${className}`}, [el("p", {class: "eyebrow"}, label), el("div", {class: "big-score"}, [value, max ? el("span", {}, ` / ${max}`) : null]), note(caption)]);
}
function bars(items) {
  return el("div", {class: "bars"}, items.map(item => el("div", {class: "bar-row"}, [
    el("span", {}, item.label), el("div", {class: "bar-track", "aria-hidden": "true"}, el("div", {class: "bar-fill", style: `width:${Math.max(0, Math.min(100, item.percent))}%`})), el("span", {class: "bar-value"}, item.text),
  ])));
}
function table(headers, rows) {
  return el("div", {class: "table-scroll", tabindex: "0", role: "region", "aria-label": headers.join(", ")}, el("table", {}, [
    el("thead", {}, el("tr", {}, headers.map(h => el("th", {scope: "col"}, h)))),
    el("tbody", {}, rows.map(row => el("tr", {}, row.map(cell => el("td", {}, cell))))),
  ]));
}
let overviewData;
let overviewRequest = 0;
async function loadOverview() {
  const model = $("saved-model").value;
  if (overviewData?.model === model) return;
  const request = ++overviewRequest;
  $("overview-results").hidden = true;
  showStatus($("overview-status"), "Loading saved assessments…");
  try {
    const data = await getJson(`/api/overview?model=${encodeURIComponent(model)}`);
    if (request !== overviewRequest) return;
    renderOverview(data); overviewData = data;
    showStatus($("overview-status"), null); $("overview-results").hidden = false;
  } catch (error) {
    if (request !== overviewRequest) return;
    showStatus($("overview-status"), error.message, true); $("overview-status").append(button("Retry", loadOverview));
  }
}
function renderOverview(data) {
  const target = $("overview-results"); target.replaceChildren();
  const full = data.full_dataset, hybrid = data.ground_truth_hybrid;
  target.append(el("div", {class: "summary-grid"}, [
    scoreCard("FULL DATASET", full.available ? full.repo_count : "Unavailable", null, "Repositories with structural assessments"),
    scoreCard("ANNOTATED CORPUS", hybrid.available ? hybrid.repo_count : "Unavailable", null, "Repositories with both assessment components", "docs-accent"),
    scoreCard("STRUCTURAL MEAN", full.available ? full.mean_total : "—", 6, "Across the full dataset"),
  ]));
  target.append(el("div", {class: "scope-note"}, "These scores describe different aspects of software. Structural and documentation totals remain separate; neither is a complete measure of FAIR compliance."));
  const charts = el("div", {class: "two-column"});
  if (full.available) charts.append(card("Structural evidence", [note(`Indicator detection rate · ${full.repo_count} repositories`), bars(Object.keys(INDICATORS).map(key => ({label: `${key.slice(0, 2)} · ${INDICATORS[key]}`, percent: full.prevalence_pct[key], text: `${full.prevalence_pct[key].toFixed(1)}%`}))), details("Distribution of structural totals", [bars(Object.entries(full.total_distribution).map(([score, count]) => ({label: `${score} / 6`, percent: 100 * count / full.repo_count, text: `${(100 * count / full.repo_count).toFixed(1)}% · ${count}`})))])]));
  if (hybrid.available) charts.append(card("README documentation", [note(`${modelLabel(data.model)} / Mean dimension scores · ${hybrid.repo_count} repositories · 0–2 scale`), bars(Object.keys(DIMENSIONS).map(key => ({label: `${key} · ${DIMENSIONS[key]}`, percent: 50 * hybrid.dimension_means[key], text: `${hybrid.dimension_means[key].toFixed(2)} / 2`}))), note(`Mean documentation total: ${hybrid.mean_total} / 12. Scores reflect the supplied README, including the study’s 12,000-character limit.`)]));
  target.append(charts, repositoryBrowser(data.repositories, data.model), comparisonMetrics());
  const metrics = data.evaluation;
  if (metrics) {
    const prf = rows => table(["Indicator", "Precision", "Recall", "F1"], rows.map(r => [INDICATORS[r.indicator] || r.indicator, ...[r.precision, r.recall, r.f1].map(v => v.toFixed(2))]));
    target.append(el("div", {class: "card"}, details("Research evaluation · agreement and validation", [
      el("h3", {}, "Structural assessment · 30-repository ground truth"), prf(metrics.rule_based_prf),
      el("h3", {}, "Structural assessment · 20-repository pilot-exclusion subset"), prf(metrics.rule_based_prf_holdout),
      note(metrics.rule_based_prf_holdout_note),
      el("h3", {}, `${modelLabel(data.model)} · Model-reported confidence`),
      note("Confidence labels are self-reported, not calibrated probabilities. HIGH does not guarantee a correct score. Exact agreement is shown as a fraction from 0 to 1."),
      table(["Confidence", "N", "Exact agreement", "MAE", "Kappa"], metrics.confidence_calibration.map(r => [r.confidence, r.n, ...[r.exact_agreement, r.mae, r.kappa].map(v => Number.isFinite(v) ? v.toFixed(2) : "—")])),
    ])));
  }
}
function repositoryBrowser(repositories, model) {
  const search = el("input", {type: "search", placeholder: "Search by owner or repository…", "aria-label": "Search saved repositories"});
  const cohort = el("select", {id: "saved-cohort", "aria-label": "Select dataset"}, [el("option", {value: "hybrid"}, "Annotated corpus · hybrid profiles"), el("option", {value: "full"}, "Full dataset · structural assessments")]);
  const count = el("p", {class: "note", "aria-live": "polite"});
  const content = el("div");
  function update() {
    const rows = (repositories[cohort.value] || []).filter(row => row.repo.toLowerCase().includes(search.value.trim().toLowerCase()));
    count.textContent = `${rows.length} repositories shown. ${cohort.value === "full" ? "This cohort displays its saved structural run; documentation was not assessed in that run." : "These saved profiles use the annotated corpus snapshots."}`;
    content.replaceChildren(rows.length ? table(["Repository", "Structural", "Documentation", "Report", "Models"], rows.map(row => [
      row.repo, `${row.rule_based_total} / 6`, row.llm_total == null ? el("span", {class: "muted"}, "Not assessed") : `${row.llm_total} / 12`,
      el("a", {href: `#report/${cohort.value}/${encodeURIComponent(row.id)}/${encodeURIComponent(model)}`, class: "report-link", "aria-label": `View report for ${row.repo}`}, "View report →"),
      cohort.value === "hybrid" ? el("a", {href: `#compare/${encodeURIComponent(row.id)}`, class: "compare-link"}, "Compare models") : "—",
    ])) : el("p", {class: "empty-state"}, "No matching repositories. Try another name or dataset."));
  }
  search.addEventListener("input", update); cohort.addEventListener("change", update); update();
  return card("Explore individual repositories", [el("div", {class: "browser-controls"}, [search, cohort]), count, content]);
}
function renderReport(data, target) {
  target.replaceChildren();
  const saved = data.source === "saved", llm = data.llm, successful = llm && !llm.error;
  const title = el("h1", {tabindex: "-1"}, data.repo);
  target.append(el("div", {class: "page-heading report-heading"}, [el("div", {}, [
    el("p", {class: "eyebrow"}, saved ? `SAVED THESIS ASSESSMENT · ${data.cohort === "hybrid" ? "ANNOTATED CORPUS" : "FULL DATASET"}` : "NEW ASSESSMENT · CURRENT GITHUB CONTENT"),
    title, el("p", {}, data.metadata.description || "Individual research software assessment"),
  ]), el("div", {class: "report-actions"}, [el("a", {href: data.metadata.html_url, target: "_blank", rel: "noopener noreferrer", class: "button"}, "Open on GitHub ↗"), button("Print report", () => window.print())])]));
  if (saved && data.cohort === "hybrid") {
    const model = el("select", {id: "report-model"}, [LLAMA, QWEN].map(value => el("option", {value}, modelLabel(value))));
    model.value = llm?.model || LLAMA;
    model.addEventListener("change", () => {
      const parts = location.hash.split("/");
      parts[3] = encodeURIComponent(model.value);
      location.hash = parts.join("/");
    });
    target.append(el("div", {class: "model-controls"}, [
      el("label", {for: "report-model"}, "Saved documentation model"), model,
      note("Switch between saved model assessments for this repository. Structural assessments are shared across models."),
    ]));
  }
  target.append(el("div", {class: "two-column totals"}, [
    scoreCard("STRUCTURAL EVIDENCE", data.rule_based.rule_based_total, 6, "Selected repository files and metadata"),
    scoreCard("README DOCUMENTATION", successful ? llm.total : "Not assessed", successful ? 12 : null, successful ? modelLabel(llm.model) : llm?.error || (saved ? "No documentation assessment in this saved run" : "Documentation assessment was not requested"), "docs-accent"),
  ]));
  target.append(el("div", {class: "scope-note"}, "Selected FAIR-related indicators, not complete FAIR4RS compliance. README assessment uses at most the first 12,000 characters; linked documentation is not retrieved. Model explanations should be checked against the supplied evidence."));
  const structural = card("Structural indicators", [note("Detected means the indicator’s evidence was found by the rule-based checks. Not detected describes the inspected evidence, rather than all possible project documentation.")]);
  for (const [key, label] of Object.entries(INDICATORS)) structural.append(el("div", {class: "indicator-row"}, [el("span", {}, [el("span", {class: "code-label"}, key.slice(0, 2)), label]), el("span", {class: `pill ${data.rule_based[key] ? "detected" : "missing"}`}, data.rule_based[key] ? "Detected" : "Not detected")]));
  const docs = card("Documentation dimensions", [note("Expand a dimension to inspect the model explanation and scoring rubric. Confidence is model-reported, not a calibrated probability.")]);
  if (successful) {
    for (const [key, label] of Object.entries(DIMENSIONS)) {
      const dim = llm.dimensions[key]; if (!dim) continue;
      docs.append(details(el("span", {class: "dimension-summary"}, [el("span", {}, [el("span", {class: "code-label"}, key), label]), el("span", {class: `pill score-${dim.score}`}, `${dim.score} / 2`)]), [
        el("p", {class: "reasoning"}, dim.reasoning), note(`Model-reported confidence: ${dim.confidence}. This does not guarantee correctness.`), el("p", {class: "rubric"}, RUBRICS[key]),
      ]));
    }
  } else docs.append(el("p", {class: "empty-state"}, llm?.error || "Documentation scores are unavailable for this assessment. They are not treated as zero."));
  target.append(el("div", {class: "two-column report-panels"}, [structural, docs]));
  const evidence = data.readme == null ? [note("The README snapshot is not available locally for this saved run. Its saved scores remain available.")] : [
    note(data.readme_truncated ? "The README exceeded the model input limit. The text below shows the first 12,000 characters available to documentation scoring." : "README snapshot for this assessment. Shown as text so that links and embedded content are not loaded."),
    el("pre", {class: "readme"}, data.readme.slice(0, data.readme_limit) || "No README was found."),
  ];
  target.append(el("div", {class: "card evidence"}, [details("Inspect README evidence", evidence), details("Assessment details", [
    note(`Source: ${saved ? "Saved thesis results; not refreshed from GitHub" : "Live GitHub collection; not added to the thesis dataset"}.`),
    note(`${saved ? "Documentation scoring timestamp" : "Collection timestamp"}: ${data.assessed_at || "Not recorded in the saved structural results"}`),
    note(`Model: ${llm?.model || "Not used in this report"}. Structural scale: 0–6. Documentation scale: 0–12. The totals are not combined.`),
  ])]));
}
function comparisonMetrics() {
  const annotator = el("select", {"aria-label": "Comparison annotator"}, [el("option", {value: "1"}, "Primary annotator"), el("option", {value: "2"}, "Second annotator")]);
  const subset = el("select", {"aria-label": "Comparison subset"}, [el("option", {value: "all"}, "Full annotated corpus"), el("option", {value: "holdout"}, "Exclude 10 pilot repositories")]);
  const content = el("div", {"aria-live": "polite"});
  let generation = 0;
  async function update() {
    const request = ++generation;
    content.replaceChildren(note("Loading model comparison…"));
    try {
      const data = await getJson(`/api/comparison?annotator=${annotator.value}&subset=${subset.value}`);
      if (request !== generation) return;
      if (!data.n) { content.replaceChildren(note("No matched saved assessments are available for this comparison.")); return; }
      content.replaceChildren(note(`${data.n} repositories present in both model runs. Higher Kappa and exact agreement, and lower MAE, indicate closer agreement with the selected annotator. Higher documentation scores alone do not indicate a better model.`),
        table(["Model", "Mean weighted Kappa", "Exact agreement", "MAE"], data.results.map(r => [modelLabel(r.model), number(r.summary.kappa), number(r.summary.exact), number(r.summary.mae)])),
        details("Per-dimension agreement", [table(["Dimension", "Model", "Weighted Kappa", "Exact agreement", "MAE"], Object.keys(DIMENSIONS).flatMap(dim => data.results.map(r => {const d = r.dimensions.find(d => d.dimension === dim); return [DIMENSIONS[dim], modelLabel(r.model), number(d.kappa), number(d.exact), number(d.mae)]; })))]),
        note("Summary metrics are averages across dimensions; undefined Kappa values are excluded. Exact agreement is a fraction from 0 to 1. Pilot exclusion is a sensitivity analysis, not a new independent experiment."));
    } catch (error) { if (request === generation) content.replaceChildren(note(error.message), button("Retry", update)); }
  }
  annotator.addEventListener("change", update); subset.addEventListener("change", update); update();
  return card("Compare model agreement with humans", [el("div", {class: "browser-controls"}, [annotator, subset]), content]);
}

function renderComparison(data, target) {
  const reports = data.models.map(m => data.reports[m.id]);
  const base = reports.find(Boolean);
  const human = el("select", {"aria-label": "Reference annotator"}, [el("option", {value: "1"}, "Primary annotator"), el("option", {value: "2"}, "Second annotator")]);
  const rows = el("div");
  function update() {
    const reference = data.humans[human.value];
    rows.replaceChildren(table(["Dimension", ...data.models.map(m => m.label), "Human reference"], Object.keys(DIMENSIONS).map(dim => {
      const scores = reports.map(r => r?.llm?.dimensions[dim]?.score);
      const disagreement = scores.every(Number.isFinite) && scores[0] !== scores[1];
      return [el("span", {}, [`${dim} · ${DIMENSIONS[dim]}`, disagreement ? el("span", {class: "pill missing"}, "Models differ") : null]), ...scores.map(score => score == null ? "Not assessed" : `${score} / 2`), reference ? `${reference[dim]} / 2` : "Unavailable"];
    })));
  }
  human.addEventListener("change", update); update();
  target.replaceChildren(el("div", {class: "page-heading"}, [el("div", {}, [el("p", {class: "eyebrow"}, "SAVED MODEL COMPARISON · ANNOTATED CORPUS"), el("h1", {tabindex: "-1"}, base.repo), note("Two saved model runs against the annotated corpus README snapshots. No live inference is performed.")]), button("Print comparison", () => window.print())]),
    scoreCard("STRUCTURAL EVIDENCE", base.rule_based.rule_based_total, 6, "Shared structural assessment for this repository"),
    card("README documentation scores", [human, rows, note("Differences identify cases to inspect; human scores are reference annotations, not a combined or adjudicated score.")]),
    el("div", {class: "two-column"}, data.models.map((m, i) => {
      const report = reports[i], llm = report?.llm;
      if (!llm) return card(m.label, [note("No saved assessment is available for this model.")]);
      return card(m.label, [note(`${m.provider} · ${llm.total} / 12 · ${report.assessed_at || "Timestamp not recorded"}`), note(`Model ID: ${m.id}`), ...Object.keys(DIMENSIONS).map(dim => details(`${dim} · ${DIMENSIONS[dim]} · ${llm.dimensions[dim].score} / 2`, [el("p", {}, llm.dimensions[dim].reasoning), note(`Self-reported confidence: ${llm.dimensions[dim].confidence}`), note(RUBRICS[dim])])), el("a", {href: `#report/hybrid/${encodeURIComponent(base.repo.replace("/", "_"))}/${encodeURIComponent(m.id)}`}, "Open full model report")]);
    })), card("Shared README evidence", [note("At most the first 12,000 characters are assessed. Linked documentation is not retrieved. Model confidence is self-reported, not a calibrated probability."), details("Inspect README snapshot", [el("pre", {class: "readme"}, base.readme?.slice(0, base.readme_limit) || "README snapshot unavailable")])]));
}
let languagesRequest = 0;
async function loadLanguages() {
  const request = ++languagesRequest;
  const target = $("languages-results");
  target.replaceChildren();
  showStatus($("languages-status"), "Loading programming languages…");
  try {
    const data = await getJson(`/api/languages?cohort=${encodeURIComponent($("language-cohort").value)}`);
    if (request !== languagesRequest) return;
    showStatus($("languages-status"), null);
    if (!data.total) { target.append(note("No saved repositories are available for this dataset.")); return; }
    target.append(el("div", {class: "summary-grid"}, [
      scoreCard("REPOSITORIES", data.total, null, "In the selected dataset"),
      scoreCard("PRIMARY LANGUAGES", data.language_count, null, "Distinct recorded language labels", "docs-accent"),
      scoreCard("UNKNOWN", data.unknown, null, "Repositories without recorded language metadata"),
    ]));
    const chart = el("div", {class: "language-chart"});
    const search = el("input", {type: "search", placeholder: "Search repositories…", "aria-label": "Search repositories by language"});
    const heading = el("h2");
    const count = el("p", {class: "note", "aria-live": "polite"});
    const list = el("div");
    let selected = null;
    function update() {
      const group = data.groups.find(group => group.language === selected);
      const repos = (group ? group.repositories : data.groups.flatMap(group => group.repositories))
        .filter(repo => repo.repo.toLowerCase().includes(search.value.trim().toLowerCase()))
        .sort((a, b) => a.repo.localeCompare(b.repo));
      heading.textContent = group ? `${group.language} repositories` : "All repositories";
      count.textContent = `${repos.length} repositories shown${group ? ` · ${group.percent}% of this dataset` : ""}.`;
      chart.querySelectorAll("button").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.language === selected)));
      all.setAttribute("aria-pressed", String(selected === null));
      list.replaceChildren(repos.length ? table(["Repository", "Report"], repos.map(repo => [repo.repo,
        el("a", {href: `#report/${data.cohort}/${encodeURIComponent(repo.id)}/${encodeURIComponent($("saved-model").value)}`}, "View report →"),
      ])) : note("No repositories match your search."));
    }
    const all = button("All languages", () => { selected = null; update(); });
    all.classList.add("language-all");
    const largest = Math.max(...data.groups.map(group => group.count));
    for (const group of data.groups) {
      const b = button("", () => { selected = group.language; update(); });
      b.classList.add("language-group");
      b.dataset.language = group.language;
      b.setAttribute("aria-label", `${group.language}: ${group.count} repositories, ${group.percent}%`);
      b.append(el("span", {class: "language-label"}, group.language),
        el("span", {class: "bar-track", "aria-hidden": "true"}, el("span", {class: "bar-fill", style: `width:${100 * group.count / largest}%`})),
        el("span", {class: "language-count"}, `${group.count} · ${group.percent}%`));
      chart.append(b);
    }
    search.addEventListener("input", update);
    target.append(el("div", {class: "two-column language-layout"}, [
      card("Language distribution", [note("Select a language to explore its repositories. Percentages use all repositories in the selected dataset."), all, chart]),
      el("section", {class: "card language-repositories"}, [heading, search, count, list]),
    ]));
    update();
  } catch (error) {
    if (request !== languagesRequest) return;
    showStatus($("languages-status"), error.message, true);
    $("languages-status").append(button("Retry", loadLanguages));
  }
}
let reportRequest = 0;
async function route() {
  const hash = location.hash.slice(1) || "overview", parts = hash.split("/");
  const view = ["report", "compare"].includes(parts[0]) ? "report" : ["assess", "languages"].includes(hash) ? hash : "overview";
  for (const name of ["overview", "assess", "report", "languages"]) $("view-" + name).hidden = name !== view;
  document.querySelectorAll(".nav-link").forEach(link => {
    const active = link.hash === `#${view === "report" ? "overview" : view}`;
    if (active) link.setAttribute("aria-current", "page"); else link.removeAttribute("aria-current");
  });
  const request = ++reportRequest;
  if (view === "overview") { loadOverview(); $("overview-title").focus({preventScroll: true}); }
  if (view === "assess") { $("assess-title").focus({preventScroll: true}); refreshModels(); }
  if (view === "languages") { loadLanguages(); $("languages-title").focus({preventScroll: true}); }
  if (view === "report") {
    $("report-results").replaceChildren(); showStatus($("report-status"), "Loading saved report…");
    try {
      if (parts[0] === "compare") {
        const data = await getJson(`/api/comparison/${encodeURIComponent(decodeURIComponent(parts[1] || ""))}`);
        if (request !== reportRequest) return;
        showStatus($("report-status"), null); renderComparison(data, $("report-results"));
        $("report-results").querySelector("h1").focus({preventScroll: true});
        return;
      }
      const data = await getJson(`/api/repositories/${encodeURIComponent(decodeURIComponent(parts[2] || ""))}?cohort=${encodeURIComponent(parts[1] || "")}&model=${encodeURIComponent(decodeURIComponent(parts[3] || LLAMA))}`);
      if (request !== reportRequest) return;
      showStatus($("report-status"), null); renderReport(data, $("report-results")); $("report-results").querySelector("h1").focus({preventScroll: true});
    } catch (error) {
      if (request !== reportRequest) return;
      showStatus($("report-status"), error.message, true); $("report-status").append(button("Retry", route));
    }
  }
  window.scrollTo(0, 0);
}
$("assess-form").addEventListener("submit", async event => {
  event.preventDefault();
  const repo = $("repo-input").value.trim(), runLlm = $("run-llm-checkbox").checked, model = $("live-model").value;
  if (!repo) return;
  $("assess-results").hidden = true;
  for (const control of $("assess-form").elements) control.disabled = true;
  $("assess-submit").textContent = "Assessing…"; $("assess-form").setAttribute("aria-busy", "true");
  const start = Date.now();
  const update = () => showStatus($("assess-status"), `${runLlm ? "Collecting evidence and assessing structural indicators and README documentation" : "Collecting evidence and assessing structural indicators"}… ${Math.floor((Date.now() - start) / 1000)}s elapsed. ${runLlm ? `${modelLabel(model)} may take several minutes.` : "Waiting for GitHub."}`);
  update(); const timer = setInterval(update, 1000);
  try {
    const data = await getJson("/api/assess", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({repo, run_llm: runLlm, model})});
    clearInterval(timer); showStatus($("assess-status"), null);
    renderReport(data, $("assess-results")); $("assess-results").hidden = false;
    if (!$("view-assess").hidden) $("assess-results").querySelector("h1").focus();
  } catch (error) { clearInterval(timer); showStatus($("assess-status"), error.message, true); }
  finally {
    clearInterval(timer); for (const control of $("assess-form").elements) control.disabled = false;
    $("assess-submit").textContent = "Assess repository"; $("assess-form").removeAttribute("aria-busy"); updateModelNote();
  }
});

let services = [];
let serviceRequest = 0;
function updateModelNote() {
  const model = $("live-model").value, enabled = $("run-llm-checkbox").checked;
  $("live-model").disabled = !enabled || $("assess-form").getAttribute("aria-busy") === "true";
  $("model-service-note").textContent = !enabled ? "Only structural indicators will be assessed." : model === QWEN ? "The repository name and up to 12,000 characters of README text are sent to the university KISTE service. Assessment may take several minutes." : "README documentation is assessed locally through Ollama. Assessment may take several minutes.";
  const service = services.find(s => s.id === model);
  $("model-service-status").textContent = enabled ? `${modelLabel(model)}: ${service?.status || "Availability not checked"}.` : "Documentation assessment is off.";
}
async function refreshModels() {
  const request = ++serviceRequest;
  $("model-service-status").textContent = "Checking model services…";
  try { const data = await getJson("/api/models"); if (request !== serviceRequest) return; services = data; updateModelNote(); }
  catch { if (request === serviceRequest) $("model-service-status").textContent = "Could not check services. You can retry the check or assessment."; }
}
$("saved-model").addEventListener("change", () => { overviewData = null; loadOverview(); });
$("language-cohort").addEventListener("change", loadLanguages);
$("live-model").addEventListener("change", updateModelNote);
$("run-llm-checkbox").addEventListener("change", updateModelNote);
$("refresh-models").addEventListener("click", refreshModels);
updateModelNote();
window.addEventListener("hashchange", route);
route();
