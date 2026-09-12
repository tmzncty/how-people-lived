# 不是一直在线：CFido、离线快信与电话资费塑造的网络社交（中国，1991—1999）

> 研究切片。问题不是“谁发明了中国 BBS”，而是：**在家庭 Internet 尚未成为普通基础设施以前，已经接触个人电脑和调制解调器的人，究竟怎样加入一个跨城市数字社群？他们的一天如何围绕电话费、单线 BBS、离线阅读、批量转信与等待来组织？**
>
> 本轮由 AI 辅助整理。严格区分拨号 BBS / FidoNet、正式 Internet、Internet BBS 与大众家庭上网；不把 CFido 技术爱好者外推成 1990 年代中国普通人口，也不把今天仍在线的 `cfido.com` 页面冒充 1990 年代的 archive capture。

## 0. 与仓库已有专题的去重

仓库已有：

- 家庭拨号上网中的计费会话、电话线争用与离线准备；
- IP 电话卡 / 公话吧；
- BP 机与 Web / Email 到寻呼网的桥；
- 168 声讯；
- Web 招聘、住房与制度事务。

因此本切片不重复：

> “拨号很贵，所以人们会离线写邮件。”

CFido 新增的是一个更强的结构：

> **整个社区、站台权限和网络路由，本身就可以围绕“只短暂连线、把信息批量搬走、离线阅读和写作、之后再批量上传”来组织。**

这不只是个人节费技巧，而是一种 **offline-first networked sociality / 离线优先的网络社交**。

同时，本切片补足用户要求中特别容易被遗漏的边界：

```text
1994 年前中国尚未正式全功能接入全球 Internet
!=
1994 年前完全没有民间数字网络通信
```

CFido 正好是一种需要单独命名的前史。

---

## 1. 先把几条时间线拆开：CFido 不是“1994 年以前的 Internet”

2024 年 *Isis* 论文《Demarcating a Pure Land》把 Chinese FidoNet（CFido）的启动放在 1991 年，并把 1991—1998 作为其核心历史阶段；研究对象是计算机爱好者借拨号 BBS 和 FidoNet 技术形成的虚拟空间。

来源：

- Wen-Ching Sung, Chen-Pang Yeang, Zhixiang Cheng, “Demarcating a Pure Land: CFido as a Cyberspace for Computer Amateurs in 1990s China,” *Isis* 115(2), 2024, pp. 267–291.  
  <https://www.journals.uchicago.edu/doi/10.1086/730229>

与此同时，CERNET 的机构史把 1994—1995 的全国 TCP/IP 网络建设、1995 年 8 月“水木清华”在教育网上开通，放在正式 Internet 基础设施的另一条时间线上。

来源：

- CERNET，《CERNET:中国互联网建设的开拓者》：  
  <https://www.cernet.edu.cn/cernet_fu_wu/cernet_news/zui_xin_bo_bao/200603/t20060323_113803.shtml>
- CERNET，《1995年CERNET大事记》：  
  <https://cernet.edu.cn/xxh/zt/cernet20/event/201411/t20141105_1198919.shtml>

所以这里必须保持：

```text
CFido dial-up BBS network
!=
TCP/IP Internet
!=
Internet-connected campus BBS
!=
ordinary household Internet access
```

这也解释了为什么后来机构史中“大陆第一个 BBS”之类措辞必须注明范围。若指 **Internet / CERNET 上的 BBS**，1995 年水木清华有明确机构史脉络；若把“BBS”泛指通过电话线和 modem 登录的 bulletin board，则 CFido 站台显然更早存在。

本切片因此采用：

**`BBS != Internet BBS`**。

---

## 2. StarStudio 的用户流程：上线只是把一捆信息搬进、搬出电脑

今天仍可访问的 `cfido.com` 保存了一页“潭城小站 / StarStudio BBS”说明。当前 HTTP 页面不是已验证的 1990 年代 archive capture，因此这里只把它作为**live legacy representation carrying historical instructions** 使用。

