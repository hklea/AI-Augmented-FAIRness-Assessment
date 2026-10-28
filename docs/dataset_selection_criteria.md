# Dataset Selection Criteria
**Issue:** #24
**Date:** 2026-06-02

## Research Software Definition

Research software is defined as software developed to support, enable,
or conduct scientific research. This includes data analysis tools,
simulation software, computational pipelines, scientific frameworks,
and domain-specific research libraries. Repositories must demonstrate
a clear research or scientific computing context through repository
descriptions, topics, documentation, associated publications, or
organizational affiliation.

## Domain Coverage

To reduce domain-specific bias and improve generalizability,
repositories will be collected from multiple research domains,
including:

- Life sciences (bioinformatics, biomedical research, neuroscience)
- Physical sciences (astronomy, physics, climate science)
- Scientific computing and data analysis
- Chemistry and materials science
- Other research-oriented domains where relevant

The final dataset will aim for a reasonably balanced representation
across domains rather than strict quotas.

## Language Diversity

Multiple programming languages will be represented where available,
including:

- Python
- R
- C/C++
- Julia
- Java
- Other languages commonly used in research software

The collection process will avoid over-representation of any single
language ecosystem.

## Inclusion Criteria

- Public GitHub repository
- README file present
- Documentation primarily available in English
- Repository not archived
- Minimum 20 GitHub stars
- At least one commit within the last three years
- Clear research or scientific computing relevance
- Repositories must contain sufficient documentation to
  enable assessment by both the rule-based and AI-based
  components.

## Exclusion Criteria

- Tutorial repositories
- Course assignments
- Template repositories
- Documentation-only repositories
- Personal experiments or toy projects
- General-purpose software with no identifiable research context

## Query Strategy

Repositories will be collected using the GitHub Search API with the
following 10 primary topics:

1. bioinformatics
2. computational-biology
3. astronomy
4. neuroscience
5. climate-science
6. scientific-computing
7. research-software
8. cheminformatics
9. computational-physics
10. reproducible-research

Each query will follow the pattern:

    topic:<topic> stars:>20 archived:false

Additional filters may be applied during post-processing
to enforce language diversity and activity requirements.

Collection will be capped per topic to ensure domain balance.
Additional repositories may be identified through known research
software organizations (e.g. numpy, scipy, astropy, biopython) if
topic-based queries return insufficient results for any domain.

## Bias Mitigation

Repositories will be sampled across multiple research domains and
programming languages. Collection results will be monitored throughout
the process to avoid over-representation of a single domain,
organization, or language ecosystem.

## Reproducibility

All GitHub API queries, parameters, collection dates, and filtering
criteria will be documented and stored within the project repository.
This enables future reproduction and extension of the dataset.