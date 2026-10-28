# AI-Augmented FAIRness Assessment of Research Software: A Hybrid Approach

This repository contains the implementation, datasets, evaluation results, and LaTeX sources for Klea Haxhiu's Master's thesis at TU Chemnitz.

- **Author:** Klea Haxhiu
- **Supervisor:** Dr. Sheeba Samuel
- **Institution:** TU Chemnitz

The project investigates how automated structural checks and large
language model (LLM)-based documentation assessment can jointly assess
research software against selected indicators derived from the FAIR4RS
principles: Findability, Accessibility, Interoperability, and
Reusability. Rule-based checks examine repository files and metadata,
while the LLM component evaluates qualitative characteristics of README
documentation. The implementation supports Llama 3.1 8B through local
Ollama and Qwen3.6-35B-A3B-MLX-8bit through the university KISTE
service. Their outputs are retained alongside the structural assessment
in per-repository hybrid profiles and evaluated against human
annotations.

This is a research prototype for assessing documented evidence. Its indicators do not constitute a complete FAIR4RS compliance assessment.

## Assessment approach

| Component | Indicators | Scale |
| --- | --- | --- |
| Rule-based assessment | F1: persistent identifier; F2: structured metadata; A1: license; I1: dependency specification; R1: README presence; R2: citation information | Binary scores, total 0–6 |
| LLM assessment | D1: installation clarity; D2: usage clarity; D3: purpose description; D4: dependency description; D5: examples and tutorials; D6: contribution information | Scores of 0–2, total 0–12 |
| Hybrid profile | Matched rule-based and LLM results, including reasoning, confidence labels, and model information | Both sets of scores retained separately |

The LLM runner uses `llama3.1:8b` through a local Ollama API, with temperature set to `0` and a structured JSON output schema. It evaluates only the supplied README text, truncated to the first 12,000 characters, and does not retrieve linked documentation. Each dimension includes a score, a `HIGH`/`MEDIUM`/`LOW` confidence label, and supporting reasoning. A second runner, `run_llm_ground_truth_qwen.py`, evaluates `Qwen3.6-35B-A3B-MLX-8bit` through university KISTE using the same input length limit and temperature 0. Its prompt requests JSON and its parser validates the response; it does not use Ollama schema enforcement. Both models have saved results for the 30 annotated repositories.

The scoring rubric and edge cases are documented in the [annotation guidelines](docs/annotation_guidelines.md).

## Data and results

- **188 research software repositories** form the full dataset, collected through GitHub searches across 10 research topics and assessed with the rule-based scorer.
- **30 manually annotated repositories** form the ground-truth evaluation set, with README snapshots, metadata, file inventories, and annotations from two annotators.
- **20-repository pilot-exclusion sensitivity analyses** exclude the 10 pilot repositories used during development.
- Saved results include rule-based scores, LLM scores, hybrid profiles, human agreement analyses, precision/recall/F1, confidence calibration, and README verbosity analysis.

The ground-truth snapshots and evaluation results are included in the repository. Full-dataset raw snapshots under `data/raw/` are ignored by Git and must be collected separately to rerun full-dataset scoring. Recollection uses live GitHub data and may produce a different dataset from the original study.

## Repository structure

```text
code/
  requirements.txt             Python dependencies
  src/
    collection/                GitHub collection, filtering, and snapshot scripts
    rule_based/scorer.py       Binary indicator scorer
    ai_based/                  LLM prompts and scoring runners
    hybrid_profile.py          Merge rule-based and Llama results
    hybrid_profile_qwen.py     Merge rule-based and Qwen results
    compute_*.py               Evaluation and diagnostic analyses
    llm_human_agreement.py     Compare LLM scores with human annotations
  web/
    backend/                  FastAPI endpoints and saved/live assessment logic
    frontend/                 HTML, CSS, and JavaScript interface
    tests/                    Backend tests and browser smoke test
data/
  ground_truth/                30 repository snapshots and primary annotations
  second_annotator/            Guidelines, blank templates, completed annotations
  results/                    Score CSVs, LLM responses, and evaluation outputs
  raw/                        Locally collected full dataset (not tracked)
docs/                         Methodology, experiment notes, and result summaries
thesis/                       LaTeX sources, bibliography, and figures
```

## Setup

Use Python 3.12 to match the existing development environment. Run the following commands from the repository root.