页面给出的最低接入条件非常具体：

- 一台电脑；
- 一台调制解调器；
- 一条可以拨打外线的电话；
- 通讯软件；
- 拨站台电话号码进入。

页面：

- <https://cfido.com/starstudio/star.htm>

它同时介绍 BlueWave / 蓝波快信：站台端有 BlueWave door，用户端安装离线阅读器。典型操作不是长时间停留在 BBS 里阅读，而是：

```text
拨号进入 BBS
→ 让站台把未读信件打成一个 packet
→ 下载 STUDIO.###
→ 断线
→ 在本地慢慢阅读、写回复
→ 客户端把回复打成 STUDIO.NEW
→ 下一次拨号
→ 上传 reply packet
→ 站台再整理并参加后续转信
```

页面自己解释这套工作流的三个目的：减少电话费和在线时间、给用户更多离线阅读/写作时间、把站台线路让给其他人。

### 新机制 1：`connection is transfer time, not reading time`

今天“上论坛”通常隐含：

```text
连接存在
→ 浏览
→ 阅读
→ 写作
→ 刷新
```

CFido / BlueWave 的常态却可以是：

```text
连接存在
→ 批量转移
连接断开
→ 阅读 / 思考 / 写作
再次连接
→ 批量转移
```

因此：

```text
time participating in a networked community
!=
time physically connected to the network
```

这比“拨号 Web 用户偶尔离线写邮件”更进一步，因为离线 packet 本身就是社区的标准用户界面之一。

---

## 3. 单线站台把“在线分钟”变成一种社区公地

StarStudio 页面说明，大多数 Fido BBS 是爱好者在家架设，常见是一条电话线，少数才有 3—4 线，因此用户在线时间有限；页面甚至把会不会使用 BlueWave 作为新用户升级正式用户的一个条件。

同一页给出的用户权限例子：

- 新用户：每天 10 分钟；
- 正式用户：每天 20 分钟，可参加全国通邮信区；
- 更高一级：每天 30 分钟。

这意味着“时间”不是今天意义上的屏幕使用统计，而是站台直接分配的一种稀缺基础设施资源。

本切片把它称为：

**`shared-line time commons / 共享线路时间公地`**。

对单线站台来说：

```text
我在线多十分钟
→ 不是只多花我自己的十分钟电话费
→ 还可能意味着另一个站友十分钟打不进来
```

于是“会离线阅读”既是个人技能，也是对共享基础设施的协作规范。

这与仓库已有的家庭电话线争用不同：

- 家庭拨号争用：一个家庭内部，Internet 占线与打电话冲突；
- CFido 单线争用：一个站台社区里，多个远程用户争夺同一入站 modem / 电话线。

---

## 4. “在线人数”在这里不是理解社群规模的好变量

`cfido.com` 当前首页保存的旧文案称，CFido 曾扩展到 13 个省市、100 多个站台，经常上站人数超过万人。

来源：

- <https://cfido.com/>

这组规模数字来自网络自身留下的介绍，不是独立统计，因此只能作为 network self-description，不能当全国抽样数据。

但它提醒一个方法问题：

一个拥有大量参与者的数字社群，完全可能在任一时刻只有很少的人“在线”。

如果多数参与行为发生在：

- 下载 packet；
- 离线读写；
- 下一次上传；
- 站台夜间批量转信；

那么：

```text
concurrent users
```

会系统性低估：

```text
people participating over a day / week
```

本切片将这种状态称为：

**`community persistence without continuous presence / 非持续在线的持续社群`**。

“在线”后来之所以会成为存在感、即时性和社会关系的重要状态，本身是基础设施变化后的历史结果，不应倒投回 1990 年代拨号网络。

---

## 5. 1997《龙音》：站台之间也不是持续联网，而是按成本定时“交换一批世界”

