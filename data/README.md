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

## Current datasets

### `china-household-durables-1985-2000.csv`

Selected benchmark observations for urban and rural household durable goods in China, including washing machines, refrigerators, color televisions and electric fans. The file is intended for adoption-curve comparison while retaining links to National Bureau of Statistics source tables.

### `us-electric-service-1920-1940.csv`

U.S. Census Bureau historical benchmark percentages for electric service in all dwellings and farm dwellings in 1920, 1930 and 1940. It preserves the large farm/non-farm infrastructure gap rather than treating national electrification as one event.

Source: https://www.census.gov/about/history/stories/monthly/2025/september-2025.html

Potential future datasets:

- household incomes and durable-goods prices
- housing floor area
- water and sanitation access
- telephone ownership
- transport ownership
- historical railway and steamship timetables
- wage/fare comparisons
- household fuel use
- postal and telegram price/time comparisons
