# 研究饱和与 artifact-first 检查点（2026-09-14）

> 性质：跨 `how-people-lived` / `old-web-archaeology` 的去重与阶段性方法检查。  
> 本文件**不新增生活机制专题**；它记录本轮为什么没有继续制造新的同义研究包，以及下一步为什么应优先做历史 artifact 核验。

## 1. 本轮先做了什么

按仓库约定，先重新检查：

- 当前 HEAD 与最近提交；
- `METHODOLOGY.zh-CN.md`；
- `ROADMAP-life-horizons.md`；
- 当前 `sources/` / `topics/` 目录；
- `old-web-archaeology` 的 `ROADMAP.md`、`docs/METHOD.md` 与现有 `research/`；
- 两仓既有的 saturation / dedup audit。

结果很明确：仓库现在的主要风险已经从“遗漏大量基本生活路径”转向“把已有机制换名字继续拆文件”。

## 2. 本轮主动放弃的候选新题

### 2.1 威客 / 自由职业 / 远程工作

这条线初看很适合继续推进“Internet 怎样改变普通人的就业边界”，但仓库已有多组高度重叠材料，例如：

- `topics/from-second-work-to-witkey-task-markets-digital-piecework-and-modular-livelihood-china-1988-2026.zh-CN.md`
- 与 workplace detachment / workplace-location decoupling 相关的既有专题；
- multiple jobholding / secondary work 等既有专题；
- OWA 已有 witkey task-market 的 bounty / submission / selection / payment / reputation / work-outcome state-gap 研究。

继续新增“SOHO / freelancer / remote work”文件，很容易只是重新命名已有的“工作地点脱钩”“任务模块化”“第二工作”“平台化零工”。本轮因此不做。

### 2.2 BBS 兴趣社群 / 版聚

西祠胡同、The WELL 等材料很容易继续展开“网友怎样变成线下朋友”“兴趣如何跨地域组群”，但 HPL 已经有 hobby networks、interest addressability、stranger life scripts、forums / peer advice、neighborhood forums 等专题。

本轮海外 The WELL 材料显示：1985 年以来的 online conferences 与 1986 年后的线下 parties 共同维系社群，外地成员甚至可能因为缺少面对面接触而感到处于边缘。这与中文 BBS 后来的版聚结构很可比，但主要是**确认已有机制**，不是新的生活路径类别。

所以本轮也不再新开“线上社群—线下版聚”专题。

## 3. 本轮真正取得的推进：把西祠从 entity 进一步推向具体 artifact

`old-web-archaeology` 既有：

- 西祠的企业/域名沿革；
- 同期媒体对 discussion board、版主、线下聚会等描述；
- 但没有实际打开核验的 1998–2015 historical BBS page capture。

本轮从后出的参考文献链恢复出一个**精确历史页面和精确 Wayback locator**：

- 页面题名：`公布亚洲展望２００７城市联赛参赛队员名单`
- 原始 URL：`http://www.xici.net/b373044/d50430566.htm`
- 原始日期：参考链标为 `2007-03-28`
- Wayback candidate：`https://web.archive.org/web/20110724135817/http://www.xici.net/b373044/d50430566.htm`
- archived date：参考链标为 `2011-07-24`
- retrieved date：参考链标为 `2012-08-24`

线索来源保留了完整 archive URL：

<https://3rabica.org/%D8%AA%D8%A7%D9%86_%D9%86%D9%8A%D9%86%D8%BA>

OWA 已单独提交 artifact-locator escalation note，严格把它标成：

```text
exact archived URL recovered
opened capture = false
```

而不是“2007 年西祠页面已经恢复”。

当前运行环境没有成功打开该 Wayback replay，因此 historical HTTP、DOM、charset、board chrome、post metadata、subresources 与 replay rewrite 都仍然未知。

这个结果很重要，因为它把工作方向从“再写一个论坛状态缺口概念”改成了**下一次直接重试一个具体 memento**。

## 4. 海外比较：The WELL 说明了什么，又没有说明什么

本轮至少检查了一个大众 Web 以前的海外对象：The WELL。

1997 年 WIRED 长篇报道记录，The WELL 于 1985 年上线，早期系统由 VAX、六个 modem、六条电话线与 PicoSpan conferencing 构成；1986 年以后线下 WELL parties 逐渐成为社群生活的一部分，线上问题也会转到线下处理。一名从 Austin 接入的用户甚至表示，在自己前往 Bay Area 参加聚会前，发言常感觉受到忽视。

来源：<https://www.wired.com/1997/05/ff-well/>

1998 年 The WELL 自己的公告又说明，Vue conferences 可以让任何 Web 用户阅读，但只有 WELL members 能发帖。

来源：<https://www.well.com/about-2/pr/well-launches-vue-conferences/>

