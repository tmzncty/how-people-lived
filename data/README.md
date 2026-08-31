# Data

Machine-readable tables used by the project live here.

This directory contains two different kinds of machine-readable material:

1. **measured data** — published statistics or values extracted from a documented study;
2. **research scaffolds** — qualitative cohort maps created by the repository to organize sourced evidence.

Never confuse the two.

## Conventions

- Preserve the source's original statistical unit.
- Keep geographic and population scope explicit.
- Use blank values for unavailable observations; do not interpolate silently.
- Keep source URLs / bibliographic identifiers with the data.
- Preserve urban/rural, sex, cohort and other meaningful splits.
- Do not convert units-per-100-households into household percentages unless the source does so.
- Do not compare nominal money values across decades without price adjustment/context.
- If the source says “about” or “near,” preserve that uncertainty.
- Mark censored younger cohorts explicitly.
- Life-horizon statistics establish the boundary of plausible choices; they do not directly measure private desire.
- Qualitative comparison CSVs must be labeled **research scaffold**.
- Keep dataset filenames as lowercase kebab-case CSVs directly inside `data/`; nested or mixed-case CSVs fail validation.

## Dataset manifest and validation

[`dataset-manifest.json`](dataset-manifest.json) is the machine-readable provenance index for every CSV in this directory. Its contract lives in [`../schemas/dataset-manifest.schema.json`](../schemas/dataset-manifest.schema.json).

The manifest records, without pretending to replace row-level documentation:

- whether a file is measured data or a research scaffold;
- geographic and temporal scope;
- the expected record count;
- which CSV columns carry row-level source locators;
- a short description suitable for indexing.

Run this before submitting a data or navigation change:

```bash
python scripts/validate_repository.py
```

The standard-library validator checks that every `data/*.csv` file is indexed exactly once, declared source columns exist, every measured row retains at least one source locator, record counts stay synchronized, CSV rows have consistent widths, and canonical inline Markdown link destinations stay inside the repository and exist. It also keeps the shipped schema aligned on its closed Draft 2020-12 root and dataset fields; full JSON Schema semantics remain the job of a dedicated implementation. Reference-style links are rejected in favor of inline links; raw HTML links and fragment identifiers are outside the validator's scope. Research scaffolds may omit row-level source columns, but must remain explicitly classified as scaffolds.

## Data sub-indexes

- [Empirical Life-Sequence Data Index](INDEX-life-sequence-data.md)
- [Family Life-Course Data Index](INDEX-family-life-course-data.md)

---

# China — material household conditions

## `china-household-durables-1985-2000.csv`

Selected urban/rural ownership benchmarks (original unit: units per 100 households) for washing machines, refrigerators, color televisions and electric fans.

Primary NBS historical sources include:

- urban: https://www.stats.gov.cn/english/Statisticaldata/yearlydata/YB1999e/j06e.htm
- rural: https://www.stats.gov.cn/english/Statisticaldata/yearlydata/YB2000e/J24E.htm

## `china-household-income-engel-1978-2005.csv`

Urban per-capita disposable income, rural per-capita net income and urban/rural Engel coefficients.

Source:

- https://www.stats.gov.cn/sj/ndsj/2007/html/J1002e.htm

Nominal incomes are not direct cross-year purchasing-power measures.

## `china-housing-space-1978-2005.csv`

Selected per-capita residential floor-space benchmarks for urban/rural residents.

Source:

- https://www.stats.gov.cn/sj/ndsj/2008/html/J0935e.htm

Do not silently mix this residential-building floor-space series with narrower historical “net living space” measures.

## `china-household-size-1980-2005.csv`

Selected average urban/rural household-size benchmarks.

Useful for family labor, sibling availability, concentrated child investment and later elder-care sharing.

## `china-urban-homeownership-1988-2002.csv`

Selected CHIP-based urban homeownership benchmarks.

Early increases were heavily shaped by privatization of public housing; ownership should not be interpreted as pure commercial-market purchase.

Source:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11771467/

---

# China — education and school-to-work

## `china-1977-gaokao-benchmark.csv`

Historical scarcity benchmark:

- applicants: about 5.7 million;
- admissions: 272,971;
- admission rate: about 4.78%.

Source:

- https://www.chinadaily.com.cn/cndy/2015-03/31/content_19957679.htm

## `china-higher-education-gross-enrollment-1990-2004.csv`

