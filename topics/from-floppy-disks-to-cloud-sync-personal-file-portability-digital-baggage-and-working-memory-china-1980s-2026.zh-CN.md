# 从“文件在那张盘里”到“换台电脑也能接着做”：个人文件、数字行李与工作记忆可携带性（中国，1980s—2026）

> 研究问题：普通人上学、换工作、出差、搬家、去网吧、在宿舍和办公室之间移动时，正在写的文档、表格、课件、代码、资料和其他数字文件，究竟怎样跟着人一起走？
>
> 本篇补的是仓库里此前没有单独建模的一层基础设施：**personal working-memory portability / 个人工作记忆可携带性**。照片专题关注“过去能不能留下来”；本篇关注“事情还没做完时，下一台机器能不能接着做”。
>
> old Web 执行层对应：`tmzncty/old-web-archaeology/docs/ONLINE_STORAGE_NETWORK_DISK_UPLOAD_DOWNLOAD_SHARE_SYNC_AND_FILE_CUSTODY_STATE_GAPS_1999_2015.md`

---

## 0. 先把“文件跟着人走”拆成五种不同能力

数字文件的“可携带”不是单一状态。

至少要区分：

1. **physical portability / 物理携带**：软盘、光盘、U 盘、移动硬盘由人带着走；
2. **network transfer / 网络传送**：把文件从一台机器主动发到另一台机器；
3. **remote storage / 远程存储**：文件放在网络端，换机器后重新取回；
4. **synchronization / 同步**：多个设备自动趋向同一版本；
5. **collaborative document state / 协作文档状态**：不再主要搬运“文件副本”，而是在同一个远程对象上继续修改。

固定边界：

```text
file exists somewhere
!= user can remember where it is
!= user can reach it now
!= user can authenticate
!= bytes can be downloaded
!= downloaded bytes are the newest version
!= file can be opened by software here
!= work can actually continue
```

本轮新增几个概念：

- **personal working-memory portability / 个人工作记忆可携带性**：一个人的未完成数字工作能否跨设备、地点和人生阶段继续；
- **digital baggage / 数字行李**：为了让未来的自己继续工作而必须随身携带、复制、同步或托管的一组文件；
- **device detachment / 文件与设备解绑**：文件能否不再依附于某台具体电脑；
- **transfer labor / 文件搬运劳动**：复制、命名、插拔、上传、下载、确认版本等人为维护；
- **sync externalization / 同步外包**：由后台服务替用户维护多设备副本的一致性；
- **version divergence / 版本分叉**：多个副本继续分别修改，产生“final / final2 / 最新 / 真最终”等冲突；
- **account-bound custody / 账号绑定保管**：文件不再依附机器，却开始依附网络账号、服务商和恢复链；
- **archive-exit labor / 存储退出劳动**：平台缩容、停服或迁移时，把多年积累重新搬回自己手里；
- **storage abundance / 存储丰裕**：容量成本下降后，“要不要保存”不再是主要筛选点，查找、整理和备份开始成为新劳动。

---

# 1. Internet 没有发明远程文件传输，也没有让普通人一夜之间停止搬盘

## 1.1 海外前史：远程文件交换远早于 consumer cloud

1980 年 RFC 765 对 FTP 的目标写得非常明确：促进程序和数据文件共享、屏蔽不同主机存储系统差异，并可靠高效地传输数据。它已经包含 `STOR`、`RETR`、账号、密码、存储配额和恢复等状态。

Source:

- RFC Editor, RFC 765, *File Transfer Protocol*, 1980-06: <https://www.rfc-editor.org/info/rfc765/>

Evidence grade：**A / original technical standard**。

但这里必须立即划边界：

> **ARPANET / Internet 上已经能传文件 ≠ 1980 年普通家庭已经拥有“云盘生活”。**

FTP 首先属于联网机构和计算机用户的技术基础设施。普通消费者的文件可携带，长期仍主要依赖物理介质。

---

## 1.2 中国 1994 之前不能写成“完全没有网络”，也不能把科研连通写成大众可得

