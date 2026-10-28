repo_id: cdk/cdk
annotated_date: 2026-07-08

# Rule-based
F1_persistent_id: 0
F2_metadata_file: 1
A1_license: 1
I1_dependency_file: 1
R1_readme_present: 1
R2_citation: 1

# AI-based
D1_installation: 2     confidence: HIGH
D1_notes: Clear build instructions with Maven commands inline. Pre-built JAR download option also provided. Java version requirement stated.

D2_usage: 2     confidence: HIGH
D2_notes: Concrete examples provided — javac/java commands with classpath, Maven dependency XML, Python via Jython explained.

D3_purpose: 2     confidence: HIGH
D3_notes: Clear description — open-source Java library for cheminformatics and bioinformatics. Key features listed explicitly.

D4_dependencies: 2     confidence: HIGH
D4_notes: Java 1.7 or later explicitly required. Maven as build tool stated. Dependencies clearly described inline.

D5_examples: 1     confidence: MEDIUM
D5_notes: Toolkit-Rosetta wiki linked for examples. No inline code examples demonstrating actual cheminformatics use.

D6_contribution: 1     confidence: HIGH
D6_notes: Mailing list and issue tracker linked. No contribution process or CONTRIBUTING.md described.

exclusion_reason:
general_notes: F1=0 no DOI anywhere. F2=1 CITATION.cff present. R2=1 CITATION.cff counts as citation information. I1=0 Java/Maven project — no standard dependency file checked by our script but Maven pom.xml handles dependencies. Worth noting as edge case for Java repos.