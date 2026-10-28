repo_id: yt-project/yt
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 0
F2_metadata_file: 0
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Both conda and pip install commands provided inline. Link to detailed installation docs for advanced cases.

D2_usage: 2     confidence: HIGH
D2_notes: Six quickstart Jupyter notebooks linked directly in README with descriptive titles. yt Hub mentioned for running notebooks online.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — open-source Python library for analyzing and visualizing volumetric data. Domains of application listed.

D4_dependencies: 1     confidence: MEDIUM
D4_notes: Python implied by pip/conda install but no explicit version or dependency list in README. pyproject.toml present but not referenced.

D5_examples: 2     confidence: HIGH
D5_notes: Six quickstart notebooks linked inline with titles. yt Hub for online execution referenced. Documentation with recipes and tutorials linked.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.rst present. Contributing guidelines linked, mailing lists linked, Slack invite linked, code of conduct referenced. Very welcoming contribution section.

exclusion_reason:
general_notes: F1=0 no DOI badge. F2=0 no CITATION.cff or codemeta.json. R2=1 explicit "please consider citing it" instruction with method paper link. A1=1 COPYING present. Strong README overall.