Create a virtual environment:

```sh
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Install the pinned dependencies:

```sh
python -m pip install -r code/requirements.txt
```

The dependencies include `requests` for HTTP requests, `python-dotenv` for configuration, `scikit-learn` for agreement cross-checks, `scipy` for statistical analysis, `fastapi` and `uvicorn` for the web app, and `openai` for the KISTE-compatible client. The rule-based scorer itself uses only the Python standard library.

Ollama is needed for new Llama scores; new Qwen scores use the university KISTE service with a server-side `KISTE_API_TOKEN`. A GitHub token is needed for the full-dataset collection workflow. Saved scores can be analyzed without either service.

## Run the assessment

### 1. Score the included ground-truth snapshots

```sh
python code/src/rule_based/scorer.py --input data/ground_truth --output data/results/rule_based_scores_ground_truth.csv
```

The scorer expects one directory per repository, containing `metadata.json` and `fair_file_checks.json`, together with a README when available. Incomplete snapshot directories are skipped. The output contains one row per scored repository, six indicator scores, and `rule_based_total`.

Use `--output` to choose a different destination when comparing runs. The command above replaces the corresponding saved score CSV.

### 2. Generate LLM scores (optional)

With Ollama installed, download the model:

```sh
ollama pull llama3.1:8b
```

Ensure Ollama is serving at `http://localhost:11434`. If it is not already running, start it in a separate terminal:

```sh
ollama serve
```

Then run:

```sh
python code/src/ai_based/run_llm_ground_truth.py
```

The runner reads `data/ground_truth/` and saves:

- `data/results/llm_scores_ground_truth.csv`: scores, confidence labels, reasoning, model, and timestamps.
- `data/results/raw_llm/llama3.1_8b/`: raw model responses.
- `data/results/parsed_llm/llama3.1_8b/`: validated per-repository JSON results.

The runner skips repositories with existing parsed JSON results and appends newly generated rows to the CSV. With the included results, it may skip every repository. For a fresh experiment, configure separate CSV, raw-response, and parsed-response output paths in the script before running it; changing only the CSV path does not bypass the parsed-result cache. Model and truncation settings are also defined in the script.

For Qwen, set the university token in the environment or in the repository-root `.env` file:

```dotenv
KISTE_API_TOKEN=your_university_token
```

Then run:

```sh
python code/src/ai_based/run_llm_ground_truth_qwen.py
```

This runner reads the same ground-truth snapshots and writes `data/results/llm_scores_ground_truth_Qwen3.6-35B-A3B-MLX-8bit.csv`. Raw and parsed responses are stored under `data/results/raw_llm/Qwen3.6-35B-A3B-MLX-8bit/` and `data/results/parsed_llm/Qwen3.6-35B-A3B-MLX-8bit/`. It uses the same parsed-result skip mechanism and CSV append behavior as the Llama runner; use separate output paths for fresh experiments. Both runners save nonempty response text per attempt, including responses that fail validation.

### 3. Build hybrid profiles

Using the saved or regenerated ground-truth scores:

```sh
python code/src/hybrid_profile.py
```

This joins `rule_based_scores_ground_truth.csv` and `llm_scores_ground_truth.csv` by repository name and writes `data/results/hybrid_fairness_profiles_ground_truth.csv`. Only repositories present in both inputs are included.

Build the corresponding Qwen profiles with:

```sh
python code/src/hybrid_profile_qwen.py
```

The Qwen merger uses the same structural score CSV and the Qwen-specific LLM CSV, writing `data/results/hybrid_fairness_profiles_ground_truth_Qwen3.6-35B-A3B-MLX-8bit.csv`. Both commands replace their respective hybrid CSVs and retain structural and documentation totals separately.

### 4. Reproduce evaluation analyses

These commands use the included annotations and score CSVs. They write their corresponding reports to `data/results/`, replacing existing reports.