中国科学院档案材料显示，1986 年高能所人员已通过卫星链路远程登录 CERN 并发送电子邮件；1984 年高能所与水电科学院之间也已有微波通信连接，可从远程终端修改或提交作业。1994 年 4 月 20 日的 64K 国际专线则是中国实现 Internet 全功能连接的明确节点。

Sources:

- 中国科学院档案馆，2024，《中国互联网从中国科学院起步——中国接入互联网始末》：<https://www.acas.ac.cn/byyxc/bydt/202404/t20240422_7174874.html>
- 中央网信办，2024，《中国全功能接入国际互联网30周年述评》：<https://www.cac.gov.cn/2024-04/20/c_1715291120716362.htm>

Evidence grade：**C/A-institutional retrospective based on archives**。

因此本篇时间边界固定为：

```text
pre-1994 research/special network file movement can exist
!= public full Internet access
!= ordinary household access
!= ordinary people routinely storing files online
```

对大多数普通人的数字文件来说，Internet 之前更现实的路径仍是：

```text
computer A
→ floppy / removable medium
→ person physically carries it
→ computer B
```

这里的“网络前史”价值，不是把少数科研人员当成普通人，而是说明：**让文件脱离机器、跨地点继续存在的技术问题早已提出；真正晚到的是普通人的可及性。**

---

# 2. 软盘、U 盘和光盘：文件第一次成为可以随身带走的“行李”

2005 年一篇同时代技术文章回顾当时的日常转换：软盘曾广泛用于携带文件，随后 U 盘普及；作者接着提出一个非常生活化的故障——如果偏偏没有带 U 盘，而面前的电脑可以联网怎么办？答案就是“网络优盘”。

Source:

- 新浪科技 / 天极 yesky，2005-08-30，《网络上常见的网络优盘介绍与点评》：<https://tech.sina.com.cn/s/2005-08-30/0909706572.shtml>

Evidence grade：**B / contemporaneous technology-use article**。

这篇材料虽然发表于 2005 年，不能直接证明某个具体 1990s 人怎样用软盘，但它非常适合保存当时人自己理解的媒介谱系：

```text
软盘
→ U盘
→ 网络优盘
```

物理介质给人的自由是巨大的：

- 学校电脑上写的作业可以带回宿舍；
- 单位里的文档可以带到另一台机器；
- 文件不再只能“住”在原电脑硬盘里。

但 transfer labor 也完全由人承担：

```text
找到正确文件
→ 复制
→ 等待写入完成
→ 安全拔出
→ 别把盘忘在原处
→ 到新机器插入
→ 再复制 / 打开
→ 判断哪个版本更新
```

因此“文件可携带”最早并不等于“文件跟着人自动出现”。

---

# 3. 1999–2005：个人网络硬盘把文件从“我带着介质”改成“我记得账号”

## 3.1 海外：1999 年 X:drive 已经把“任何联网电脑都能拿到文件”做成 consumer proposition

1999 年的 X:drive 提供 25MB Web 存储；同年报道说用户可以用浏览器存储、访问和共享文件。2000 年法国 01net 的操作文章则把日常场景说得非常清楚：25MB 免费空间，文件以后可以从世界上任何一台联网电脑重新取回。

Sources:

- InternetNews, 1999-12-01, X:drive funding / Web hard-drive service: <https://www.internetnews.com/small-business/xdrive-secures-20-million-in-funding/>
- 01net, 2000-07-03, *Sauvegarder ses données sur le Web*: <https://www.01net.com/actualites/sauvegarder-ses-donnees-sur-le-web-112928.html>
- WIRED, 1999-08-09, *File Storage Matter of Trust*: <https://www.wired.com/1999/08/file-storage-matter-of-trust/>

Evidence grade：**A/B contemporaneous press**。

WIRED 同期就已经提出隐私与信任问题：把个人文件放到远方公司的硬盘上，方便和风险从一开始就是同一个设计的两面。

于是“设备解绑”并没有消灭依赖，而是迁移了依赖：

```text
before:
我的文件依赖我有没有把那张盘带来

after:
我的文件依赖网络 + 账号 + 服务商仍然运行
```

---

## 3.2 中国：2004 QQ 网络硬盘已经直接把 U 盘当成要被替代的对象

