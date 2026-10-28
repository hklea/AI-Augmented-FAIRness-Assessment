repo_id: jupyter/nbconvert
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       0
F2_metadata_file:       0
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        1  confidence: MEDIUM
D1_notes: Dev install (clone + pip install -e .) and pandoc prerequisite are present, but no clear end-user pip/conda install of a release package.

D2_usage:               2  confidence: HIGH
D2_notes: Clear CLI usage pattern and concrete HTML conversion example with explained output.

D3_purpose:             2  confidence: HIGH
D3_notes: Explains jupyter nbconvert converts notebooks via Jinja to HTML, LaTeX, PDF, Reveal JS, Markdown, rst, scripts.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Pandoc called out for setup; otherwise limited environment detail (no Python version list for users).

D5_examples:            2  confidence: HIGH
D5_notes: Concrete convert-to-HTML example inline plus link to nbconvert-examples on GitHub.

D6_contribution:        1  confidence: MEDIUM
D6_notes: Issues and Discourse support present, and copyright/team context, but no contribution guidelines or CONTRIBUTING process described.

exclusion_reason:
general_notes: No DOI (F1=0). No structured citation metadata file (F2=0). No citation instruction or CITATION file (R2=0). A1 from LICENSE; I1 from pyproject.toml.
