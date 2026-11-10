# From "remembering one password" to "too many accounts to remember": passwords, account recovery and digital-identity maintenance labor (China, 1995–2026)

> Cross-repo companion: `tmzncty/old-web-archaeology/docs/PASSWORD_LOGIN_RECOVERY_QUESTION_EMAIL_SMS_SESSION_AND_ACCOUNT_CONTROL_STATE_GAPS_1998_2015.md`

## 0. Why this is a life-horizon problem

Passwords are easily written off as a small technical detail in the history of information security. But for ordinary people's life courses they have gradually taken on a more basic function:

> **How does the future self prove again that "this digital entrance established ten years ago still belongs to me"?**

As communication, work, gaming, shopping, banking, education and government affairs move into digital systems, a person does not merely "have more online choices"; they must also keep custody of the credentials that allow re-entry into those choices.

This topic therefore does not study "how to set a strong password" as such, but studies:

- how many digital entrances an ordinary person has to maintain over a lifetime;
- how passwords, security questions, registration email addresses, mobile numbers, SMS codes, identity documents, devices and biometrics combine into a recovery chain;
- why an account unused for a long time may still produce social consequences in your name;
- why password reuse appears to reduce memory load while binding the risks of different platforms together;
- why 2020s "passwordlessness" did not make identity-maintenance labor disappear, but moved it to devices, cloud accounts, password managers and recovery channels.

This is a form of labor that the history of technology and the history of everyday life have both tended to miss:

**`authentication maintenance labor`**.

---

## 1. Core concepts

### 1.1 `credential memory load`

The total quantity of secrets and verification relationships a person must remember, store or be able to recover in order to keep a number of digital services enterable.

It includes at least:

```text
username / QQ number / email address
+ login password
+ secondary / super password
+ security questions and answers
+ identity details entered at registration
+ recovery email address
+ bound mobile number
+ SMS verification code channel
+ trusted devices
+ password-manager master password / device unlock capability
= credential portfolio
```

"One account, one password" must not be taken here as a model of actual life.

### 1.2 `credential custody`

Credentials do not only need to be "remembered"; they need to remain usable across many years.

```text
secret created
→ user remembers/stores it
→ recovery endpoint remains accessible
→ platform still accepts it
→ device/session survives or can be rebuilt
→ future self can regain control
```

A sheet of paper, a notebook, browser autofill, a password manager, a bound mobile number — all are credential-custody solutions of different eras.

### 1.3 `recovery dependency chain`

Recovering account A may require getting into mailbox B; mailbox B in turn requires mobile number C; mobile number C has already been cancelled; or recovering C's carrier account requires yet another piece of identity data.

Therefore:

```text
ACCOUNT_A
  → RECOVERY_EMAIL_B
       → PASSWORD_B
       → PHONE_C
            → SIM / subscriber status
```

**A recovery endpoint existing is not the same as a recovery chain being executable.**

### 1.4 `dormant-account liability`

An account unused for a long time has not necessarily withdrawn from social relations.

If an old account still holds:

- a friend list;
- clients;
- group relationships;
- payment capability;
- game / virtual property;
- old photographs and materials;

then once the account is re-controlled, real consequences can still occur under the old identity.

### 1.5 `reuse blast radius`

To lower credential memory load, a person may reuse the same password across several services.

This turns:

```text
site A breach
```

into:

```text
site A leaked credential
→ try on B
→ try on C
→ try on D
→ unrelated identities become reachable
```

This is not simply "poor user security awareness", but a structural outcome of real human memory constraints colliding with platform growth.

### 1.6 `authentication burden transfer`

2020s passkeys / biometrics / password managers try to reduce the work of holding secret strings in the human brain, but the labor has not disappeared. It has moved to:

- which device holds the passkey;
- which cloud keychain synchronizes it;
- how to recover after the device is lost;
- whether it spans Windows / Android / iOS;
- whether old services still accept only passwords;
- how the password manager itself is recovered.

