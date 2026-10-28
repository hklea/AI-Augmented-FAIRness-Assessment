repo_id: cdk/cdk
annotated_date: 2026-07-18

# Rule-based
F1_persistent_id:       1
F2_metadata_file:       1
A1_license:             1
I1_dependency_file:     1
R1_readme_present:      1
R2_citation:            0

# AI-based
D1_installation:        2  confidence: HIGH
D1_notes: Maven install, Java 1.7+ requirement, pre-built JAR download, classpath compile/run examples, and Maven dependency XML.

D2_usage:               1  confidence: MEDIUM
D2_notes: Shows compiling against the JAR with a placeholder MyClass, but no concrete cheminformatics API example; points to Toolkit-Rosetta wiki for common tasks.

D3_purpose:             2  confidence: HIGH
D3_notes: Clear description of an open-source Java library for cheminformatics and bioinformatics with listed key features.

D4_dependencies:        2  confidence: HIGH
D4_notes: States Java 1.7+ and Apache Maven as build/runtime environment requirements in the README.

D5_examples:            2  confidence: HIGH
D5_notes: Links Toolkit-Rosetta wiki page providing examples for common tasks.

D6_contribution:        1  confidence: HIGH
D6_notes: Issues and user mailing list for help, but no contribution guidelines or CONTRIBUTING process described.

exclusion_reason:
general_notes: F1 from DOI in CITATION.cff. F2 from CITATION.cff. R2=0 — CITATION.cff alone does not satisfy R2. I1=1 from pom.xml (Maven equivalent dependency/build file; standard Python dep flags were false).
