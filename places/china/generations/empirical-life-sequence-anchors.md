# Empirical life-sequence anchors across Chinese cohorts

The repository's cohort framework began as a structural reconstruction:

> what institutions and technologies existed when a cohort reached a certain age?

This file marks the next stage:

> **what do event-history and cohort studies actually show about the order and timing of marriage, work, migration and housing?**

The purpose is not to build one universal Chinese life sequence.

It is to connect the repository's conceptual timelines to measured transitions.

---

## 1. Marriage: a cohort transition that can now be plotted directly

CFPS 2018 cohort estimates provide a clean example.

### Men

Median age at first marriage:

- born before 1950: 23.3;
- 1950s: 24.4;
- 1960s: 23.3;
- 1970s: 24.3;
- 1980–84: 25.2;
- 1985–89: 26.0.

Share married before age 30:

- before 1950: 89.9%;
- 1950s: 91.8%;
- 1960s: 93.1%;
- 1970s: 87.6%;
- 1980–84: 81.5%;
- 1985–89: 72.6%.

### Women

Median age at first marriage:

- before 1950: 20.2;
- 1950s: 22.6;
- 1960s: 21.9;
- 1970s: 22.4;
- 1980–84: 23.1;
- 1985–89: 23.3.

Share married before age 30:

- before 1950: 98.0%;
- 1950s: 97.0%;
- 1960s: 97.3%;
- 1970s: 96.5%;
- 1980–84: 94.2%;
- 1985–89: 90.9%.

Source:

- Yu et al., *Is there a Chinese pattern of the second demographic transition?*: https://link.springer.com/article/10.1007/s42379-022-00113-0

Dataset:

- [`../../../data/china-first-marriage-by-birth-cohort-cfps2018.csv`](../../../data/china-first-marriage-by-birth-cohort-cfps2018.csv)

### What this changes in the cohort story

The historical claim should not be:

> “marriage suddenly became unimportant.”

The measured pattern is subtler:

- marriage remains highly prevalent;
- entry shifts later for younger cohorts;
- the proportion still unmarried at age 25 and 30 rises, especially among men;
- education, housing and labor-market position increasingly interact with timing.

So age 30 changes from a nearly completed family-formation stage for many older cohorts into a more variable transition point for younger cohorts.

---

## 2. Childbearing: family sequences stretch and diversify

CFPS 2018 cohort estimates also show changing childbirth patterns among women.

Published proportions with at least one child:

- before 1950: 97.4%;
- 1950s: 97.0%;
- 1960s: 97.9%;
- 1970s: 97.7%;
- 1980s: 90.8%;
- 1990s: 41.0% at the time of observation.

The younger cohorts are right-censored and must not be treated as completed-fertility estimates.

Among published cohort estimates, the median interval between first and second childbirth also varies substantially:

- before 1950: 3.7 years;
- 1950s: 4.4;
- 1960s: 5.8;
- 1970s: 9.5;
- 1980s: 7.9.

Source:

- Jia Yu, *Union formation and childbearing among Chinese youth*: https://journals.sagepub.com/doi/full/10.1177/2057150X211040936

Dataset:

- [`../../../data/china-childbearing-by-birth-cohort-cfps2018.csv`](../../../data/china-childbearing-by-birth-cohort-cfps2018.csv)

The life-course point is not only whether people had children.

It is whether childbirth followed marriage quickly, whether a second child followed soon, and how much of adult life occurred between milestones.

---

## 3. Migration: marriage, work and childbirth alter the probability of moving

A 2022 study using the 2014 CHARLS Life History Survey reconstructs migration histories for people born 1930–1969.

Source:

- Lyu Lidan & Zhao Xiangyu, *Migration History from a Gender Perspective: Based on 1930–1969 Birth Cohorts*: https://rkyj.ruc.edu.cn/EN/Y2022/V46/I1/54

The study uses event-history analysis and finds:

- clear birth-cohort differences in lifetime migration;
- clear gender differences;
- education raises migration opportunity;
- movement into nonagricultural employment raises migration opportunity;
- earlier marriage reduces subsequent migration;
- more childbirth reduces subsequent migration;
- divorce raises migration probability;
- marriage and childbirth affect women's migration more strongly than men's.

This is exactly why a life history cannot be represented as independent columns.

A job event can cause a move.

A marriage can reduce later mobility.

A child can change where work is feasible.

For women, those linkages can be stronger.

### Cohort timing

The study further notes that migration is strongly concentrated around ages 20–24 and that the historical environment encountered at that age differs by birth cohort.

That supports the repository's central generational method:

> **the same event matters differently depending on when it intersects the life course.**

---

## 4. Higher education creates a new transition between graduation and stable skilled work

China's 1999 accelerated higher-education expansion did more than raise enrollment.

A natural-experiment study uses nationally representative education/work histories to examine time to the first skilled job.

Source:

- Hao & Zhang, *China's College Expansion and the Timing of College-to-Work Transition*: https://pubmed.ncbi.nlm.nih.gov/32773820/

