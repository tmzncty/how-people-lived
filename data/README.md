# Data

Machine-readable tables used by the project live here.

## Conventions

- Preserve the source's original statistical unit.
- Keep geographic scope explicit.
- Keep population scope explicit.
- Use blank values for unavailable observations; do not interpolate silently.
- Keep source URLs or bibliographic identifiers alongside the data.
- If values for different years come from different historical tables, record the source for each relevant range.
- Do not convert units-per-100-households into household percentages unless the original source actually reports percentages.
- Preserve meaningful population splits such as urban/rural or farm/non-farm instead of collapsing them into a national average.
- Do not compare nominal money values across decades without considering price change.
- Life-horizon data should define the boundary of plausible choices, not pretend to measure private desire directly.
- If a published source gives only an approximate benchmark such as "about 42%" or "near 80%," preserve that uncertainty explicitly instead of fabricating precision.
- Qualitative comparison CSVs must be clearly labeled as **research scaffolds**, not measured survey variables.

## China — material conditions

### `china-household-durables-1985-2000.csv`

Selected urban/rural durable-goods benchmarks including washing machines, refrigerators, color televisions and electric fans.

### `china-household-income-engel-1978-2005.csv`

Historical urban/rural household income and Engel-coefficient series.

Source: https://www.stats.gov.cn/sj/ndsj/2007/html/J1002e.htm

### `china-housing-space-1978-2005.csv`

Selected National Bureau of Statistics per-capita residential floor-space benchmarks for urban and rural residents.

Important: this file uses the later historical **residential floor space** series. It should not be silently mixed with older tables reporting narrower **net living space** measures.

Source: https://www.stats.gov.cn/sj/ndsj/2008/html/J0935e.htm

### `china-household-size-1980-2005.csv`

Selected urban and rural average household-size benchmarks.

Urban sources:

- https://www.stats.gov.cn/english/Statisticaldata/yearlydata/YB2001e/htm/J1004e.htm
- https://www.stats.gov.cn/sj/ndsj/2006/html/J1005e.htm

Rural source:

- https://www.stats.gov.cn/yearbook/1999/j14c.htm

### `china-urban-homeownership-1988-2002.csv`

Selected CHIP-based benchmarks from published research on urban housing-tenure transformation.

The 1995 and 2002 observations are explicitly approximate because the source reports them as approximately 42% and near 80%.

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11771467/

## China — education and adulthood

### `china-1977-gaokao-benchmark.csv`

Historical benchmark for the 1977 national university entrance examination:

- applicants: about 5.7 million;
- admitted: 272,971;
- admission rate: 4.78%.

This is useful as a **scarcity benchmark**, not a complete higher-education time series.

Source: https://www.chinadaily.com.cn/cndy/2015-03/31/content_19957679.htm

### `china-higher-education-gross-enrollment-1990-2004.csv`

Ministry of Education historical higher-education gross-enrolment rates.

Useful for studying when university moves from a rare visible route toward a mass family-planning question.

Source: https://www.moe.gov.cn/jyb_sjzl/moe_560/moe_1389/moe_1390/moe_1393/201002/t20100226_20347.html

### `china-old-age-support-expectations-charls.csv`

Urban/rural differences in expected primary source of economic support in old age from a World Bank analysis using CHARLS.

This is a later-period expectation dataset, not evidence that the same percentages applied in earlier decades.

Source: https://documents1.worldbank.org/curated/en/099245006232237362/pdf/P1719590c42d060b209a3a0202aaea992e2.pdf

## China — migration

### `china-rural-urban-migrant-workers-1990-2022.csv`

World Bank / census / monitoring benchmarks for rural-to-urban migrant workers:

- 1990: 21.6 million;
- 2000: 78.8 million;
- 2008: 140.4 million;
- 2019: 174.3 million;
- 2022: 171.9 million.

Useful for showing when "go out to work" becomes a mass life route rather than a marginal exception.

