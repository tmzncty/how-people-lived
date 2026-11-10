# 数据

项目使用的机器可读表格放在这里。

这个目录包含两类不同的机器可读材料：

1. **实测数据**——已发表的统计数值，或从有文献记载的研究中提取的数值；
2. **研究脚手架**——由本仓库创建、用于组织有出处证据的定性世代地图。

永远不要把两者混淆。

## 约定

- 保留来源的原始统计单位。
- 明确写出地理范围和人群范围。
- 观测值缺失时留空，不要悄悄插值。
- 数据必须与来源 URL／文献编号一起保留。
- 保留城市／农村、性别、世代以及其他有意义的分类。
- 除非来源本身如此，不要把“每百户台数”换算成家庭百分比。
- 不要在没有价格调整或背景说明的情况下，跨年代比较名义货币值。
- 如果来源写的是“约”或“接近”，要保留这种不确定性。
- 明确标注被截断的年轻世代。
- 人生视野统计确立的是可能选择的边界，它并不直接测量私人愿望。
- 定性比较类 CSV 必须标注为 **research scaffold（研究脚手架）**。
- 数据集文件名放在 `data/` 目录下，使用小写 kebab-case 的 CSV；嵌套目录或大小写混用的 CSV 无法通过校验。

## 数据集清单与校验

[`dataset-manifest.json`](dataset-manifest.json) 是这个目录里每个 CSV 的机器可读来源索引。它的契约写在 [`../schemas/dataset-manifest.schema.json`](../schemas/dataset-manifest.schema.json) 里。

这份清单记录以下内容（但并不假装取代行级文档）：

- 某个文件属于实测数据还是研究脚手架；
- 地理范围与时间范围；
- 预期的记录条数；
- 哪些 CSV 列承载行级来源定位；
- 一段适合用于索引的简短描述。

提交数据改动或导航改动之前，运行：

```bash
python scripts/validate_repository.py
```

这个仅依赖标准库的校验器会检查：每个 `data/*.csv` 文件恰好被索引一次；声明的来源列确实存在；每条实测记录至少保留一个来源定位；记录条数与清单保持同步；CSV 各行宽度一致；以及规范形式的行内 Markdown 链接目标都留在仓库内且实际存在。它还会让随仓库发布的 schema 在其闭合的 Draft 2020-12 根结构和数据集字段上保持一致；完整的 JSON Schema 语义仍要由专门的实现来验证。引用式链接会被拒绝，必须改用行内链接；裸 HTML 链接与片段标识不在校验器的检查范围内。研究脚手架可以省略行级来源列，但必须明确归类为脚手架。

## 数据子索引

- [实证生命序列数据索引](INDEX-life-sequence-data.zh-CN.md)
- [家庭生命历程数据索引](INDEX-family-life-course-data.zh-CN.md)

---

# 中国——家庭物质条件

## `china-household-durables-1985-2000.csv`

洗衣机、冰箱、彩色电视机和电风扇的城乡拥有率基准（原始单位：每百户台数）。

国家统计局的主要历史来源包括：

- 城市：https://www.stats.gov.cn/english/Statisticaldata/yearlydata/YB1999e/j06e.htm
- 农村：https://www.stats.gov.cn/english/Statisticaldata/yearlydata/YB2000e/J24E.htm

## `china-household-income-engel-1978-2005.csv`

城镇人均可支配收入、农村人均纯收入，以及城乡恩格尔系数。

来源：

- https://www.stats.gov.cn/sj/ndsj/2007/html/J1002e.htm

名义收入不是直接的跨年购买力度量。

## `china-housing-space-1978-2005.csv`

城乡居民人均住宅建筑面积的部分基准值。

来源：

- https://www.stats.gov.cn/sj/ndsj/2008/html/J0935e.htm

不要把这个“住宅建筑面积”序列与更窄口径的历史“净居住面积”指标悄悄混用。

## `china-household-size-1980-2005.csv`

城乡平均家庭规模的部分基准值。

可用于分析家庭劳动力、兄弟姐妹的可获得性、对单个孩子的集中投入，以及后来的养老分担。

## `china-urban-homeownership-1988-2002.csv`

基于 CHIP 的城市住房自有率部分基准值。

早期的上升在相当程度上由公有住房私有化塑造；不应把“拥有住房”直接理解为在商业市场上购买。

来源：

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11771467/

---

# 中国——教育与从学校到工作

## `china-1977-gaokao-benchmark.csv`

历史稀缺度基准：

- 报考人数：约 570 万；
- 录取人数：272,971；
- 录取率：约 4.78%。

来源：

- https://www.chinadaily.com.cn/cndy/2015-03/31/content_19957679.htm

## `china-higher-education-gross-enrollment-1990-2004.csv`

教育部高等教育毛入学率基准。

部分数值：

