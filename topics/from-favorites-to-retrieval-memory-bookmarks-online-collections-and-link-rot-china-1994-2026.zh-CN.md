# 从“加到收藏夹”到“把这段网页也保下来”：书签、信息路径可携带性与检索记忆保管（中国，1994—2026）

Status: research note / cross-repo topic  
Companion: `tmzncty/old-web-archaeology/docs/BROWSER_FAVORITES_ONLINE_BOOKMARK_SOCIAL_BOOKMARK_SYNC_AND_LINK_ROT_STATE_GAPS_1995_2015.md`  
Last research pass: 2026-09-09

## 0. 研究问题

搜索引擎解决的是：

> 我现在不知道答案，怎样第一次找到它？

收藏夹/书签解决的是另一件事：

> 我以前已经找到过一个有用的地方，几天、几年、换一台电脑甚至换一种浏览器以后，我还能不能回去？

这是一种很基础、但容易被产品史掩盖的生活能力。一个学生保存招生简章，一个求职者保存招聘页，一个病人保存医院说明，一个租房者保存政策页面，一个程序员保存技术文档，本质上都在把未来的一部分行动建立在“以后还能重新找到这里”之上。

因此本专题研究的不是浏览器功能史，而是普通人的 **retrieval memory——检索记忆** 如何被外包、搬运、同步、堆积、腐烂和重新保管。

核心区分：

```text
found once
≠ bookmarked
≠ bookmark survives
≠ target URL resolves
≠ same content still exists
≠ user can re-find the bookmark
≠ user can still understand why it mattered
≠ information remains valid
≠ real-world action remains possible
```

本专题与已有两个专题相邻但不重复：

- 搜索/目录专题研究 `discoverability` 与检索劳动；
- personal digital baggage 专题研究文件本体怎样跟着人和设备移动；
- 本专题研究的是**通向外部信息的路径**怎样跟着人移动，以及为什么“保存一个地址”并不等于“保存了一份信息”。

---

## 1. 方法与新概念

遵循仓库 `METHODOLOGY.md`：不把功能存在写成普通人普及，不把一个技术用户的实践外推为全国，不把今天“云同步理所当然”的体验倒投回 2000s。

这一轮新增几个可跨专题复用的概念。

### 1.1 retrieval-memory externalization / 检索记忆外包

人不再依靠大脑记住：

- 网站叫什么；
- 域名怎样拼；
- 从哪个门户点进去；
- 当时用什么关键词搜到。

而是把“以后怎样回去”写成一个机器对象。

### 1.2 information-trail portability / 信息路径可携带性

一组长期积累的入口能否从：

```text
这台电脑
→ 另一台电脑
→ 另一个浏览器
→ 另一座城市
→ 手机
→ 新账号/新服务
```

继续可用。

### 1.3 bookmark custody / 书签保管权

真正的问题不是“平台上现在还能看到”，而是：

- 我能否导出？
- 导出的格式是否可读？
- 平台关停后能否迁移？
- 能否保留文件夹、标签、标题、备注、时间？
- 错误同步以后能否回滚？

### 1.4 collection debt / 收藏债

保存成本持续下降以后，人可以极低成本地“先收藏再说”。结果可能是：

```text
保存越来越快
→ 集合越来越大
→ 组织/命名越来越滞后
→ 以后真正需要时反而找不到
```

收藏不是自动兑现的未来；它可能只是把今天的选择推迟给未来的自己。

### 1.5 link-rot exposure / 链接腐烂暴露

书签保存的是一个 locator，不是历史内容本身。

```text
bookmark survives
→ URL can die
→ domain can be reused
→ page can move
→ page can be rewritten
→ content can become obsolete
```

因此“我的收藏夹还在”与“我保存的知识还在”是两件不同的事。

---

## 2. 海外前史：Web 很早就需要“把路记下来”

1994 年《WIRED》同期报道 Mosaic 时，已经把 `hotlist` 列为普通浏览动作之一：用户可以把经常访问的 Web 地点加入列表。

Source:
- Gary Wolf, “The (Second Phase of the) Revolution Has Begun,” WIRED, 1994-10-01:  
  https://www.wired.com/1994/10/mosaic/

Evidence:
- A-/B+：同期媒体对当时浏览器和实际使用界面的描述。

