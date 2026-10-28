repo_id: scikit-learn/scikit-learn
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: pip and conda install commands plus dependency prerequisites and link to fuller install docs.

D2_usage:               1  confidence: MEDIUM
D2_notes: No end-user modeling example in the README; only install/testing commands. Usage deferred to website documentation.

D3_purpose:             2  confidence: HIGH
D3_notes: States Python machine-learning module built on SciPy under BSD; purpose is clear.

D4_dependencies:        2  confidence: HIGH
D4_notes: Explicit required packages with minimum versions (Python, NumPy, SciPy, Narwhals, joblib, threadpoolctl) plus optional plotting deps.

D5_examples:            1  confidence: MEDIUM
D5_notes: Documentation links present but README does not include an inline working ML example or explicitly label a tutorials/examples gallery.

D6_contribution:        2  confidence: HIGH
D6_notes: Development/Contributing/PR sections with contributing guide links plus issues, discussions, Discord, mailing list, and Stack Overflow.

exclusion_reason:
general_notes: F1 from Zenodo DOI badge. F2 from CITATION.cff. A1 from COPYING. R2=1 from "we would appreciate citations" with link to citing page (not from CITATION.cff alone).