- 1990：3.4%；
- 1995：7.2%；
- 2000：12.5%；
- 2004：19.0%。

来源：

- https://www.moe.gov.cn/jyb_sjzl/moe_560/moe_1389/moe_1390/moe_1393/201002/t20100226_20347.html

## `china-educational-mobility-1986-1995-selected.csv`

代际教育流动性的部分 rank-rank 系数。

1986–95 年出生者的父女对照示例：

- 城镇户籍出身：0.51；
- 农村户籍出身：0.27。

相关性更高意味着持续性更强，而不是受教育程度更高。

来源：

- https://link.springer.com/article/10.1007/s11113-024-09887-2

## 从学校到工作的序列证据（暂无简单 CSV）

一项 2025 年的 CGSS 序列分析重构了 1946–1995 年出生者在 10–29 岁期间的轨迹，并识别出：

- 早转型；
- 延迟转型；
- 不顺畅转型；
- 逆向转型。

参见：

- [`../topics/school-to-work-transition-as-a-life-stage.zh-CN.md`](../topics/school-to-work-transition-as-a-life-stage.zh-CN.md)

来源：

- https://www.tandfonline.com/doi/full/10.1080/21620555.2025.2480280

---

# 中国——就业与迁移

## `china-job-tenure-urban-resident-migrant-1999.csv`

Knight & Yueh 分析 1999 年调查时给出的一个历史对照：

- 城镇居民：平均工作任期 19.9 年；
- 乡城流动人口：4.5 年。

来源：

- https://www.sciencedirect.com/science/article/pii/S0147596704000551

不要把这两个样本推广到全体中国劳动者。

## `china-rural-urban-migrant-workers-1990-2022.csv`

全国农民工存量的部分估计：

- 1990：2,160 万；
- 2000：7,880 万；
- 2008：1.404 亿；
- 2019：1.743 亿；
- 2022：1.719 亿。

来源：

- https://documents1.worldbank.org/curated/en/099020325194013546/pdf/P180848-980daabd-c4df-4314-a796-5df3bf5c97c5.pdf

这说明“出去打工”何时成为一条大众化的路径。它并不揭示个体的迁移序列。

---

# 中国——婚姻、生育与成家

## `china-first-marriage-age-selected-1990-2021.csv`

部分**时期**平均初婚年龄端点值。

1990：

- 男性 23.57；
- 女性 22.02。

2021：

- 男性 25.63；
- 女性 23.89。

来源：

- https://pmc.ncbi.nlm.nih.gov/articles/PMC9516001/

## `china-first-marriage-by-birth-cohort-cfps2018.csv`

CFPS 2018 的**出生世代**初婚时间表。

包含：

- 初婚年龄中位数；
- 25 岁前结婚比例；
- 30 岁前；
- 35 岁前；
- 40 岁前（观测充分时）。

世代范围从 1950 年前出生到 1985–89 年出生。

来源：

- https://link.springer.com/article/10.1007/s42379-022-00113-0

时期口径与世代口径的婚姻指标回答的是不同问题，不应混用。

## `china-childbearing-by-birth-cohort-cfps2018.csv`

已发表的 CFPS 2018 女性世代估计：

- 至少生育一孩；
- 生育二孩；
- 母亲中生育二孩的比例；
- 一孩到二孩的间隔中位数。

来源：

- https://journals.sagepub.com/doi/full/10.1177/2057150X211040936

1980 年代和 1990 年代世代尚未完整观测；尤其是 1990 年代的数值**不是完成生育率估计**。

---

# 中国——代际家庭与晚年

## `china-old-age-support-expectations-charls.csv`

晚年主要经济来源预期的城乡差异。

可用于说明“靠养老金”与“靠子女”两类晚年视野的差别。

来源：

- https://documents1.worldbank.org/curated/en/099245006232237362/pdf/P1719590c42d060b209a3a0202aaea992e2.pdf

## `china-retirement-rates-charls-2018.csv`

CHARLS 2018 加权退休率，按年龄、性别和城乡居住地划分。

部分总体数值：

- 60–64 岁：城市 70.8%，农村 26.1%；
- 65–69 岁：城市 81.3%，农村 35.2%；
- 70–74 岁：城市 83.4%，农村 45.0%。

来源：

- https://pmc.ncbi.nlm.nih.gov/articles/PMC10187591/

## `china-elderly-coresidence-with-adult-children-1982-2010.csv`

基于人口普查的 65 岁及以上与成年子女同住比例的端点值：

- 1982：69.4%；
- 2010：51.7%。

来源：

- https://www.demographic-research.org/volumes/vol41/48/41-48.pdf

同住比例下降并不意味着家庭支持消失。

## `china-grandparent-care-urban-rural-charls-2011.csv`

CHARLS 2011–2012 分析样本中参与照看孙辈的比例：

- 农村：42.69%；
- 城市：48.01%。

来源：

