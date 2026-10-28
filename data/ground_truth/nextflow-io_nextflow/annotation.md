repo_id: nextflow-io/nextflow
annotated_date: 2026-07-09

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Single curl command for installation provided inline. Conda alternative also provided. Clear and complete.

D2_usage: 1     confidence: HIGH
D2_notes: No inline usage examples or workflow code. Documentation linked externally for stable and edge releases.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — workflow system for scalable, portable and reproducible workflows based on dataflow programming model. Deployment platforms listed.

D4_dependencies: 1     confidence: HIGH
D4_notes: No explicit dependency or environment requirements stated. Groovy and GPars mentioned in credits but not as user-facing requirements.

D5_examples: 1     confidence: HIGH
D5_notes: No inline examples. Documentation and nf-core workflows linked externally.

D6_contribution: 2     confidence: HIGH
D6_notes: CONTRIBUTING.md present and linked. Community forum, Slack, GitHub issues, YouTube channels all linked. Very active community described.

exclusion_reason:
general_notes: DOI present in Citations section with explicit "please cite" instruction (F1=1, R2=1). CITATION.cff present (F2=1). COPYING file covers license (A1=1). I1=0 Groovy/Java project — no standard dependency file detected by script.