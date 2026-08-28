# How People Lived

> A public, source-based atlas of ordinary life across time.
>
> Not only **what happened in history**, but **what a person could actually eat, wear, buy, use, know, expect, and do**.

History is often organized around states, wars, institutions, inventions, and famous people. Those things matter, but they can leave a surprisingly simple question unanswered:

**What did it feel like to live an ordinary day in that world?**

This repository collects evidence about everyday life: housing, food, work, income, prices, transport, communication, household technology, education, leisure, family life, hygiene, health, time use, and the futures people could realistically imagine for themselves.

It is intended both as a small digital-history project and as a **context companion for reading literature**. If a novel mentions a railway, a steam packet, a refrigerator, a boarding house, a telegram, a servant, a bicycle, or a week's wages, this project asks what those things meant in the material world of the time.

## The central rule: invention is not availability

A technology can exist for decades before it becomes part of ordinary life.

For every technology, service, or convenience, we try to distinguish:

1. **technical existence** — could it be built at all?
2. **commercial availability** — could someone buy or use it somewhere?
3. **infrastructure availability** — did electricity, water, roads, rails, fuel, repair networks, etc. support it?
4. **economic accessibility** — could an ordinary household afford it?
5. **social distribution** — who actually had access: urban/rural, rich/poor, region, occupation, gender, age?
6. **mass adoption** — when did it become normal rather than exceptional?
7. **behavioral effect** — when did it actually change how people cooked, washed, traveled, communicated, worked, or planned their lives?

For example, household refrigerators existed long before they became ordinary possessions everywhere. Chinese statistical yearbooks show the importance of place and social distribution: in 1985 urban China had 6.58 refrigerators per 100 households, rising to 42.33 in 1990 and 66.22 in 1995. Rural households had only 1.22 refrigerators per 100 households in 1990 and 5.15 in 1995. A statement such as "refrigerators existed in the 1980s" therefore tells us almost nothing about a particular family's daily life.

Sources: National Bureau of Statistics of China, historical statistical yearbook tables on durable consumer goods: [urban households](https://www.stats.gov.cn/english/Statisticaldata/yearlydata/YB1999e/j06e.htm) and [rural households](https://www.stats.gov.cn/english/Statisticaldata/yearlydata/YB2000e/J24E.htm).

## What belongs here

We are interested in both **material conditions** and **lived experience**.

### Material foundations

- wages, prices, working hours, household budgets
- food supply, cooking fuel, preservation and shopping frequency
- housing size, heating, lighting, water, sanitation
- clothing, laundry, sewing and repair
- electricity, gas, plumbing and telecommunications
- household appliances and their real adoption rates
- roads, railways, ships, bicycles, cars and public transport
- postal systems, telegraph, telephone, radio, television and computers
- schools, libraries, hospitals, shops and other everyday institutions
- production systems and supply chains that made consumption possible

### Life itself

- what a normal day looked like
- how much unstructured time people had
- what children did after school
- what work felt like hour by hour
- how people met friends or partners
- what counted as leisure
- how people dealt with boredom
- how often people traveled and how far
- what information reached them, and how quickly
- what people feared, hoped for, saved for, or expected from adulthood
- what choices were realistically available to them
- what was considered normal, luxurious, shameful, dangerous, or impossible

## Not a political-event encyclopedia

Politics can affect everyday life and cannot always be removed from historical explanation. But this repository is **not organized around political controversy**. When political or institutional conditions are necessary to explain housing, work, schooling, migration, rationing, infrastructure, or other aspects of daily life, they should be described narrowly, factually, and with sources.

The organizing question remains: **how did people live?**

## Literature as a window — and a problem

Literature is one of the reasons this repository exists.

A reader of *Around the World in Eighty Days* may know that Phileas Fogg travels rapidly around the globe, but the plot becomes much more intelligible when placed beside the material network available in the early 1870s: steamships, mail packets, the Suez Canal, expanding Indian railways, and the recently completed U.S. transcontinental railroad. The novel's famous timetable is not merely fantasy; it is built around a newly connected transport system.

See: [`literature/around-the-world-in-eighty-days.md`](literature/around-the-world-in-eighty-days.md).

Literary texts are evidence, but not transparent records. A novel may depict an elite household, exaggerate for comedy, omit routine labor, or assume contemporary knowledge that modern readers no longer possess. Where possible, literary examples should be checked against statistics, manuals, advertisements, diaries, letters, oral histories, newspapers, photographs, catalogues, and scholarly research.

## Repository map

```text
how-people-lived/
├── README.md
├── README.zh-CN.md
├── METHODOLOGY.md
├── CONTRIBUTING.md
├── templates/
│   ├── life-slice.md
│   └── technology-adoption.md
├── foundations/
│   ├── README.md
│   └── technology-existence-vs-adoption.md
├── places/
│   └── china/
│       ├── 1980s-urban-household-technology.md
│       └── 1990s-rural-household-technology.md
├── literature/
│   ├── README.md
│   └── around-the-world-in-eighty-days.md
├── topics/
│   ├── refrigeration.md
│   └── laundry-and-washing-machines.md
├── sources/
│   └── source-catalog.md
└── data/
    └── china-household-durables-1985-2000.csv
```

This structure will grow. Period, place, class and rural/urban differences should be preserved rather than flattened into a single timeline.

## Evidence levels

Entries should make clear what kind of claim is being made.

- **Measured** — census, household survey, price series, timetable, wage table, official statistics.
- **Documented** — diary, letter, oral testimony, contemporary manual, advertisement, photograph.
- **Scholarly reconstruction** — supported by secondary historical research.
- **Illustrative** — a literary or anecdotal example used to make a condition easier to understand.
- **Uncertain** — plausible, but evidence is incomplete or contradictory.

Do not convert "available somewhere" into "normal everywhere".

## A useful unit: the life slice

Instead of trying to summarize an entire society in a paragraph, contributors are encouraged to build **life slices**: a specific kind of person in a specific place and period.

Examples:

- an urban Chinese household in 1985
- a rural Chinese household in 1995
- a London clerk in the early 1870s
- an Atlantic steamship passenger in the 1890s
- a U.S. factory worker in 1910
- a British household using an icebox in the 1920s

A life slice should answer concrete questions: Where do they sleep? What do they eat? How do they wash clothes? How far do they travel? How much do things cost? What technologies are genuinely available to them? What does a day feel like?

## Source and copyright policy

This repository primarily stores **research notes, structured data, summaries, and citations**, not indiscriminate copies of archival material.

- Public-domain material may be quoted or transcribed where useful.
- Modern copyrighted books and archival scans should normally be cited, linked, and summarized rather than copied wholesale.
- Short quotations should be used only where wording itself matters.
- Every quantitative claim should identify its unit, place, period, and source.
- Retrospective oral histories and memoirs should be marked as retrospective memory, not treated as contemporaneous recordings without qualification.

## AI authorship

The initial structure and a substantial part of the early research notes in this repository were written by **OpenAI GPT-5.6 Sol**, working with the repository owner. AI-written historical material should not be trusted merely because it sounds plausible: claims are expected to remain traceable to human-readable sources, and corrections are welcome.

## The question behind the project

A historical person was not a modern person wearing old clothes.

Their range of possible actions was shaped by income, infrastructure, production, transport, information, institutions, household technology, geography, social expectations, and simple physical limits. If we reconstruct those conditions carefully, unfamiliar choices in history and literature often become much easier to understand.

The aim is not to make the past quaint.

The aim is to make it **inhabitable enough to imagine**.
