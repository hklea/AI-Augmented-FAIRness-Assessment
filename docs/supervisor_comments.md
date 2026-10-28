# Supervisor Notes

## Tool Identity & Usability

You can give the tool a name.
Then can be installed and used it to check single repo.
e.g.
```
pip install <tool-name>
<tool-name> <repo_link>
```

- CLI-based 
- web portal (if time is there)
- Single repo checking and bulk checking
- GitHub 
- Docker container for reproducible deploymen
- See also: https://github.com/fair-software/howfairis/

---

## What Must Be Done for a strong thesis

The core claim is: a hybrid rule-based + LLM approach assesses research software
FAIRness better than rule-based tools alone. 

---

### 1. Scale Up the Dataset

- Annotate the full 30-repo ground truth set as planned in the thesis timeline.
- For a paper, aim for **50–100 repos** with full manual annotations.
- Ensure **domain diversity**: currently all repos are Python scientific computing
  (astropy, numpy, biopython, networkx, etc.). Make sure there are repos from other domains and programming languages: 
  can limits generalizability claims.
- Apply the existing inclusion/exclusion criteria consistently.
- Log every exclusion with a reason for transparency.

---

### 2. Inter-Annotator Agreement — Second Annotator Required 

Examiner/reviewer will ask how reliable is the ground truth?

- You can have a second annotator for a **random sample of at least 20 repos**
  (ideally the full 30-repo ground truth batch).
- Compute **Cohen's Kappa** (weighted Kappa for the 0–2 AI dimensions,
  unweighted for binary rule-based dimensions).
- Target: Kappa ≥ 0.60 (substantial agreement). Report per-dimension Kappa,
  not just overall.
- If Kappa is below 0.60 on any dimension, revise the rubric definition for
  that dimension and re-annotate.
- Resolve disagreements using a discussion protocol; document the outcome.
- This is the methodological prerequisite for using
  the annotations as ground truth in any quantitative evaluation.

---

### 3. Proper Evaluation Metrics 

Current state: evaluation uses % exact agreement between LLM and human.

For each rubric dimension (D1–D6), report:
- **Cohen's Kappa** (weighted, to account for ordinal 0–2 scale)
- **Exact agreement %** (already computed — keep as secondary metric)
- **Mean Absolute Error** (MAE) per dimension
- For binary rule-based dimensions: **Precision, Recall, F1** vs. manual ground truth