这说明 bookmark 并不是 Web 成熟以后才补上的功能。超文本一开始迅速扩张，就立即产生了一个日常问题：

> 链接可以把我带去任何地方，但我怎样保证以后还能回到这个地方？

需要特别避免后见之明：中国 1994 年刚实现全功能 Internet 接入，并不意味着普通家庭已经在同年开始使用浏览器 hotlist。中国普通生活层面的 Web 收藏需要等公众接入、家庭电脑、学校/单位终端和网吧等接入场景扩张以后再讨论。

而且在 Web 以前，“保存信息路径”并不不存在：人会保留剪报出处、书目卡片、电话号码、报刊期号、图书馆索引路径。Internet 改变的不是人第一次需要记路，而是**路本身变成可以点击、复制、机器保存的 URL**。

---

## 3. 1990s—2005：本地收藏夹——“我记得”，其实是“这台电脑记得”

早期浏览器 Favorites/Bookmarks 看起来已经把记忆外包给机器，但那个“机器”常常非常具体：某一台 PC、某一个 Windows 用户目录、某一个浏览器 profile。

2005 年 PCPOP/新浪的一篇同期 Windows XP 教程写得非常直接：IE 收藏夹里长期积累的网站，如果重装系统就可能一起消失；因此教程教用户通过 IE 的导入/导出向导把收藏夹导出为 HTML，再备份到 CD，或导入另一台电脑。

Source:
- PCPOP / 新浪科技，《Windows XP实用技巧：自动备份你的收藏夹》，2005-12-06：  
  https://tech.sina.com.cn/s/2005-12-06/0901783556.shtml

Evidence:
- B：同期技术媒体操作教程；可以证明当时常见风险与可执行迁移路径，不能证明所有 IE 用户都会备份。

这暴露了一个今天容易忘记的事实：

## **local bookmark portability was manual labor**

```text
找到收藏夹
→ 导出 HTML
→ 保存到软盘/U盘/CD/其他介质
→ 在另一台机器导入
→ 检查文件夹和标题
→ 再点击目标 URL
```

所以“收藏夹”并没有天然解除地点绑定。它只是把人的大脑记忆换成了设备记忆。

---

## 4. 为什么中国的“网络收藏夹”在 2000s 有真实生活意义：很多人并不只用一台终端

2008 年 CNNIC 第 22 次报告显示，截至当年 6 月底中国网民 2.53 亿、普及率 19.1%；同期报道依据该报告指出，74.1% 网民在家上网，39.2% 使用网吧，网吧网民约 9918 万，而且场所是复选项。

Sources:
- CNNIC，《第22次中国互联网络发展状况调查统计报告》，2008-07：  
  https://www3.cnnic.cn/n4/2022/0401/c88-813.html
- 人民网/CNNIC数据同期报道，《中国网民上网设备趋于多样化 近亿人到网吧上网》，2008-07-24：  
  https://news.sohu.com/20080724/n258354852.shtml

Evidence:
- A-/B+：CNNIC 官方调查 + 同期报道。

青少年层面更明显。CNNIC 2008—2009 青少年报告显示，2008 年青少年网民在网吧上网比例为 57.5%，农村青少年达到 65.4%，同时已有近半使用过手机上网。

Source:
- CNNIC，《2008-2009中国青少年上网行为调查报告》：  
  https://www.cnnic.cn/n4/2022/0401/c116-890.html

Evidence:
- A：官方调查摘要。

这些比例不能拿来直接证明“网络书签被大量使用”。但它们解释了这种功能为什么有现实问题背景：一个人可能在家、学校、单位、网吧之间移动，而浏览器本地收藏夹不会自动跟着他。

2008 年腾讯 TT4.3 的同期教程甚至直接把场景写成：公司一台电脑、家里另一台，难道每天用 U 盘搬 IE 收藏夹；其网络收藏夹允许本地收藏与网络收藏之间拖动。

Source:
- 多特软件站，《腾讯TT4.3版收藏夹使用技》，2008-10-21：  
  https://www.duote.com/tech/1/1215.html

Evidence:
- B：同期产品教程/媒体稿；能证明产品功能与被想象的使用场景，不证明用户规模。

这正是 **information-trail portability** 的生活含义：

