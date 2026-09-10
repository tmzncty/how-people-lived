# 丢了身份证以后，我还是“同一个人”，但还能不能继续生活？——居民身份证、补领、异地办理与身份连续性（中国，1984—2026）

> 核心问题：现代生活越来越多地要求一个人随时证明“我就是我”。但现实中的人、公安人口登记中的人、身份证号码、手里那张卡、某个业务系统实际接受的身份证明，并不是同一个状态。一个人在异地工作、求学、迁移或旅行时丢失身份证，为什么曾经会被迫产生一次“行政返乡”？后来网络、异地受理、临时证明和全程网办，又分别消除了哪一段身体移动，而没有消除哪些制度边界？

Status: research note / cross-repo life-history study  
Last research pass: 2026-09-10  
Companion old-Web note: `tmzncty/old-web-archaeology/docs/RESIDENT_ID_CARD_WEB_REPLACEMENT_LOSS_DECLARATION_REMOTE_PHOTO_AND_CREDENTIAL_STATE_GAPS_2006_2015.md`

---

## 0. 去重：这不是已有“身份证字段”“户籍”“实名制”专题的重复

本仓已经有：

- `documents-as-life-course-interfaces.zh-CN.md`：证件怎样把生活事实压成制度可调用状态；
- `legal-name-identity-record-continuity-rare-characters-and-machine-legibility-china-1984-2026.zh-CN.md`：姓名、生僻字、15/18 位号码和跨系统 identity-string continuity；
- `documentary-portability-personnel-files-and-administrative-shadow-china-1936-2024.zh-CN.md`：档案和长期记录怎样跟着人迁移；
- 居住登记、铁路实名、手机实名、网吧实名、社保、医保、护照等多个下游接口专题。

这些专题多数把“居民身份证这张凭证能否继续被本人持有并及时重建”当作背景。本专题补的是一个更具体、也更日常的故障模式：

> **credential continuity / 凭证连续性**——现实中的人没有消失、法定身份没有消失、身份证号码也没有消失，但那张最常用的可携带证明因为遗失、损坏、到期或人在异地而暂时不可用时，生活是否仍有可执行的备用路线？

因此这里不重写完整户籍史，也不重写“身份证号能否被 Web 表单正确表示”。重点是：

```text
人仍在
≠ 权威人口记录丢失
≠ 手中仍有有效实体证件
≠ 下游机构此刻能完成身份核验
≠ 本次现实事务仍可继续
```

---

## 1. 把“一张身份证”拆成至少十个状态

至少区分：

1. **physical person**：现实中的人；
2. **authoritative civil/person record**：公安人口信息系统中的权威记录；
3. **citizen identity number**：长期标识符；
4. **credential issuance record**：某一版身份证已经签发；
5. **physical card possession**：卡片此刻在不在本人手中；
6. **card validity**：证件是否在有效期内、是否已进入失效状态；
7. **visual readability**：肉眼可否读取；
8. **machine readability**：芯片/机读是否可工作；
9. **relying-party verification**：银行、铁路、旅馆、政务窗口等是否完成“人—证—权威状态”核查；
10. **transaction-specific acceptance**：当前业务是否承认这种身份证明；
11. **real-world completion**：取款、乘车、住宿、办事等是否真正完成。

因此固定以下边界：

```text
person exists ≠ card possessed
card possessed ≠ card valid
card machine-readable ≠ card currently accepted
identity number known ≠ identity sufficiently proven
replacement application submitted ≠ new card issued
new card issued ≠ new card in hand
lost-card declaration ≠ replacement completed
temporary proof accepted for one transaction ≠ general-purpose identity card
```

把这一整套能力称为 **portable personhood / 可携带的人格证明**：不是说人靠证件才存在，而是一个已经存在的人在离开熟人、单位和户籍所在地以后，能否用一个标准接口快速让陌生机构确认其制度身份。

---

## 2. 前互联网基线：1984 年以后，“证明我是我”开始更可携带

北京市公安局警察博物馆的机构史记录，1984 年 8 月北京首批居民获得居民身份证，第一张证件在当年首发。后来的公安机构回顾还保存了一个很具体的生活理由：第一位领证者经常外出演出、领取稿费，身份证对这种离开固定单位和居住地的活动尤其有用。

Source:
- 北京市公安局警察博物馆，《1984年全国首发第一张居民身份证》：https://gaj.beijing.gov.cn/jcbwg/zgdc/jzzn/202007/t20200720_1952436.html
- 北京市公安局，《40年变迁背后，两代身份证的北京试点》，2024-10-02：https://gaj.beijing.gov.cn/xxfb/jwbd/202410/t20241002_3911265.html