因此海外比较确认：

- “远程文字社群 + 线下面对面关系”不是中文 BBS 独有；
- public readability、membership 与 posting entitlement 应分开；
- 社群技术上可以跨地域，社会关系上的中心/边缘仍可能受面对面接触影响。

但这些都没有实质推翻或改写 HPL 现有结论，因此不能为了满足“每轮一个海外对象”而硬说它是新机制。

## 5. 对核心矩阵的判断

结合既有 saturation audit 与本轮目录复查，目前核心矩阵已经有相当广的跨时期覆盖：

- 教育；
- 就业与第二工作；
- 住房与迁移；
- 婚姻家庭；
- 照护；
- 非正规劳动；
- 长期中断；
- 证件与记录；
- 邮政、电话、寻呼、公共终端、Internet 与移动接入；
- 信息发现、地图/导航、预约、物流、支付等生活执行基础设施；
- 社交关系和线上/线下身份；
- 未来预期；
- 平台消失与 archive state loss。

这不意味着“所有问题都做完了”，而意味着下一步最有价值的工作越来越不是再发明第 N 个生活机制，而是：

1. 把已有结论压成更少、更强的综合结构；
2. 为已有机制补真正同时代第一人称材料；
3. 把 OWA 的 historical locator 变成真正打开核验的 artifact；
4. 对同一平台取得第二历史时点，开始真正做 change-over-time；
5. 在确有新证据推翻旧结论时，再新开专题。

## 6. 本轮饱和计数

上一轮“纸质交通图 → 手机导航”确实新增了 `route executability`，并新增了动态地图 archive 对象，因此饱和计数重置为 `0/3`。

本轮：

- 没有发现新的生活路径类别；
- 没有发现新的制度接口；
- 没有发现新的时代时间感机制；
- 没有发现新的通信/Internet 转折机制；
- The WELL 主要是跨国确认已有机制；
- 西祠取得的是**更具体的 artifact locator**，但还不是能改变 HPL 结论的一手 capture。

因此本轮应记为：

**阶段饱和连续计数：`1/3`。**

尚未达到 closure 条件，不应停止研究任务。

## 7. 下一轮优先级

下一轮不应再从主题列表里随便挑一个新名词，而应优先：

1. 重试西祠精确 Wayback memento：  
   `https://web.archive.org/web/20110724135817/http://www.xici.net/b373044/d50430566.htm`
2. 若成功打开，完整记录 capture timestamp、HTTP/replay、DOM、charset、缺失资源和浏览器假设；
3. 找西祠同一 board/site 第二历史时点；
4. 或转向另一个已经拥有精确 historical locator、最可能补成 M1 complete case 的对象；
5. 只有真的出现新的生活路径/制度接口/时间机制/跨国差异，才重置饱和计数。

这比继续扩张专题数更接近当前阶段真正的研究瓶颈。

---

## 8. Artifact-first 复查：第二轮（2026-09-14）

上一轮之后，仓库又补过一轮新浪职业规划材料的 provenance 校正：第一人称正文作者、共享出版账号、实际发布者、显示发布时间与原始写作时间必须分开。那一轮同样属于证据升级而非新机制，因此进入本轮时，跨仓连续 no-new-mechanism 计数仍为 `1/3`。

本轮再次先读两仓最新 HEAD、最近提交、方法文件、ROADMAP / INDEX、既有 saturation audit 与已有专题，然后才选择 artifact。这个顺序产生了一个直接的去重收益：原本候选的“拨号上网怎样占用家庭电话、怎样按连接时长计算成本”已经有专门研究包：

- `sources/contemporaneous-dial-up-household-time-bills-and-phone-line-decoupling-china-1997-2003.zh-CN.md`
- `topics/from-dial-up-session-budgeting-to-always-on-household-connectivity-home-internet-provisioning-china-1986-2026.zh-CN.md`
- OWA 对应 `research/dial-up-metered-session-phone-line-contention-and-access-context-loss-1997-2003.md`

因此本轮明确放弃再写“占线 / 猫叫 / 按分钟上网”的同义专题。

## 9. 西祠精确 memento：重试仍未取得可核验 artifact

本轮按上一检查点给出的第一优先级，重新追：

- 原始 URL：`http://www.xici.net/b373044/d50430566.htm`
- candidate memento：`https://web.archive.org/web/20110724135817/http://www.xici.net/b373044/d50430566.htm`

当前 3rabica 参考页仍然直接暴露这条精确 Wayback locator，可再次确认“这个 locator 确实存在于后出的参考链中”。但沿该链接获取历史 replay 时，本轮返回的是当前研究通路的 fetch/cache failure，主文档没有被取回；另一路 archive index 查询也遇到当前环境的网络解析失败。

所以证据状态**没有升级**：