So:

**`passwordless != maintenance-free identity`**.

---

## 2. Key prehistory before the Internet: passwords were not originally a mass consumer item

### 2.1 1960s: passwords first solved "several people sharing one computer"

MIT CSAIL's institutional-history retrospective on Fernando Corbató notes that CTSS was first demonstrated in 1961, allowing several people to use one computer at the same time; it is also widely regarded as the first computer system to use personal account passwords. Here the password was first of all a boundary between files and accounts on a shared machine, not today's life burden of "every ordinary person having dozens of website accounts".

Source:
- MIT CSAIL, `Fernando "Corby" Corbató (1926-2019)`, 2019-07-13: https://www.csail.mit.edu/news/fernando-corby-corbato-1926-2019

**Grade:** B/C — an authoritative institutional retrospective, citing early CTSS historical materials.

This overseas prehistory shows:

```text
multi-user computing
→ individual account
→ personal secret
```

decades before the Web.

But it does not follow from this that ordinary households in the 1960s already had to maintain digital passwords.

### 2.2 The boundary around 1994 in China cannot be taken lazily

Before its formal full-function connection to the global Internet, China already had research networks, email and computer-account environments; but this cannot be written as ordinary households having already entered a mass password culture.

This topic therefore places the main timeline of ordinary life in China after mass network services became gradually available, rather than drawing 1994 as the breakpoint at which "passwords went from nonexistent to existing".

What actually needs tracking is:

```text
a small number of computer-account secrets
→ email / BBS / IM / online-game accounts
→ e-commerce / payment / online banking
→ a large number of app / government / work accounts
→ password managers / passkeys
```

---

## 3. 1999–2005: accounts begin to become "things in life worth recovering"

### 3.1 The value of an early account was not only in logging in

When a QQ, mailbox or game account was used only for a brief trial, the loss from forgetting the password might be very small.

But once an account begins to accumulate:

```text
contacts
+ group relationships
+ mail
+ game characters
+ virtual property
+ registration history
```

"forgetting the password" becomes a question of biographical continuity.

### 3.2 2004: email begins to become recovery infrastructure

During the 2004 open beta of *Lineage II*, contemporary materials record that the account registration system sent verification codes by email, and users had to wait for the mail to complete account verification; when the system was busy, some users did not receive the code.

Source:
- Sina Games, "A summary of recent *Lineage II* open-beta news", 2004-08-25: https://games.sina.com.cn/newgames/2004/08/082542676.shtml

**Grade:** B — contemporary operator/media material.

It shows that:

```text
GAME_ACCOUNT
→ EMAIL_ENDPOINT
→ VERIFICATION_CODE
→ ACCOUNT_ACTIVATION
```

was already a cross-system transaction.

`verification mail generated != mail received`.

### 3.3 2005: passwords begin to stratify, with external recovery channels layered on top

In 2005 *Lineage II* began promoting a "security card" and stated that a mobile-binding account service had already been launched earlier; *Yulgang* successively offered a soft keyboard, mobile password protection and mobile account locking.

Sources:
- Sina Games, "*Lineage II* security card: two-factor protection for game accounts", 2005-03-11: https://games.sina.com.cn/o/n/2005-03-11/88449.shtml
- Sina Games, "*Yulgang*: multiple measures help you prevent account theft", 2005-09-05: https://games.sina.com.cn/o/n/2005-09-05/1603124246.shtml

**Grade:** B — media mirrors of contemporary platform/operator material.

An important change appears here:

```text
knows password
```

is no longer the only recovery path; control over an account gradually layers up:

```text
password
+ super/secondary secret
+ recovery question/data
+ email
+ mobile phone
+ security card
```

So what users had to maintain was not one secret but a set of secrets and relationships that backstop one another.

---

## 4. 2005–2012: the expansive future — more online possibility, and also more "keys"