Evidence: **C（后来的官方机构史；可确认制度谱系，不作为 1984 年普通人总体体验统计）**。

这里发生的变化不是“国家第一次有个人登记”。户口、单位、人事和基层证明链早已存在。居民身份证更重要的生活史意义是：

> **身份从一个需要回到原关系网络里证明的事实，逐渐获得了一件可随身携带、可在陌生场所重复出示的标准载体。**

这与互联网无关，甚至早于普通家庭个人电脑普及。

---

## 3. 2003—2004：二代证把实体证件变成“可机读凭证”，但不是互联网凭证

《中华人民共和国居民身份证法》于 2003 年 6 月 28 日通过、2004 年 1 月 1 日施行。法律明确：居民身份证用于证明公民身份；公民身份号码是唯一、终身不变的身份代码；在申请领取、换领、补领居民身份证期间，急需使用身份证的，可以申请临时居民身份证。

Source:
- 政府站点保存的《中华人民共和国居民身份证法》：https://www.miluo.gov.cn/25287/25292/25293/42753/content_1231204.html

Evidence: **A（法律文本的政府保存版本）**。

2004 年 3 月，上海、深圳、浙江湖州启动第二代居民身份证试点换发。同期新华社材料说明二代证采用非接触 IC 卡技术，具备视读和机读两种功能；全国计划 2005 年全面启动集中换发、到 2008 年底基本完成。

Sources:
- 新华社同期稿的搜狐保存页，2004-03-30：https://news.sohu.com/2004/03/30/84/news219658493.shtml
- 福建省政府 2004 年换发二代证通知：https://zfgb.fujian.gov.cn/6614

Evidence: **A/B（同期政府文件 + 新华社同期报道）**。

### 关键边界：machine-readable ≠ Internet-connected

二代身份证本身已经是一种数字化凭证，但“芯片可机读”不能写成“刷卡时必须连公共互联网”。实际核验可以发生在专网、封闭系统、本地读卡器与后台数据库的组合中。

因此中国数字身份史至少要分：

```text
人口登记数字化
→ 身份号码标准化
→ 实体证件机读化
→ 部门联网核验
→ Web/移动端远程办证
→ 事务型电子身份证明
```

这些不是同一天发生的。

---

## 4. 一个丢证事件为什么会把流动生活突然“拉回户籍地”

假设一个人在深圳工作、户籍在湖南：

```text
本人现实位置：深圳
权威人口记录：湖南
日常工作与租住：深圳
身份证遗失：深圳
传统补领受理点：户籍所在地
```

那么证件遗失会制造 **credential loss shock / 证件丢失冲击**：本人没有失去法律身份，却可能突然失去多个下游事务的最快入口；而修复入口又在几百或上千公里之外。

这会产生 **administrative return journey / 行政返乡**：

> 返乡不是为了探亲、过节或搬回去生活，而只是为了把一个已经存在的制度身份重新装进一张可携带卡片。

这类行程很少进入宏观“人口迁移”统计，却会真实吞掉请假、路费和工作机会。

---

## 5. 2005—2012 的扩张型未来：不是“网上办身份证”一步完成，而是不断削掉返乡链条中的一段

### 5.1 2006 重庆：先让照片穿过互联网，人和权威签发仍不必同时移动

2006 年重庆针对大量外出务工人员推广异地办理二代证。同期《华西都市报》/重庆晨报材料描述的并不是今天意义上的全程网办，而是一条非常典型的混合链：

```text
务工地数码照相馆拍照
→ Internet 上传照片检测
→ 合格后得到可打印回执/委托书
→ 照片经网络传回重庆公安
→ 本人把纸质回执/委托书寄回家
→ 亲友携户口簿到户籍地派出所代办
→ 原籍完成权威办证
```

同期报道估计梁平县约有 20 万农民外出务工，其中深圳、东莞等地超过 10 万；报道时已经为 2000 多名长期在外人员办理二代证。

Sources:
- 《华西都市报》同期稿，2006-09-27：https://news.sina.com.cn/c/2006-09-27/080010118888s.shtml
- 《重庆晨报》同期稿，2006-10-19：https://news.sina.com.cn/c/2006-10-19/030710269283s.shtml

Evidence: **B（同期报刊，含公安部门流程说明）**。