| Command | Analysis |
| --- | --- |
| `python code/src/compute_kappa.py` | Agreement between the two human annotators |
| `python code/src/compute_kappa.py --diagnostics` | Human agreement with contingency tables and disagreement details |
| `python code/src/compute_rule_based_prf.py` | Rule-based precision, recall, and F1 for the full ground-truth set and holdout |
| `python code/src/llm_human_agreement.py --model llama3.1:8b` | Llama agreement with both annotators and a pilot-exclusion comparison |
| `python code/src/llm_human_agreement.py --model Qwen3.6-35B-A3B-MLX-8bit` | Qwen agreement with both annotators and a pilot-exclusion comparison |
| `python code/src/compute_confidence_calibration.py` | Relationship between Llama confidence labels and agreement |
| `python code/src/compute_confidence_calibration_qwen.py` | Relationship between Qwen confidence labels and agreement |
| `python code/src/compute_verbosity_bias.py` | Relationship between README length and Llama scoring behavior |
| `python code/src/compute_verbosity_bias_qwen.py` | Relationship between README length and Qwen scoring behavior |

These saved-result analyses require neither Ollama nor a KISTE token. The agreement script requires an explicit `--model` argument and writes separate reports for each model.

### 5. Reproduce structural–documentation correlations

To reproduce the thesis's Spearman correlations, start `python` from the repository root and paste the following code. It reads the saved hybrid CSVs and prints results without modifying them:

```python
import csv
from pathlib import Path
from scipy.stats import spearmanr

models = {
    "Llama": "",
    "Qwen": "_Qwen3.6-35B-A3B-MLX-8bit",
}
for model, suffix in models.items():
    path = Path("data/results") / f"hybrid_fairness_profiles_ground_truth{suffix}.csv"
    with path.open(encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    structural = [int(row["rule_based_total"]) for row in rows]
    documentation = [int(row["llm_total"]) for row in rows]
    rho, p_value = spearmanr(structural, documentation)
    print(f"{model}: n={len(rows)}, rho={rho:.3f}, p={p_value:.3f}")

```

For the saved 30-repository profiles, Llama yields `rho=0.175, p=0.356` and Qwen yields `rho=0.134, p=0.480`. Both associations are weak and not statistically significant; this does not establish independence between the assessment components. This analysis compares structural and documentation totals, unlike the README-length analysis above.

## Web demo

The FastAPI + vanilla-JS web app supports saved Llama/Qwen results, model comparison, and live assessment of public GitHub repositories.

Install the project requirements (including `fastapi`, `uvicorn`, and `openai`), then start the app:

```sh
python -m pip install -r code/requirements.txt
python code/web/backend/main.py
```

Open `http://127.0.0.1:8000`.

- **Saved documentation model:** choose Llama 3.1 8B or Qwen3.6 35B. The overview, repository documentation scores, and confidence analysis all use that model's saved CSVs. Structural results remain independent of the model selection.
- **Programming languages:** browse either cohort grouped by its primary language in the saved GitHub metadata. Each repository appears once; missing language metadata is shown as **Unknown**. Full-dataset language information requires the local snapshots under `data/raw/`.
- **View report:** inspect scores, model explanations, confidence, rubric, README evidence, and timestamp. Model-specific report links preserve the chosen model; older links without a model still open Llama results.
- **Compare models:** open a repository's saved Llama and Qwen scores side by side with either annotator's reference scores. Differences are highlighted, with expandable explanations and a shared structural assessment. This view does not run inference.
- **Compare model agreement with humans:** inspect macro-average and per-dimension weighted Kappa, exact agreement, and MAE. Select either annotator and the full corpus or pilot-exclusion subset. Metrics are computed from saved agreement rows on repositories present in both model runs. Undefined values appear as unavailable. A higher documentation score is not evidence of better model performance.
- **Assess a repository:** optionally choose Llama through local Ollama or Qwen through university KISTE. The form shows service status and where README text is processed. Ollama readiness checks whether the configured model is installed; KISTE status checks server configuration only, with connectivity tested during assessment.

For live Llama scoring, start Ollama and install `llama3.1:8b`. For live Qwen scoring, configure the following in the server environment or root `.env` file, then restart the app:

```dotenv
KISTE_API_TOKEN=your_university_token
```

The token stays on the backend. Qwen assessment sends the repository name and up to the first 12,000 README characters to `https://kiste.informatik.tu-chemnitz.de/v1`. The web backend reuses each model's existing batch prompt and response parser, followed by validation of all six dimensions. Saved views work without GitHub, Ollama, or KISTE connectivity. Live assessments require GitHub access; `GITHUB_TOKEN` remains optional for increased API limits.

Saved Llama files retain their original filenames; Qwen files use the `_Qwen3.6-35B-A3B-MLX-8bit` suffix. Both models currently cover 30 repositories. The full dataset contains 188 structural assessments and does not inherit documentation scores from other snapshots.