Ministry of Education higher-education gross-enrolment benchmarks.

Selected values:

- 1990: 3.4%;
- 1995: 7.2%;
- 2000: 12.5%;
- 2004: 19.0%.

Source:

- https://www.moe.gov.cn/jyb_sjzl/moe_560/moe_1389/moe_1390/moe_1393/201002/t20100226_20347.html

## `china-educational-mobility-1986-1995-selected.csv`

Selected rank-rank intergenerational educational-mobility coefficients.

Illustrative father-daughter contrast for 1986–95 births:

- urban-hukou origin: 0.51;
- rural-hukou origin: 0.27.

Higher correlation means stronger persistence, not higher attainment.

Source:

- https://link.springer.com/article/10.1007/s11113-024-09887-2

## School-to-work sequence evidence (no simple CSV yet)

A 2025 CGSS sequence analysis reconstructs ages 10–29 for people born 1946–1995 and identifies:

- early transition;
- delayed transition;
- unsmooth transition;
- reversed transition.

See:

- [`../topics/school-to-work-transition-as-a-life-stage.md`](../topics/school-to-work-transition-as-a-life-stage.md)

Source:

- https://www.tandfonline.com/doi/full/10.1080/21620555.2025.2480280

---

# China — employment and migration

## `china-job-tenure-urban-resident-migrant-1999.csv`

One historical comparison from the 1999 survey analyzed by Knight & Yueh:

- urban residents: mean job tenure 19.9 years;
- rural–urban migrants: 4.5 years.

Source:

- https://www.sciencedirect.com/science/article/pii/S0147596704000551

Do not generalize these two samples to all Chinese workers.

## `china-rural-urban-migrant-workers-1990-2022.csv`

Selected national migrant-worker stock estimates:

- 1990: 21.6 million;
- 2000: 78.8 million;
- 2008: 140.4 million;
- 2019: 174.3 million;
- 2022: 171.9 million.

Source:

- https://documents1.worldbank.org/curated/en/099020325194013546/pdf/P180848-980daabd-c4df-4314-a796-5df3bf5c97c5.pdf

This shows when “go out to work” becomes a mass route. It does not reveal individual migration sequences.

---

# China — marriage, childbearing and household formation

## `china-first-marriage-age-selected-1990-2021.csv`

Selected **period** mean-age-at-first-marriage endpoints.

1990:

- men 23.57;
- women 22.02.

2021:

- men 25.63;
- women 23.89.

Source:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC9516001/

## `china-first-marriage-by-birth-cohort-cfps2018.csv`

CFPS 2018 **birth-cohort** first-marriage timing table.

Contains:

- median first-marriage age;
- married before 25;
- before 30;
- before 35;
- before 40 where sufficiently observed.

Cohorts range from pre-1950 through 1985–89.

Source:

- https://link.springer.com/article/10.1007/s42379-022-00113-0

Period and cohort marriage measures answer different questions and should not be mixed.

## `china-childbearing-by-birth-cohort-cfps2018.csv`

Published CFPS 2018 cohort estimates for women:

- at least one child;
- second child;
- second child among mothers;
- median first-to-second-birth interval.

Source:

- https://journals.sagepub.com/doi/full/10.1177/2057150X211040936

The 1980s/1990s cohorts are incompletely observed; especially the 1990s values are **not completed-fertility estimates**.

---

# China — intergenerational family and later life

## `china-old-age-support-expectations-charls.csv`

Urban/rural differences in expected primary economic support in old age.

Useful for showing pension-backed versus child-supported old-age horizons.

Source:

- https://documents1.worldbank.org/curated/en/099245006232237362/pdf/P1719590c42d060b209a3a0202aaea992e2.pdf

## `china-retirement-rates-charls-2018.csv`

Weighted CHARLS 2018 retirement rates by age, sex and urban/rural residence.

Selected totals:

- age 60–64: urban 70.8%, rural 26.1%;
- age 65–69: urban 81.3%, rural 35.2%;
- age 70–74: urban 83.4%, rural 45.0%.

Source:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC10187591/

## `china-elderly-coresidence-with-adult-children-1982-2010.csv`

Selected census-based endpoints for age 65+ living with adult children:

- 1982: 69.4%;
- 2010: 51.7%.

Source:

- https://www.demographic-research.org/volumes/vol41/48/41-48.pdf

Declining co-residence does not mean family support disappears.

## `china-grandparent-care-urban-rural-charls-2011.csv`