### 4.1 2006: a stolen QQ could directly cut off work relationships

In 2006 Sichuan Online / Huaxi Metropolis Daily reported on Mr Li, an internet-marketing practitioner:

- QQ had been in use for 7 years;
- the password had never been changed;
- many clients contacted him only through QQ;
- one day the system suddenly reported "wrong password";
- he believed the account had been stolen;
- Tencent customer service said he could fill in a QQ-number appeal form online to recover it.

Source:
- Sina reprint of Sichuan Online–Huaxi Metropolis Daily, "QQ number stolen: getting it back costs 30 yuan", 2006-07-03: https://news.sina.com.cn/c/2006-07-03/06059355251s.shtml

**Grade:** B — a same-era ordinary-user case plus a platform customer-service response.

The importance of this case is not that "account theft is frightening", but that:

> **A QQ password already controlled a person's client network.**

Therefore:

```text
password lost
!= merely software inconvenience

password lost
→ client reachability interrupted
→ work continuity threatened
```

### 4.2 "Seven years without changing the password" must not be explained backwards through today's security norms

Seen from today, not changing a password for a long time and reusing it across services is easily criticized as "poor security awareness".

But life-history needs first to restore the life constraints of that time:

- users were already maintaining more and more accounts;
- password managers were not mass infrastructure;
- recovery rules differed from service to service;
- registration details might have been filled in casually years earlier;
- contacts and virtual assets might exist only inside the platform.

So the real historical question is:

**whether the speed at which platforms demanded more and more separate secrets had already exceeded the speed at which ordinary people were willing or able to remember them.**

### 4.3 2006: the scale of account theft made "credential custody" a mass internet problem

A 2006 *Legal Daily* report on a large QQ / Q-coin theft case relayed Tencent's report to the police: from March that year complaints about stolen QQ accounts rose sharply, reaching nearly 30,000–40,000 a day by May; technical analysis said large numbers of account passwords were captured by trojans, initially sent back by email and later written to remote servers via HTTP POST.

Source:
- Sina reprint of *Legal Daily*, "The story of solving the largest Q-coin theft case in the country", 2006-12-31: https://news.sina.com.cn/o/2006-12-31/083510902403s.shtml

**Grade:** B — contemporary police/company case material.

This evidence can establish that:

- account-password theft had already generated complaints at large scale at the time;
- trojans could carry "the secret the user knows" off the local machine;
- a password was not safe merely because the user remembered it.

It cannot by itself establish the theft probability for all QQ users in China.

### 4.4 2009: an account/password could already lead straight to living expenses

In a 2009 same-era case, university student Xiao Xi shopped online routinely; after talking with a fake customer-service agent on QQ he clicked a link disguised as Taobao, `taobao.con`, and was phished, losing 2256 yuan — the report described this as about four months of living expenses.

Source:
- Phoenix Net, "Phished out of his living expenses, a university student posts online to hunt the fraudster", 2009-10-13: https://news.ifeng.com/society/2/200910/1013_344_1385831.shtml

**Grade:** B — a same-era case involving an ordinary university student.

It shows that once accounts, payment and web forms begin to connect:

```text
looks like known service
→ user enters credential/payment data
→ credential/control moves elsewhere
→ loss leaves screen and enters monthly budget
```

This is also the reverse side of the "expansive future":

> Remote consumption expands the space of choice while requiring ordinary people to learn to judge whether a page that looks almost identical really is the same institutional entrance.

### 4.5 The network was still far from "everyone is using it"

CNNIC's 23rd report recorded that by the end of 2008 China had about 298 million internet users and an internet penetration rate of 22.6%; mobile internet users numbered about 117.6 million.

Source:
- CNNIC, 23rd *Statistical Report on Internet Development in China*, 2009 (official report page/mirror relocatable).

**Grade:** A — contemporary official statistics.