这一阶段应叫 **remote artifact transport / 远程材料运输**，而不是“身份关系已经全国可迁移”。互联网先替代的是照片和部分材料的身体移动。

### 5.2 同一天的另一个 old-Web 事实：公安部已经用网站回答普通人的二代证问题

2006 年 10 月 19 日，公安部政府网站治安管理部门负责人参加在线访谈、回答网友关于二代身份证换发的问题。至少说明 Web 已经进入政策说明与群众问答层。

Source:
- 中新网保存的公安部网站访谈内容：https://news.sina.cn/sa/2006-10-19/detail-ikkntiam7926509.d.html

Evidence: **B（同期转载，可证明公安部网站当时举办在线访谈；原始网页 capture 尚未核）**。

这里也要固定：

```text
policy information online
≠ application online
≠ authority decision online to user
```

### 5.3 2009 湖南：网上“遗失声明”和网上“补领”已经是两个不同事务

2009 年 12 月人民网同期报道保存了湖南公安网上服务的截图与操作说明：湖南试运行居民身份证遗失声明网上受理，同时此前已经试点遗失补领网上受理。补领可从 `hnga.gov.cn`、`96305.com` 或 `hnidcard.com` 进入，提交户口簿影印件、数码照片、身份信息并完成费用与邮递步骤；遗失声明则是另一条业务链。

Source:
- 人民网同期稿的搜狐保存页，2009-12-07：https://news.sohu.com/20091207/n268739057.shtml

Evidence: **B+visual artifact（同期媒体对服务页面的截图与流程记录；不是原站 archive capture）**。

这很重要，因为：

```text
loss declaration ≠ invalidation everywhere
loss declaration ≠ replacement application
replacement application ≠ new card in hand
```

### 5.4 2010 湖南：摄像头、网吧和 EMS 构成一条非常“旧网”的身份修复链

2010 年《湖南日报》报道，湖南正式推出居民身份证遗失补领网上受理。申请人可以在带摄像头的电脑上操作，报道甚至明确写“网吧亦可”；进入电子政务网/湖南公信网后填写身份号码、姓名、户号，通过摄像头提交视频照片进行身份验证，再填写投递地址，正式受理后由邮政速递寄送。

Source:
- 平江县政府保存《湖南日报》2010-09-16稿：https://www.pingjiang.gov.cn/35048/35055/35056/content_1041601.html

Evidence: **B（同期报纸内容由政府站点保存）**。

这个过程很值得作为普通生活史保存：

> **“我丢了最重要的身份证件”与“我还能证明自己”之间，一度需要一台能上网、带摄像头的电脑，甚至可能借用网吧。**

这不是手机时代的“线上补证”的早期弱版本，而是一套完全不同的设备—地点—邮政组合。

### 5.5 2010 同期个人自述：Internet 入口存在，不等于整个故障链消失

阿里云开发者社区目前保留一篇标记为 2010-06-12 的用户内容。作者自述新办二代证在 EMS 寄送过程中遗失，随后搜索到湖南网上补办路径，并转载当时办理公告和原始 `96305.com` URL。

Source:
- https://developer.aliyun.com/article/511813

Evidence: **C/B 边界材料**：页面带 2010 时间戳并以第一人称叙述，但当前承载平台不是已验证的 2010 原始博客 capture；只用于证明“一名当时用户把网上补领理解为现实补救路径”，不用于推断使用率或后台成功率。

这还暴露了另一条链：

```text
online application can succeed
≠ postal delivery cannot fail
```

数字化可以减少行政返乡，却仍然把最后一公里交给物理物流。

---

## 6. 2015—2019 的拥堵型未来：身份接口越来越多，证件修复也开始跟着人走

### 6.1 2015：异地受理从地方办法走向跨省制度化

2015 年公安部部署居民身份证异地受理一对一试点。同期人民日报报道，一名 22 岁湖南青年在湖北完成异地身份证手续，登记、核验、拍照、指纹采集后得到取证回执，全程约十分钟。

Source:
- 人民日报，2015-12-18：https://finance.people.com.cn/n1/2015/1218/c1004-27944218.html

Evidence: **B + contemporaneous person**。

2015 年南昌另一名在九江工作的浙江籍 80 后受访者，也明确把异地换证理解成“不再花几个小时赶回老家”。

Source:
- 南昌新闻网同期稿保存页，2015-11-21：https://jx.sina.com.cn/news/m/2015-11-21/detail-ifxkxfvn8931390.shtml

Evidence: **B + contemporaneous first-person**。