CHARLS 2011–2012 analytic-sample participation in grandchild care:

- rural: 42.69%;
- urban: 48.01%.

Source:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC6244459/

Participation is not care intensity.

---

# China — communications and Internet

## `china-internet-scale-1997-2011.csv`

Selected CNNIC benchmarks for the transition from rare dial-up use to mass/mobile connectivity.

Useful for cohort history: a 1990-born child can move from nearly offline childhood to mass mobile Internet by early adulthood.

## `china-household-communication-devices-2000-2010.csv`

Urban/rural household computers and mobile phones per 100 households.

Selected 2000 contrast:

- urban computers 9.70 / rural 0.47;
- urban mobile phones 19.50 / rural 4.32.

Selected 2010 contrast:

- urban computers 71.16 / rural 10.37;
- urban mobile phones 188.86 / rural 136.54.

Sources:

- urban: https://www.stats.gov.cn/sj/ndsj/2012/html/J1010e.htm
- rural: https://www.stats.gov.cn/sj/ndsj/2012/html/J1030e.htm

---

# China — pandemic

## `china-pandemic-graduate-cohorts-2020-2023.csv`

Graduate-cohort planning benchmarks:

- 2020: 8.74 million;
- 2021: 9.09 million;
- 2022: 10.76 million;
- 2023: 11.58 million.

Use to distinguish pandemic recruitment disruption from the structural rise in cohort size.

## `china-pandemic-railway-passenger-trips-2019-2023.csv`

Railway passenger trips:

- 2019: 3.66 billion;
- 2020: 2.20 billion;
- 2021: 2.61 billion;
- 2022: 1.67 billion;
- 2023: 3.85 billion.

Use as a mobility-system benchmark, not as an explanation for individual travel.

---

# China — generative AI

## `china-generative-ai-adoption-2024-2025.csv`

CNNIC-based benchmarks for generative-AI use.

Use with:

- [`../INDEX-gen-z.md`](../INDEX-gen-z.md)
- [`../topics/ai-as-cognitive-infrastructure.md`](../topics/ai-as-cognitive-infrastructure.md)

Adoption is not proof of skill, dependence or cognitive change by itself.

---

# China — cohort research scaffolds

## `china-cohort-age-anchors-1955-2005.csv`

Arithmetic age anchors for c.1955 / 1965 / 1975 / 1985 / 1995 / 2005.

## `china-generational-life-course-matrix.csv`

**Research scaffold**, not survey data.

Summarizes sourced cohort interpretations across:

- childhood material conditions;
- education problem;
- first-work problem;
- housing problem;
- information environment;
- historical breaks;
- simplified adult problem.

---

# United States

## `us-electric-service-1920-1940.csv`

U.S. Census Bureau historical percentages for electric service in all dwellings and farm dwellings.

Source:

- https://www.census.gov/about/history/stories/monthly/2025/september-2025.html

---

# Why life-course data belongs here

Numbers do not reveal what someone privately wanted.

They establish what was realistically possible and how common a route could be.

The project increasingly distinguishes:

- **stock/status data** — what someone has now;
- **period data** — what happens in a calendar year;
- **cohort data** — what happens to people born in a particular period;
- **event-history data** — when a transition occurs;
- **sequence data** — the order/duration of multiple transitions.

The strongest ordinary-life reconstruction combines these levels.

## Highest-value future derived datasets

Primary next targets:

- first-work age by birth cohort;
- first-job duration by cohort;
- number of jobs by age 30/40;
- first migration age / episode count;
- first-marriage age by cohort × origin × education;
- marriage-to-first-child interval;
- first independent residence;
- first ownership age / route;
- parental first-home transfers;
- actual retirement age by cohort;
- grandchild-care hours;
- elder-care time and money transfers;
- AI use by age and occupation.

Primary data route:

- CHARLS 2014 Life History Survey;
- CFPS longitudinal/event-history modules;
- CGSS retrospective school/work histories.

Guide:

- [`../sources/life-history-survey-guide.md`](../sources/life-history-survey-guide.md)

## Final data rule

Do not infer a life sequence from current status.

A current homeowner may have:

- bought on the market;
- received privatized work-unit housing;
- inherited;
- received parental transfer.

A current worker may have started at 16 or 26.

A current married person may have married at 20 or 35.

Always preserve:

> **unit + population + age + period/cohort + transition definition + source.**
