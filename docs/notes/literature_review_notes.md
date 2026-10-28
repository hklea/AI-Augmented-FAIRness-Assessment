# Literature Review Notes

# Wilkinson et al. 2016 — The FAIR Guiding Principles

## Full Citation
M. D. Wilkinson et al., "The FAIR Guiding Principles for scientific data management and stewardship," *Scientific Data*, 3:160018, 2016.
DOI: 10.1038/sdata.2016.18

---

## Main Contribution
Introduces the FAIR Guiding Principles for scientific data management and stewardship — a minimal, domain-independent framework applicable to all scholarly digital objects including data, software, and workflows.

---

## Core FAIR Principles
- **Findable** — (meta)data assigned a unique/persistent identifier, described with rich metadata, indexed in searchable resources
- **Accessible** — retrievable via open, standardized protocol; metadata remains accessible even if data is removed
- **Interoperable** — uses formal knowledge representation language, FAIR vocabularies, qualified references to other data
- **Reusable** — rich attributes, clear license, detailed provenance, meets community standards

---

## Key Ideas
- FAIR supports both humans and machines
- **Machine-actionability is a central goal** — automated agents should be able to discover, evaluate, and act on digital objects without prior knowledge of them
- Machine-actionability is a **continuum**, not a binary — more FAIR means more actionable
- FAIR applies not only to data but also to tools, workflows, and algorithms
- Rich metadata is essential for discovery and reuse
- The principles are **modular and independent** — they can be adopted incrementally and in any combination

---

## Relevance to My Thesis
- Provides the conceptual foundation for FAIRness assessment of research software
- The machine-actionability continuum directly motivates automated assessment tools like F-UJI
- The explicit extension of FAIR to workflows and tools justifies applying the principles to software repositories (before FAIR4RS formally did so)

---

## Important Insight
Machine-actionability is described as a spectrum — a computational agent should be able to identify an object's type, determine its usefulness, check licensing, and act on it. This explains why qualitative aspects like documentation clarity matter beyond just structural checks.

---

## Limitation / Gap
- Focused primarily on scientific **data**, not research software specifically
- No concrete implementation prescribed — intentionally technology-agnostic
- Does not address how to assess **qualitative** aspects of documentation — the gap this thesis targets

# Barker et al. 2022 — Introducing the FAIR Principles for Research Software

## Full Citation
M. Barker et al., "Introducing the FAIR Principles for Research Software," *Scientific Data*, vol. 9, no. 622, 2022.
DOI: 10.1038/s41597-022-01710-x

---

## Main Contribution
Introduces the FAIR Principles for Research Software (FAIR4RS), adapting the original FAIR principles to address the unique characteristics and challenges of research software. Developed by the FAIR4RS Working Group, jointly convened by ReSA, FORCE11, and RDA, with input from ~500 people across 110+ organisations.

---

## Core FAIR4RS Principles

### Findable
- Software assigned globally unique and persistent identifiers
- Different versions and granular components receive distinct identifiers (F1.1, F1.2 — new vs. original FAIR)
- Metadata should be searchable and indexable

### Accessible
- Software retrievable via standardized protocols
- Metadata remains accessible even if software becomes unavailable

### Interoperable
- Software exchanges data using community standards
- Includes references to other software and related objects
- Covers API interaction — broader than original FAIR's metadata-focused interoperability

### Reusable
- Software should be executable, understandable, modifiable, and reusable
- Clear licensing and provenance required
- Must meet community standards
- R2 (qualified references to other software) is a new addition not present in original FAIR

---

## Key Ideas
- Research software is a fundamental part of modern research and reproducibility
- Original FAIR principles were designed mainly for data, requiring adaptation for software
- Software has unique characteristics including:
  - executability
  - dependencies
  - versioning
  - continuous evolution
  - package ecosystems
- FAIRness for software should begin **during development**, not only at publication time — unlike data, software may be used directly from its development environment
- Metadata, identifiers, repositories, and licenses are central to software FAIRness
- FAIR4RS is an aspirational and community-driven framework
- Early adopters include ELIXIR, ARDC, Netherlands eScience Center, ZB MED — showing growing institutional support

---

## Relevance to My Thesis
- Provides the software-specific FAIR framework underlying this thesis
- Establishes why research software FAIRness differs from data FAIRness
- Highlights software characteristics relevant to GitHub repository assessment
- Supports evaluating aspects such as documentation, dependencies, licensing, and versioning
- F1.1/F1.2 and R1–R1.2 are directly relevant to the rule-based component (versioning, license, provenance)
- R1 and reusability sub-principles are the primary target of the AI-based documentation assessment component
- Motivates automated FAIRness assessment for research software repositories
- Growing institutional adoption supports the relevance and timeliness of this thesis

