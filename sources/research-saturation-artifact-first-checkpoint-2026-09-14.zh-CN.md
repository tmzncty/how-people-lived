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