So the password burden of the 2000s cannot be written as a shared condition of the whole population. It was concentrated first among people already inside digital life: IM, online games, email, online shopping, online banking.

---

## 5. A contemporary overseas comparison: by 2007 some people already called "too many passwords" a life burden

A 2007 VOA Chinese report discussing the digitization of everyday services in the United States already listed online shopping, banking, email, ATMs and website logins side by side, and noted that a growing number of usernames/passwords would create memory pressure; some people forgot a bank password after changing it, and repeated attempts triggered a lockout.

Source:
- VOA Chinese, "Americans can do everything online in daily life; digitalization is immensely convenient but passwords become a burden", 2007-10-05 (the article is locatable through public web search).

**Grade:** B — a contemporary overseas life report.

What appears here is not "a peculiar defect of Chinese internet users" but a shared structure of modern network services:

```text
more remote services
→ more accounts
→ more secrets
→ more recovery procedures
```

So the password burden is first of all a shared phenomenon of internet platformization; differences between countries fall more in identity infrastructure, service concentration, recovery channels and regulatory structure.

---

## 6. 2015–2019: the congested future — accounts did not disappear, they became harder and harder to exit completely

### 6.1 `dormant-account liability`: not using QQ any more does not mean the QQ identity is already dead

The 2018 same-era material about Guangzhou office worker Mr Lin is especially important:

- after changing jobs he had basically stopped using QQ;
- he had not logged in for about half a year;
- one day a friend suddenly called to ask "has your QQ been stolen?";
- the account thief had already mass-messaged his contacts with fraud messages;
- although he quickly recovered the password through an appeal, he still had to explain it to relatives and friends one by one.

Source:
- People's Daily Online reprint of *New Express*, "QQ account-theft fraud: an old trick returns to the scene", 2018-11-28: https://it.people.com.cn/BIG5/n1/2018/1128/c1009-30429175.html

**Grade:** B — same-era first-person user material plus platform response.

This establishes a new life-course boundary:

```text
user stops active use
!= account socially inert
```

The relationships stored in an old account can still be reactivated by someone else.

### 6.2 2018: exiting itself also requires identity-maintenance labor

A 2018 China News Service investigation found that many apps were "easy to register, hard to cancel". Beijing office worker Mi Qiang wanted to cancel Weibo for work reasons and tried many times without success; in the same period QQ briefly grey-tested a cancellation capability.

Sources:
- People's Daily Online reprint of China News Service, "Investigation into 'hard cancellation of mobile app accounts': why is it so hard, what are the risks?", 2018-05-04: https://media.people.com.cn/n1/2018/0504/c40606-29964125.html
- People's Daily Online, "QQ account cancellation feature taken offline, to return after the experience is optimized", 2018-03-22: https://it.people.com.cn/BIG5/n1/2018/0322/c1009-29882099.html

**Grade:** B — contemporary media investigation / platform response.

So digital-identity maintenance includes not only "how to get in" but also "how to really leave".

### 6.3 2019: password reuse turns a memory optimization into a cross-platform failure

In 2019 China News Service / People's Daily Online reported a "credential stuffing" case: attackers obtained tens of millions of account-password pairs from external channels and then tried them in bulk against several popular applications; Douyin received tens of millions of external credential attempts, of which more than a million account passwords matched externally leaked passwords. The report stated explicitly that many internet users used the same account password on multiple websites, which gave credential stuffing a success rate.

Source:
- People's Daily Online reprint of China News Service, "Hackers 'stuff credentials' against popular apps to steal passwords and earn a million; they hit Douyin and fell", 2019-06-21: https://media.people.com.cn/n1/2019/0621/c14677-31174338.html

**Grade:** B — contemporary police/platform case material.

This links `credential memory load` and `reuse blast radius` together:

```text
remember one password everywhere
→ low cognitive cost
→ one leak can unlock unrelated platforms
```

