# Contributing

Contributions are welcome, especially corrections, local sources, household statistics, diaries, oral histories, price data and small details that conventional histories often omit.

## What makes a good contribution

A good contribution usually answers a concrete question such as:

- How did a household without a refrigerator store food in this place and period?
- What did a washing machine cost relative to wages?
- How long did a normal commute take?
- How frequently did trains or ships depart?
- How many households actually owned a telephone?
- What did a schoolchild do after class?
- How much time did laundry consume?
- What did a worker eat during a shift?
- What did an ordinary person consider a realistic future?

Small, well-sourced answers are more valuable than sweeping unsourced summaries.

## Please preserve place and population

Avoid:

> "People used refrigerators by 1930."

Prefer:

> "General Electric's Monitor Top became a widely popular household refrigerator in the United States after its 1927 introduction, while mass adoption continued through the 1930s."

Even better, add ownership data for a specific population when available.

## Keep original statistical units

If a source says:

> 42.33 refrigerators per 100 households

record that exact measure. Do not silently turn it into 42.33% of households.

## Separate evidence from reconstruction

Useful labels:

- **Measured**
- **Documented**
- **Scholarly reconstruction**
- **Illustrative**
- **Inference**
- **Uncertain**

If a diary records one household's breakfast, that is excellent evidence for that household. It is not automatically a national diet survey.

## Sources

Prefer, where possible:

1. official statistics and censuses
2. archival records and contemporary documents
3. museums and libraries
4. scholarly historical research
5. reliable syntheses

Advertisements, catalogues, manuals and fiction are valuable primary materials, but each proves something different.

An advertisement proves that a product was marketed, not that most people owned it.

A novel proves that an author could imagine or represent a practice, not that everyone lived that way.

## Politics

This project is about ordinary life rather than political controversy. Political or institutional context is appropriate when it is necessary to explain a concrete material condition such as schooling, rationing, housing, work, migration, infrastructure or access to goods.

Keep such discussion narrow, sourced and relevant to the life being reconstructed.

## Copyright

Do not upload copyrighted books, scans, photographs or interview collections merely because they are historically useful.

Prefer:

- bibliographic citation
- stable link
- archive identifier
- page number or timestamp
- concise summary
- short quotation only when wording matters

Respect the source institution's rights statement.

## AI-generated contributions

AI assistance is allowed, but AI-generated prose is not evidence.

An AI-assisted contribution should still provide checkable sources for factual claims. If a claim cannot be verified, label it as an open research question rather than smoothing over the gap.

## Suggested workflow

1. Start with a narrow question.
2. Find at least one strong source.
3. Preserve its population, place, year and unit.
4. Explain the lived consequence.
5. List what the source does **not** tell us.
6. Cross-link relevant technologies, places and literature.
7. Run `python scripts/validate_repository.py` when changing data files or local links.

The repository should grow like a map: many small, reliable connections rather than one giant claim to explain all of human life.