### 6.2 2017：权威记录开始替人完成跨地“往返”

2017 年 7 月 1 日起，全国范围实施居民身份证异地受理、挂失申报和丢失招领。人民日报当年采访的一名长期在郑州工作的天津籍居民说，如果回天津补证，不仅有几百元路费，还会耽误工作；异地办理让他感觉“离故乡天津很近”。当时全国已设 23613 个异地受理点，累计异地办理身份证超过 1149 万张。

更关键的是公安部门对后台链的描述：

```text
现居住地受理
→ 受理信息传回户籍地
→ 户籍地审核签发
→ 信息再回受理地
→ 异地制作/核验/发放
```

Source:
- 人民日报 / 新华网，2017-12-14：https://www.xinhuanet.com/politics/2017-12/14/c_1122107312.htm

Evidence: **B + institution response + contemporaneous first-person**。

这就是 **proof portability / 证明可迁移性** 的关键变化：

> 权威登记仍有原籍责任，但本人不再必须跟着责任链一起移动；数据替本人完成制度往返。

### 6.3 2018：补领变快以后，“等新证的二十天”仍然需要一种身份退路

2018 年 12 月，丹阳户籍、在镇江新区上班的张先生身份证遗失。他因为工作忙、很少回丹阳，在公司附近派出所使用自助机完成补领：输入号码、人像与指纹验证、拍照、缴费，十几分钟完成申请；但正式证件还需约 20 个工作日，所以他同时办理临时身份证，用于出差乘车和住宿登记。

Source:
- 扬子晚报同期稿的新浪保存页，2018-12-30：https://news.sina.com.cn/o/2018-12-30/doc-ihqhqcis1801349.shtml

Evidence: **B + contemporaneous first-person + operational description**。

这形成 **identity fallback / 身份回退**：

```text
replacement initiation latency ↓
≠ production latency = 0
```

成熟系统必须处理“新证还没来，但今天的人仍要出差、住宿、办事”这一中间态。

### 6.4 2019 的反例：挂失数据库存在，不等于所有使用方都已经接入

2016 年公安部建成失效居民身份证信息系统并试运行；但 2019 年法治报道仍记录，失效信息联网并未在所有用证部门全面铺开，一名身份被冒用者在处理企业注销时，相关部门并没有查到她身份证的丢失记录。

Source:
- 《法制日报》/人民网，2019-03-19：https://legal.people.com.cn/n1/2019/0319/c42510-30983427.html

Evidence: **B + contemporaneous person + institutional background**。

因此固定：

```text
central invalid-card database exists
≠ every relying party queries it
≠ every transaction rejects the old card
```

“把旧卡标成无效”真正需要的是网络化核验生态，而不仅是中心库里多一个 flag。

---

## 7. 2020—2022 的偶发型未来：身份凭证开始拥有“事务型临时分身”

### 7.1 2021—2022：连首次申领也开始试着从户籍地解绑

长三角 2021 年启动首次申领居民身份证跨省通办试点；2022 年重庆等地继续扩大试点。此前“换领/补领可以异地、首次申领仍回原籍”这一边界开始松动。

Sources:
- 人民网，2021-10-21：https://sh.people.com.cn/n2/2021/1021/c138654-34966961.html
- 重庆市政府，2022-10-25：https://www.cq.gov.cn/ywdt/jrcq/202210/t20221025_11222084.html

Evidence: **B/A-adjacent（地方政府/同期报道）**。

### 7.2 2022 铁路电子临时乘车身份证明：不是“电子身份证”，而是 transaction-scoped proof

2022 年 1 月，铁路 12306 App 上线电子临时乘车身份证明。旅客忘带或遗失身份证后，可在线申请、通过人脸核验，生成动态二维码用于铁路售退改、实名核验、进出站等业务；当年 1—8 月已办理 883 万人次，线下窗口制证量同比下降 48.9%。与此同时，铁路仍保留人工制证窗口，面向脱网、老年和非智能终端用户。

Sources:
- 人民网，2022-01-16：https://ah.people.com.cn/n2/2022/0116/c358428-35097172.html
- 公安部相关数据的湖南省公安厅保存页，2022-08-23：https://gat.hunan.gov.cn/gat/jwgk/jwzx/jqfb/202208/t20220823_27716812.html

Evidence: **B + institutional statistics**。

必须固定：

```text
electronic temporary passenger identity proof
≠ temporary Resident Identity Card
≠ general e-ID
```