This should not be answered only with moralizing user education. Password reuse is also a low-cost adaptation to an explosion in the number of accounts; it merely externalizes risk onto other accounts.

### 6.4 Overseas 2019 comparison: dozens of passwords are not rare, but the statistics call for caution

A 2019 HYPR vendor survey of more than 500 full-time workers in the US/Canada said: 37% of respondents had more than 20 personal passwords, 78% had reset a forgotten personal password in the past 90 days, and 65% used an app or a paper/digital list to keep passwords.

Source:
- HYPR / PR Newswire, 2019 password study (vendor survey).

**Grade:** B, low-to-medium confidence for population prevalence — a non-random/vendor study, not directly generalizable to the whole population.

It is suitable as a **cross-national mechanism comparison**, not as a precise population fact.

---

## 7. 2020–2022: the contingent future — digital entrances suddenly turn from "convenience" into a real-world admission condition

This stage needs to avoid one error:

> Not all digital divides can be explained as "old people cannot remember passwords".

Real difficulties include eyesight, hearing, input methods, verification codes, devices, networks, bound bank cards, interface depth, identity-verification procedures and more.

### 7.1 2020: the password-verification flow of financial apps itself became one exclusion factor

A 2020 *Economic Information Daily* report on digital finance for older people relayed a related Ningbo survey: mobile-banking and payment-app interfaces were complex, fonts were small, and card-binding and password-verification flows were complicated, all of which were listed among the reasons some older people kept their distance from digital financial tools.

Source:
- People's Daily Online reprint of *Economic Information Daily*, "Hard to pay, hard to travel: how can 200 million 'silver-haired' people cross the digital divide", 2020-10-20: https://hb.people.com.cn/n2/2020/1020/c192237-34360625-4.html

**Grade:** B — contemporary survey reporting.

### 7.2 2021: the `human fallback layer` is still necessary

During 2021 community visits in Guangzhou, 68-year-old Aunt Luo and 63-year-old Uncle Zhang described obstacles of eyesight and hearing respectively; the report summarized the common difficulties of older people as "cannot see clearly, cannot hear clearly, cannot remember". Another report on age-friendly adaptation noted that some older people simply gave up because they could not find the entrance to "elder mode", and recommended human voice/video guidance.

Sources:
- People's Daily Online, "In the 5G era, how do we bring back the older people 'out of contact' in the internet world?", 2021-01-22: https://it.people.com.cn/n1/2021/0122/c1009-32008150.html
- People's Daily Online reprint of *Beijing Daily*, "Elder-mode entrances in mobile apps are hard to find: how can app age-friendly retrofits be more considerate", 2021-04-14: https://finance.people.com.cn/n1/2021/0414/c1004-32077599.html

**Grade:** B — contemporary on-site visits.

What really matters here is:

```text
digital authentication fails
→ family proxy / clerk / hotline / physical counter
```

It is not "not digital enough" but the system's fault-tolerance layer.

### 7.3 2021: whether a verification code can be operated also belongs to authentication, not just to password

In 2021, for visually impaired users, the Ministry of Industry and Information Technology's age-friendly / accessibility requirements specifically addressed verification-code obstacles; Alipay launched an alternative verification interaction for visually impaired scenarios.

Source:
- China Daily, "'A wave of the hand' solves the mobile verification-code problem for visually impaired users", 2021-10-15: https://caijing.chinadaily.com.cn/a/202110/15/WS61696e02a3107be4979f2de2.html

**Grade:** B — contemporary product/policy reporting.

This topic must therefore insist that:

**`authentication burden != password burden only`**.

---

## 8. 2023–2026: the defensive future — no longer requiring the human brain to hold every key

### 8.1 2024: an account logged into once a year produces "periodic forgetting"

A 2024 State Taxation Administration reminder about the annual individual income tax settlement used a typical case to explain: a user had not logged into the individual income tax app for a year and had already forgotten the password; the system could reset it through a bound mobile number or the user's own bank card for verification, and if recovery still failed the user could bring identity documents to an offline counter.