Overall:
- **Macro-averaged Kappa** across all 12 dimensions (6 rule-based + 6 AI)
- **Score correlation** between rule-based total and AI total (Spearman's ρ)
  — this is the quantitative form of pilot Finding 1 (scores are not strongly correlated)
- **Statistical significance** where appropriate (Wilcoxon signed-rank test for
  paired comparisons between system variants or LLM models)

---

### 4. LLM Model Comparison 
The literature (Dvivedi et al. 2024, Zheng et al. 2023) consistently shows
closed-source and larger models outperform small open-source models. Examiner can ask: does this result hold with a better model?

Minimum comparison set (choose based on resources):
- **llama3.1:8b** (baseline — already done)
- **llama3.1:70b** (same architecture, 9× larger — test if scale alone helps)
- **GPT-4o-mini or Claude Haiku** (capable, low-cost closed-source model)

Report per model:
- Cohen's Kappa vs. human ground truth per dimension
- Output stability (variance across repeated runs on same repo)
- Token cost and runtime (for the tool feasibility argument)

This comparison directly answers whether the 58.3% agreement rate is a
**model limitation** (as pilot experiments suggest) or a **task limitation**.
If GPT-4 class models reach 75–80% Kappa, the finding is that model choice
matters enormously. If they don't, the finding is that README-level scoring
is inherently hard for LLMs 

---

### 5. F-UJI Baseline Comparison (Critical)

Current state: F-UJI is described as a baseline comparator in the literature
notes but no comparison has been run.

- Run F-UJI on all repos in the ground truth set (or on repos with persistent
  identifiers that F-UJI can accept).
- Compare F-UJI scores against: (a) manual ground truth, (b) rule-based scorer,
  (c) hybrid system output.
- If F-UJI cannot accept GitHub URLs directly (a known limitation noted in the
  literature), document this and use it as concrete evidence for why a
  GitHub-native tool is needed.
- The comparison table is the central result of the paper.

---

### 6. howfairis Comparison


- Run howfairis (https://github.com/fair-software/howfairis/) on repos.
- Compare howfairis binary outputs against the rule-based scorer output for
  the overlapping dimensions (license, README, citation).
- Identify any repos where the two tools disagree — these are the most
  interesting cases (e.g., LICENSE.rst false negative that the pilot already
  found).
- This positions the tool relative to the most widely used existing tool
  in this space.

---

### 7. Verbosity Bias Analysis 

- Compute README length (word count, or token count) for all repos.
- Test whether LLM scores correlate with README length independently of
  human scores: run a Spearman correlation between (LLM score − human score)
  and README length.
- If significant positive correlation exists, the LLM is exhibiting verbosity
  bias: longer READMEs receive inflated scores regardless of quality.
- Report this as a known limitation and discuss the mitigation (rubric-based
  prompting partially corrects this per Zheng et al.).

---

### 8. Uncertainty / Confidence Calibration

Current state: the LLM outputs HIGH/MEDIUM/LOW confidence flags per dimension,
and the annotation guidelines define confidence flags for human annotations.
But neither is validated — we do not know if HIGH actually predicts accuracy.

- For the LLM: compute accuracy (Kappa) separately for HIGH, MEDIUM, and LOW
  confidence outputs. If HIGH confidence scores are more accurate than LOW,
  the flags are calibrated and useful.
- For human annotations: check whether MEDIUM/LOW confidence annotations have
  higher disagreement with the second annotator than HIGH confidence ones.
- A calibrated confidence flag turns the system from a score generator into
  a triage tool: HIGH confidence scores can be trusted, LOW scores should be
  reviewed. This is a usable, practical contribution.

---

### 9. Score Combination / Hybrid Layer (Core Contribution)

Current state: rule-based and AI-based scores are separate outputs.
The "hybrid" in the thesis title is not yet implemented as a combined output.

- Implement a principled combination layer. Options (pick one and justify):
  - **Concatenated profile**: present both score vectors side by side with
    no arithmetic combination (clean, transparent, avoids false precision).
    This is probably the right choice for a thesis.
  - **Weighted sum**: define weights for each dimension based on FAIR4RS
    compliance levels (Essential / Important / Useful from FAIR-IMPACT D5.2).
  - **Decision rule**: flag as "at-risk" any repo with rule_based_total < 4
    OR any AI dimension ≤ 1 on D1/D2 (critical usability dimensions).
- Whatever is chosen, report whether the hybrid output predicts adoption or
  reuse better than either component alone. This requires an external validity
  signal (e.g., GitHub stars, citation count, or practitioner survey).

--

### 10. Output Stability / Repeated Run Analysis

- Run each repo through the LLM **3–5 times** with the same prompt.
- Compute standard deviation of score per dimension across runs.
- Dimensions with σ > 0.5 are flagged as inherently unstable for this model.
- Report the **instability profile** per dimension.
- Use this to justify the confidence flag: if a dimension is stable across
  runs, confidence is HIGH; if it varies by ≥1 point across runs, flag LOW
  and recommend human review.

---

### 11. Replication Package

Prepare:
- All collected data (READMEs, metadata.json, fair_file_checks.json) for the
  full ground truth set
- All manual annotation files (annotation.md per repo).
- The full prompt (v1.2 as selected final prompt) in a standalone file.
- The rule-based scorer and LLM scorer code with dependencies pinned
  (requirements.txt with exact versions).
- A README for the replication package explaining how to reproduce each
  result table in the paper.

---

### 14. Research Questions — State and Answer Explicitly

The thesis must state 2–3 RQs and answer each with a number.
Example RQs based on the current work:

**RQ1**: To what extent do automated rule-based FAIR indicators agree with
qualitative documentation quality assessment for research software repositories?
→ Answer: Spearman correlation between rule_based_total and AI total across N repos.

**RQ2**: How reliably can a locally-deployed LLM score README documentation
quality against a structured FAIR4RS rubric?
→ Answer: Cohen's Kappa per dimension, output instability σ per dimension.

**RQ3**: Does a hybrid rule-based + LLM approach identify FAIRness gaps that
existing tools (F-UJI, howfairis) miss?
→ Answer: cases where rule-based score is high but LLM score is low (e.g., astropy),
  and cases where the hybrid system catches a gap the existing tools do not.

---

---

## Check this recent Fair-Way Paper (CIKM 2025) 

DOI: 10.1145/3746252.3760811

This paper is the closest related work and **must be cited** in the thesis. The thesis must clearly differentiate itself from Fair-Way.

---

### What Fair-Way Does

Fair-Way is an open-source LLM-based tool for automatic FAIR assessment.
Key design choices:

- **Scope:** FAIR assessment of **datasets** (structured and unstructured
  metadata from Zenodo, etc.), using the FAIRsFAIR DOAM metrics (v0.5).
  Not specific to research software.
- **Architecture:** VueJS frontend + FastAPI backend + Ollama or OpenAI
  LLM interface. Divide-and-conquer: chunks metadata via LangChain, processes
  each chunk with a tailored prompt, synthesises results.
- **Prompt engineering:** Specific Instructions + Structured Output (JSON
  schema enforcement) + Chain-of-Thought sequential subtasks + Two-Shot
  Prompting (2 examples per test) + Special Prompts for multi-chunk synthesis.
- **LLM comparison (Table 2 in paper):** GPT-4o is best overall (Exact Match
  Accuracy 0.905). Mistral-Small is the best open-source model (Exact Match
  0.84). llama3.3 at temp 0.5 scored only 0.603 exact match — significantly
  weaker. Qwen2.5-Coder: 0.778.
- **Benchmark (Table 3):** Fair-Way outperforms F-UJI on 10-11/12 metrics vs
  8-9/12 for F-UJI, across Earth Sciences, Finance, and Climate Science datasets.
- **Limitations (explicitly stated in paper):** purely LLM-based approach has
  hallucination risk; common metrics could be verified with explicit logic
  (they flag a hybrid approach as future work); GPU requirements for strong
  models.

---


These are concrete technical improvements the thesis can adopt:

**A. Two-Shot Prompting**
Fair-Way found 2 examples per test to be the optimal balance between context
size and output quality. The current thesis prompt uses zero examples.
Add 2 worked examples (one score-2 case, one score-0 case) to the LLM prompt
for at least D1 and D2 — the dimensions with the highest instability — and
measure whether this reduces variance across repeated runs.

**B. Chain-of-Thought Decomposition**
Fair-Way decomposes each FAIR test into sequential subtasks with intermediate
JSON outputs. The current prompt asks the LLM to score all 6 dimensions in a
single call. Consider splitting into per-dimension calls, asking the LLM to:
(1) identify relevant evidence in the README, (2) assess against the rubric
criterion, (3) output a score. This increases token usage but reduces
instability (supported by Zheng et al. 2023 CoT finding).

**C. Temperature Testing**
Fair-Way varied temperature 0.3–0.9 and found lower temperatures better for
most models. The current experiments use Ollama's default temperature (likely
0.8). Run temperature ablation at 0.0, 0.3, 0.5 on the 4 pilot repos already
scored. Report the optimal temperature setting.

**D. Mistral-Small as Open-Source Alternative**
Fair-Way shows Mistral-Small outperforms llama3.3 and Qwen2.5-Coder on FAIR
assessment. Include Mistral-Small in the LLM
model comparison.

**E. README Chunking for Long Inputs**
Fair-Way chunks large metadata files when they would exceed the LLM context
window. Several pilot READMEs (numpy, scikit-learn) are very long. Implement
chunking: split README by section headings, score relevant sections, synthesise.
Measure whether chunking changes scores for long READMEs vs. passing full text.

**F. Mean BERT Score as an Evaluation Metric**
Fair-Way uses BERT Score to evaluate the quality of LLM reasoning text (the
"reasoning" field in each dimension's output). Add BERT Score evaluation of
LLM reasoning against human annotation notes — this gives a metric for
reasoning quality beyond score agreement, and aligns with Fair-Way's evaluation
for comparability.

---

