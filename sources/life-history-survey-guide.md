# Life-History Survey Guide

This guide collects survey resources that can reconstruct **sequences of life events**, not just one cross-sectional snapshot.

The central methodological rule is:

> **A life is not a list of statuses. It is a sequence with dates, durations and transitions.**

For cohort history, this matters enormously.

Knowing that someone was married, employed and urban at age 60 is not enough.

We want to know:

- when education ended;
- when the first job began;
- how long it lasted;
- when migration occurred;
- when marriage happened;
- when residence changed;
- when housing was acquired;
- when parents died or needed support;
- when retirement began;
- when grandchild care began.

## 1. CHARLS 2014 Life History Survey

The China Health and Retirement Longitudinal Study (CHARLS) conducted a dedicated national life-history survey in 2014.

Official data page:

- https://charls.pku.edu.cn/en/Data/a2014_CHARLS_Life_History_Survey.htm

Chinese page:

- https://charls.pku.edu.cn/sj/a2014nqgzzdc_smlcdc_.htm

The official download page provides separate modules for:

- residence / migration;
- demographic background;
- family information;
- education history;
- health history;
- wealth history;
- work history;
- sample information.

This is extremely valuable for this repository because the survey was designed to reconstruct past experiences of middle-aged and older respondents rather than only their current status.

The project description states that the 2014 survey used retrospective interviews to record respondents' life experience from birth and was intended to help fill gaps in historical data after the founding of the PRC.

Source:

- https://charls.pku.edu.cn/info/1015/1108.htm

A project summary reports that the survey followed more than 20,000 people in over 10,000 households across 28 provinces/municipalities.

Source:

- https://charls.pku.edu.cn/info/1015/1110.htm

### What this can answer for the repository

For people born c.1950s–1960s, CHARLS life history can potentially reconstruct:

- childhood household background;
- rural/urban residence changes;
- complete education sequence;
- work sequence;
- migration;
- housing/wealth history;
- family history;
- retirement and later-life status.

This is exactly the kind of evidence needed to move from structural cohort summaries toward real life-course sequences.

### High-value extraction projects

Potential derived files should be created only after checking documentation and variable definitions.

Useful future projects:

- first-job start age by birth cohort;
- number of jobs before age 40;
- age at first urban migration;
- first residential move after marriage;
- retirement age by cohort and hukou/origin;
- first home / major housing event;
- education interruption and return;
- parent survival and intergenerational overlap.

Do not upload the raw survey dataset to this repository unless licensing explicitly permits redistribution.

Store:

- variable definitions;
- derived aggregates;
- analysis code where appropriate;
- citations to the original data source.

## 2. China Family Panel Studies (CFPS)

Official project page:

- https://www.isss.pku.edu.cn/cfps/index.htm

English introduction:

- https://www.isss.pku.edu.cn/cfps/en/about/introduction/index.htm

Public data archive:

- https://opendata.pku.edu.cn/dataverse/cfps_public

CFPS is a nationally representative longitudinal survey covering individuals, families and communities, launched nationally in 2010.

It follows family members over time and contains information on:

- economic activity;
- education;
- family dynamics;
- migration;
- health;
- household resources.

An introduction to the CFPS explicitly describes integrated rural/urban modules and event histories including marriage, education and employment.

Source:

- Xie & Hu, *An Introduction to the China Family Panel Studies*: https://www.isss.pku.edu.cn/cfps/docs/20201225093508045085.pdf

### Event History Calendar

From 2014 onward, CFPS documentation includes an event-history-calendar design for recording changes in residence, marriage status and jobs.

The public documentation archive includes:

- technical report 038 on the event-history-calendar design;
- cross-wave core-variable reports;
- questionnaires and user guides.

Archive:

- https://opendata.pku.edu.cn/dataverse/cfps_public

### Why CFPS complements CHARLS

CHARLS is especially powerful for reconstructing older cohorts retrospectively.

CFPS is especially powerful for:

- following contemporary families prospectively;
- connecting parent and child information;
- observing household resources and transfers;
- studying education and marriage histories;
- tracking residence and job changes in later waves.

Together they allow a useful division:

> **older-cohort retrospective life history + newer-cohort longitudinal family history**

## 3. Why event-history data matters

A conventional cross-section can tell us:

> Person A is 45, married, employed and owns a home.

A life-history dataset can potentially tell us:

> finished school at 18 → first job at 19 → married at 24 → moved city at 27 → changed jobs at 30 → acquired housing at 34.

This sequence reveals the actual structure of adulthood.

Two people with the same current status can arrive there through completely different routes.

## 4. Cohort questions to build

### Born c.1955

- age at first work;
- whether schooling resumed later;
- first marriage timing;
- first independent or allocated housing;
- number of jobs before retirement;
- urban/rural migration;
- actual retirement age.

### Born c.1965

- whether first job remained long-term;
- job changes during the 1990s;
- housing conversion/ownership;
- adult children's education;
- digital adoption after career formation.

### Born c.1975

- first voluntary job change;
- first migration episode;
- marriage relative to migration;
- first home during housing transition;
- number of employers by 40.

### Born c.1985

- education duration;
- first job duration;
- first home and parental support;
- marriage/cohabitation sequence;
- city mobility;
- first-child timing.

### Born c.1995 and later

CFPS and newer surveys can be used to follow:

- school-to-work transitions;
- postgraduate study;
- repeated job change;
- rent/home purchase;
- return migration;
- delayed family formation;
- pandemic interruption.

## 5. Parent-child linking

Family panel data becomes especially valuable when the analysis keeps generations linked.

Questions include:

- Did parents have less education than children?
- At what age did each generation begin paid work?
- Did parents help finance university?
- Did parents help finance housing?
- Did children later transfer money upward?
- Did grandparents provide childcare?

This makes it possible to reconstruct not only individual life courses but **family strategies across generations**.

## 6. Data ethics and preservation

This repository should not become a mirror of restricted microdata.

Preserve:

- source documentation;
- variable maps;
- derived non-identifying aggregates;
- reproducible analysis code where permitted;
- notes on weighting and sample definition;
- links to official repositories.

Do not publish:

- respondent-level identifiable data;
- restricted microdata;
- raw files whose license forbids redistribution.

## 7. A future analysis pipeline

For each life-history dataset:

1. read release notes and questionnaire;
2. identify event variables and date units;
3. define cohort and population precisely;
4. preserve rural/urban and gender splits;
5. reconstruct sequences;
6. calculate milestone timing;
7. validate suspicious transitions;
8. publish only derived statistics and methods;
9. link results back to human-readable life-course notes.

## Core insight

The repository has already built a strong structural map.

Life-history surveys make the next step possible:

> **turning “people born in 1965 faced changing job rules” into “how many jobs did people born in 1965 actually move through, at what ages, and in what order?”**

That is the bridge from historical context to empirical life-course history.