> 换机器以后，不只是文件要回来；“我过去常去哪里、以后还要去哪里”的路径也要回来。

---

## 5. 2005—2012：扩张型未来——从本地文件夹到“个人在线图书馆”

### 5.1 2006：收藏地址开始变成账号中的远程对象

2006 年《解放日报》/新浪科技报道，当时国内已经出现 365key、新浪 VIVI、35766 等网络书签/网摘服务；文章直接以“碰到有用网页会加到 IE 收藏夹”为旧习惯，再解释如何把个人收藏上传到公共网站，也允许保持私人收藏。

Source:
- 《网民联手搭建网上图书馆》，2006-12-01：  
  https://tech.sina.com.cn/i/2006-12-01/13491267213.shtml

Evidence:
- B+：同期主流媒体观察；其中用户数/页面数来自当时服务或采访，应保留来源局限。

此时 bookmark 的“地址”开始变化：

```text
浏览器 profile 里的对象
→ 账号里的远程对象
```

于是人在别的机器上，只要能登录，就有机会把原来的信息路径接回来。

### 5.2 百度搜藏：一个非常关键的功能分叉——保存 URL，还是保存内容？

新浪科技在 2006-11-22 测试期报道中记录，`cang.baidu.com` 当时显示“全文收藏、快速查找、网页快照、分享”等能力。

Source:
- 新浪科技，《百度进军网摘领域悄然测试搜藏频道》，2006-11-22：  
  https://tech.sina.com.cn/i/2006-11-22/09251250212.shtml

Evidence:
- B+：同期媒体观察到的测试页面。

11 月 28 日正式发布的同期转述进一步把传统书签的弱点说得很清楚：只记录 URL 时，原站删除页面或失效，收藏也会失去作用；百度则把“全文收藏/网页快照”作为补偿机制。

Source:
- cnBeta 转赛迪网，《百度搜藏今日正式发布 打造个人在线图书馆》，2006-11-28：  
  https://www.cnbeta.com.tw/articles/18683.htm

Evidence:
- B：同期二手/转稿，可证明当时产品宣称与问题意识；不能把“快照永远可取”当成已验证事实。

这使本专题增加一条非常重要的分界：

```text
save locator
≠
save representation/content
```

早期收藏解决“我怎样回去”；内容快照开始尝试解决“如果那里已经不是原来的那里怎么办”。

### 5.3 QQ书签：账号身份把收藏能力带进更大的日常账号体系

2007 年同期 QQ 工具栏材料把 `shuqian.qq.com` 描述为免费网络收藏夹：可用 QQ 号码登录，在浏览时直接收藏，并随时管理和分享。

Sources:
- cnBeta，《搜搜推出QQ工具栏》，2007-07-25：  
  https://www.cnbeta.com.tw/articles/soft/33673.htm
- cnBeta，《下一代视频观看方式——QQ实验室发布QQVideo Gadget》，2007-04-19，其中列出此前已发布 `QQ书签（shuqian.qq.com）`：  
  https://www.cnbeta.com.tw/articles/soft/25271.htm

Evidence:
- B：同期行业媒体/产品转述。

这里的变化不是 QQ 发明了 bookmark，而是**收藏记忆可以挂到一个已经存在于聊天、邮箱、社区等活动里的长期账号身份上**。

### 5.4 2008：Web2.0 收藏服务很多，但不要把一份插件日志当全国市场份额

WPJAM 在 2008-06-16 公布自己的 17fav WordPress 插件行为日志：截至当时，QQ书签 1283 次、百度搜藏 959、Google书签 666、del.icio.us 651，此外还有雅虎收藏、新浪 VIVI、365Key 等。

Source:
- WPJAM，《收藏和分享工具使用统计第一期》，2008-06-16：  
  https://blog.wpjam.com/2008/06/16/bookmark-and-share-stats-1/

Evidence:
- A-/B+：站长公开的同期自身日志/汇总；**只代表安装该 WordPress 插件并触发操作的样本**，不能外推为中国网络书签市场份额。

但它可靠证明了一件更窄的事：2008 年一个中文博客页面完全可能同时向普通访问者摆出一长排本地/在线/国内/海外收藏服务，收藏生态高度碎片化而非“一家独大”。

