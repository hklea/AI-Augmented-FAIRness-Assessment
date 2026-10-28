# F-UJI Baseline Evaluation

**Date:** 2026-08-18  
**F-UJI version:** 3.5.1  
**Metric version:** FAIRsFAIR / FsF Metrics v0.8  
**Input type:** GitHub repository URL

## Purpose

The purpose of this experiment is to investigate whether F-UJI can
serve as an external FAIR assessment baseline for the proposed
research software FAIRness framework.

F-UJI is primarily designed for research data objects. Therefore,
the experiment evaluates whether F-UJI can process research software
repositories represented by GitHub repository URLs and whether the
resulting metrics provide a meaningful comparison for software.

Five repositories with different profiles under the proposed
software-oriented assessment framework were selected for the pilot.

---

## Pilot Test

### astropy/astropy

**Input**

https://github.com/astropy/astropy

**Proposed framework**

- Rule-based score: 6/6
- LLM documentation score: 7/12

**F-UJI result**

- Overall FAIR score: 42.31% (11/26)
- Overall FAIR level: initial
- Findable: 42.86% (3/7)
- Accessible: 42.86% (3/7)
- Interoperable: 33.33% (2/6)
- Reusable: 50.00% (3/6)

**Resource-type warning**

F-UJI reported that the evaluated resource did not identify itself
as a dataset. Instead, the detected resource types included
`softwaresourcecode` and `object`.

F-UJI consequently warned that it may not be the appropriate tool
for this type of resource.

**Observation**

F-UJI was technically able to process the GitHub repository and
produce an assessment. However, several F-UJI metrics explicitly
refer to data and data metadata rather than software-specific
properties.

Examples include metrics concerning:

- identifiers for data
- metadata describing data
- access conditions for data
- provenance of data
- research-community data formats

Notably, the license check (FsF-R1.1-01M) was not satisfied despite
the repository's README explicitly stating a BSD 3-clause license.
This illustrates that F-UJI's metadata-based checks can diverge from
repository-level file or content checks even for clearly licensed
software.

**Interpretation**

The result demonstrates partial conceptual overlap between F-UJI
and the proposed framework, particularly for generic FAIR concepts
such as identifiers, metadata, accessibility, and licensing.
However, F-UJI does not directly assess software documentation
dimensions such as installation, usage, dependencies, examples,
and contribution information.

This initial result motivated evaluation of additional repositories
with different software-oriented FAIRness profiles.

---

### sunpy/sunpy

**Input**

https://github.com/sunpy/sunpy

**Proposed framework**

- Rule-based score: 6/6
- LLM documentation score: 9/12

**F-UJI result**

- Overall FAIR score: 42.31% (11/26)
- Overall FAIR level: initial
- Findable: 42.86% (3/7)
- Accessible: 42.86% (3/7)
- Interoperable: 33.33% (2/6)
- Reusable: 50.00% (3/6)

**Resource-type warning**

As with astropy/astropy, F-UJI reported that the evaluated resource
did not identify itself as a dataset. Instead, the detected resource
types included `softwaresourcecode` and `object`.

F-UJI therefore warned that it may not be the appropriate assessment
tool for this type of resource.

**Observation**

F-UJI successfully processed the SunPy GitHub repository and produced
the same overall and category-level scores as astropy/astropy.

The detailed metric results showed a similar pattern. Generic
web-access and metadata-representation checks were satisfied, while
several metrics requiring dataset-oriented metadata, including
persistent identifier metadata, descriptive data metadata, access
conditions, semantic resources, and data-format information, were
not satisfied.

The license metadata metric (FsF-R1.1-01M) was also not satisfied,
although licensing is represented at repository level in the
software-oriented assessment.

**Interpretation**

The SunPy result reinforced the initial observation that F-UJI can
technically process a GitHub software repository while evaluating it
using metrics primarily designed for research data objects. Its
identical score to astropy/astropy motivated testing repositories
with more substantially different software-oriented profiles.

---

### gonum/gonum

**Input**

https://github.com/gonum/gonum

**Proposed framework**

- Rule-based score: 2/6
- LLM documentation score: 5/12

**F-UJI result**

- Overall FAIR score: 42.31% (11/26)
- Overall FAIR level: initial
- Findable: 42.86% (3/7)
- Accessible: 42.86% (3/7)
- Interoperable: 33.33% (2/6)
- Reusable: 50.00% (3/6)

**Resource-type warning**

F-UJI again reported that the evaluated resource did not identify
itself as a dataset. Instead, the detected resource types included
`softwaresourcecode` and `object`.

F-UJI therefore warned that it may not be the appropriate tool for
this type of resource.

**Observation**

Gonum provides a particularly useful contrast with the previous
repositories. Its rule-based ground-truth profile satisfies only
two of the six indicators (A1 and R1), with no detected persistent
identifier, structured metadata file, dependency file, or citation
information.

Despite this substantially different software-oriented profile,
F-UJI produced exactly the same overall and category-level scores
as for astropy/astropy and sunpy/sunpy.

The F-UJI license metadata metric (FsF-R1.1-01M) was also not
satisfied, whereas the proposed rule-based assessment identifies
a repository license for Gonum (A1=1).

**Interpretation**

The Gonum result provides evidence that the identical F-UJI scores
are not limited to repositories with strong structural FAIR
characteristics. A repository scoring only 2/6 under the proposed
rule-based assessment received the same F-UJI result as repositories
with substantially stronger software-oriented profiles.

