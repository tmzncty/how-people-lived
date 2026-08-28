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

## Current datasets

### `china-household-durables-1985-2000.csv`

Selected benchmark observations for urban and rural household durable goods in China, including washing machines, refrigerators, color televisions and electric fans. The file is intended for adoption-curve comparison while retaining links to National Bureau of Statistics source tables.

### `china-household-income-engel-1978-2005.csv`

National Bureau of Statistics historical series for:

- urban per-capita disposable income
- rural per-capita net income
- urban Engel coefficient
- rural Engel coefficient

The values make long-run changes in household budget structure visible. Nominal incomes should **not** be read as direct cross-year purchasing-power comparisons without additional price data.

Source: https://www.stats.gov.cn/sj/ndsj/2007/html/J1002e.htm

### `china-higher-education-gross-enrollment-1990-2004.csv`

Ministry of Education historical higher-education gross enrolment rates.

This dataset is useful for studying when university moved from an elite-visible route toward a much more ordinary family planning question.

Preserve the original measure: **gross enrolment rate**, not "percentage of people who went to university."

Source: https://www.moe.gov.cn/jyb_sjzl/moe_560/moe_1389/moe_1390/moe_1393/201002/t20100226_20347.html

### `us-electric-service-1920-1940.csv`

U.S. Census Bureau historical benchmark percentages for electric service in all dwellings and farm dwellings in 1920, 1930 and 1940. It preserves the large farm/non-farm infrastructure gap rather than treating national electrification as one event.

Source: https://www.census.gov/about/history/stories/monthly/2025/september-2025.html

## Why life-horizon data belongs here

The project now reconstructs two linked layers:

1. **material possibility** — income, housing, infrastructure, technology, transport;
2. **life-course possibility** — education routes, work routes, migration, marriage and household formation.

Some life-horizon boundaries can be measured indirectly.

Examples:

- higher-education gross enrolment tells us how ordinary university attendance could plausibly be;
- income and food-expenditure shares show how much household budget remained tied to necessities;
- household durable ownership shows what counted as normal domestic equipment;
- migration counts show whether "go elsewhere to work" was a marginal or mass route;
- marriage-age distributions show how the timing of household formation changed.

Numbers do not reveal what a person privately wanted. They help establish what a person was realistically planning around.

## Potential future datasets

- historical price indices and durable-goods prices
- housing floor area
- rent / wage and home-price / income ratios
- water and sanitation access
- telephone ownership
- transport ownership
- rural migrant-worker counts by destination and age
- age at first marriage
- school completion and transition rates
- historical railway and steamship timetables
- wage/fare comparisons
- household fuel use
- postal and telegram price/time comparisons
