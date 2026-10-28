repo_id: nilearn/nilearn
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
D1_notes: Detailed step-by-step installation with venv and conda options, pip install command, and installation verification step.

D2_usage:            1   confidence: MEDIUM
D2_notes: Only import nilearn shown as installation check. No actual usage examples or analysis workflows inline.

D3_purpose:          2   confidence: HIGH
D3_notes: Clearly described as brain volume and surface analysis tool with statistical and ML capabilities. Accessible to non-specialists.

D4_dependencies:     2   confidence: HIGH
D4_notes: matplotlib >= 3.8.0 explicitly stated, plotly and kaleido mentioned with install instructions, pyproject.toml referenced for full list.

D5_examples:         0   confidence: MEDIUM
D5_notes:No inline examples or tutorial workflows. Import statement is installation verification only, not a usage example.

D6_contribution:     2   confidence: HIGH
D6_notes: Contribution guide linked, drop-in hours described with schedule, Discord and community channels present.

exclusion_reason:
general_notes: R2 corrected from 0 to 1 during final rule-based validation — the repository contains CITATION.cff, which satisfies R2 under the finalized annotation guideline definition of citation information (Zenodo badge alone does not satisfy R2, but CITATION.cff does). D5=0 corrected — import statement is not a usage example. F1=1 from Zenodo badge.