2004 年 QQ 网络硬盘推出时，同期报道直接用“还在用 U 盘插来插去、光盘刻来刻去吗”作为卖点；普通用户可有 16MB，QQ 会员 128MB，并要求 QQ2004 Beta 或更高版本。

Sources:

- cnBeta, 2004-07-07，《QQ推出128M网络硬盘!》：<https://www.cnbeta.com.tw/articles/4207.htm>
- 2005 年网络优盘横向资料见：<https://tech.sina.com.cn/s/2005-08-30/0909706572.shtml>

Evidence grade：**B / contemporaneous technology news**。

这里有一个非常重要的旧 Web / IM 边界：

> QQ 网络硬盘并不是“纯网页产品”。

它依赖 QQ 客户端版本和登录状态；因此 Internet Archive 即使以后保存了一个 `disk.qq.com` 的外部页面，也不等于保存了当时用户真正使用的客户端事务链。

---

## 3.3 2005：同一个“网盘”内部就已经存在不同时间语义

2005 年免费网络硬盘横评记录：

- QQ 免费空间约 16MB；
- Mofile 有 8MB **保管箱**；
- 同时另有约 1024MB **接力站**；
- 接力站大文件最多存放三天，之后自动删除。

Source:

- 新浪科技 / IT.COM.CN，2005-09-08，《网络大仓库 免费网络硬盘横向评测》：<https://tech.sina.com.cn/s/s/2005-09-08/1159715065.shtml>

Evidence grade：**B / contemporaneous comparative review**。

这件事对生活史很关键：

```text
remote storage
!= durable personal archive
```

一个服务可以同时承担两种完全不同的生活功能：

- **保管箱**：未来的我还要回来；
- **接力站**：我只要让另一台机器 / 另一个人这几天拿到它。

如果把两者都概括成“云存储”，就会丢掉当时普通用户真实的时间感。

---

# 4. 2005–2012：扩张型未来——“我可以去别的地方，工作不必留在这台电脑里”

这一阶段最值得研究的不是容量数字本身，而是 **pre-positioned work / 工作预置**：人在出发以前就可以把下一站要用的文件放到网络上。

2005 年“网络优盘”文章的基本场景，就是“没有带 U 盘但面前有网络”；2008 年新浪博客上仍有人整理大量免费网络硬盘 / 网络 U 盘服务，说明“文件不随机器走、而随账号走”的使用想象已经进入普通 Web 内容。

Sources:

- 新浪博客，2008-01-30，《免费网络硬盘[U盘]大全》：<https://blog.sina.com.cn/s/blog_4b02f08c01008fko.html>
- 新浪科技，2005-08-30：<https://tech.sina.com.cn/s/2005-08-30/0909706572.shtml>

Evidence grade：**B/C contemporaneous user-curated / technology-use material**。

注意：博客汇总能证明“普通 Web 用户在整理和讨论这些服务”，不能证明所有学生或白领都在用网盘。

---

## 4.1 2008 海外第一人称：Dropbox 的起点恰好就是“忘带 U 盘以后没法继续工作”

Dropbox 在 2008 年 9 月公开发布时，创始人 Drew Houston 写道，2006 年自己在波士顿南站准备坐车去纽约时忘了 U 盘，因此无法做“real work”，于是开始写后来成为 Dropbox 的代码。

Source:

- Dropbox 官方博客，2008-09-11, *Dropbox launches to the public!*: <https://blog.dropbox.com/topics/company/dropbox-launches-to-the-public>

Evidence grade：**A/B contemporaneous founder first-person**。

这当然不是“普通用户调查”，但它准确抓住了一个跨国共同问题：

> **physical portability still fails when the person and the medium separate.**

Dropbox 进一步把问题从“我主动上传、以后主动下载”改成：

```text
把文件放进一个本地文件夹
→ 客户端自动上传
→ 另一台电脑自动得到同一对象
```

也就是从 **remote disk** 转向 **sync externalization**。

---

## 4.2 2012：百度网盘把“跨终端”变成大众产品的中心承诺

