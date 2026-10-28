repo_id: fieldtrip/fieldtrip
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 0
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Clear installation steps — clone/download, add to MATLAB path, call ft_defaults. Inline commands provided.

D2_usage: 1     confidence: MEDIUM
D2_notes: No inline usage examples. Links to external website for documentation and tutorials.

D3_purpose: 2     confidence: HIGH
D3_notes: Purpose clearly stated — MATLAB toolbox for MEG/EEG/iEEG analysis. Analysis methods listed explicitly.

D4_dependencies: 1     confidence: MEDIUM
D4_notes: MATLAB required but not explicitly stated. External toolboxes mentioned but not listed. No version requirements given.

D5_examples: 1     confidence: MEDIUM
D5_notes: No inline examples. External website referenced for tutorials.

D6_contribution: 0     confidence: MEDIUM
D6_notes: No contributing guidelines, no issue tracker link, no contact info, no community channel in README. External website link is for documentation only.

exclusion_reason:
general_notes: MATLAB toolbox — no standard dependency file hence I1=0. COPYING file covers license. Zenodo DOI badge in README confirms F1=1.