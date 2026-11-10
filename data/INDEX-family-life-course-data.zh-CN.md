# 家庭生命历程数据索引

这个索引收集与伴侣关系、成家、代际支持、祖辈照护以及晚年生活相关的机器可读文件。

## 婚姻

### `china-first-marriage-age-selected-1990-2021.csv`

全国平均初婚年龄的部分基准值：

- 1990 男性：23.57；
- 1990 女性：22.02；
- 2021 男性：25.63；
- 2021 女性：23.89。

来源：

- https://pmc.ncbi.nlm.nih.gov/articles/PMC9516001/

只把它当作粗略的时间基准。城乡、教育和地区差异仍然重要。

## 与老年父母同住

### `china-elderly-coresidence-with-adult-children-1982-2010.csv`

基于人口普查的 65 岁及以上与成年子女同住比例端点值：

- 1982：69.4%；
- 2010：51.7%。

来源：

- https://www.demographic-research.org/volumes/vol41/48/41-48.pdf

不要把同住比例下降理解为家庭支持消失。

## 祖辈照看孙辈

### `china-grandparent-care-urban-rural-charls-2011.csv`

CHARLS 2011–2012 分析样本基准：

- 参与照护的农村祖辈：42.69%；
- 参与照护的城市祖辈：48.01%。

来源：

- https://pmc.ncbi.nlm.nih.gov/articles/PMC6244459/

这个文件记录的是参与率，不是照护强度。

## 退休

### `china-retirement-rates-charls-2018.csv`

可用于对照城乡晚年劳动状态的差异。

60–64 岁的部分总体数值：

- 城市退休率：70.8%；
- 农村退休率：26.1%。

来源：

- https://pmc.ncbi.nlm.nih.gov/articles/PMC10187591/

## 家庭结构

### `china-household-size-1980-2005.csv`

追踪城乡样本中平均家庭规模的缩小。

可用于理解：

- 兄弟姐妹的可获得性；
- 同住情况；
- 父母投入的集中程度；
- 未来的养老分担。

## 住房

### `china-housing-space-1978-2005.csv`

人均住宅建筑面积基准。

### `china-urban-homeownership-1988-2002.csv`

城市住房自有率的部分基准，可用于分析成家史。

## 亲子资源

目前还没有一条完整的直接转移序列。

相关的量化脚手架包括：

- 住房自有；
- 教育机会；
- 家庭规模；
- 养老支持预期；
- 工作任期；
- 迁移。

高优先级的未来文件：

- 父母对首个住房的资助金额；
- 按年龄／世代划分的对老年父母的支持；
- 照看孙辈的小时数；
- 按年龄与世代的同住情况；
- 第一个孩子的生育时间；
- 第一次独立居住；
- 首次购房年龄；
- 育儿支出；
- 养老照护的时间使用。

## 相关索引

- [`../INDEX-family-life-course.zh-CN.md`](../INDEX-family-life-course.zh-CN.md)
- [`../INDEX-generations.zh-CN.md`](../INDEX-generations.zh-CN.md)
- [`../sources/family-life-course-source-guide.zh-CN.md`](../sources/family-life-course-source-guide.zh-CN.md)

## 规则

家庭数据特别容易被过度解读。

平均初婚年龄、同住比例或家庭规模的下降，本身**并不**透露动机。

用定量序列确立“什么样的生活安排是可行的”这一边界的变化，再把它与调查、访谈和生命史结合起来。