2012 年百度网盘公测时提供 15GB 初始空间、Windows / Android 等客户端、跨端同步和链接分享。同期报道把“手机及电脑中的文件备份到云端”“Windows、Web、手机跨终端同步”当成主要卖点。

Sources:

- IT之家，2012-03-23，《百度网盘初体验：进军云存储，注册即送15G》：<https://www.ithome.com/0/013/422.htm>
- 中新网 / CNTV，2012-05-07，《无限云存储体验：百度网盘开放用户邀请》：<https://news.cntv.cn/20120507/111385.shtml>
- 第一财经转新浪科技，2012-03-23：<https://www.yicai.com/news/1559633.html>

Evidence grade：**B / contemporaneous product reporting**。

于是文件的位置越来越不像一个物理坐标：

```text
以前：文件 = 哪台机器 / 哪张盘上的哪个路径
后来：文件 = 我的账号里那个对象
```

这就是 **location-addressable → identity-addressable file** 的转折。

---

# 5. 2013：存储丰裕并不只是“容量变大”，它改变了人的筛选行为

2013 年国内云盘“空间大战”中，100GB、1TB、2TB 乃至更大宣传快速出现。同期技术媒体记录百度从 1TB 活动继续提升到 2TB，115、360、腾讯等也以大容量争夺用户。

Sources:

- 快科技，2013-09-02，国内云盘空间大战：<https://news.mydrivers.com/1/274/274622.htm>
- 同期个人技术博客对 2TB 活动的操作记录：<https://albertblog.tw/641/%E3%80%90app%E8%BB%9F%E9%AB%94%E3%80%91%E5%85%8D%E8%B2%BB%E9%9B%B2%E7%AB%AF%E7%A9%BA%E9%96%93%EF%BC%8E%E7%99%BE%E5%BA%A6%E9%9B%B2>

Evidence grade：**B / contemporaneous technology press + user tutorial**。

不要把广告容量直接写成“普通人实际存了 2TB”。真正重要的生活机制是：

```text
容量稀缺：
保存前先决定值不值得占空间

容量丰裕：
先存下来 → 以后再决定是否整理 / 删除
```

于是新的成本开始累积：

- 文件越来越多；
- 目录越来越深；
- 旧副本越来越难辨认；
- “在哪里”不再是唯一问题，“哪一份才是现在要用的”变得更重要。

这就是 `storage abundance → curation debt / 整理债`。

---

# 6. 2015–2019：拥堵型未来——不是带不走，而是“已经存了这么多，我还能不能把它们搬出来”

## 6.1 2016 停服潮把云端依赖突然变成退出劳动

2016 年不到两个月，华为网盘、UC 网盘、金山快盘、新浪微盘等先后关闭或调整个人存储服务；人民网同期报道把网盘定义为能够进行文件存储、访问、备份和共享的在线服务，并回顾 2013 年容量大战。

Source:

- 人民网 IT，2016-05-07，《多家百万用户网盘关停服务 网盘行业出路何在》：<https://it.people.com.cn/n1/2016/0507/c1009-28332179.html>

Evidence grade：**B / contemporaneous news**。

360 云盘后来宣布停止个人服务以后，因大量用户集中下载，下载期限不得不按数据量延长：200GB 以下延至 2017 年 4 月 30 日，200GB 以上延至 2017 年 10 月 31 日。同期报道描述，一些很久不上线的人也重新登录下载，造成拥堵。

Sources:

- 中国经济网转载，2016-11-01：《360云盘关停：教你快速转移个人照片》：<https://district.ce.cn/newarea/roll/201611/01/t20161101_17402175.shtml>
- 360 社区，2016-10-25，云盘停止服务说明：<https://bbs.360.cn/thread-14620422-1-1.html>

Evidence grade：**A/B platform notice + contemporaneous reporting**。

这里出现了一个此前物理介质时代很少有的时间结构：

```text
过去几年：上传几乎不费思考
某一天：平台宣布未来某日清空
接下来几个月：必须反向把多年数据重新搬走
```

即 **archive-exit labor / 存储退出劳动**。

云端让积累容易，却可能把退出成本延迟到未来一次性结算。

---

## 6.2 2018–2019：账号持续存在也开始需要维护

