repo_id: JuliaClimate/ClimateTools.jl
annotated_date: 2026-07-09

# Rule-based
F1_persistent_id: 1
F2_metadata_file: 0
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 0

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Clear Julia Pkg.add command inline. Local development install also provided.

D2_usage: 2     confidence: HIGH
D2_notes: Two complete inline code examples showing bias correction and ensemble workflow. Actionable and well explained.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — climate analysis toolkit for gridded observations, reanalyses and climate model simulations. Workflow steps listed explicitly.

D4_dependencies: 2     confidence: HIGH
D4_notes: Julia 1.10+ required, YAXArrays 0.7 compatibility stated explicitly in Status section. Core dependencies mentioned inline.

D5_examples: 2     confidence: HIGH
D5_notes: Two complete working code examples inline. Documentation map and stable docs linked.

D6_contribution: 0     confidence: HIGH
D6_notes: No contributing guidelines, no issue tracker link, no contact info, no community channel mentioned anywhere in README.

exclusion_reason:
general_notes: Zenodo DOI badge present (F1=1). R2=0 — DOI badge only, no explicit citation instruction per v1.2 edge case. F2=0 no CITATION.cff or codemeta.json. I1=0 — Julia package, no standard dependency file detected by script. Strong documentation quality despite weak metadata.