---

## Important Insight
The paper expands the meaning of reusability for software beyond simple access. Research software should be executable, understandable, modifiable, and integrable into other systems. This highlights the importance of qualitative aspects such as documentation clarity and usability, which are difficult to assess using only rule-based approaches.

---

## Limitation / Gap
- FAIR4RS defines high-level principles but does not prescribe concrete automated assessment methods
- The framework identifies important software qualities but does not explain how to evaluate qualitative aspects like documentation understandability
- Many FAIR4RS indicators rely on metadata and structural information, leaving room for complementary AI-assisted qualitative assessment approaches
- Early institutional adoption shows traction, but consistent implementation across repositories is not yet the norm — further motivating the need for automated assessment tools

# Chue Hong et al. 2025 — Metrics for Automated FAIR Software Assessment in a Disciplinary Context

## Full Citation
N. Chue Hong, E. Breitmoser, et al., "D5.2 - Metrics for Automated FAIR Software Assessment in a Disciplinary Context," FAIR-IMPACT Project Deliverable, v1.1, 2025.

---

## Main Contribution
Defines 17 concrete, measurable FAIR Research Software Metrics (FRSM-01 to FRSM-17) for automated assessment of research software against the FAIR4RS Principles. The metrics are intended to operationalize FAIR4RS in practical automated assessment systems and extend existing FAIR assessment tooling toward research software.

---

## Core FAIR Research Software Metrics

### Findable
- Persistent and globally unique identifiers for software (FRSM-01)
- Distinct identifiers for software components and versions (FRSM-02, FRSM-03)
- Rich and searchable metadata (FRSM-04, FRSM-07, FRSM-08)

### Accessible
- Software retrievable through standard communication protocols (FRSM-09)
- Persistent metadata records maintained independently of software availability

### Interoperable
- Open data formats and standards references (FRSM-10)
- Open APIs with machine-readable interface definitions (FRSM-11)
- References to related software and objects (FRSM-12)

### Reusable
- Installation and dependency documentation (FRSM-13)
- Test cases demonstrating functionality (FRSM-14)
- Licensing information in code and metadata (FRSM-15, FRSM-16)
- Provenance and development history information (FRSM-17)

---

## Key Ideas
- FAIR4RS principles can be operationalized into concrete automated metrics
- Metrics are designed to be domain-agnostic but adaptable to disciplinary contexts
- Three compliance levels are used:
  - Essential
  - Important
  - Useful
- Metrics apply at multiple levels:
  - code level
  - software project level
  - repository level
- Automated tools are effective at checking:
  - metadata existence
  - identifiers
  - licenses
  - repository structure
  - provenance
- The document explicitly acknowledges that automated tools can often verify the existence of metadata, but not its quality, relevance, or correctness
- Metrics were mapped to the CESSDA social sciences domain as a disciplinary exemplar
- Planned integration into F-UJI demonstrates practical application potential

---

## Relevance to My Thesis
- Provides the direct operational framework for the rule-based component of this thesis
- The 17 FRSMs map FAIR4RS principles into measurable repository indicators
- FRSM-04, FRSM-05, FRSM-13, and FRSM-17 are especially relevant because they involve documentation, development metadata, dependency information, and provenance
- The distinction between structural validation and qualitative understanding directly motivates the AI-assisted component explored in this thesis
- The Essential / Important / Useful compliance structure could inform scoring or profiling strategies in the prototype system
- Demonstrates how FAIRness assessment can be automated for GitHub-hosted research software repositories

---

## Important Insight
Several metrics explicitly acknowledge the limitations of automated rule-based assessment. The document notes that tools may automatically verify the existence of documentation or metadata, but cannot reliably determine its quality, relevance, correctness, or usefulness. This creates a gap between structural FAIR compliance and meaningful software reusability, particularly regarding README clarity, installation guidance, and documentation understandability.

---

## Limitation / Gap
- Metrics are primarily structural and existence-based rather than quality-oriented
- No AI- or NLP-based approach for qualitative assessment is proposed
- Qualitative aspects such as documentation clarity and usability remain difficult to assess automatically
- Domain-specific implementations (e.g. CESSDA exemplar) confirm that universal FAIR assessment requires contextual adaptation — relevant when discussing the generalisability of the GitHub-focused prototype in this thesis
- FAIR assessment criteria are expected to evolve as FAIR4RS adoption matures

# F-UJI — Automated FAIR Data Assessment Tool

## Full Citation
FAIRsFAIR, "F-UJI Automated FAIR Data Assessment Tool," https://www.f-uji.net

