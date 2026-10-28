repo_id: scikit-learn/scikit-learn
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    1
F2_metadata_file:    1
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         1

# AI-based
D1_installation:     2   confidence: HIGH
D1_notes: Explicit pip and conda installation commands provided. Detailed installation guide linked. Users can install directly from README.

D2_usage:            1   confidence: MEDIUM
D2_notes: No ML usage example or code snippet. Development commands present (git clone, pytest) but not end-user usage examples.

D3_purpose:          2   confidence: HIGH
D3_notes: Purpose clearly stated — machine learning library for Python built on SciPy. Scope and audience immediately understandable.

D4_dependencies:     2   confidence: HIGH
D4_notes: Core dependencies listed with minimum versions — Python, NumPy, SciPy, Narwhals, joblib and threadpoolctl. Optional dependencies such as Matplotlib, scikit-image, pandas, seaborn and Plotly are also listed.

D5_examples:         1   confidence: MEDIUM
D5_notes: Documentation and example ecosystem referenced but no worked ML examples directly in README.

D6_contribution:     2   confidence: HIGH
D6_notes: Contribution process described, help links present, community channels referenced.

exclusion_reason:
general_notes: Perfect rule-based score. A1 required manual check — license file named COPYING not LICENSE. Strong installation docs but no inline usage examples. Guidelines updated to v1.3 for COPYING edge case.