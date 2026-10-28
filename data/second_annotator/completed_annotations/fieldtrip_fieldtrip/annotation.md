repo_id: fieldtrip/fieldtrip
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     0
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Step-by-step MATLAB install via clone/zip, addpath, ft_defaults, startup.m advice, and FAQ install link; warns against genpath.

D2_usage:               1  confidence: MEDIUM
D2_notes: No concrete analysis example in the README; points to fieldtriptoolbox.org for documentation and tutorials.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of MATLAB toolbox for MEG/EEG/iEEG analysis with methods and supported systems.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Assumes MATLAB and discusses path/toolbox setup, but does not state a MATLAB version or other package requirements in prose.

D5_examples:            2  confidence: HIGH
D5_notes: Explicitly points to the project website for documentation and tutorials supporting reuse.

D6_contribution:        0  confidence: HIGH
D6_notes: No contribution guidelines, issue tracker reference, or support/community channel described in the README.

exclusion_reason:
general_notes: Zenodo DOI gives F1=1. CITATION.cff gives F2=1. R2=0 — DOI badge/CITATION.cff alone without explicit citation instruction. I1=0 — no standard dependency specification file (MATLAB toolbox; none of the checked files present).