---

### yt-project/yt

**Input**

https://github.com/yt-project/yt

**Proposed framework**

- Rule-based score: 4/6
- LLM documentation score: 11/12

**F-UJI result**

- Overall FAIR score: 42.31% (11/26)
- Overall FAIR level: initial
- Findable: 42.86% (3/7)
- Accessible: 42.86% (3/7)
- Interoperable: 33.33% (2/6)
- Reusable: 50.00% (3/6)

**Resource-type warning**

F-UJI again reported that the evaluated resource did not identify
itself as a dataset. Instead, the detected resource types included
`softwaresourcecode` and `object`.

F-UJI therefore warned that it may not be the appropriate tool for
this type of resource.

**Observation**

The yt repository provides a different type of contrast. It satisfies
four of the six rule-based indicators and achieves a high LLM
documentation quality score of 11/12, including complete scores for
installation, usage, purpose, examples, and contribution information.

Despite this strong documentation profile, F-UJI again produced the
same overall and category-level scores observed for the other pilot
repositories.

This is consistent with the different assessment scope of F-UJI,
whose evaluated metrics primarily concern data and metadata
properties rather than software documentation quality.

The license metadata metric (FsF-R1.1-01M) was again not satisfied,
although the proposed rule-based assessment identifies a repository
license (A1=1).

**Interpretation**

The yt result illustrates that software documentation quality is
largely outside the scope of the evaluated F-UJI metrics. Strong
installation, usage, examples, and contribution documentation did
not result in a different F-UJI assessment.

---

### scipy/scipy

**Input**

https://github.com/scipy/scipy

**Proposed framework**

- Rule-based score: 5/6
- LLM documentation score: 8/12

**F-UJI result**

- Overall FAIR score: 42.31% (11/26)
- Overall FAIR level: initial
- Findable: 42.86% (3/7)
- Accessible: 42.86% (3/7)
- Interoperable: 33.33% (2/6)
- Reusable: 50.00% (3/6)

**Resource-type warning**

F-UJI again reported that the evaluated resource did not identify
itself as a dataset. The detected resource types included
`softwaresourcecode` and `object`.

F-UJI warned that it may not be the appropriate tool for this type
of resource.

**Observation**

SciPy received a rule-based score of 5/6 in the proposed framework,
including a positive persistent identifier indicator (F1).

Despite this, the F-UJI persistent identifier metric
(FsF-F1-02MD) was not satisfied when the GitHub repository URL was
used as input.

This provides a concrete example of the difference between metadata
harvested by F-UJI from a GitHub repository URL and the
software-specific repository indicators evaluated by the proposed
framework.

**Interpretation**

The SciPy result further supports the pattern observed across the
pilot. Even a repository with a positive software-oriented
persistent identifier indicator and a high rule-based total
received the same F-UJI assessment as the other tested
repositories.

---

## Pilot Summary


| Repository | Rule-based | LLM total | F-UJI | F | A | I | R | Warning |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| astropy/astropy | 6/6 | 7/12 | 42.31% | 42.86% | 42.86% | 33.33% | 50.00% | Yes |
| sunpy/sunpy | 6/6 | 9/12 | 42.31% | 42.86% | 42.86% | 33.33% | 50.00% | Yes |
| gonum/gonum | 2/6 | 5/12 | 42.31% | 42.86% | 42.86% | 33.33% | 50.00% | Yes |
| yt-project/yt | 4/6 | 11/12 | 42.31% | 42.86% | 42.86% | 33.33% | 50.00% | Yes |
| scipy/scipy | 5/6 | 8/12 | 42.31% | 42.86% | 42.86% | 33.33% | 50.00% | Yes |

## Cross-Repository Observation

The five pilot repositories exhibit substantially different
software-oriented assessment profiles. Their rule-based scores range
from 2/6 to 6/6, while their documentation quality also varies
considerably.

Nevertheless, F-UJI produced the same result for every GitHub
repository URL:

- Overall: 11/26 (42.31%)
- Findable: 3/7 (42.86%)
- Accessible: 3/7 (42.86%)
- Interoperable: 2/6 (33.33%)
- Reusable: 3/6 (50.00%)

The same resource-type warning was also produced for all five
repositories.

The repeated metric pattern suggests that, for these GitHub inputs,
the F-UJI assessment was primarily determined by generic properties
available through the repository webpage and harvested metadata,
rather than by the software-specific FAIR characteristics evaluated
by the proposed framework.

## Pilot Conclusion

F-UJI successfully processed all five tested GitHub repository URLs.
However, for every repository it reported that the evaluated
resource was identified as software rather than as a dataset and
warned that F-UJI might not be appropriate for this resource type.

Despite substantial differences between the repositories according
to the software-oriented rule-based and documentation-quality
assessments, all five repositories received the same F-UJI score of
42.31% (11/26), with identical Findable, Accessible, Interoperable,
and Reusable category scores.

The pilot therefore indicates that applying F-UJI directly to GitHub
repository URLs provides limited discrimination between the tested
research software repositories. In addition, several F-UJI metrics
refer explicitly to data, data metadata, provenance, and data formats,
which limits their direct comparability with software-oriented
assessment indicators.

For these reasons, F-UJI is retained as an exploratory external
baseline demonstrating the limitations of applying a data-oriented
FAIR assessment directly to software repository URLs, rather than
being used as a direct quantitative comparator across the complete
30-repository ground-truth set.