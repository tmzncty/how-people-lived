# China Time-Use Data Index

This index collects machine-readable time-use benchmarks used by the repository.

## 2018 selected data

- [`china-time-use-2018-selected.csv`](china-time-use-2018-selected.csv)

Source:

- National Bureau of Statistics, 2018 National Time Use Survey: https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900224.html

Includes selected:

- paid labor;
- unpaid labor;
- household work;
- childcare;
- employment-work participant time;
- transport;
- Internet use;
- sex and urban/rural differences.

## 2024 selected data

- [`china-time-use-2024-selected.csv`](china-time-use-2024-selected.csv)

Sources:

- https://www.stats.gov.cn/english/PressRelease/202411/t20241115_1957436.html
- https://www.stats.gov.cn/english/PressRelease/202411/t20241115_1957437.html

Includes selected:

- resident-average and participant-average paid labor;
- unpaid labor;
- discretionary time;
- transportation;
- ICT use;
- sex, urban/rural and broad age-group splits.

## Comparison rule

Do not treat 2018 and 2024 as a perfectly harmonized time series.

The 2024 survey changed geographic/age coverage, categories and collection method.

Use:

- official NBS 2008→2018 comparisons for explicit historical trends;
- 2018 and 2024 as strong period cross-sections;
- harmonized categories only when definitions have been checked.

See:

- [`../sources/time-use-source-guide.md`](../sources/time-use-source-guide.md)
- [`../INDEX-time-use.md`](../INDEX-time-use.md)

## Important measure distinctions

### Resident/population average

Average minutes across everyone in the target population, including people who did not perform the activity.

### Participant average

Average minutes only among people who actually performed the activity.

### Participation rate

Share of the population that performed the activity during the survey day(s).

### ICT/Internet time

Can overlap primary activities.

Do not add ICT minutes to the six primary activity domains as if the day exceeded 24 hours.

## Future data targets

- age × sex detailed tables;
- parent time by age of youngest child;
- commute by city size;
- remote-work time use;
- elder-care hours;
- grandparent-care hours;
- AI-assisted work/study time;
- comparable 2008 microtables where definitions permit.