The study finds:

- the expansion delayed landing a first skilled job among technical-college graduates;
- four-year-college graduates did not show the same effect on job acquisition;
- family origin and social position continued to matter in entry into college before and after expansion.

This supports an important historical distinction:

> **graduation and stable occupational landing become separate statuses.**

For older cohorts, leaving school may lead almost directly into a durable work position.

For mass-higher-education cohorts, a new period can appear:

> graduation → search / temporary work / exam / internship → first satisfactory or skilled job.

The school-to-work transition itself becomes a life stage.

---

## 5. Housing: younger cohorts can enter ownership earlier even when housing is more expensive

A common modernization story would predict:

> higher housing prices → younger people always buy later.

Shanghai life-history evidence complicates that story.

A retrospective 2018–2019 survey analyzed four cohorts with discrete-time event-history models.

Source:

- Mu et al., *Generational variations in the timing of entry into homeownership in Shanghai*: https://journals.sagepub.com/doi/10.1177/00420980211040947

The study reports:

- first homeownership differs sharply by cohort and housing-reform period;
- many post-1960 and some post-1970 people entered ownership through work-unit housing privatization in 1995–2000;
- post-1980 and post-1990 cohorts entered ownership increasingly after 2010;
- younger cohorts entered homeownership at younger ages in the Shanghai sample;
- first homeownership became more synchronized with family formation among younger cohorts;
- family-of-origin resources became increasingly important.

This is a major warning for life-course interpretation.

A difficult market does not necessarily produce a later first-home age when:

- parents transfer capital;
- marriage creates strong demand for a marital home;
- older cohorts obtained ownership through privatization at later ages;
- younger cohorts enter a mature ownership society from the start.

So “first home age” must be interpreted together with **route of acquisition**.

---

## 6. Homeownership means different things by period

Other longitudinal research reinforces this point.

### Urban China, 1949–1994

A 20-city life-history survey analyzed transition to first homeownership.

Source:

- Huang, *The road to homeownership: a longitudinal analysis of tenure transition in urban China (1949–94)*: https://ideas.repec.org/a/bla/ijurrs/v28y2004i4p774-795.html

Homeownership under the older housing system did not have the same meaning as market purchase today.

Before later reforms, public-sector and public-housing position could actually reduce the likelihood of moving into ownership because strong institutional position already provided secure rental access.

### Guangzhou, 1980–2010

An event-history study distinguishes welfare-housing and commodity-housing routes and finds both period and cohort effects.

Source:

- https://link.springer.com/article/10.1186/s40711-019-0101-5

The lesson for the repository is:

> **the same milestone label can refer to different institutions.**

“Became a homeowner” must always be accompanied by:

- year;
- age;
- purchase/privatization/inheritance route;
- marriage stage;
- employer/family support.

---

## 7. A first empirical sequence matrix

The evidence above suggests several distinct adult sequences.

These are not universal models; they are research hypotheses grounded in measured transitions.

### Older institutional urban sequence

> school exit → durable job → marriage → institution/family housing → children → later conversion to ownership → retirement

### Reform-transition urban sequence

> school → first job → marriage → housing privatization / purchase → possible job change → children's education → pension-backed later life

### Rural migration sequence

> school/household work → first migration → nonagricultural employment → marriage/childbirth changes mobility → repeated migration or return → rural/urban split household → later work + grandchild care

### Mass-higher-education sequence

> longer schooling → graduation → search for skilled landing → job/city choice → rent → parental support / first home → marriage / childbearing later and less uniformly timed

### AI-era sequence now emerging

> long education → pandemic/digital schooling memory → AI-assisted learning → graduation → uncertain first skilled job → portfolio of exams/work/credentials → housing and family decisions while cognitive work itself changes

The last sequence is not yet historically settled and must be preserved as provisional.

---

## 8. What the next analysis should derive

With CHARLS and CFPS documentation now identified, the highest-value derived statistics are:

### Work

- age at first paid/nonagricultural work by cohort;
- first-job duration;
- number of jobs by ages 30 and 40;
- age at first voluntary change;
- retirement age.

### Migration

- age at first migration;
- number of migration episodes;
- migration before/after marriage;
- migration before/after childbirth;
- gender gap by cohort.

### Family

- age at first marriage by cohort/origin/education;
- time from marriage to first child;
- age at first child;
- interval to second child;
- co-residence with parents after marriage.

### Housing

- age at first independent residence;
- age at first ownership;
- route into ownership;
- parental transfer;
- relationship between marriage and ownership.

The repository should publish only derived, non-identifying statistics and analysis methods when microdata redistribution is restricted.

---

## Core insight

The central unit of ordinary-life history is increasingly becoming:

> **transition + age + sequence + institution.**

Not simply:

> “This person had a job, a spouse and a home.”

But:

> “At what ages did those things arrive, in what order, through which institutions, and how did one transition alter the probability of the next?”

That is the empirical form of the project's life-horizon method.