它只为一个明确事务域提供短期 **transaction-specific identity / 事务型临时身份**。这恰恰是系统鲁棒性的另一条路线：不要求人在丢证后先恢复“完整凭证”，而是先让最紧急的一趟火车继续走。

---

## 8. 2023—2026 的防守型未来：不是“所有身份都进手机”，而是多条修复与回退路线同时存在

### 8.1 2024：首次申领也在全国范围实现跨省通办

公安部 2024 年 5 月通报，全国范围已实现户口迁移、首次申领居民身份证、开具户籍类证明“跨省通办”；截至 2024 年 4 月底，累计异地换、补领居民身份证 1.06 亿张。

Source:
- 人民网转公安部新闻发布会，2024-05-27：https://society.people.com.cn/n1/2024/0527/c1008-40244355.html

Evidence: **A/B（公安部发布会经人民日报网络平台传播）**。

这意味着“出生/首次申领这一最初身份凭证必须回户籍地”也不再是全国性的自然前提。

### 8.2 2024—2026：全程网办有条件，失败时必须还能回到自助机和窗口

湖南 2024 年扩展身份证全流程网上办理，但首次申领、需要重新采集指纹以及部分身份信息发生变化的情形仍需窗口；广州 2026 年网上办理须知也明确，符合历史指纹、实名认证等条件者可以在线换领/补领，但无法成功网办者可转自助机或窗口。

Sources:
- 湖南公安服务说明，2024-08-28：https://www.hengyang.gov.cn/xxgk/dtxx/tzgg/gsgg/20240828/i3441398.html
- 广州市政府《居民身份证网上办理须知》，2026-07-13：https://www.thnet.gov.cn/zwfw/zdfw/sfzbl/xgzc/content/post_10898501.html

Evidence: **A/B（地方政府/公安公开办事规则）**。

因此“防守型未来”的成熟方向不是：

```text
窗口 → 全部删除 → 只剩 App
```

而更像：

```text
网办
├─ 成功：远程申请 + 邮递
├─ 历史生物特征不足：自助机/窗口
├─ 首次采集：窗口
└─ 急需用证：临时证/事务型临时证明
```

### 8.3 2026 同期第一人称：修复证件不再必须和正常工作发生冲突

北京警方披露，本市户籍居民身份证换领、补领“全程网办”自 2024 年 12 月实施后，到 2026 年 4 月已办理 5 万余件。一名密云居民因身份证丢失需要补领，但工作繁忙无法去窗口，看到网上政策后申请，数日后证件邮寄到家。他把最大价值概括为正常工作与补证可以同时维持。

Source:
- 央视网稿的央广网保存页，2026-04-12：https://news.cnr.cn/native/gd/kx/20260412/t20260412_527582396.shtml

Evidence: **B + contemporaneous first-person + official operational data**。

这是一种很具体的 **life-course interruption shielding / 生命历程中断屏蔽**：身份证故障仍需修复，但修复不再必然要求请假、跨城、停下一整天现有生活。

---

## 9. 海外比较一：英国 1939—1952——“国家身份号码”可以比实体身份证活得更久

英国 National Archives 说明，1939 年 9 月 29 日编制的 National Register 用于制作身份卡，后来还用于配给、征兵、劳动力调配和人口移动管理。

Source:
- The National Archives, `1939 Register`：https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/1939-register/

Evidence: **A/B（国家档案馆对原始制度档案的研究指南）**。

1952 年英国政府决定不再要求公众持有和出示 National Registration identity card，也停止新发卡；但当时的官方议会记录明确说，原编号序列仍继续用于 National Health Service，以避免重新建立一套号码。

Source:
- UK Parliament Hansard, `IDENTITY CARDS (ABOLITION)`, 1952-02-21：https://api.parliament.uk/historic-hansard/commons/1952/feb/21/identity-cards-abolition

Evidence: **A（同期议会记录）**。

这个海外对象最重要的比较不是“英国后来不用身份证、中国使用身份证”。真正可迁移的机制是：

```text
registry identifier can survive
while
physical credential regime changes
```

也就是说，**人、号码、登记、卡片从来不是同一个生命周期。**

---

## 10. 海外比较二：爱沙尼亚 2002—2008——全国发了 eID，也不等于全国立即在电子使用

爱沙尼亚 Information System Authority 记录，首批 174 张国家 ID card 于 2002 年 1 月 28 日发放；2002 年全年发出 117609 张。同年 10 月完成第一份基于国家电子身份体系的数字签名。