---

## Main Contribution
F-UJI is an automated web-based FAIR assessment tool developed within the FAIRsFAIR initiative to evaluate the FAIRness of digital research objects using machine-actionable metadata and standardized FAIR metrics. It operationalizes FAIR assessment through automated rule-based checks and produces structured FAIRness scores across the Findable, Accessible, Interoperable, and Reusable dimensions.

---

## Core Assessment Features

### Automated FAIR Evaluation
- Assesses FAIRness programmatically using FAIR metrics
- Accepts persistent identifiers (DOIs, URLs) and metadata endpoints
- Produces quantitative FAIRness scores and FAIR maturity levels

### Metadata-Centric Assessment
- Evaluates:
  - metadata presence
  - persistent identifiers
  - licenses
  - semantic vocabularies
  - provenance information
  - machine-readable formats
  - accessibility protocols
- Uses structured metadata standards such as:
  - JSON-LD
  - RDF
  - schema.org
  - SPDX
  - PROV-O

### FAIR Scoring
- Scores each FAIR dimension separately:
  - Findable
  - Accessible
  - Interoperable
  - Reusable
- FAIRness treated as a spectrum/maturity model rather than a binary property
- Provides detailed metric-level reporting and evidence traces

---

## Key Ideas
- FAIR assessment can be operationalized through machine-actionable metadata checks
- Automated FAIR evaluation is strongly dependent on structured metadata availability
- F-UJI focuses primarily on structural and machine-readable FAIR indicators
- Findability and Accessibility are generally easier to assess automatically than Interoperability and Reusability
- The tool intentionally distinguishes FAIRness assessment from broader data/software quality assessment
- Many FAIR checks evaluate the existence of metadata or documentation rather than its semantic quality

---

## Relevance to My Thesis
- Provides a strong baseline example of rule-based automated FAIR assessment
- Demonstrates how FAIR principles can be translated into measurable automated checks
- The metric-based scoring approach is relevant for the rule-based component of this thesis
- Highlights the strengths of machine-readable metadata assessment for GitHub-hosted research software repositories
- The distinction between structural FAIRness and qualitative understanding directly motivates the AI-assisted component explored in this thesis
- F-UJI serves as an important reference system when comparing automated FAIR assessment approaches
- F-UJI serves as the baseline comparator in the evaluation of this thesis, where the AI-enhanced assessment approach is compared against F-UJI outputs on a shared repository set

---

## Important Insight
F-UJI demonstrates that automated FAIR assessment tools are highly effective at verifying structural and machine-readable aspects of FAIR compliance, such as identifier presence, metadata schemas, licenses, and interoperability standards. However, the system does not deeply evaluate qualitative aspects such as documentation clarity, usability, explanation quality, or whether installation and usage instructions are understandable to humans. This creates a gap between structural FAIR compliance and meaningful software reusability.

---

## Limitation / Gap
- Assessment is heavily metadata-centric and dependent on structured FAIR infrastructure
- Primarily evaluates existence and machine-readability rather than semantic quality or usefulness
- Documentation quality, understandability, and usability are not deeply assessed
- Originally designed primarily for FAIR digital objects and datasets rather than research software repositories specifically
- F-UJI was not designed specifically for direct GitHub repository assessment and instead expects persistent identifiers and structured metadata records as input, which many repositories in the thesis dataset may not provide
- Qualitative FAIR-related dimensions still require human interpretation or more advanced semantic analysis approaches

# FAIR-Aware — FAIR Self-Assessment and Awareness Tool

## Full Citation
FAIRsFAIR, "FAIR-Aware: FAIR Self-Assessment Tool," https://fairsfair.eu/fair-aware

---

## Main Contribution
FAIR-Aware is a human-centered FAIR self-assessment and awareness tool designed to help researchers understand the FAIR Principles and reflect on how FAIR practices can be integrated into their research workflows. Unlike automated FAIR assessment tools, FAIR-Aware focuses on increasing FAIR literacy and supporting informed FAIR-related decision making.

---

## Core Assessment Features

### Human-Guided FAIR Self-Assessment
- Uses a questionnaire-based self-assessment approach
- Researchers answer reflective FAIR-related questions
- Focuses on FAIR awareness rather than strict automated validation
- Provides guidance and recommendations for improving FAIR practices

### FAIR Principles Coverage
- Questions organized around the four FAIR dimensions:
  - Findable
  - Accessible
  - Interoperable
  - Reusable
- Covers topics such as:
  - persistent identifiers
  - metadata practices
  - licenses
  - provenance
  - repositories
  - community standards
  - preservation planning

