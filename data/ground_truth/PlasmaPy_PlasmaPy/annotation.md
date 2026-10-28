repo_id: PlasmaPy/PlasmaPy
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Clear pip install commands for macOS/Linux and Windows inline. Python version notes included.

D2_usage: 1     confidence: MEDIUM
D2_notes: No inline usage examples. Links to example gallery of Jupyter notebooks and documentation externally.

D3_purpose: 2     confidence: HIGH
D3_notes: Purpose clearly stated — open source Python package for plasma research and education. Analogy to Astropy helps situate it.

D4_dependencies: 1     confidence: MEDIUM
D4_notes: Python version mentioned in install commands but no explicit dependency list in README. pyproject.toml referenced implicitly.

D5_examples: 2     confidence: HIGH
D5_notes: Example gallery of Jupyter notebooks linked and accessible at docs.plasmapy.org/en/stable/examples.html.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.md present. Contributor guide linked, code of conduct linked, good first issues linked, community meetings, mailing list, GitHub discussions, email contact all provided.

exclusion_reason:
general_notes: Zenodo DOI badge present (F1=1). Explicit "cite PlasmaPy" instruction in README (R2=1). One of the most complete READMEs seen so far — strong across all dimensions.