到 2008 年，RIA 仍专门组织鼓励 ID card 电子使用的活动。其同期官方页面记录，参与活动的人中有 18% 完成了人生第一次数字签名；官方还说此前注意力更多停留在技术解决方案本身，此次活动才主动鼓励更广泛公众使用电子功能。

Sources:
- RIA, 2022 retrospective with issuance statistics：https://www.ria.ee/en/news/id-card-turned-20-years-old
- RIA, contemporary 2008 report：https://ria.ee/en/news/record-has-been-set

Evidence: **A/C combination**：2008 页面是同期机构材料；2002 数字由 2022 官方机构史回顾。

这再次证明：

```text
credential issued ≠ electronic certificates actively used
hardware exists ≠ ordinary routine integrated
```

这和中国二代证“卡片先机读化，Web/移动身份事务后来分阶段进入生活”具有很强可比性。

---

## 11. 四种未来：同一张证件怎样折射时代时间感

### 11.1 2005—2012：扩张型未来——“我可以走得更远，制度也许会慢慢追上我”

外出务工者已经在深圳、东莞、沿海城市生活；问题是办证仍然绑定原籍。2006 的网络传照片、2009—2010 的湖南网上补领，体现的是一种很典型的扩张逻辑：

> 人先流动出去，再不断发明让制度材料跟上人的办法。

### 11.2 2015—2019：拥堵型未来——“我在哪儿生活”与“我的权威记录在哪儿”开始通过后台长期协调

异地受理把请假、路费、跨省往返砍掉，但也产生更复杂的状态：受理地、审核地、制证地、失效库、使用方联网核查不一定同一时刻完成。身份基础设施变方便的同时，也变得更像一个多系统事务。

### 11.3 2020—2022：偶发型未来——“主凭证出故障时，要先让今天继续”

电子临时乘车身份证明的关键不是数字炫技，而是承认现实中一定会有人忘带、丢失、手机失败、超过次数。于是同一趟旅行同时保留 App 动态证明和人工纸质制证。

### 11.4 2023—2026：防守型未来——“尽量不让一次证件故障把整套生活拉停”

跨省首次申领、全程网办、邮寄、自助机、窗口和临时证明组成多层修复路径。理想不再只是“最多业务上线”，而是：

> **正常生活已经很忙，所以身份维护最好能在后台完成；而后台失败时，我仍有另一条路。**

---

## 12. 对“标准人生脚本”的修正：证件故障是一种很小却很真实的非标准中断

标准叙事常假设：

```text
成年 → 有身份证 → 一直带着 → 到期再换
```

真实生活却可能是：

- 学生在异地求学时遗失；
- 外出务工者多年不回户籍地；
- 一个人刚跳槽，不敢请几天假返乡；
- 老人行动困难，无法亲自到窗口；
- 证件在邮递过程中遗失；
- 新证尚未制作完成，但第二天必须出差；
- 手机或人脸核验失败，只能回人工入口；
- 数据库认为旧卡失效，但某使用方没有接入失效核验；
- 人仍然是同一个人，可某个业务系统暂时无法确认。

因此支持多种生活路径的身份制度，不仅需要一个统一证件，还需要：

1. **credential repairability / 凭证可修复性**；
2. **geographic portability / 地理可迁移性**；
3. **temporary fallback / 临时回退**；
4. **relying-party interoperability / 使用方互操作**；
5. **non-smartphone fallback / 非智能机回退**。

---

## 13. 新增的生活史矩阵项

| 维度 | 本专题新增的问题 |
|---|---|
| 教育 | 异地学生首次申领、遗失补领能否不返乡 |
| 就业 | 办证是否要求请假、跨省往返；证件中断是否影响工资、招聘、出差 |
| 住房 | 租住地能否成为补证受理地；住宿登记需要什么临时证明 |
| 迁移 | “人已经迁移，证件服务仍留原籍”形成行政返乡 |
| 长期中断 | 丢失、过期、损坏形成短期身份接口中断 |
| 证件与记录 | person / registry / number / card / status / relying-party acceptance 分离 |
| 通信与互联网 | 照片传输、Web 表单、摄像头验证、App、人脸核验逐步替代身体移动 |
| 信息获取 | 2006 公安网站在线答疑、2009–2010 网上服务说明变成办证入口 |
| 线上/线下身份 | 网上实人核验不等于实体卡已经到手；实体卡机读不等于 Internet 身份 |
| 未来预期 | 从“丢证要回家”到“可以就近/网上修复”，异地生活的制度尾部成本下降 |
| 历史保存 | 公开页面能保存规则，个人真实身份事务应当保持私密 |