### 5.5 2009：收藏继续从 PC 向手机移动

2009 年 QQ 手机浏览器 beta 的同期评测记录，其起始页把“我的书签”和“我要搜索”放在最前面。

Source:
- 多特，《新版QQ手机浏览器发布 支持web浏览》，2009-09-23：  
  https://www.duote.com/tech/1/2752.html

Evidence:
- B：同期产品评测。

因此扩张型未来可以写成一条更精确的链：

```text
我知道网址
→ 这台电脑替我记住
→ 我的账号替我记住
→ 不同电脑可以取回
→ 手机也可以带着这些入口走
```

这并不意味着所有人都同步成功，但“信息路径跟人走”已经成为可以销售、解释和使用的产品能力。

---

## 6. 一个海外对照：Delicious 把“私人找回”变成“公共发现”

2006 年 WIRED 对 del.icio.us 的介绍已经清楚描述：用户可以保存 bookmarks、用 tag 组织，也可以通过 network、tag、RSS 等看到别人公开保存的页面。

Source:
- WIRED, “The Social Bookmarking Showdown: Del.icio.us,” 2006-10：  
  https://www.wired.com/2006/10/the-social-bookmarking-showdown-deldoticiodotus/

Evidence:
- B+：同期技术媒体产品评测。

2006 年对 12 名 del.icio.us 用户的访谈研究（后发表于 2007）则发现，受访者报告的动机包括保存有用/有趣页面、从多台电脑访问、以及获得其他用户认可。

Source:
- Rick Wash, “Public bookmarks and private benefits,” 2007：  
  https://doi.org/10.1002/meet.1450440240

Evidence:
- A-/B+：小样本同期用户研究，样本偏大学与 IT 人群，不具人口代表性。

这个海外对照说明：中国 2006–2009 的“网络书签/网摘”不是孤立现象。Web2.0 时代出现了共同的结构转换：

```text
private refinding tool
→ account-portable collection
→ public tag/interest signal
→ collective discovery layer
```

收藏一个页面开始同时可能在做两件事：替未来的自己留路，也替别人投下一张“这个值得看”的票。

---

## 7. 2009：当“云端记忆”出现以后，错误也会成为可以传播的状态

2009 年搜狐数码对傲游浏览器“恢复收藏”功能的同期介绍，直接讨论了误删收藏、导入新收藏覆盖旧数据，以及从本地/在线备份恢复到过去某一天的状态。

Source:
- 搜狐数码，《妙用傲游“月光宝盒”快速恢复浏览记忆》，2009-07-16：  
  https://digi.it.sohu.com/20090716/n265266624.shtml

Evidence:
- B：同期产品教程/媒体稿。

这里已经出现一个 2020s 仍然存在的问题：

## **sync externalizes memory, but also externalizes mistakes**

本地收藏夹时代，一台机器误删可能只坏一份；同步时代，错误状态可能被复制到其他设备。因此真正成熟的同步不仅需要“最新”，还需要：

- 冲突规则；
- 备份；
- 历史版本；
- 可理解的 merge/overwrite 语义；
- rollback。

---

## 8. 2015—2019：拥堵型未来——保存入口越来越容易，保管入口越来越复杂

### 8.1 2018：跨浏览器同步服务关闭，证明“可携带性”本身也依赖平台

Xmarks 是跨 Firefox/Chrome/IE/Safari 的书签同步服务。2018 年 3 月，运营方通知用户将于 5 月 1 日停止服务，账号随后失效，既有浏览器里的 bookmark 可以留下，但不再同步。

Contemporary sources:
- BetaNews, “Bookmark syncing service Xmarks to close on May 1,” 2018-04-01：  
  https://betanews.com/article/xmarks-to-close/
- Greg McLeod, “RIP Xmarks, Hello Syncmarx!”, 2018-04-30：  
  https://www.gregmcleod.com/rip-xmarks-hello-syncmarx/

Evidence:
- B+ + 同期第一人称：媒体保存关闭通知；McLeod 明确自述长期使用、关闭后寻找替代并自己写同步扩展。

Slashdot 同期读者讨论里，一名长期用户把 Xmarks 的价值概括为：即使操作系统、浏览器、雇主变化，仍能拿到同一批书签。

