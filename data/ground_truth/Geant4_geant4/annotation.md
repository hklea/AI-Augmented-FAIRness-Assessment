repo_id: Geant4/geant4
annotated_date: 2026-07-09

# Rule-based
F1_persistent_id: 0
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 0
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 1     confidence: HIGH
D1_notes: Installation instructions are provided only through a link to the external Installation Guide. No inline installation commands or steps are included in the README.

D2_usage: 1     confidence: MEDIUM
D2_notes: README links to comprehensive user documentation but does not provide an inline usage example, command, or workflow.

D3_purpose: 2     confidence: HIGH
D3_notes: Purpose is clearly stated as a toolkit for simulating the passage of particles through matter, with application domains explicitly described.

D4_dependencies: 0     confidence: HIGH
D4_notes: No dependency, software requirement, or environment information is described in the README.

D5_examples: 1     confidence: MEDIUM
D5_notes: README links to user documentation covering toolkit usage but does not include or directly reference example workflows or code snippets.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.rst is linked directly from the README. Community support is available through the user forum and Bugzilla issue tracker.

exclusion_reason:

general_notes: CITATION.cff present (F2=1). README lists the primary Geant4 reference papers, satisfying R2=1. No DOI badge or other persistent software identifier found in the README, therefore F1=0.