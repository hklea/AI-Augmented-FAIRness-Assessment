repo_id: jupyter/nbconvert
annotated_date: 2026-05-29

# Rule-based
F1_persistent_id:    0
F2_metadata_file:    0
A1_license:          1
I1_dependency_file:  1
R1_readme_present:   1
R2_citation:         0

# AI-based
D1_installation:     2   confidence: MEDIUM
D1_notes: Step-by-step dev install present with git clone, pip install, pandoc installation commands. Clear and actionable.

D2_usage:            2   confidence: HIGH
D2_notes: Concrete executable example present — command structure explained, real example with mynotebook.ipynb shown, output filename described. User can run immediately from README alone.

D3_purpose:          2   confidence: MEDIUM
D3_notes: Converts notebooks to various formats clearly stated, output formats listed. Purpose clear to non-specialist.

D4_dependencies:     1   confidence: MEDIUM
D4_notes: Pandoc mentioned as dependency but no Python version requirements or other dependencies listed explicitly.

D5_examples:         2   confidence: HIGH
D5_notes: Inline working example present — full command demonstrated with real input file and expected output. Dedicated examples repo also linked as additional resource.

D6_contribution:     2   confidence: MEDIUM
D6_notes: Issue tracker, Discourse community support, mailing list all linked for specific needs.

exclusion_reason:
general_notes: No DOI or citation information — F1 and R2 both 0. Weakest FAIR metadata so far. But inline documentation quality is reasonable with concrete usage example.