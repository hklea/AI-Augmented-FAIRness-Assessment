repo_id: healpy/healpy
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    1
F2_metadata_file:    0
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         1

# AI-based
D1_installation:     2   confidence: HIGH
D1_notes: Inline pip command present, Python versions explicitly listed, references INSTALL.rst for further details.

D2_usage:            1   confidence: MEDIUM
D2_notes: Tutorial and mybinder links present but no inline usage examples or code snippets.

D3_purpose:          2   confidence: HIGH
D3_notes: Purpose and domain clearly stated. Non-specialist can understand scope even without astrophysics background.

D4_dependencies:     2   confidence: HIGH
D4_notes: Python versions explicitly listed with ranges, Numpy minimum version specified, Matplotlib and Astropy named.

D5_examples:         2   confidence: HIGH
D5_notes: Live mybinder notebook available, tutorial link present and accessible.

D6_contribution:     2   confidence: HIGH
D6_notes: Contribution process described, GitHub issues linked, StackOverflow tag, core developers listed.

exclusion_reason:
general_notes: License file named COPYING — detected after collector updated in v1.3. F2=0 despite CITATION file being present — plain CITATION counts for R2 only, not F2 which requires structured metadata like CITATION.cff.