2018 年末，百度网盘宣布：2018-12-25 至 2019-12-31 期间至少登录一次才能继续保留此前获得的 2TB 免费空间；否则 2020 年起调整为 100GB，超过新容量的账号只能访问和下载旧文件、不能继续写入。

Source:

- 2018-12-25 同期报道：<https://www.ifanr.com/1152540>

Evidence grade：**B / contemporaneous product-policy reporting**。

这形成一种新的“数字家务”：

> 文件也许多年没动，但为了让过去积累的空间和写入权继续存在，用户必须在规定时间内回来证明自己仍然“活跃”。

2019 年少数派的一篇第一人称技术文章则明确说，很多用户同时使用一个或多个国内外云盘；作者讨论自己已经形成固定文件管理习惯，不愿把散落在不同路径的文件全部搬进某个“同步盘”，于是寻找任意文件夹同步方法。

Source:

- 少数派，2019-10-19，《3 种方法，帮你实现云盘的任意文件夹同步》：<https://sspai.com/post/57053>

Evidence grade：**B / contemporaneous first-person technical-use trace**。

它很适合描述“拥堵型未来”的文件版本：

```text
文件已经到处都是
+ 云盘也不只一个
+ 本地已有自己的目录秩序
→ 现在真正困难的是让这些既有秩序彼此同步
```

这不是“没地方存”，而是 **too many locations, too many copies, too much history**。

---

# 7. 2020–2022：偶发型未来——文件不只是跟着人走，而是人突然不能去办公室时，工作对象仍必须活着

2020 年 2 月，北京一名互联网投资公司员工王爱文接受同期采访时说，公司开始“云复工”；因为通勤和聚集有感染风险，很多事情通过视频会议就能解决，项目书可以在线协同编辑，他直接评价“很方便”。

Source:

- 人民日报海外版 / 人民网，2020-02-21，《“云复工”解企业燃眉之急》：<https://env.people.com.cn/n1/2020/0221/c1010-31598008.html>

Evidence grade：**B / contemporaneous first-person workplace interview**。

另有 2020 年同期报道记录在线文档在学校、企业中的实时多人修改和异地协同。

Source:

- 科技日报 / 人民网，2020-03-10，《疫情催热远程办公 在线文档迎来春天》：<https://it.people.com.cn/n1/2020/0310/c1009-31624506.html>

Evidence grade：**B**。

这里发生的是比“云盘”更深的一步：

```text
U盘时代：我带走一个文件副本
网络硬盘：我去远端取一个文件副本
同步盘：多台机器自动拥有相近副本
在线文档：大家修改的本来就是同一个远程状态
```

所以疫情期间真正提供 resilience 的，不只是“文件备份在云端”，而是 **unfinished work no longer requires access to the office computer**。

反例也必须保留：

- 不是所有职业都能远程；
- 在线协同依赖网络、账号和平台容量；
- 多人编辑并不会自动解决权限、误删、版本恢复和组织管理问题；
- “能打开文档”不能代替实验室、机器、柜台、物流和照护等必须在场的劳动。

因此：

```text
file portability increases remote-work feasibility
!= remote work becomes universally possible
```

---

# 8. 2023–2026：防守型未来——“在云上”不再等于“已经备份”

2025 年 Western Digital 委托 Researchscape 的全球在线调查覆盖 10 个国家、6118 名受访者；厂商公布的结果称，87% 表示会主动或自动备份个人数据。中国相关报道给出的受访者数据中，云存储、U 盘、外置硬盘、NAS 等同时存在，而不是单一媒介全面替代其他媒介。

Sources:

- Western Digital, 2025-03-25, World Backup Day survey: <https://www.westerndigital.com/en-ie/company/newsroom/press-releases/2025/2025-03-25-western-digital-world-backup-day>
- 新浪财经对中国侧数据的整理：<https://finance.sina.com.cn/cj/2025-04-10/doc-inesschw3265380.shtml>

Evidence grade：**B/C / vendor-sponsored survey**。

限制必须写在前面：这是厂商委托的在线调查，不能把百分比直接外推成“中国所有普通人的真实备份率”。

但它至少支持一个当代结构判断：