- https://pmc.ncbi.nlm.nih.gov/articles/PMC6244459/

参与率不等于照护强度。

---

# 中国——通信与互联网

## `china-internet-scale-1997-2011.csv`

CNNIC 的部分基准值，记录了从稀少的拨号上网到大众／移动连接的转变。

对世代史很有用：一个 1990 年出生的人，可以在童年几乎离线的情况下长大，到成年早期已进入移动互联网的大众时代。

## `china-household-communication-devices-2000-2010.csv`

城乡每百户家庭电脑与移动电话数量。

2000 年的部分对照：

- 城市电脑 9.70／农村 0.47；
- 城市移动电话 19.50／农村 4.32。

2010 年的部分对照：

- 城市电脑 71.16／农村 10.37；
- 城市移动电话 188.86／农村 136.54。

来源：

- 城市：https://www.stats.gov.cn/sj/ndsj/2012/html/J1010e.htm
- 农村：https://www.stats.gov.cn/sj/ndsj/2012/html/J1030e.htm

---

# 中国——疫情

## `china-pandemic-graduate-cohorts-2020-2023.csv`

毕业世代规模基准：

- 2020：874 万；
- 2021：909 万；
- 2022：1,076 万；
- 2023：1,158 万。

用于把疫情造成的招聘中断与世代规模的长期结构性上升区分开来。

## `china-pandemic-railway-passenger-trips-2019-2023.csv`

铁路旅客发送量：

- 2019：36.6 亿人次；
- 2020：22.0 亿人次；
- 2021：26.1 亿人次；
- 2022：16.7 亿人次；
- 2023：38.5 亿人次。

作为流动系统的基准使用，不要用它解释个体的出行。

---

# 中国——生成式 AI

## `china-generative-ai-adoption-2024-2025.csv`

基于 CNNIC 的生成式 AI 使用基准。

配合使用：

- [`../INDEX-gen-z.zh-CN.md`](../INDEX-gen-z.zh-CN.md)
- [`../topics/ai-as-cognitive-infrastructure.zh-CN.md`](../topics/ai-as-cognitive-infrastructure.zh-CN.md)

采用率本身并不证明技能、依赖或认知变化。

---

# 中国——世代研究脚手架

## `china-cohort-age-anchors-1955-2005.csv`

1955／1965／1975／1985／1995／2005 年前后出生的年龄算术锚点。

## `china-generational-life-course-matrix.csv`

**研究脚手架**，不是调查数据。

汇总了有出处的世代解释，覆盖：

- 童年物质条件；
- 教育问题；
- 第一份工作问题；
- 住房问题；
- 信息环境；
- 历史断裂；
- 简化的成年问题。

---

# 美国

## `us-electric-service-1920-1940.csv`

美国人口普查局关于全部住宅与农场住宅电力服务覆盖率的历史百分比。

来源：

- https://www.census.gov/about/history/stories/monthly/2025/september-2025.html

---

# 为什么生命历程数据要放在这里

数字不会透露某个人私下想要什么。

它们确立的是：在当时什么在现实中可行，以及某条路径可以有多普遍。

本项目日益区分以下几类：

- **存量／状态数据**——某人现在拥有什么；
- **时期数据**——某个日历年里发生了什么；
- **世代数据**——某个时期出生的人身上发生了什么；
- **事件史数据**——某个转变何时发生；
- **序列数据**——多个转变的顺序与间隔。

最扎实的日常生活重构，会把这些层次结合起来。

## 价值最高的未来派生数据集

下一批优先目标：

- 分出生世代的首次工作年龄；
- 分世代的第一份工作持续时长；
- 30 岁／40 岁时换过几份工作；
- 首次迁移年龄／迁移次数；
- 分世代 × 出身 × 教育的初婚年龄；
- 结婚到生第一个孩子的间隔；
- 第一次独立居住；
- 首次购房年龄／途径；
- 父母对首个住房的资助；
- 分世代的实际退休年龄；
- 照看孙辈的小时数；
- 养老照护的时间与金钱转移；
- 分年龄与职业的 AI 使用。

主要数据路线：

- CHARLS 2014 生命历程调查；
- CFPS 纵向／事件史模块；
- CGSS 回溯性学校／工作史。

指南：

- [`../sources/life-history-survey-guide.zh-CN.md`](../sources/life-history-survey-guide.zh-CN.md)

## 最终的数据规则

不要从当前状态反推生命序列。

一个今天有房的人可能是：

- 在市场上买的；
- 分到了私有化的单位房；
- 继承的；
- 接受了父母的资助。

一个今天在工作的人，可能是 16 岁开始的，也可能是 26 岁开始的。

一个今天已婚的人，可能是 20 岁结的婚，也可能是 35 岁。

永远保留：

> **单位 + 人群 + 年龄 + 时期／世代 + 转变定义 + 来源。**