```text
exact locator independently re-confirmed
opened historical main document = false
HTTP / DOM / charset / board chrome / post metadata = unknown
capture absence = NOT established
```

这次失败应只理解为 `replay not obtained in this run`，不能改写为“Wayback 没存”“历史页不存在”或“西祠 artifact 已经恢复”。OWA 同一 artifact note 已追加这次 retry 结果，不另造新的状态缺口文件。

## 10. Carboy 的一个新 artifact lead：1997 年确有整站本地下载行为，但副本尚未恢复

本轮检查另一个已有具体对象 `完全上网手册 / Carboy` 时，找到一条接近时代的一手/记者材料，可把“本地副本可能参与旧网页保存”从一般方法假设收窄到具体人物与年份。

刘韧在新浪科技 2000-11-06 的《杨震霆广州网事》中写到：1997 年王峻涛为了学习做网站，把“完全上网手册”整个下载到本机，在家集中研读数日。

来源：

- <https://tech.sina.com.cn/path/2000-11-06/491.shtml>

同年 12 月，杨震霆自己的文章又给出历史路径 `business.gznet.com/carboy/`，并回顾“完全上网手册”的内容、托管迁移和后来只剩碎片的状态：

- <https://tech.sina.com.cn/r/m/46310.shtml>

这带来一个**artifact recovery lead**：至少在 1997 年曾存在某个用户侧的整站本地副本，旧个人主页的后续恢复不必只盯 Wayback，也可以检查公开捐赠的硬盘镜像、CD-ROM、离线网页包、软件附盘、个人公开镜像或后来合法公开的保存副本。

但必须严格限制结论：

- 2000 年报道能证明“1997 年有人整站下载并离线阅读”这一叙述进入了接近时代的公开文本；
- 它**不能证明**那份 1997 本地副本今天仍然存在；
- 不能据此去追私人硬盘、私人账号或未公开个人文件；
- 仓库已经有 offline browser / local corpus / personal homepage preservation 相关机制，因此这不是新的生活路径或新的通信机制，只是把既有保存路径钉到一个具体历史对象上。

## 11. 海外 artifact 对照：GeoCities 的保存依赖“抢救生态”，不是原站天然幸存

本轮重新检查 GeoCities 的保存路径作为海外对照。Archive Team 的 GeoCities Project 记录：Yahoo 宣布关闭后，项目从 2009 年 4 月持续抢救到 10 月关闭前；与此同时 Internet Archive 进行了大规模 deep crawl。Archive Team 的后续说明还明确说，不同抢救项目得到的 GeoCities 子集并不相同，彼此需要交换数据和寻找缺口。

来源：

- <https://wiki.archiveteam.org/index.php/GeoCities_Project>
- <https://wiki.archiveteam.org/index.php/Geocities>

这对 Carboy / 中文个人主页的意义主要是**保存生态对照**：

- 原始托管服务消失，并不意味着 artifact 必然消失；
- 历史可见性可能取决于停站前的大规模抓取、用户侧下载、镜像站、离线介质和后来数据整理；
- 反过来，没有出现类似 GeoCities 大规模协调抢救的中文个人主页集合，会造成更严重的 survivor bias。

但本轮没有取得一个新的中国历史页面本体，也没有证明 Carboy 存在仍可读取的私人/公开副本。因此这个海外比较仍属于方法和保存路径上的确认，不应被夸大为新的跨国生活机制。

## 12. 第二轮后的饱和判断

本轮取得了两类进展：

1. 西祠精确 memento 的 replay 失败被再次结构化确认，没有再制造一个新的 state-gap 文件；
2. Carboy 得到一个 1997 年“整站下载到本机”的具体 preservation lead，可指导未来寻找公开 derivative artifact。

但按用户定义的研究饱和标准，本轮仍然：

- 没有发现新的生活路径类别；
- 没有发现新的制度接口；
- 没有发现新的时代时间感机制；
- 没有发现新的通信 / Internet 转折机制；
- GeoCities 主要强化既有 preservation ecology 判断；
- 没有取得足以实质改变当前 HPL 结论的新一手 artifact。

因此，本轮应把连续饱和计数推进为：

**阶段饱和连续计数：`2/3`。**

尚未达到 closure 条件，因此现在仍不应关闭本阶段研究。

下一轮的判断阈值应更严格：优先继续尝试**实际可打开、可检查 DOM / charset / headers / subresources 的历史 artifact**，或取得同一对象第二历史时点。如果下一轮再次只有 locator、后出回忆或已有机制的佐证，而没有新路径 / 新接口 / 新时间机制 / 新通信转折 / 结论改变型一手证据，则应按既定标准进入 `3/3`，先做 coverage audit，然后写阶段性 closure / synthesis，而不是继续靠新名词延长专题列表。