`cfido.com` 保存的《龙音》第二期标明 1997 年 5 月 9 日出版。当前页面是现代 live representation，但刊物文本本身有明确同期日期和作者署名。

来源：

- 《龙音》第二期：<https://www.cfido.com/deq.htm>

其中《fts 网络标准与网络运转》解释：dial-up BBS 站台之间并非实时持续互联。站台在每天特定时段拨上游或等待上游拨入，modem 建链后批量交换 netmail、echomail 和文件；交换频率取决于信息量和站长经济能力，文中给出的常见情形是每天一次。

它还明确解释，FidoNet 的区域 / net / hub 组织与节约电话费密切相关，区域划分通常沿电话区号或地理区域组织。

### 新机制 2：`tariff-shaped network geography / 资费塑造的网络地理`

互联网时代很容易把路由地理想成抽象的自治系统、IP 前缀与骨干网。

而在这类拨号存储转发网络里，网络拓扑直接受到长途电话账单塑形：

```text
尽量本地拨号
→ 先集中到本地 hub
→ 再由少数上游承担跨区交换
→ 信息沿树状路径逐级移动
```

所以“远方”并没有因为数据数字化而立刻消失。

它仍然以：

- 电话区号；
- 长途资费；
- 夜间拨号窗口；
- 站长愿意承担多少电话费；
- 每天交换几次；

进入一条数字消息的传播速度。

### 新机制 3：`batch-latency social time / 批量延迟的社交时间`

如果每个中间站只在固定时间交换，普通用户写下的一封信并不要求几秒内出现在全国。

更合适的问题是：

> “它会在下一轮转信后，到哪些站？”

这是一种介于纸信和实时 IM 之间的数字时间感。

当前证据不能给出任意两站的精确端到端小时数，因此不把“每天一次”机械换算成固定 N 天到达。

---

## 6. 1998/1999 nodelist：地址首先是一串站号与电话号码，不是 URL

`cfido.com` 现在仍有 nodelist 索引，列出 1996—1999 多个 `NODELIST.xxx` 与 diff 文件，并注明现代保存副本来自 GitHub。

索引：

- <https://www.cfido.com/nodelist/list.html>
- 保存仓库：<https://github.com/lshw/cfido_nodelist>

本轮实际检查了：

- `NODELIST.254` — 文件内部日期 1998-09-11；
- `NODELIST.099` — 文件内部日期 1999-04-09。

这些 preserved copies 列出：

- zone / region / net / hub；
- 站名；
- 城市；
- sysop；
- 电话号码或 unpublished；
- modem 能力 / flags。

这让一个非常朴素、但容易被 Web 史遮住的事实重新可见：

> **加入一个远方数字空间，首先可能意味着“知道该拨哪个电话号码”。**

而网络级身份又是类似 `6:655/403` 的 Fido address。

因此可以把地址史暂时写成：

```text
telephone number + Fido node address
→ IP address / hostname
→ URL / account identity
```

但这不是严格线性替代；它们会长期重叠。

### 1998 的过渡边界

`NODELIST.254` 和 1999 `NODELIST.099` 中，广州 `Electronic_Space` 一项把 `202-116-78-254` 放在通常出现电话号码的位置，并附有说明这不是电话号码而是 Internet IP。

这是一条非常有价值的过渡 artifact：

**同一个 CFido nodelist 已经开始容纳 Internet 地址。**

所以：

```text
Fido era → Internet era
```

并不是某一天整齐切断。

---

## 7. 信区不是只有“技术求助”：数字社群已经进入兴趣、生活与关系

保存下来的 1998 `MAILRULE.TXT` 以及 StarStudio 站台页面列出大量全国或地方信区：

- CHAT / LIFE；
- GAMES；
- LITERATURE；
- MUSIC；
- SPORTS；
- FINANCE；
- HAM；
- PHOTOGRAPHY；
- FOOD；
- SOFTWARE / HARDWARE / WINDOWS / UNIX / PROGRAMMING；
- INTERNET；
- 本地聊天、私人信箱等。

