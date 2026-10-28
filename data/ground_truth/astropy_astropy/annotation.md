repo_id: astropy/astropy
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    1
F2_metadata_file:    1
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         1

# AI-based
D1_installation:     1   confidence: MEDIUM
D1_notes: Inline pip command present but no Python version or prerequisites listed. Links to external install guide.

D2_usage:            1   confidence: MEDIUM
D2_notes: No inline usage examples. Links to documentation present but nothing actionable in README.

D3_purpose:          2   confidence: MEDIUM
D3_notes: Core purpose clear — single core package for astronomy in Python. Interoperability goal is jargon-heavy but overall scope understandable.

D4_dependencies:     0   confidence: MEDIUM
D4_notes: No dependency or environment information in README text. Python versions badge present but not human-readable text.

D5_examples:         1   confidence: MEDIUM
D5_notes: Tutorial linked in documentation but no inline examples or code snippets in README. External link is accessible but nothing 
actionable without leaving the README.
D6_contribution:     2   confidence: HIGH
D6_notes: Full contribution process described, CONTRIBUTING.md linked, multiple community channels present.

exclusion_reason:
general_notes: Perfect rule-based score (all 1s) but weak AI-based scores. Strongest example yet of rule-based vs AI-based divergence. F-UJI would rate this highly but README inline content is thin.