# Empirical Life-Sequence Data Index

This index collects machine-readable files that help reconstruct **the timing and ordering of life transitions**.

The key unit is not a status but an event:

> education exit → first work → migration → marriage → household formation → children → housing → retirement

Not every person follows this order. The purpose of the data is precisely to make variation visible.

## Marriage by birth cohort

### `china-first-marriage-by-birth-cohort-cfps2018.csv`

CFPS 2018 cohort table containing median first-marriage age and percentages married before age 25, 30, 35 and 40 where sufficiently observed.

Birth cohorts:

- before 1950;
- 1950–59;
- 1960–69;
- 1970–79;
- 1980–84;
- 1985–89.

Selected contrast:

- men married before age 30: 93.1% for 1960–69 versus 72.6% for 1985–89;
- women married before age 30: 97.3% versus 90.9%.

Source:

- https://link.springer.com/article/10.1007/s42379-022-00113-0

## Period first-marriage benchmark

### `china-first-marriage-age-selected-1990-2021.csv`

Keep this separate from the birth-cohort file above.

A period mean answers:

> how old were people marrying in that calendar year?

A cohort measure answers:

> how did the marriage sequence unfold for people born in a particular period?

Those are not interchangeable.

## Childbearing by birth cohort

### `china-childbearing-by-birth-cohort-cfps2018.csv`

Published CFPS 2018 cohort estimates for women:

- proportion with at least one child;
- proportion with second child;
- second child among mothers;
- median interval between first and second childbirth.

Important censoring warning: the 1980s and especially 1990s cohorts had not completed their reproductive life course at the survey date. Do not interpret their observed percentages as completed fertility.

Source:

- https://journals.sagepub.com/doi/full/10.1177/2057150X211040936

## Work attachment

### `china-job-tenure-urban-resident-migrant-1999.csv`

One cross-sectional historical benchmark:

- urban residents: mean tenure 19.9 years;
- rural–urban migrants: mean tenure 4.5 years.

Source:

- https://www.sciencedirect.com/science/article/pii/S0147596704000551

This is not yet a true birth-cohort first-job series. It demonstrates that different employment-time regimes coexisted in the same calendar year.

## Migration

### `china-rural-urban-migrant-workers-1990-2022.csv`

Mass-scale stock benchmarks. This establishes when migration becomes an ordinary route; it does not reconstruct individual migration sequences.

For event-history analysis, use:

- [`../places/china/generations/empirical-life-sequence-anchors.md`](../places/china/generations/empirical-life-sequence-anchors.md)
- [`../sources/life-history-survey-guide.md`](../sources/life-history-survey-guide.md)

## Housing

Current files:

- `china-urban-homeownership-1988-2002.csv` — period ownership benchmarks;
- `china-housing-space-1978-2005.csv` — physical residential space.

Still missing in machine-readable form:

- first-home age by cohort;
- route into first ownership;
- marriage-relative-to-first-home timing;
- parental transfer by cohort.

## Retirement

### `china-retirement-rates-charls-2018.csv`

Retirement status by age, sex and urban/rural residence.

This is an age-period snapshot, not a retrospective cohort retirement-age distribution. A future life-history analysis should derive actual age at retirement by birth cohort.

## Intergenerational family sequence

Useful files:

- `china-elderly-coresidence-with-adult-children-1982-2010.csv`;
- `china-grandparent-care-urban-rural-charls-2011.csv`;
- `china-old-age-support-expectations-charls.csv`.

These show what can happen after the classic “marriage + children” part of the sequence:

> adult children leave → parents age → co-residence/proximity/transfer → grandchild care → retirement/continued work.

## Education-to-work transition

No direct CSV has been created yet because the strongest current source reports causal findings rather than a simple reusable descriptive table.

Hao & Zhang find that China's accelerated 1999 higher-education expansion delayed the landing of a first skilled job for technical-college graduates, while four-year-college graduates did not show the same acquisition effect.

Source:

- https://pubmed.ncbi.nlm.nih.gov/32773820/

This is an important reminder:

> expanding education can lengthen the transition from school to occupational landing even while increasing educational attainment.

## Next derived datasets

Priority:

1. first-work age by birth cohort;
2. first-job duration by birth cohort;
3. number of jobs by age 30 / 40;
4. first migration age and migration episode count;
5. first marriage age by cohort × urban/rural × education;
6. marriage-to-first-child interval;
7. first independent residence;
8. first homeownership age and acquisition route;
9. actual retirement age by cohort;
10. grandparent-care start age and intensity.

## Data-source route

Primary next sources:

- CHARLS 2014 Life History Survey;
- CFPS longitudinal/event-history modules.

Guide:

- [`../sources/life-history-survey-guide.md`](../sources/life-history-survey-guide.md)

## Core rule

Do not infer sequence from current status.

A person who is currently married + homeowner + retired could have arrived through very different histories.

Life-course data should preserve:

> **age + transition + duration + order + institutional route.**
