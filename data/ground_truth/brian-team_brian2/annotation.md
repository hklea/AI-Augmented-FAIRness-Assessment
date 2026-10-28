repo_id: brian-team/brian2
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 1     confidence: HIGH
D1_notes: No inline install command. Links to pyproject.toml for dependencies. Installation assumed via pip but not explicitly stated in README.

D2_usage: 1     confidence: MEDIUM
D2_notes: No inline usage examples. Links to external documentation at brian2.readthedocs.org. Mybinder quickstart link provided but no code shown.

D3_purpose: 2     confidence: HIGH
D3_notes: Purpose clearly stated in first paragraph — free open source simulator for spiking neural networks, written in Python.

D4_dependencies: 2     confidence: HIGH
D4_notes: Full dependency list with version numbers explicitly provided inline, including core, optional, documentation and testing dependencies.

D5_examples: 1     confidence: MEDIUM
D5_notes: Mybinder link provided for interactive quickstart but no inline code examples in README.

D6_contribution: 2     confidence: HIGH
D6_notes: Issue tracker linked, Discourse forum linked, Contributor Covenant badge present, community chat linked. Multiple support channels provided.

exclusion_reason:
general_notes: Zenodo DOI badge present (F1=1). CITATION.cff + CITATION.md + codemeta.json all present (F2=1). Citation instructions explicitly in README (R2=1). Very strong metadata profile.