Source:
- Slashdot, “Bookmark Syncing Service Xmarks Closes For Good On May 1,” 2018-04-27：  
  https://news.slashdot.org/story/18/04/27/1924210/bookmark-syncing-service-xmarks-closes-for-good-on-may-1

Evidence:
- B / community first-person；不能外推为全体用户。

这非常适合定义 **bookmark custody gap**：

> 我把信息路径从浏览器搬到了同步平台，于是摆脱了某一台机器；但如果平台本身消失，我仍要在期限内重新选择一个保管人。

### 8.2 2019 中国第一人称：跨浏览器已经成为真实的日常摩擦

2019 年一名中文博主写自己同时使用 Chrome 和 Firefox，Linux 使用增加以后，原先方案不能继续同步；他试过 Raindrop，最后使用 Floccus + 坚果云 WebDAV，并留下具体映射/目录问题。

Source:
- 方寸间，《Floccus：跨浏览器书签同步》，2019-07-07：  
  https://www.10101.io/2019/07/07/floccus

Evidence:
- A-/B+：同期个人操作记录；个案，不代表普通网民总体。

这和 2008 腾讯 TT“公司/家里两台电脑”的问题很相似，却又多了一层：

```text
2008：地点/电脑之间怎样一致？
2019：浏览器/操作系统/云服务之间怎样一致？
```

可携带性扩大以后，故障域也变多了。

### 8.3 收藏债：保存动作越来越便宜，并不意味着未来更容易找回

2019 年一篇 Floccus 介绍者以自己的编辑经验描述，每天遇到大量感兴趣的文章、图片、视频，“当下没有时间”就不断收藏，最终收藏夹日积月累。

Source:
- 画夹插件网，《Floccus - 浏览器书签同步插件》，2019-07-04：  
  https://huajiakeji.com/accessibility/2019-07/2622.html

Evidence:
- B-/C+：同期编辑个人化表述 + 产品介绍；只用于说明一种实际问题感，不作群体统计。

真正更强的学术反例来自早期个人信息管理研究：2001/2002 年的工作观察就发现，人并不只用 bookmark，还会把 URL 邮给自己、打印页面、保存到硬盘、粘进文档或个人主页，因为这些方法能够附带提醒和上下文。

Source:
- William Jones, Harry Bruce, Susan Dumais, “Keeping Found Things Found on the Web,” CIKM 2001：  
  https://www.microsoft.com/en-us/research/publication/keeping-found-things-found-web/

Evidence:
- A-/B+：同期观察研究；工作场景小样本，不代表所有用户。

这说明一个重要反例：

> bookmark 从来没有自然胜出成为“唯一正确的个人知识管理方式”。

普通人一直会混用搜索、历史记录、邮件、文件、笔记、截图、打印、网址导航和聊天发给自己。

---

## 9. 2020—2022：偶发型未来——“已经收藏”仍可能等于“真正需要时找不到”

2020 年发表的一项实验研究让“收藏债”变得可测量。研究让 50 名参与者重新找 21 个目标 URL，其中每人有 5 个目标来自自己的 bookmarks；在共 250 个 bookmark 目标中，只有 41 次（16%）真正通过 bookmark 功能取回，且多数来自始终可见的 bookmark bar，而不是层级菜单。

Source:
- Ofer Bergman, Steve Whittaker, Joel Schooler, “Out of sight and out of mind: Bookmarks are created but not used,” first online 2020-08-21：  
  https://journals.sagepub.com/doi/10.1177/0961000620949652

Evidence:
- A：同行评议实验研究；样本 50 人，不能作为全球总体频率。

它直接打破一个很自然的推论：

```text
saved more
!=
retrieved better
```

同一时期，中国 QQ 浏览器 HD 的 2020-08-09 App Store 用户评论要求完善书签分类、跨浏览器导入导出和同账号同步。

Source:
- Apple App Store, QQ浏览器HD ratings/reviews：  
  https://apps.apple.com/cn/app/qq%E6%B5%8F%E8%A7%88%E5%99%A8hd-%E4%B8%93%E4%B8%BA%E5%B9%B3%E6%9D%BF%E6%89%93%E9%80%A0%E7%9A%84%E6%9E%81%E9%80%9F%E6%B5%8F%E8%A7%88%E5%99%A8/id426097375?platform=ipad&see-all=reviews