Live assessments never modify thesis results. Failed GitHub evidence requests stop assessment; a documentation-service failure preserves structural results and displays **Not assessed** with a service-specific message. README scoring is limited to 12,000 characters and does not retrieve linked documentation. Confidence is self-reported, not a calibrated probability. Saved explanations are cleaned for terminal formatting artifacts at display time; original CSVs remain unchanged.

For a defense walkthrough, open `http://127.0.0.1:8000/#compare/astropy_astropy`: its saved structural score is 6/6, while Llama gives 4/12 and Qwen 5/12. Inspect per-dimension differences against the human reference. **Print comparison** and **Print report** print the current view; expand explanations you want included first. Preview screenshots are in [docs/ui](docs/ui).

Run backend regression checks without external services:

```sh
python -m unittest discover -s code/web/tests -v
```

The optional `code/web/tests/browser_smoke.mjs` uses Node 22+ and an isolated Chrome instance with remote debugging on port 9223. It expects the app on port 8765 (override with `UI_BASE_URL`), checks model switching, comparison, annotator/subset filters, report provenance, search, mobile layout, and failure states, and refreshes preview screenshots. Inference responses are mocked in tests; the checks do not execute real Llama or KISTE inference.

## Collect and score the full dataset

Set `GITHUB_TOKEN` in the environment or add it to a `.env` file at the repository root:

```dotenv
GITHUB_TOKEN=your_github_token
```

The `.env` file is ignored by Git. Collection topics, repository limits, minimum stars, and the activity cutoff are defined in [config.py](code/src/collection/config.py); filtering logic is in [filters.py](code/src/collection/filters.py).

Collect repository metadata:

```sh
python code/src/collection/full_collector.py
```

This writes timestamped `full_dataset_*.json` and `.csv` files under `data/raw/`. Pass the generated JSON filename to the cleaning script, replacing the example timestamp below:

```sh
python code/src/collection/clean_dataset.py data/raw/full_dataset_YYYYMMDD_HHMMSS.json
python code/src/collection/fetch_full_dataset.py
python code/src/rule_based/scorer.py --input data/raw --output data/results/rule_based_scores_full.csv
```

The cleaning step produces `data/raw/cleaned_dataset.json`, which the snapshot fetcher reads to download READMEs, metadata, and file inventories. These collection steps require network access and are subject to GitHub API rate limits.

## Thesis PDF

The thesis is auto-compiled via GitLab CI on every change to `thesis/`. Download the latest built version from the `main` branch here:

**[📄 Latest Thesis PDF](https://gitlab.hrz.tu-chemnitz.de/vsr/edu/advising/ma-klea-haxhiu/-/jobs/artifacts/main/raw/thesis/main.pdf?job=build-thesis)**

View the source code and build pipelines in the [GitLab project](https://gitlab.hrz.tu-chemnitz.de/vsr/edu/advising/ma-klea-haxhiu).

## Build the thesis

Install a LaTeX distribution with PDFLaTeX, BibTeX, and `latexmk`, including the packages used by `thesis/main.tex`. From the repository root:

```sh
cd thesis
latexmk -pdf -interaction=nonstopmode -file-line-error main.tex
```

The output is `thesis/main.pdf`. The GitLab CI configuration runs the thesis build when files under `thesis/` change; its runner must provide the LaTeX tools.

## Further documentation

- [Dataset selection criteria](docs/dataset_selection_criteria.md) and [dataset summary](docs/dataset_summary.md)
- [Annotation guidelines](docs/annotation_guidelines.md) and [second-annotator instructions](data/second_annotator/README.md)
- [Rule-based validation](docs/rule_based_validation.md) and [full-dataset results](docs/rule_based_full_dataset_results.md)
- [LLM prompt design](docs/llm_prompt_design.md) and [experiment notes](docs/llm_experiments.md)
- [Inter-annotator agreement](docs/inter_annotator_agreement.md) and [LLM–human agreement](docs/llm_human_agreement.md)
- [howfairis comparison](docs/howfairis_comparison.md) and [F-UJI baseline](docs/fuji_baseline.md)

Interpret scores alongside the rubric and evaluation results: README truncation, external-link handling, snapshot coverage, and model behavior can affect the assessment. LLM confidence labels are self-reported categories, not calibrated probabilities.
