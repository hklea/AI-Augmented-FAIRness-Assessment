repo_id: OpenMS/OpenMS
annotated_date: 2026-07-15

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            1

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Building section links platform-specific install docs; Linux build page verified live with full dependency lists and cmake steps. Conda/bioconda install badges also present.

D2_usage:               1  confidence: MEDIUM
D2_notes: Strong product description and docs links, but no concrete command/code example showing how to run a TOPP tool or pyOpenMS snippet in the README.

D3_purpose:             2  confidence: HIGH
D3_notes: Detailed explanation of LC-MS library, TOPP tools, visualization, quantitation protocols, and pyOpenMS bindings.

D4_dependencies:        1  confidence: MEDIUM
D4_notes: Mentions C++20 and OS support in Features; detailed dependency install lives in linked build docs rather than in README prose.

D5_examples:            1  confidence: MEDIUM
D5_notes: Documentation and Developer Tutorial linked; no inline working example or clearly labeled examples gallery in the README.

D6_contribution:        1  confidence: MEDIUM
D6_notes: Discord/Gitter community channels and build instructions for developers, but no contribution guidelines/CONTRIBUTING process described.

exclusion_reason:
general_notes: F1 from DOI in Citation section. F2 from CITATION.cff. R2=1 from explicit "Please cite:" with full bibliographic citation. I1=1 from CMakeLists.txt (C++ equivalent build/dependency specification; standard files in fair_file_checks were all false).