Evidence:
- A-/B+：平台保留的同期普通用户评论；一名用户，不具代表性。

因此 2020–2022 在这条线上不宜硬写成“疫情创造了书签革命”。更稳妥的结论是：在多设备、远程工作/学习条件已经变得重要的阶段，**跨终端检索记忆依然不是一个已经彻底解决的问题**。

2022 年一个海外个人案例又把 link rot 具体化：David Roessli 检查自己从 2006 年开始积累的 Pinboard 收藏，发现约 12% 链接失效。

Source:
- David Roessli, “Evaluating link rot,” 2022-03-15：  
  https://davidroessli.com/logs/2022/03/evaluating-link-rot/

Evidence:
- A-/B+：第一人称个人集合测量；非常适合证明机制，不可外推为 Web 平均失效率。

---

## 10. 2023—2026：防守型未来——从“云同步就好”转向“我需要版本、出口和自己可控制的副本”

### 10.1 先出现的是收藏过量，而不是收藏不足

2023 年 V2EX 一名用户说自己习惯性收藏网页，已经积累 1000 多个，查找和使用不便，因而考虑开发新的书签管理器。

Source:
- V2EX，《大家是如何管理浏览器书签的》，2023-07-26：  
  https://www.v2ex.com/t/959784

Evidence:
- A-/B+：同期第一人称社区材料；技术社区样本，不具人口代表性。

这非常适合定义 **collection debt**：

> 2000s 的困难是“换电脑以后收藏会不会丢”；2020s 的困难之一已经变成“我明明什么都没丢，却还是找不到真正要用的那一个”。

### 10.2 同步成功不再只是便利问题，而是故障半径问题

2024 年多个公开浏览器社区第一人称显示，当书签已经同步多年以后，新的焦虑包括：文件夹顺序被同步打乱、旧 bookmark 重新出现、某设备不再同步、数年积累的文件夹突然消失。

Examples:
- Chrome Reddit, 2024-11-15，一名用户称多年组织的约 1.8 万 bookmarks 在新设备同步后顺序混乱；
- Safari Reddit, 2024-12-17，一名用户为修复文件夹异常，先导出 HTML、关闭多设备同步、再导回；
- Vivaldi Reddit, 2025-02-17，一名用户称新电脑同步失败后，旧设备的数百 bookmarks 也被远端新状态替换，最后依靠离线备份导出/再导入恢复。

Sources:
- https://www.reddit.com/r/chrome/comments/1gs5mpp/
- https://www.reddit.com/r/Safari/comments/1hg4bth/
- https://www.reddit.com/r/vivaldibrowser/comments/1irg2ui/

Evidence:
- A-/B+：公开同期第一人称故障报告；用于机制，不作为故障率统计。

这条线对应的不是“反云”，而是成熟后的 **defensive portability**：

```text
sync
+ export
+ offline copy
+ version history
+ rollback
+ understandable conflict semantics
```

### 10.3 中国同期用户开始主动寻找“浏览器之外”的保管层

2024 年一名 V2EX 用户同时使用 Arc/Chrome/Safari，因为三者不能顺利统一同步，只能导出 Arc bookmarks 再导入其他浏览器；另一名 Arc 用户甚至描述，收藏网站时会再打开 Edge 收藏一份。

Sources:
- V2EX，《Mac 下，如何同步 Arc, Chrome & Safari 三家浏览器的 bookmark？》，2024-11-29：  
  https://v2ex.com/t/1093608
- V2EX，《有没有 arc 浏览器和其他浏览器书签同步的插件？》，2024-12-12：  
  https://fast.v2ex.com/t/1097045

Evidence:
- A-/B+：同期第一人称技术社区材料。

2025 年又有中文用户/开发者直接把 WebDAV、GitHub Gist、自托管作为跨设备同步后端，甚至把“能查看变更历史”当成优势。

Sources:
- V2EX，《TabTab 支持自托管的书签自动同步》，2025-03-23：  
  https://v2ex.com/t/1120433
- V2EX，《请问有哪款好用的书签同步管理的浏览器插件吗》，2025-08-07：  
  https://www.v2ex.com/t/1150511

Evidence:
- A-/B+：同期社区实践；明显偏技术用户，不代表普通用户总体。

