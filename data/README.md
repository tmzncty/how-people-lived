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
- Do not compare nominal money values across decades without considering price change. A nominal-income series is useful for contemporary budgets only when paired with prices, indices or expenditure structure.
- Life-horizon data should define the boundary of plausible choices, not pretend to measure private desire directly.
- If a published source gives only an approximate benchmark such as "about 42%" or "near 80%," preserve that uncertainty explicitly instead of fabricating precision.

## Current datasets

### `china-household-durables-1985-2000.csv`

Selected benchmark observations for urban and rural household durable goods in China, including washing machines, refrigerators, color televisions and electric fans.

### `china-household-income-engel-1978-2005.csv`

National Bureau of Statistics historical series for urban per-capita disposable income, rural per-capita net income and urban/rural Engel coefficients.

Source: https://www.stats.gov.cn/sj/ndsj/2007/html/J1002e.htm

### `china-higher-education-gross-enrollment-1990-2004.csv`

Ministry of Education historical higher-education gross enrolment rates, useful for studying when university became a mass family planning question rather than merely an elite-visible route.

Source: https://www.moe.gov.cn/jyb_sjzl/moe_560/moe_1389/moe_1390/moe_1393/201002/t20100226_20347.html

### `china-urban-homeownership-1988-2002.csv`

Selected CHIP-based benchmarks from published research on the rapid transformation of urban housing tenure.

The 1995 and 2002 observations are explicitly marked approximate because the source reports them as approximately 42% and near 80%, respectively.

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11771467/

### `china-old-age-support-expectations-charls.csv`

Urban/rural differences in expected primary source of economic support in old age from a World Bank analysis using CHARLS.

This is a later-period expectation dataset, not evidence that the same percentages applied in the 1980s or 1990s. Its value is to demonstrate that urban pension-backed retirement and rural family-supported old age can remain distinct life-horizon systems.

Source: https://documents1.worldbank.org/curated/en/099245006232237362/pdf/P1719590c42d060b209a3a0202aaea992e2.pdf

### `china-pandemic-graduate-cohorts-2020-2023.csv`

Ministry of Education benchmark figures for the ordinary higher-education graduate cohorts entering the labor market during the pandemic period:

- 2020: 8.74 million
- 2021: 9.09 million
- 2022: 10.76 million
- 2023: 11.58 million

The dataset is useful because it prevents two changes from being conflated:

1. the extraordinary disruption to recruitment and school-to-work transitions during the pandemic;
2. the simultaneous structural increase in the size of graduate cohorts.

The figures are cohort/planning figures used by the Ministry of Education in the relevant employment season. Do not substitute them silently for final statistical counts of all graduates under a different educational definition.

### `china-pandemic-railway-passenger-trips-2019-2023.csv`

National Bureau of Statistics railway passenger-trip benchmarks for the five years surrounding the pandemic break:

- 2019: 3.66 billion
- 2020: 2.20 billion
- 2021: 2.61 billion
- 2022: 1.67 billion
- 2023: 3.85 billion

The series is useful for visualizing how dramatically ordinary intercity movement contracted and then rebounded. It does **not** by itself explain why any individual trip occurred or failed to occur.

Sources are the NBS annual statistical communiqués for 2019–2023 and are retained row-by-row in the CSV.

### `us-electric-service-1920-1940.csv`

U.S. Census Bureau historical benchmark percentages for electric service in all dwellings and farm dwellings in 1920, 1930 and 1940.

Source: https://www.census.gov/about/history/stories/monthly/2025/september-2025.html

## Why life-horizon data belongs here

The project now reconstructs two linked layers:

1. **material possibility** — income, housing, infrastructure, technology, transport;
2. **life-course possibility** — education routes, work routes, migration, marriage, household formation and old-age support.

Some life-horizon boundaries can be measured indirectly.

Examples:

- higher-education gross enrolment tells us how ordinary university attendance could plausibly be;
- income and food-expenditure shares show how much household budget remained tied to necessities;
- household durable ownership shows what counted as normal domestic equipment;
- migration counts show whether "go elsewhere to work" was a marginal or mass route;
- marriage-age distributions show how the timing of household formation changed;
- housing tenure shows whether independent housing was mainly allocated, rented, subsidized or market-purchased;
- pension/support expectations reveal whether old age is imagined primarily through institutional retirement or intergenerational family support;
- graduate cohort sizes show how many people are entering the school-to-work transition at the same time, but do not by themselves reveal employment quality;
- transport series show whether ordinary movement expanded or contracted but do not directly reveal subjective experience.

Numbers do not reveal what a person privately wanted. They help establish what a person was realistically planning around.

## Potential future datasets

- historical price indices and durable-goods prices
- housing floor area
- rent / wage and home-price / income ratios
- parental transfers for first-home purchase
- water and sanitation access
- telephone ownership
- transport ownership
- rural migrant-worker counts by destination and age
- age at first marriage
- school completion and transition rates
- first-job duration and job-change rates
- pension coverage by population
- co-residence with elderly parents
- household education expenditure
- pandemic-era remote-work prevalence by occupation
- online recruitment and interview adoption
- desired working hours and commuting time by cohort
- historical railway and steamship timetables
- wage/fare comparisons
- household fuel use
- postal and telegram price/time comparisons