> **cloud did not simply erase removable storage; many users now build mixed storage stacks.**

2025 年另一份中国个人网盘用户调查称，受访网盘用户同时关注安全、共享、资料存储和手机备份。它同样属于市场调查而非官方人口统计，只能作为“当前网盘功能重心”辅助证据。

Source:

- 艾媒咨询，2025-06-07，《2025年中国个人网盘市场发展状况及用户行为调查数据》：<https://www.iimedia.cn/c400/106309.html>

Evidence grade：**C / commercial market survey**。

防守型未来因此不宜写成“NAS 取代云盘”，而应写成：

```text
单一副本意识下降
→ 多位置副本 / 自动同步 / 本地 + 云端并存
→ 重新关注谁控制副本、如何退出、账号失效后怎么办
```

新的生活技能不是继续追求“更大免费空间”，而是知道：

- sync 不是 backup；
- 一个账号不是全部副本；
- 自动同步也会同步误删；
- 云平台会调整价格、政策和容量；
- 本地硬盘也会坏；
- 真正的 resilience 来自故障域分离。

---

# 9. 这一条线怎样改变“普通人有多少种活法”

## 9.1 教育

文件可携带以后，学生不必在同一台学校电脑上从头到尾完成作业；网络存储和同步进一步让宿舍、机房、家里、图书馆之间形成连续工作面。

但：

```text
有网盘账号 != 有稳定宽带 != 所有课程都数字化
```

## 9.2 就业与职业迁移

对于文字、设计、编程、行政等数字对象密集职业，工作文件从“办公室电脑里的东西”变成账号可达对象以后，换地点、出差、临时远程工作的可行性提高。

这不是“互联网让人可以任意迁移”，但它减少了一种具体的地点锁定：

> **必须回到那台机器旁边才能继续。**

## 9.3 非正规劳动

自由职业者、临时合作、外包者特别依赖文件交换和版本控制；网络硬盘降低大文件交付门槛，却也可能把工作证据、交付物和账号权限绑到私人平台上。

需要后续补更多第一人称材料。

## 9.4 长期中断

一段工作中断几年以后，本地旧电脑可能已经坏了；云账号也可能缩容、停服或忘记密码。

“文件曾经上传过”因此不能自动等于“人生重新开始时还能找回来”。

## 9.5 迁移

物理介质降低的是“搬电脑”的必要；云端降低的是“搬介质”的必要。

但每次减少一种行李，都增加一种后台依赖。

---

# 10. 四种未来的对照

| 时段 | 文件基础设施 | 当时更典型的未来感 | 新自由 | 新负担 |
|---|---|---|---|---|
| 2005–2012 扩张型 | U盘 + 网络硬盘 + 初代同步 | “换台电脑也能拿到我的东西” | 地点选择扩大 | 上传下载、带宽、账号、版本 |
| 2015–2019 拥堵型 | 多云盘 + 多设备 + 大量历史文件 | “都存下来了，但现在到底在哪一份” | 可积累、可同步 | 版本分叉、整理债、停服迁移 |
| 2020–2022 偶发型 | 在线文档 + 云协同 | “人突然去不了办公室，项目还能继续” | 异地连续工作 | 网络/平台/权限成为新故障域 |
| 2023–2026 防守型 | 云 + 本地 + 自动备份 + 多副本 | “不要让一个账号或一块盘成为唯一副本” | 恢复路径增加 | 多位置管理、成本、隐私、退出 |

这条变化不是线性进步。

每个阶段都只是把“数字行李”放到了不同地方：

```text
手里
→ 口袋
→ 远端账号
→ 自动同步服务
→ 多个服务与多个本地副本共同组成的存储栈
```

---

# 11. 跨国比较：哪些是 Internet 时代共同变化，哪些不能照搬

## 11.1 共同变化

美国/欧洲 1999–2000 的 X:drive 与中国 2004–2005 的 QQ 网络硬盘 / Mofile 有高度相似的问题结构：

- 浏览器或客户端登录；
- 免费小容量；
- 在线保存；
- 异地访问；
- 分享；
- 对服务商信任；
- 收费模型不稳定。