这里的历史方向很值得保存：

> 早期云同步的未来想象，是“我终于不必自己搬”；防守型未来的一部分，却是在重新争取“我至少要有一个自己能导出、能备份、能回滚的版本”。

### 10.4 平台级“收藏”也会终止，出口决定记忆是否真正可携带

2026-01 的报道显示，Microsoft Edge Dev 已向用户提示准备淘汰 Collections/“集锦”，并提供迁到 Favorites 或导出 CSV 的路径；迁到 Favorites 时网页链接可以迁移，但图片、备注等信息需要另行处理。

Source:
- 新浪科技转 IT之家，《曝微软 Edge 浏览器“集锦”功能将停用，用户需尽快导出数据》，2026-01-11：  
  https://finance.sina.com.cn/tech/digi/2026-01-11/doc-inhfxmct7841645.shtml

Evidence:
- B：媒体基于 Edge Dev 提示的报道；不是本轮直接核验的微软正式停用公告，因此只写“已出现迁移提示/报道”，不把最终停用日期写死。

这说明：

**平台内收藏对象经常比 URL bookmark 更丰富，也因此更难无损迁走。**

网页、图片、备注、标签、排序、上下文一旦被一个平台私有数据模型吸收，导出时就可能重新退化成一串链接。

---

## 11. 四种时代时间感：书签怎样参与“未来”

### 11.1 2005–2012：扩张型未来——“以后还会用，所以先存下来”

收藏表达的是一种轻微但明确的未来信念：

> 这个页面对未来的我仍然有价值。

网络收藏夹又让这种未来跨过机器和地点。

### 11.2 2015–2019：拥堵型未来——“值得以后看”的东西越来越多

保存摩擦越来越低、信息供给越来越大、浏览器/账号/平台越来越多，于是：

```text
future-useful candidates ↑
organization labor ↑
platform dependencies ↑
```

未来不是没有，而是“以后再看”堆成了长期 backlog。

### 11.3 2020–2022：偶发型未来——路径还在，不代表条件还在

书签目标可能因为：

- 页面更新；
- 服务关闭；
- 域名迁移；
- 权限变化；
- 政策/价格/招聘过期；
- 设备/账号不可用

而失效。

收藏的是过去一次可达状态，不是未来的保证。

### 11.4 2023–2026：防守型未来——“不要只告诉我能同步，还要告诉我怎样退出”

成熟问题从：

> 能不能把收藏放进云里？

转成：

> 能不能导出、自己托管、保留历史、检测死链、在错误同步后恢复？

这是从 **availability promise** 转向 **custody + reversibility**。

---

## 12. 对“普通人有多少种活法”的具体影响矩阵

| 生活维度 | bookmark / retrieval memory 能改变什么 | 不能自动解决什么 |
|---|---|---|
| 教育 | 保留招生、课程、论文、工具入口，跨设备继续查 | 页面过期、资格条件与真正能否入学 |
| 就业 | 保存职位、公司、考试、技能资料 | 招聘是否仍有效、候选人是否被录用 |
| 住房/迁移 | 保存租房、地图、政策、城市信息入口 | 房源仍在、价格可承受、制度资格 |
| 照护/医疗 | 保存医院说明、用药/疾病资料入口 | 临床信息是否可靠、患者是否真正获得服务 |
| 非正规劳动 | 保存客户、平台规则、工作教程入口 | 平台规则是否改变、劳动关系是否正式化 |
| 长期中断 | 数年后重新接上旧兴趣/职业资料路径 | URL 和内容是否仍存在、本人是否还懂当时上下文 |
| 社交关系 | 共享 bookmark/tag 可形成兴趣弱连接 | 不能等同真实关系强度 |
| 未来预期 | “以后再看/以后会用”变成机器对象 | 收藏本身不证明未来一定执行 |
| 身份 | 网络收藏夹常绑定长期账号 | 账号失效/平台关闭时仍可能断裂 |
| 历史保存 | bookmark 集合可以留下旧 Web 的路径清单 | bookmark 不是 WARC，也不证明目标内容被保存 |

---

## 13. 历史可见性：bookmark 是旧 Web 的目录化石，但不是网页快照

个人 bookmark collection 对研究者很诱人，因为它可能记录：