---

## 14. 历史可见性：旧网最容易保存“怎么办”，最难保存“这个人到底办成没有”

居民身份证是一个特别强的 archive-bias 对象。

公开 Web 可能保存：

- 办事指南；
- 服务入口；
- 表单字段；
- 费用；
- 办理时限；
- 截图；
- 新闻中的操作流程；
- 某个历史 host / endpoint。

真正权威却不适合公开保存的是：

- 某个普通人的身份证号码；
- 户号；
- 户口簿影印件；
- 人脸/照片/指纹；
- 挂失时间；
- 后台审核状态；
- 卡片制证记录；
- 投递地址；
- 哪些现实机构后来核验过这张证。

因此形成 **public-guidance / private-authority inversion**：

> **越能证明一个具体人真实身份事务状态的记录，越不应该成为公开 old-Web 文物；越容易公开保存的页面，越多只是事务外壳。**

这不是档案缺陷，而是隐私边界本来就应如此。

---

## 15. 反例与后见之明风险

### 15.1 不要把 2017 写成“中国人第一次可以异地办身份证”

2006 重庆已有针对外出务工者的远程照片/亲友代办路径，2009—2010 湖南已有网上遗失补领服务，很多省份又先于全国制度进行了省内异地或跨省试点。2017 是全国性制度节点，不是所有局部实践的起点。

### 15.2 不要把 2009 湖南网上补领写成“全国普通人都能网上办”

这是明确的地方服务；需要湖南户籍、既有二代证记录、电脑/摄像头/材料和邮递等条件。

### 15.3 不要把“二代证有芯片”写成“身份证从此联网”

芯片机读、后台人口库、社会用证单位联网核验、Web 办证是不同层次。

### 15.4 不要把“挂失”写成一按按钮旧卡物理芯片立刻自毁

2016 以后失效居民身份证系统依赖各使用方联网核查；2019 同期材料仍显示接入并非全面完成。卡片本体和权威失效状态必须分开。

### 15.5 不要把电子临时乘车证明写成“电子身份证普及”

它是铁路事务域的临时证明，有次数、时效和使用范围，而且继续保留人工纸质通道。

### 15.6 不要把英爱比较写成制度优劣排行榜

英国 1939 身份卡是战争动员条件下建立、1952 取消的制度；爱沙尼亚 2002 eID 处于完全不同人口规模、国家架构和数字基础设施中。它们用于比较“登记、号码、实体凭证、电子使用生命周期不一致”这一共同机制，不用于证明哪个国家更先进。

---

## 16. 尚未确定

1. 1980s—1990s 普通人身份证遗失后，在银行、住宿、交通等具体生活领域分别有哪些最常用替代证明；目前缺少足够同期第一人称。
2. 2006 重庆异地照片流程中具体采用的照片检测网站 host、浏览器兼容、字符集与客户端要求，尚未取得 verified historical capture。
3. 2009 `hnidcard.com`、`96305.com`、`hnga.gov.cn` 相关页面的 Wayback/Common Crawl 可验证历史快照，尚未取得。
4. 2009 湖南“遗失声明”与后来的国家级挂失/失效信息系统在法律效果和下游核验上的关系，需要进一步沿政策原文追踪，不能只凭媒体措辞类比。
5. 2010 个人自述的原始博客来源和当年页面 capture 尚未核实。
6. 2024—2026 各省全程网办条件并不统一，不能从北京/湖南/广东外推全国统一流程。
7. 需要更多 2023—2026 普通流动人口，而不仅是官方便民报道中的成功用户，来观察失败路径、邮递延迟、人脸核验失败和临时证实际使用。

---

## 17. 这一轮改变了我们对“人怎么活着”的哪一点理解

此前很多“可迁移生活”研究关注的是工作、住房、社保、医保和人际关系能不能跟着人走。这一轮补出一个更底层的条件：

> **一个人走得再远，也必须还能让陌生系统在需要时承认“这个人就是她自己”。**

居民身份证把身份变成可携带接口以后，也制造了一个过去没那么明显的单点故障：那张卡丢了，人并没有消失，可生活中的很多门会突然要求重新证明。2000s 最有意思的技术不是“一夜之间把身份证搬上网”，而是先让照片穿过 Internet、让亲友代跑、让纸回执邮寄，再让本人远程补领；后来才让受理地和户籍地在后台交换数据，最后又为铁路这种高时效事务发明 24 小时的电子临时证明。