Source:
- People's Daily Online, "About the annual individual income tax settlement, please note these 13 questions", 2024-03-13: https://finance.people.com.cn/n1/2024/0313/c1004-40195265.html

**Grade:** A/B — an official tax-authority example published through People's Daily Online; it is evidence of institutional design and should not be passed off as a randomly sampled real individual speaking in the first person.

It illustrates well:

```text
low-frequency but high-stakes account
→ easy to forget secret
→ recovery must be multi-channel
```

### 8.2 2025: the absence of a "forgot password" entrance can already block a real business obligation

In a 2025 public case from the Beijing 12345 enterprise service hotline, a catering business reported that the "Sunshine Catering" app had no password-reset function, so that once the password was forgotten it was impossible to log in, and it worried that it could not complete operations on the regulatory platform in time; after the feedback, the market regulation department added a password-reset function and an operating guide.

Source:
- People's Daily Online / *Beijing Daily*, "Beijing 12345 helps 133,000 enterprises solve pressing difficulties", 2025-11-13: https://bj.people.com.cn/n2/2025/1113/c14540-41409924.html

**Grade:** A/B — official/contemporary reporting of an actual request to a government hotline.

This material is very important because it proves that:

> **Password recovery is not an "extra convenience" of a website; it can be part of whether a real institutional interface is executable.**

### 8.3 Passkey: from "remembering a secret" to "holding a device/key"

In 2024 WIRED journalist Matt Burgess ran a good overseas first-person experiment:

- over more than a decade he had accumulated 337 accounts;
- he used a password manager to generate and store large numbers of unique passwords;
- he tried moving some accounts to passkeys;
- when passkeys worked smoothly, Face ID and similar could complete a login within tens of seconds;
- but support across devices, operating systems, browsers and password managers remained inconsistent;
- he still had to remember whether a passkey was stored in iCloud, Bitwarden, the device, or a hardware key.

Source:
- WIRED, `I Stopped Using Passwords. It’s Great—and a Total Mess`, 2024-02-08: https://www.wired.com/story/stopped-using-passwords-passkeys/

**Grade:** B — contemporary overseas first-person technology-life material.

It provides a good counterexample:

```text
no password string to remember
!= no credential custody problem
```

The future question shifts from:

> "What is the password?"

gradually to:

> "Which device / which cloud keychain is the key actually in?"

### 8.4 2025: platforms begin to make "passwordless" the default direction

In May 2025 Microsoft announced that new Microsoft Account registrations would adopt a passwordless method by default, allowing sign-in through passkeys, push notifications and other means.

Source:
- ITHome relaying a Microsoft announcement, 2025-05-02: https://www.ithome.com/0/850/417.htm

**Grade:** B — contemporary technology reporting; the specific product mechanics can be further strengthened with Microsoft's original announcement.

It cannot prove that "Chinese users already generally do not use passwords"; it can only prove that the direction of platform design has changed.

---

## 9. Comparing new evidence across the four future stages

### 9.1 2005–2012: the expansive future

Keywords: **more digital entrances, more distant relationships, cheaper transactions, accounts more worth keeping.**

Typical mechanism:

```text
QQ / email / games / shopping / banking expand
→ account becomes persistent asset
→ password loss has larger real-world cost
→ recovery email / mobile / security card proliferate
```

The imagination of the future leaned toward "more and more things can be done online".

The cost was that ordinary people, for the first time, had to keep a key for more and more digital doors.

### 9.2 2015–2019: the congested future

Keywords: **too many accounts, old accounts that do not die, password reuse, hard to exit.**

Typical mechanism:

```text
many accounts
→ reuse or save passwords somewhere
→ breach spills across platforms
→ dormant identity can still be hijacked
→ user must clean up old digital selves
```

"More opportunities" gradually became "maintaining these entrances is itself work".