- 当时哪些站点被某人认为值得再次访问；
- 网站旧 URL；
- 用户自定义标题；
- 文件夹分类；
- 社交书签 tag；
- 某些已经死亡的 Web 路径。

但必须非常谨慎：

1. 私人收藏本身可能暴露疾病、宗教、性、财务、职业、家庭等敏感兴趣；
2. 一个人收藏某页不等于赞同它；
3. 收藏时间不一定等于首次访问时间；
4. 当前导出的收藏集合可能经历多次迁移、合并、同步和重命名；
5. 一个 URL 今天还活着，也不代表今天的内容就是当年收藏时的内容。

因此高质量旧网研究应优先保存/分析：

```text
service architecture
format
field semantics
export/import behavior
public product/help pages
anonymized aggregate patterns
```

而不是批量重新公开普通人的私人兴趣图谱。

---

## 14. 反例与后见之明风险

### 14.1 不要写成“收藏夹取代记忆”

早期研究明确显示用户会混用邮件给自己、打印、保存文件、写文档、个人主页等方法。bookmark 只是众多 keeping strategies 之一。

### 14.2 不要写成“在线书签一出现，普通人就跨设备无缝工作”

账号、浏览器兼容、网络环境、插件、登录、网吧安全、移动端能力都可能成为条件。

### 14.3 不要把“收藏次数”当“阅读次数”

`save != read != revisit != act`。

### 14.4 不要把社会书签公开数据当全部生活

公开 Delicious/QQ书签/网摘容易被研究；私人 IE Favorites、手机本地 bookmark 和私人账号集合更难被 archive，因此历史样本天然偏向公开/可索引行为。

### 14.5 不要把链接腐烂浪漫化成“旧互联网消失了”

URL 失效可能是内容删除，也可能是域名迁移、HTTPS、路径重构、登录限制、robots、编码、重定向或 archive replay 问题。必须逐 URL 判断。

---

## 15. 尚未确定

1. 中国 1998–2003 普通用户收藏夹平均规模、备份频率，目前没有可靠总体调查；
2. 365Key、新浪 VIVI、百度搜藏、QQ书签的可比活跃用户/留存数据仍不足；
3. `cang.baidu.com`、`shuqian.qq.com` 的高质量 historical memento 尚未在本轮实际验证；
4. 社交书签与后来微博/微信/视频平台内部“收藏”的迁移关系需要另做平台状态研究，不能直接写成线性替代；
5. 2015–2019 普通非技术用户究竟怎样在浏览器 bookmark、微信收藏、App 内收藏、截图和“发给自己”之间分配，仍缺代表性材料；
6. 2023–2026 自托管/版本化 bookmark 是技术用户防守性实践，目前不能写成大众趋势。

---

## 16. 这轮改变了什么理解

此前的“信息获取”容易被写成一条从目录到搜索引擎、再到推荐/AI 的线；这一轮补出了另一半：

> **第一次找到信息，只解决今天；能否多年以后重新找到它，决定这条信息能不能真正成为一个人长期生活的一部分。**

早期收藏夹把“回去的路”交给一台电脑；网络书签把路交给账号；同步把路复制到所有设备；社会书签把私人路径变成公共兴趣信号；快照/全文收藏又开始承认只保存 URL 不够；到今天，出口、版本和自托管重新成为问题。

所以 Internet 给普通人的并不只是“世界上更多东西可找”。它还逐渐形成一种新的生活资产：

## **一套自己走过、以后还可能再走的信息路径。**

而这套资产是否真的属于你，最终要看你在设备损坏、浏览器更换、平台关停、同步出错和网页死亡以后，是否仍能把它带走。

---

## 17. 研究饱和判断

本轮出现新的生活/通信机制：

- retrieval-memory externalization；
- information-trail portability；
- collection debt；
- bookmark custody / sync blast radius；
- locator preservation 与 content preservation 的分离；
- 私人检索记忆的 archive visibility bias。

并取得 1994 Mosaic 海外前史、2006–2009 中文同时代材料、2018/2019 同期跨浏览器第一人称、2020–2022 反例研究及 2023–2026 同期防守型实践。因此本阶段连续“无实质新增”计数仍为 **0/3**，不进入 closure。