因此成熟的身份基础设施不是让人永远不要丢证，也不是让一部手机成为新的唯一钥匙，而是：

**当最常用的身份凭证坏掉、过期、丢失，或者本人离原籍一千公里时，这个社会仍然有办法连续地认出她，并让她今天的工作、出行和生活尽量不要一起停掉。**

---

## Sources / evidence ledger

- 北京市公安局警察博物馆，1984 首批居民身份证机构史（C）：https://gaj.beijing.gov.cn/jcbwg/zgdc/jzzn/202007/t20200720_1952436.html
- 北京市公安局，40 年身份证试点回顾（C）：https://gaj.beijing.gov.cn/xxfb/jwbd/202410/t20241002_3911265.html
- 《中华人民共和国居民身份证法》政府保存文本（A）：https://www.miluo.gov.cn/25287/25292/25293/42753/content_1231204.html
- 新华社 2004 二代证首发同期稿（B）：https://news.sohu.com/2004/03/30/84/news219658493.shtml
- 福建省政府 2004 换发二代证通知（A）：https://zfgb.fujian.gov.cn/6614
- 2006 重庆外出务工人员网络传照/代办（B）：https://news.sina.com.cn/c/2006-09-27/080010118888s.shtml
- 2006 重庆全市推广异地照片传输（B）：https://news.sina.com.cn/c/2006-10-19/030710269283s.shtml
- 2006 公安部网站二代证在线访谈的同期转载（B）：https://news.sina.cn/sa/2006-10-19/detail-ikkntiam7926509.d.html
- 2009 湖南网上遗失声明/补领截图与流程（B）：https://news.sohu.com/20091207/n268739057.shtml
- 2010 湖南日报网上补领报道（B）：https://www.pingjiang.gov.cn/35048/35055/35056/content_1041601.html
- 2010 用户对网上补领的第一人称页面（B/C boundary）：https://developer.aliyun.com/article/511813
- 2015 跨省异地受理试点普通人案例（B）：https://finance.people.com.cn/n1/2015/1218/c1004-27944218.html
- 2015 南昌异地换领同期人物（B）：https://jx.sina.com.cn/news/m/2015-11-21/detail-ifxkxfvn8931390.shtml
- 2017 全国异地办理、后台流程与普通人案例（B）：https://www.xinhuanet.com/politics/2017-12/14/c_1122107312.htm
- 2018 自助补领、临时证同期人物（B）：https://news.sina.com.cn/o/2018-12-30/doc-ihqhqcis1801349.shtml
- 2019 失效信息联网边界与身份冒用案例（B）：https://legal.people.com.cn/n1/2019/0319/c42510-30983427.html
- 2021 长三角首次申领跨省通办试点（B）：https://sh.people.com.cn/n2/2021/1021/c138654-34966961.html
- 2022 重庆首次申领跨省通办案例（A/B）：https://www.cq.gov.cn/ywdt/jrcq/202210/t20221025_11222084.html
- 2022 铁路电子临时乘车身份证明（B）：https://ah.people.com.cn/n2/2022/0116/c358428-35097172.html
- 2022 公安部电子临时乘车身份证明使用数据（A/B）：https://gat.hunan.gov.cn/gat/jwgk/jwzx/jqfb/202208/t20220823_27716812.html
- 2024 公安部全国首次申领跨省通办数据（A/B）：https://society.people.com.cn/n1/2024/0527/c1008-40244355.html
- 2024 湖南全流程网办规则（A/B）：https://www.hengyang.gov.cn/xxgk/dtxx/tzgg/gsgg/20240828/i3441398.html
- 2026 广州身份证网上办理须知（A）：https://www.thnet.gov.cn/zwfw/zdfw/sfzbl/xgzc/content/post_10898501.html
- 2026 北京全程网办案例与 5 万余件数据（B）：https://news.cnr.cn/native/gd/kx/20260412/t20260412_527582396.shtml
- UK National Archives, 1939 Register（A/B）：https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/1939-register/
- UK Parliament Hansard, 1952 identity-card abolition（A）：https://api.parliament.uk/historic-hansard/commons/1952/feb/21/identity-cards-abolition
- Estonia RIA, ID-card 20-year history（C institutional retrospective）：https://www.ria.ee/en/news/id-card-turned-20-years-old
- Estonia RIA, 2008 contemporary e-ID use campaign（A）：https://ria.ee/en/news/record-has-been-set
