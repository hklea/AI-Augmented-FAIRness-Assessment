repo_id: nilearn/nilearn
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Step-by-step venv/conda environment setup, pip install, Windows activate note, and import check.

D2_usage:               1  confidence: MEDIUM
D2_notes: Only an import check after install; no concrete analysis/API usage example. Points to HTML documentation.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of brain volume/surface analysis with GLM and scikit-learn-based multivariate tools.

D4_dependencies:        1  confidence: HIGH
D4_notes: Required deps deferred to pyproject.toml; some optional packaging notes (matplotlib, plotly/kaleido, pytest) explained partially.

D5_examples:            1  confidence: MEDIUM
D5_notes: Stable HTML documentation linked; README does not explicitly point to a tutorial/examples gallery or include an inline example.

D6_contribution:        2  confidence: HIGH
D6_notes: Development section links detailed contribution guide; drop-in hours, Discord/social channels, and help docs also provided.

exclusion_reason:
general_notes: Zenodo DOI badge gives F1=1. CITATION.cff gives F2=1 but not R2. R2=0 — DOI badge only, no please-cite wording and no CITATION.md/bib/txt/plain CITATION.