### 9.3 2020–2022: the contingent future

Keywords: **certain digital entrances suddenly become the necessary path into real-world affairs.**

As the pandemic, online handling of affairs and appification accelerated, logins, verification codes, card binding and account recovery — previously merely convenience features — could suddenly decide whether a person could pay, handle affairs or enter a service smoothly.

So systems had to add:

- family proxy;
- manual counters;
- telephone;
- accessible verification codes;
- age-friendly interfaces.

### 9.4 2023–2026: the defensive future

Keywords: **fewer repeatable secrets, lower memory load, more recovery and fallback.**

Typical mechanism:

```text
password manager
+ biometric unlock
+ passkey
+ device-bound / synced cryptographic credential
+ recovery fallback
```

Defense is not "no identity maintenance at all"; it is an attempt to let ordinary people remember and repeatedly type fewer phishable secrets.

---

## 10. A new life course: an account can outlive a segment of a life

Putting this topic back into the life course reveals a very unnatural yet increasingly common relationship:

```text
build a QQ in high school
→ accumulate classmates in university
→ accumulate clients after graduation
→ stop logging in after changing jobs
→ years later the account still holds old relationships
→ after a password leak it suddenly "speaks for you" again
```

The person's life stage has passed, but the digital identity does not naturally end with the stage.

So one judgment should be added to Life Horizons:

**`life-stage exit != account-state exit`**.

This can form a larger structure together with `account-binding debt` from the earlier mobile-number topic, `archive exit labor` from the photograph topic, and `social recoverability` from the class-address-book topic:

> Digital infrastructure increases continuity across stages, and also makes past identity relationships harder to let dissipate naturally.

---

## 11. Counterexamples and what not to over-interpret

### 11.1 Many passwords ≠ everyone suffers

Some people:

- reuse a small number of passwords for a long time;
- let the browser remember them;
- use a password manager;
- rely on SMS login;
- almost never log out of apps;
- simply ask family / customer service for help.

"An ideal security norm requires unique passwords" must not be miswritten as everyone's actual life.

### 11.2 Forgetting a password ≠ the only cause of digital exclusion

The digital divide also includes devices, networks, literacy, audio-visual ability, cognition, interfaces, bank cards, mobile numbers, verification codes and institutional design.

### 11.3 Successful recovery ≠ complete restoration of the original state

After a QQ number is recovered, groups, photographs, virtual property, contacts who were defrauded and altered profile data are not necessarily all restored.

### 11.4 Having a passkey ≠ no password any more

During the transition many services keep simultaneously:

```text
password
+ passkey
+ SMS/email recovery
```

A new scheme may reduce one risk while increasing dependence on a device / cloud ecosystem.

### 11.5 Security advice ≠ the historical facts of behavior

Knowing today that "use a different password for every website" is a good habit cannot be used to infer backwards that ordinary users in 2006 should already have lived by today's norms.

---

## 12. Summary of evidence grades