保存仓库：

- <https://github.com/lshw/cfido_nodelist>

因此不能把 CFido 简化成“程序员交换驱动和源代码”。

对进入这个高门槛爱好者圈层的人来说，它也可以承担：

- 认识远方同好；
- 聊生活；
- 谈文学、音乐、体育；
- 获得技术支持；
- 文件共享；
- 本地见面关系的前置社交。

但仍需避免反向夸大：能买/借到 PC、modem，并拥有外线电话和相应技能，本身已经构成显著选择效应。

---

## 8. 1997 第一人称：CFido 与 Internet 不是先后两个世界，而是同一个人同时使用的两个空间

《龙音》第二期收录白勺（White Spoon）1997-04-20 写于北京的《让 Internet 上多一些中国的声音！》。这是本轮最有价值的同时代个人材料之一。

作者回忆，朋友在 1996 年 8 月送给他一台 14400 bps modem；半年多 Internet 使用让他感到视野、知识和电脑技术迅速扩张。他希望把中国民族音乐做成 MIDI，通过 Internet 让更远的人听见；但他的第一版作品完成后，实际首先上传到 CFidoNet，并在数天内得到网友意见和鼓励。随后他又计划把更多作品放到 Internet。

来源：

- <https://www.cfido.com/deq.htm>

### 证据类型

- contemporaneous first-person text，原文标明 1997-04-20；
- 当前取得的是后来持续在线的 HTML 表示，不是已验证 1997 capture；
- 因此“1997 年作者这样写”强于“今天看到的 HTML 就是 1997 DOM”。

### 它改变了什么理解

这一材料拒绝一种整齐的替代模型：

```text
CFido 用完
→ Internet 到来
→ 人迁走
```

至少对这个使用者，更像：

```text
CFido：熟悉的中文同好反馈网络
+
Internet：突然扩大的全球可见空间
+
email / Web：新增入口
```

而且他对未来的想象明显是扩张性的：数字网络意味着自己的作品可能被海外亲属和更广泛的世界听见。

这是 2005–2012“扩张型未来”之前一个很重要的前史：**未来先在少数早期用户那里被体验为“世界突然可以伸得更远”。**

---

## 9. 1997—1999：协议栈开始相互渗透，而不是整齐换代

《龙音》1997 年第二期本身就是一个混合 artifact：

- 内容基本取材自 CFido 信件；
- 有纯文本版本供 BBS 下载；
- 同时又有 HTML 版本；
- 已经通过 `cfido.com` 进入 Web；
- 编辑和作者使用 Internet email。

`MAILRULE.TXT` 保存的 HAM.CHINA 规则消息里，还能看到 email / HTTP 地址以及 Fido Echomail ↔ Internet gateway 的 origin 描述。

到 1998 nodelist，又出现用 Internet IP 填进节点联系字段的例子。

因此本切片将过渡模型写成：

**`protocol overlap transition / 协议重叠式转型`**。

不是：

```text
旧协议死亡
→ 新协议出生
```

而是：

```text
拨号 BBS
↔ Fido echomail / netmail
↔ Internet gateway
↔ email
↔ Web
```

在一段时间里共同存在。

---

## 10. 海外对照：低成本、批量、存储转发不是中国特有

### 美国 FidoNet，1993

1993 年《Washington Post》同期报道解释，FidoNet 最初就利用夜间较低电话费在城市间交换消息；它由业余 BBS 节点协作承担成本，routed netmail 会走多跳路径，速度更慢但成本更低。

来源：

- Steve Snow, “FidoNet Enthusiasts Share a Low-Cost Way to Communicate,” *The Washington Post*, 1993-07-18.  
  <https://www.washingtonpost.com/archive/business/1993/07/19/fidonet-enthusiasts-share-a-low-cost-way-to-communicate/eaf20b43-5c52-4663-82c4-c22c48ba5ca8/>

