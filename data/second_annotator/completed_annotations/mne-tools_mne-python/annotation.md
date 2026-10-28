repo_id: mne-tools/mne-python
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: pip install command plus link to a fuller installation guide covering standalone installers and advanced methods.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete usage example in the README; usage is deferred to documentation that includes tutorials and examples.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of MEG/EEG/sEEG/ECoG analysis, visualization, source estimation, and related neurophysiology workflows.

D4_dependencies:        2  confidence: HIGH
D4_notes: Explicit core dependency list with minimum versions (Python, NumPy, SciPy, Matplotlib, and others) in the README.

D5_examples:            2  confidence: HIGH
D5_notes: Documentation is described as encompassing tutorials and examples and is linked from the README.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.md present; README links contributing guidelines, user forum, and GitHub issue tracker.

exclusion_reason:
general_notes: Zenodo DOI gives F1=1. CITATION.cff and codemeta.json give F2=1. R2=0 — DOI badge and CITATION.cff alone do not satisfy R2; no explicit please-cite wording or CITATION.md/bib/txt.