| Claim | Evidence | Grade | Confidence |
|---|---|---:|---:|
| Personal account passwords already existed in the CTSS era, 1961 | MIT CSAIL institutional history | B/C | high |
| 2004: online-game registration depended on email verification codes | Contemporary Sina Games operator material | B | high |
| 2005: multi-factor protection such as mobile binding / security cards already existed | Contemporary operator material | B | high for existence |
| 2006: a stolen QQ could directly affect an internet marketer's client contact | Contemporary ordinary-user interview | B | high for case |
| 2006: QQ theft complaints reached the scale of tens of thousands per day (Tencent's report to police) | Legal Daily / police case reporting | B | medium-high |
| 2009: phishing could cost a university student several months of living expenses | Contemporary individual case | B | high for case |
| 2018: a long-unused stolen QQ could still defraud old relationships | Contemporary ordinary-user interview | B | high for case |
| 2019: password reuse enabled successful cross-platform credential stuffing | Police / platform case material | B | high for mechanism |
| 2020–21: complex identity verification is part of the digital obstacles for some older people | Contemporary surveys / on-site interviews | B | medium-high |
| 2024: the tax app offers password recovery by mobile number / bank card / offline | Official tax-service explanation | A/B | high |
| 2025: the absence of a reset function can block use of a real regulatory app | An actual request to Beijing 12345 | A/B | high |
| 2024: passkeys reduce memorized secrets but still have device / ecosystem management problems | WIRED first-person | B | high for case |

---

## 13. Hindsight risks

### Risk A: writing password history as today's cybersecurity textbook

The object of this topic is not "where historical users went wrong", but what combinations of credentials and recovery institutions ordinary users faced at the time.

### Risk B: attributing all account theft to weak passwords

Trojans, phishing, social engineering, appeal mechanisms, third-party leaks, endpoint environments and platform design may all play a part.

### Risk C: writing 1994 as the starting point of password culture

China already had computer-network / account environments before that; and ordinary households did not instantly go online afterwards either.

### Risk D: writing passkeys as an already-completed "passwordless era"

We are still in a stage where several sets of mechanisms coexist.

### Risk E: treating some platform's security help page as ordinary people's actual usage rate

`exists != used != popular`.

---

## 14. Still unsettled, worth strengthening later

1. First-person same-era material on password management by ordinary users of 1990s Chinese BBS, campus networks and dial-up ISPs is still insufficient;
2. Better captures are needed of the original 1998–2003 QQ/OICQ and email "forgot password / password protection" help pages;
3. The actual usage rates of security questions, super passwords and mobile security protection in 2005–2010 remain unknown;
4. Whether ordinary households commonly used paper notebooks, Excel or browsers to save passwords needs more contemporary material;
5. A representative survey of "how many accounts/passwords do I actually have" among ordinary Chinese people in 2015–2019 still needs strengthening;
6. High-quality aggregate evidence on actual passkey adoption rates and cross-device recovery experience in mainland China's mainstream consumer services is still lacking for 2023–2026;
7. Account inheritance, digital assets after death and password escrow are another life-course interface, not developed in this round.

---

## 15. What it changes in our understanding of "how people live"

In the past, saying that the Internet expanded life choices usually meant counting only:

- whom you can chat with;
- where you can buy things;
- how much work you can do;
- how many communities you can enter.

But for every newly added world that can be entered remotely, ordinary people usually also gain one more door whose key has to be kept over the long term.

So modern digital life has a cost that is rarely calculated on its own:

> **You must not only decide which lives you want to enter today, but also keep, for your future self, the proof that "you can still come back later".**

In 2006, a QQ password that had worked for seven years suddenly failing could mean a client network cut off; in 2018, a QQ unused for half a year could still suddenly go looking for old friends in your name; in 2019, reusing secrets in order to remember a few fewer passwords could let a single leak pass through several platforms. By the 2020s, platforms finally began trying to take this work out of human memory — letting phones, biometrics, password managers and passkeys keep the keys for you.

But the keys have not disappeared.

They have only turned from a string you must remember into another set of devices, cloud accounts and recovery relationships that you must maintain.

This shows that a new life capability is forming:

**Ordinary people must manage not only money, documents, contacts and addresses, but also "who they still are" in the digital society.**

---

## 16. Saturation judgment for this round

This round added:

- a new life mechanism: `authentication maintenance labor`;
- a new institutional interface: account recovery chains and the executability of real services;
- new era mechanisms: `dormant-account liability`, `reuse blast radius`;
- a new communication/internet transition: personal secret → multiple recovery channels → password managers/passkeys;
- new overseas comparisons: 1960s CTSS and the 2024 passkey first-person account;
- concrete same-era cases from 2006, 2009, 2018 and 2025.

This round is therefore not a saturation round; the consecutive "no substantial addition" count remains **0/3**.