Dropbox 2008 又把“网络硬盘”推进到本地目录自动同步。

这些更像 consumer Internet 的共同演化，而不是中国特有。

## 11.2 中国材料的特殊点

中文旧网里，网络硬盘常与：

- QQ 客户端；
- 门户账号；
- SP / 大型综合互联网公司；
- 网吧、校园机房等共享电脑场景；
- 2013 年极端免费容量竞争；
- 2016 年集中式个人网盘退出潮

发生紧密耦合。

但这些差异需要逐项比较，不能仅凭印象宣布“中国更依赖网盘”或“海外更重视同步”。

---

# 12. 历史可见性：为什么旧 Web 会把“网盘首页”保存得比“普通人的文件生活”完整得多

这是本专题和 `old-web-archaeology` 最重要的交叉点。

公共 archive 比较容易保存：

- 网盘首页；
- 帮助页；
- 容量宣传；
- 客户端下载页；
- 服务调整 / 停服公告；
- 公开分享页的一部分外壳。

很难保存：

- 登录后的私人目录树；
- 文件真实 payload；
- quota state；
- ACL；
- share token；
- 临时接力文件；
- 客户端同步数据库；
- “这台设备有没有真正下载完成”；
- 用户口袋里那只 U 盘。

因此固定：

```text
archive-visible storage service
!= historical personal file corpus
!= historical ordinary use
```

并且私人文件恰恰属于不应该为了考古而重新暴露的对象。

高质量研究的目标不是“把某个普通人的旧网盘全扒出来”，而是：

> **复原当时一个文件怎样从本地进入服务、如何被寻址、多久有效、怎样被另一台机器取回，以及其中哪些状态今天已经不可见。**

---

# 13. 反例与后见之明风险

## 13.1 不要写“U盘被云盘淘汰”

2025 年各种本地与云端存储并存；很多环境在无网、速度、容量、隐私和组织政策上仍需要本地介质。

## 13.2 不要把“网盘”自动等同“备份”

同步可能传播误删；分享盘可能有期限；服务可能退出；账号也可能失效。

## 13.3 不要把 2013 免费 TB 容量写成普通人真实数据量

广告配额、用户领取配额和用户真正写入的数据量是三种状态。

## 13.4 不要把 FTP 前史写成大众 Internet 使用

它证明技术谱系，不证明社会可及性。

## 13.5 不要把 2020 远程办公经验投射到所有职业

文件可携带是远程工作的必要条件之一，但绝不是充分条件。

---

# 14. 仍未确定 / 下一轮若继续可补

1. 1990s 中国高校、单位机房中普通学生/职员使用软盘、FTP、校园文件服务的更强同时代第一人称材料；
2. 2004–2007 QQ 网络硬盘、网易网盘、Mofile 的 verified Wayback capture；
3. 网吧场景里“U盘 / 邮箱附件 / QQ硬盘 / 网络盘”实际如何混用；
4. 2016 网盘退出时普通用户迁移几十 GB / 数百 GB 数据的完整个人日记；
5. 2019 年普通白领、学生对多设备同步和版本冲突的非产品评测材料；
6. 2023–2026 普通家庭和个人在云盘、移动硬盘、NAS 之间实际如何配置，而不是厂商调查中的选择题。

---

# 15. 本轮结论

这轮改变理解的关键不是“网盘越来越大”，而是：

> **数字生活里，人的行动半径有一部分取决于未完成的事情能不能跟着身体一起移动。**

软盘和 U 盘让文件第一次成为真正可以随身携带的行李；网络硬盘又让人连那件行李都可以忘在家里，只要记得账号；同步服务进一步让“搬文件”从人的动作退到后台；在线文档则让不同地点的人不必再交换多个副本，而直接共同维护一个远程状态。

但每一次“更轻”都把重量搬到了别处：

```text
忘带软盘
→ 忘带 U盘
→ 忘记账号
→ 服务停运
→ 同步错版本
→ 云上唯一副本
```

所以真正成熟的个人数字基础设施，不是让一个人永远不用想文件在哪里，而是让他即使换设备、换城市、换工作、经历中断，仍然有一条可验证的路径把自己的未完成生活接回来。
