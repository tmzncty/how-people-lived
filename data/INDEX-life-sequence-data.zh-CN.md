# 实证生命序列数据索引

这个索引收集有助于重构**人生转变的时间与顺序**的机器可读文件。

关键单位不是状态，而是事件：

> 离开教育 → 第一份工作 → 迁移 → 结婚 → 成家 → 生育 → 住房 → 退休

并不是每个人都按这个顺序走。数据的目的，恰恰是让差异变得可见。

## 分出生世代的婚姻

### `china-first-marriage-by-birth-cohort-cfps2018.csv`

CFPS 2018 的世代表，包含初婚年龄中位数，以及观测充分时 25、30、35、40 岁前结婚的比例。

出生世代：

- 1950 年前；
- 1950–59；
- 1960–69；
- 1970–79；
- 1980–84；
- 1985–89。

部分对照：

- 30 岁前结婚的男性：1960–69 世代 93.1%，1985–89 世代 72.6%；
- 30 岁前结婚的女性：97.3% 对 90.9%。

来源：

- https://link.springer.com/article/10.1007/s42379-022-00113-0

## 时期初婚基准

### `china-first-marriage-age-selected-1990-2021.csv`

请把这份文件与上面的出生世代文件分开。

时期均值回答的是：

> 在那个日历年里结婚的人，是多大年纪？

世代指标回答的是：

> 对某个时期出生的人而言，婚姻序列是怎样展开的？

这两者不能互换。

## 分出生世代的生育

### `china-childbearing-by-birth-cohort-cfps2018.csv`

已发表的 CFPS 2018 女性世代估计：

- 至少生育一孩的比例；
- 生育二孩的比例；
- 母亲中生育二孩的比例；
- 一孩与二孩之间的生育间隔中位数。

重要的截断警告：1980 年代、尤其是 1990 年代出生的世代，在调查时点尚未走完其生育历程。不要把他们观测到的比例当成完成生育率。

来源：

- https://journals.sagepub.com/doi/full/10.1177/2057150X211040936

## 工作黏着度

### `china-job-tenure-urban-resident-migrant-1999.csv`

一个横截面的历史基准：

- 城镇居民：平均任期 19.9 年；
- 乡城流动人口：平均任期 4.5 年。

来源：

- https://www.sciencedirect.com/science/article/pii/S0147596704000551

这还不是真正的分出生世代的第一份工作序列。它说明的是：同一个日历年里，存在几种不同的就业时间制度。

## 迁移

### `china-rural-urban-migrant-workers-1990-2022.csv`

大规模存量基准。它确立的是“外出打工”何时成为一条寻常路径；它并不重构个体的迁移序列。

做事件史分析时，请用：

- [`../places/china/generations/empirical-life-sequence-anchors.zh-CN.md`](../places/china/generations/empirical-life-sequence-anchors.zh-CN.md)
- [`../sources/life-history-survey-guide.zh-CN.md`](../sources/life-history-survey-guide.zh-CN.md)

## 住房

现有文件：

- `china-urban-homeownership-1988-2002.csv`——时期自有率基准；
- `china-housing-space-1978-2005.csv`——实际居住空间。

仍缺机器可读形式的：

- 分世代的首次购房年龄；
- 进入首次自有的途径；
- 婚姻相对于首个住房的时间关系；
- 分世代的父母资助。

## 退休

### `china-retirement-rates-charls-2018.csv`

按年龄、性别和城乡居住地划分的退休状态。

这是年龄—时期的截面快照，不是回溯性的分世代退休年龄分布。未来的生命史分析应当派生各出生世代的实际退休年龄。

## 代际家庭序列

有用的文件：

- `china-elderly-coresidence-with-adult-children-1982-2010.csv`；
- `china-grandparent-care-urban-rural-charls-2011.csv`；
- `china-old-age-support-expectations-charls.csv`。

它们展示的是序列中经典的“结婚 + 生育”之后可能发生什么：

> 成年子女离家 → 父母变老 → 同住／就近／转移 → 照看孙辈 → 退休／继续劳动。

## 从教育到工作的转变

目前还没有创建直接的 CSV，因为当前最强的来源报告的是因果发现，而不是一张简单可复用的描述性表格。

Hao & Zhang 发现：中国 1999 年起加速的高等教育扩张，推迟了专科毕业生第一份技能型工作的落地，而四年制本科毕业生没有表现出同样的获得效应。

来源：

- https://pubmed.ncbi.nlm.nih.gov/32773820/

这是一个重要的提醒：

> 扩大教育规模，可能在提高受教育程度的同时，反而拉长从学校到职业落地的转变期。

## 下一批派生数据集

优先级：

1. 分出生世代的首次工作年龄；
2. 分出生世代的第一份工作持续时长；
3. 30 岁／40 岁时换过几份工作；
4. 首次迁移年龄与迁移次数；
5. 分世代 × 城乡 × 教育的初婚年龄；
6. 结婚到生第一个孩子的间隔；
7. 第一次独立居住；
8. 首次购房年龄与获得途径；
9. 分世代的实际退休年龄；
10. 开始照看孙辈的年龄与强度。

## 数据来源路线

下一批主要来源：

- CHARLS 2014 生命历程调查；
- CFPS 纵向／事件史模块。

指南：

- [`../sources/life-history-survey-guide.zh-CN.md`](../sources/life-history-survey-guide.zh-CN.md)

## 核心规则

不要从当前状态反推序列。

一个今天已婚 + 有房 + 退休的人，可能是沿着非常不同的历史走到这里的。

生命历程数据应当保留：

> **年龄 + 转变 + 持续时长 + 顺序 + 制度路径。**
