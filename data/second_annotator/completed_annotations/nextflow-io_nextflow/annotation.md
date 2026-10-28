repo_id: nextflow-io/nextflow
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Single curl install command and bioconda install; explains placing the executable on PATH.

D2_usage:               1  confidence: MEDIUM
D2_notes: Install-focused Quick start with no concrete workflow script example; documentation linked for usage.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of a dataflow workflow system for scalable, portable, reproducible pipelines across platforms.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Mentions dependency managers (Conda, Spack, Docker, etc.) and execution platforms, but not a precise required runtime version matrix in prose.

D5_examples:            1  confidence: MEDIUM
D5_notes: Documentation and nf-core community workflows referenced; no inline workflow example in the README.

D6_contribution:        2  confidence: HIGH
D6_notes: CONTRIBUTING.md present; community forum, Slack, and GitHub issues for bugs/features.

exclusion_reason:
general_notes: F1 from citation DOI. F2 from CITATION.cff. R2=1 from explicit Citations section ("If you use Nextflow... please cite"). I1=1 from build.gradle (Gradle equivalent dependency/build file). A1 from COPYING.