Source: https://documents1.worldbank.org/curated/en/099020325194013546/pdf/P180848-980daabd-c4df-4314-a796-5df3bf5c97c5.pdf

## China — Internet, pandemic and AI

### `china-internet-scale-1997-2011.csv`

Selected CNNIC benchmarks for the transition from rare dial-up Internet to mass and mobile connectivity.

### `china-pandemic-graduate-cohorts-2020-2023.csv`

Ministry of Education benchmark figures for graduate cohorts entering the labor market during the pandemic period:

- 2020: 8.74 million;
- 2021: 9.09 million;
- 2022: 10.76 million;
- 2023: 11.58 million.

The file prevents pandemic recruitment disruption from being conflated with the simultaneous structural increase in graduate-cohort size.

### `china-pandemic-railway-passenger-trips-2019-2023.csv`

NBS railway passenger-trip benchmarks:

- 2019: 3.66 billion;
- 2020: 2.20 billion;
- 2021: 2.61 billion;
- 2022: 1.67 billion;
- 2023: 3.85 billion.

Useful for visualizing the contraction and rebound of ordinary intercity movement.

### `china-generative-ai-adoption-2024-2025.csv`

CNNIC-based benchmarks for generative-AI use in China.

Use with the Gen-Z / AI archive rather than treating adoption as proof of dependence or skill.

## China — generational comparison scaffolds

### `china-cohort-age-anchors-1955-2005.csv`

Simple arithmetic age anchors for six observation cohorts:

- 1955;
- 1965;
- 1975;
- 1985;
- 1995;
- 2005.

The file answers questions such as:

- how old was this cohort in 1977?
- what age was it when the Internet became visible?
- what age was it during the pandemic?
- had professional routines formed before generative AI arrived?

### `china-generational-life-course-matrix.csv`

Qualitative research scaffold comparing, by anchor cohort:

- formative household conditions;
- education problem;
- first-work problem;
- housing problem;
- information environment;
- later historical break;
- simplified adult problem.

This is **not survey data**. It is a machine-readable index into the repository's sourced research notes.

## United States

### `us-electric-service-1920-1940.csv`

U.S. Census Bureau historical benchmark percentages for electric service in all dwellings and farm dwellings in 1920, 1930 and 1940.

Source: https://www.census.gov/about/history/stories/monthly/2025/september-2025.html

## Why life-horizon data belongs here

The project reconstructs two linked layers:

1. **material possibility** — income, housing, infrastructure, technology, transport;
2. **life-course possibility** — education routes, work routes, migration, marriage, household formation, old-age support and cognitive tools.

Numbers do not reveal what a person privately wanted.

They help establish what a person was realistically planning around.

Examples:

- higher-education gross enrolment shows how ordinary university attendance could plausibly be;
- housing space shows how much privacy and household separation were physically possible;
- household size changes the number of people sharing labor and care;
- durable ownership shows what counted as normal domestic equipment;
- Internet scale shows whether online life was rare, destination-based, mass or mobile;
- migration counts show whether "go elsewhere to work" was marginal or ordinary;
- homeownership data show whether housing was allocated, privatized or market-purchased;
- pension/support expectations reveal whether old age is imagined through institutional retirement or intergenerational support;
- AI adoption shows scale, while qualitative sources are still needed to show how cognition actually changed.

## High-value future datasets

- historical price indices and durable-goods prices;
- rent/wage and home-price/income ratios;
- parental transfers for first-home purchase;
- water and sanitation access;
- telephone ownership;
- Internet-café prices and access patterns;
- SMS prices and message volumes;
- transport ownership;
- age at first marriage;
- school completion and transition rates;
- first-job duration and job-change rates by birth cohort;
- pension coverage by cohort;
- co-residence with elderly parents;
- household education expenditure;
- time-use by age and period;
- pandemic-era remote-work prevalence by occupation;
- desired working hours and commute by cohort;
- AI use by occupation and age;
- historical railway and steamship timetables;
- wage/fare comparisons;
- household fuel use;
- postal and telegram price/time comparisons.