这说明：

- 电话资费塑造路由；
- hobbyist 共同承担基础设施；
- cheaper but slower 的 store-and-forward；

不是中国独有。

### GreenNet / GnFido，1990—1997

Internet Hall of Fame 对 Karen Banks 的机构介绍记录，她在 1990—1997 年维护 GreenNet 的 GnFido gateway，用 FidoNet / UUCP 的 store-and-forward 为非洲、南亚、东欧 60 多个合作方提供低成本电子通信；很多地方这曾是 NGO、研究者和机构少数可行的电子通信手段。

来源：

- <https://www.internethalloffame.org/inductee/karen-banks/>

这提供了另一种比较：

> **“间歇连接也能组成跨地域数字网络”是一种全球基础设施策略，不只是早期中国电脑爱好者的权宜之计。**

中国材料的特殊性更多在：

- 中文编码与本地软件实践；
- 电话网络和城市区号形成的具体节点地理；
- 1990 年代中国 PC / modem / 电话接入的阶层和地域门槛；
- CFido 与 1994 后快速生长的 TCP/IP Internet 在极短时间内重叠。

---

## 11. 一个更准确的普通用户动作模型

对一个已经拥有必要设备和技能的 1997 年 CFido 用户，典型的一次“去全国社区看看”可能更接近：

```text
白天 / 晚上：先准备要做的事
→ 拨本地或可负担的 BBS 电话
→ 登录
→ 在每日分钟额度内取信包 / 文件
→ 断线
→ 本地离线读几十封信
→ 慢慢写回复
→ 下一次拨号上传 reply packet
→ 本站把信件放入相应 echomail
→ 到站台转信窗口，批量送上游
→ 经过若干站台传播
→ 远方用户下一次取包时读到
```

关键不是“网速慢”三个字，而是整套生活节奏不同：

- 阅读和连接分离；
- 写作和连接分离；
- 用户与用户未必同时出现；
- 站与站也未必同时长期互联；
- 信息仍能形成持续社群。

---

## 12. 证据等级与反例

| 材料 | 本轮用途 | 类型 / 强度 | 不能证明什么 |
|---|---|---|---|
| 2024 *Isis* CFido 论文 | 1991—1998 历史框架 | 高质量 scholarly reconstruction | 不能替代具体站台当年界面 |
| 1997《龙音》第二期文本 | 网络运行、同期第一人称、CFido/Web overlap | 同期文本内容强；当前 HTML 为后续保存表示 | 不能证明当前 DOM/charset 即 1997 原页面 |
| StarStudio 说明页 | BlueWave 工作流、分钟配额、接入条件 | live legacy operational text | 缺少已验证历史 capture datetime |
| `NODELIST.254` / `.099` preserved copies | 节点地址、电话、站名、拓扑、IP 过渡 | dated operational-artifact copy，provenance 较强但非原始介质链 | 不能证明每个节点当日都实际可拨通 |
| `MAILRULE.TXT` preserved copy | 信区、编码、origin、网关痕迹 | dated message-archive copy | 不能证明每个用户都读过全部规则 |
| CERNET 机构史 | Internet / campus BBS 边界 | institutionally curated retrospective | “第一”措辞必须限定 Internet 范围 |
| Washington Post 1993 | 海外同期 Fido 成本/路由比较 | contemporaneous media | 不能直接外推中国资费 |
| Internet Hall of Fame | GnFido 全球比较 | institutional retrospective | 不能外推家庭用户体验 |

### 主要反例与限制

1. **这不是大众家庭通信。** PC、modem、可拨外线电话和技能构成明显门槛。
2. **24 小时开放的站台不等于用户 24 小时在线。** 单线和每日分钟配额仍然塑造使用。
3. **有 Internet gateway 不等于 CFido 已变成 Internet。** 协议和终端仍可能完全不同。
4. **nodelist 中有 IP 不等于所有节点已经 IP 化。** 同一份表的大多数节点仍是电话号码。
5. **今天页面还活着不等于今天看到的是历史原页面。** 当前是 legacy representation。