### Educational and Reflective Design
- Intended to support FAIR understanding during research planning and data management
- Encourages researchers to think critically about FAIR implementation decisions
- Domain-agnostic and applicable across disciplines
- Designed as a lightweight awareness and training tool

---

## Key Ideas
- FAIRness is not purely a technical problem but also involves human understanding and decision-making
- Many FAIR-related decisions require contextual interpretation and domain knowledge
- FAIR-Aware complements automated FAIR assessment approaches by addressing researcher awareness
- FAIR assessment can include both machine-centered and human-centered perspectives
- Human interpretation remains important for evaluating provenance, standards, reuse conditions, and preservation strategies

---

## Relevance to My Thesis
- Demonstrates an alternative FAIR assessment approach focused on human interpretation rather than automated validation
- Highlights the limitations of purely rule-based FAIR assessment systems
- Supports the idea that some FAIR-related dimensions require semantic and contextual understanding
- Reinforces the motivation for hybrid assessment approaches combining automated checks with higher-level interpretation
- Provides an important contrast to tools like F-UJI in the FAIR assessment ecosystem
- Illustrates that FAIRness evaluation includes qualitative and interpretive dimensions relevant to AI-assisted assessment

---

## Important Insight
FAIR-Aware shows that FAIR assessment is not limited to verifying machine-readable metadata or repository structure. Many FAIR considerations require researchers to interpret community standards, evaluate reuse conditions, understand provenance, and make contextual decisions regarding preservation and interoperability. This highlights the importance of qualitative reasoning in FAIR evaluation.

---

## Limitation / Gap
- Relies heavily on self-reporting and researcher interpretation rather than automated validation
- Does not directly inspect repositories, metadata records, or software artifacts programmatically
- Produces awareness-oriented guidance rather than measurable FAIR compliance metrics
- Limited scalability compared to automated FAIR assessment systems
- Does not provide automated qualitative analysis of documentation or repository content

# FAIRsharing — FAIR Standards, Repositories, and Policy Registry

## Full Citation
FAIRsharing, "FAIRsharing Registry," https://fairsharing.org/

---

## Main Contribution
FAIRsharing is a curated registry of FAIR-related standards, repositories, databases, policies, and metadata schemas. It provides a centralized infrastructure to support the discovery, adoption, and interconnection of community standards and FAIR-enabling resources across research domains.

---

## Core Features

### Standards and Repository Registry
- Catalogues:
  - metadata standards
  - data and software repositories
  - identifier schemas
  - ontologies and vocabularies
  - data policies
  - reporting guidelines
- Supports cross-linking between standards, repositories, and policies

### FAIR Ecosystem Support
- Helps researchers identify domain-relevant community standards
- Promotes interoperability and metadata harmonization
- Supports machine-readable FAIR infrastructure
- Enables discoverability of FAIR-compliant resources

### Community and Domain Orientation
- Domain-agnostic but supports discipline-specific standards
- Community-curated and continuously updated
- Used by repositories, funders, publishers, and infrastructure providers

---

## Key Ideas
- FAIRness depends not only on individual datasets or repositories but also on broader ecosystem infrastructure
- Community standards and controlled vocabularies are central to interoperability and reuse
- Machine-readable metadata and shared standards enable automated FAIR assessment
- FAIRsharing acts as supporting infrastructure for FAIR implementation and validation
- FAIR assessment tools rely heavily on standardized metadata ecosystems

---

## Relevance to My Thesis
- Provides important contextual infrastructure for automated FAIR software assessment
- Highlights the importance of metadata standards, vocabularies, and repositories in FAIR evaluation
- Supports understanding of how rule-based FAIR assessment systems validate interoperability and metadata quality
- Demonstrates that FAIRness assessment depends on broader ecosystem support beyond repository-level analysis
- Relevant when discussing interoperability, metadata standards, and machine-readable FAIR infrastructures in GitHub-hosted research software repositories

---

## Important Insight
FAIRsharing demonstrates that FAIRness is deeply connected to the existence and adoption of shared standards, metadata schemas, repositories, and controlled vocabularies. Automated FAIR assessment systems rely heavily on this ecosystem infrastructure to validate interoperability and machine-readability. Without standardized metadata practices, automated FAIR evaluation becomes significantly more difficult.

---

## Limitation / Gap
- FAIRsharing is an infrastructure and registry platform rather than a direct FAIR assessment system
- Does not itself evaluate repository FAIRness or documentation quality
- Relies on community adoption and maintenance of standards
- Many GitHub repositories and open-source projects lack explicit alignment with FAIR-related standards or structured metadata schemas
- Does not address qualitative aspects such as documentation clarity, usability, or understandability