---

## 13. 后见之明风险

### 风险 A：把 CFido 写成“原始版社交媒体”

它确实有群组讨论、身份、规则、兴趣社群，但基础设施逻辑和今天平台信息流非常不同。

### 风险 B：把 1994 以前写成“没有网络”

错误。至少对部分计算机爱好者，电话网 + modem + BBS + store-and-forward 已经形成跨城数字通信。

### 风险 C：反过来把这些爱好者写成“中国人已经上网”

同样错误。CFido 不等于 TCP/IP Internet，更不等于大众家庭 Internet。

### 风险 D：把 1998 写成旧网消失、新网出现

nodelist、gateway、email、Web 和同期个人使用说明都显示两套系统有明显重叠。

---

## 14. 它改变了我们对“人怎么活”的哪一点理解

本轮至少增加了五个此前矩阵中没有被单独固定的机制：

1. **offline-first networked sociality**：数字社交可以主要发生在断线以后；
2. **shared-line time commons**：在线分钟既是个人成本，也是社区共享线路资源；
3. **tariff-shaped network geography**：长途电话资费直接参与塑造数字网络的地理；
4. **batch-latency social time**：数字信息可以很快，但并不必然实时；
5. **protocol overlap transition**：Internet 到来时，旧数字网络可能先被网关和 Web 包裹，而不是当天消失。

因此，中国普通生活的数字化前史不应写成：

```text
邮政 / 电话
→ 1994 Internet
→ Web
```

更接近：

```text
邮政 / 电话 / 传真 / 寻呼
+
电话线上的 BBS / Fido store-and-forward
+
科研与高校 TCP/IP 网络
+
Web / email / Internet BBS
→ 逐渐走向更普遍、更持续的家庭 Internet
```

---

## 15. 对重点矩阵的贡献

| 维度 | 本轮新增 |
|---|---|
| 通信方式 | 拨号 BBS、FidoNet、BlueWave packet、echomail/netmail |
| 互联网前史 | 明确提供 1991—1994 前的民间数字网络层 |
| 信息获取 | 全国信区通过批量转信进入本地 BBS |
| 社交关系 | 非同时在线也能维持兴趣与生活社群 |
| 时间感 | 日用分钟限额、站台定时转信、批量延迟 |
| 成本 | 电话费同时影响用户停留与节点路由 |
| 线上/线下身份 | Fido 地址、站台 ID、电话号码先于 URL / Web account 成为网络定位方式 |
| 未来预期 | 1997 同期第一人称把 Internet 想象成让作品与“中国声音”走向更大世界的空间 |
| 历史可见性 | nodelist / mail packet / 规则文本可能比网页更能保存早期网络的运行结构 |

---

## 16. 仍不知道什么

下一轮若继续这条线，优先补：

- 1991—1994 最早 CFido 站台的原始 nodelist / 软件 / 电话账单；
- 普通用户而非站长的 1992—1996 同期日记、BBS 信件、杂志投稿；
- BlueWave 在中国不同站台的实际普及率，而不只是 StarStudio 的使用规范；
- 拨本地站、跨区直拨、站台转信各自的实际资费；
- 用户的年龄、职业、城市、家庭电话和电脑获取方式；
- 站台同时在线人数、忙线率、失败拨号次数；
- 最早的 Fido ↔ Internet gateway 软件/配置；
- `cfido.com` 1997—2000 经验证的 historical captures；
- 1998 nodelist 中 IP 节点究竟通过什么 transport 参与 CFido；
- CFido 衰退后，同一批普通用户分别迁到 Internet BBS、OICQ、论坛、Web 还是完全离开网络。

如果这些材料出现，最值得做的是**同一人的通信栈迁移生命史**，而不是再写一个抽象“中国互联网发展史”。
