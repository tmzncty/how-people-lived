# From "mailing two copies of a contract back and forth" to "signed on a phone in a few minutes": electronic signatures, remote contracts and commitment executability (China, 1995–2026; with a global prehistory)

> Cross-repo companion: `tmzncty/old-web-archaeology/docs/ELECTRONIC_SIGNATURE_ECONTRACT_CA_BROWSER_AND_CONSENT_STATE_GAPS_2004_2015.md`

## 0. Why this is a life-horizon problem

Legal history easily reduces a contract to a set of articles, information-security history to an algorithm, and corporate digitalization history to "paperlessness". But for an ordinary person's life course, the more basic question is actually:

> **Does a future job, tenancy, loan, transaction or collaboration have to wait until both parties' bodies appear in the same place before it can formally come into existence?**

A paper contract did not mean distant parties could not conclude an agreement: post, fax, agents and telephone negotiation all predate the mass Internet. What the Internet and electronic signatures actually changed is that more and more functions once scattered across different media and different places could be compressed into a single digital transaction chain:

```text
see the text
→ confirm "who this is"
→ express "I agree"
→ fix "which version I agreed to"
→ record "when it was signed"
→ deliver the result to the other party
→ let both parties retrieve it later
→ let them prove it if a dispute arises
```

This topic calls that capability:

**`remote commitment executability`**

What it changes is not whether people need to make commitments, but the spatial and temporal conditions under which a commitment enters a future life.

---

## 1. Core concepts

### 1.1 `signature-function unbundling`

A "signature" on paper looks like one action, but it actually carries several different functions:

- identity: who signed;
- declaration of intent: whether the person actually agreed;
- textual integrity: whether the text was altered after signing;
- time: when it was signed;
- delivery: whether the other party received it;
- custody: whether the same text can still be produced later;
- evidence: whether those states can be proven in a dispute.

An electronic signature does not perform these functions automatically just because a handwriting image has been scanned into a PDF.

So we must distinguish:

```text
visible signature image
!= identity proof
!= reliable electronic signature
!= mutual assent
!= durable contract evidence
```

### 1.2 `commitment mobility`

Must a person, in order to make a formal commitment:

- return to the office;
- go to an agency branch;
- go to a bank counter;
- wait for paper to arrive by post;
- post the contract back again;
- find someone to sign or deliver on their behalf.

If identity, text, signing and delivery can all be completed remotely, then people who are migrating, job-hunting in another city, on business trips, in cross-city families or in long-term mobility can lock in the next step earlier.

### 1.3 `contract custody`

One important fact about the paper era is that a contract was often something a person literally held in their hand.

An electronic contract, by contrast, may exist in:

- a company HR system;
- a third-party e-signature platform;
- a government human-resources and social-security platform;
- an email inbox;
- an app account;
- a cloud document;
- a locally downloaded copy.

Therefore:

**`contract exists != party can still retrieve it later`**.

After leaving a job, changing a phone number, closing an account, a platform shutting down or permissions being revoked, "I once signed it" and "I can still produce that contract today" are two different states.

### 1.4 `consent evidence chain`

Electronic contracts are especially prone to one faulty inference:

```text
there is a signed PDF in the system
→ this person must have read it
→ it must have been the person themselves
→ they must have known the terms
→ they must have voluntarily agreed
```

None of these conclusions follows automatically.

A more defensible chain is:

```text
identity proof
→ signing credential control
→ contract version presented
→ opportunity to review
→ explicit signing action
→ signature bound to exact data
→ delivery / retrieval evidence
→ later verification
```

### 1.5 `commitment acceleration`

Remote signing cuts postal, travel and queueing time, but it can also compress "read it slowly, take it home to think, then sign" into a few taps on a phone.

Therefore:

**`faster execution != better bargaining != better comprehension`**.

### 1.6 `contractualization gap`

Even where reliable electronic signatures already exist, it does not follow that informal workers will all obtain formal contracts.

Technology can only lower some signing costs; it cannot automatically resolve:

- whether the employer is willing to sign;
- whether the employment relationship is recognized;
- whether the platform defines the worker as an employee;
- whether bargaining power is symmetrical;
- whether the worker dares to ask for a contract.

Therefore:

**`e-signature availability != formalization of informal work`**.

---

## 2. Global prehistory: the Internet did not invent "remote commitment", but it began turning commitment into verifiable data

### 2.1 1994: the digital signature standard first settled "who signed the data, and was it altered"

NIST published FIPS 186, the Digital Signature Standard, in May 1994. The official description explicitly assigns digital signatures to verifying the integrity of electronic data and the identity of the signer, and notes that electronic messages, forms and contracts can benefit from this authentication capability; the standard relies on public-key/private-key cryptography.

Source:
- NIST, `NIST Announces "Digital Signature" Standard For Computer Security`, 1994-05-20: https://www.nist.gov/news-events/news/1994/05/nist-announces-digital-signature-standard-computer-security
- NIST CSRC, `FIPS 186 Digital Signature Standard`, 1994-05-19: https://csrc.nist.gov/pubs/fips/186/final

**Grade:** A — official standard and contemporaneous agency announcement.

But this only proves that digital signature technology and a standard existed; it does not support the inference that ordinary households were already signing contracts online in 1994.

### 2.2 1996: the law began to break "paper" into functions rather than material

UNCITRAL's 1996 Model Law on Electronic Commerce set out the principles of non-discrimination, technological neutrality and functional equivalence; one of its aims was precisely to let electronic information carry the legal role of a paper document when it performs the corresponding functions. It also dealt with the attribution of data messages and the time and place of their sending and receipt.

Source:
- UNCITRAL, `Model Law on Electronic Commerce (1996)`: https://uncitral.un.org/en/texts/ecommerce/modellaw/electronic_commerce

**Grade:** A — original explanatory text of an international organization's legal instrument.

This meant the key question of digitalization gradually shifted from "is there a sheet of paper" to:

> **whether the electronic record performs the functions that the law assigns to paper, signature, original and delivery.**

### 2.3 2000–2001: paperlessness also had to prove that ordinary people could actually obtain the record

The US ESIGN Act passed in 2000. In 2001, discussing the consumer-consent provisions, the FTC stated explicitly that where information required by law to be provided in writing is instead provided as an electronic record, the manner of consumer consent should reasonably demonstrate that the consumer has the ability to access that electronic record.

Source:
- FTC, `FTC, Department of Commerce to Host Esign Workshop`, 2001-02-16: https://www.ftc.gov/news-events/news/press-releases/2001/02/ftc-department-commerce-host-esign-workshop

**Grade:** A — contemporaneous government material.

This is a very important overseas counter-example:

**`electronic legal equivalence != meaningful access`**.

If a person lacks suitable equipment, software or a long-term accessible account, "the law permits electronic form" does not mean they actually obtained a contract they can keep.

---

## 3. The Chinese boundary: the law taking effect in 2005 did not mean ordinary people suddenly began signing electronically in 2005

### 3.1 1994 must not be written as "contract digitalization went from nothing to something"

Research networks, email, leased lines and computer systems already existed in China before 1994; and full-function connection to the global Internet after 1994 did not mean that household access, enterprise workflows, CA systems and ordinary users' devices all became widespread at the same time.

This topic therefore does not treat the "Internet connection date" directly as the starting point of the everyday history of electronic contracts, and instead uses layers:

```text
network / computer systems exist
→ digital signature technology and authentication infrastructure exist
→ the law recognizes data messages / reliable electronic signatures
→ enterprise or sector pilots
→ ordinary individuals can actually obtain it
→ signing enters work / housing / consumption as a norm
→ contract status is further connected to public service systems
```

### 3.2 2004–2005: the Electronic Signature Law settled legal recognizability

The Electronic Signature Law of the People's Republic of China was adopted on 28 August 2004 and took effect on 1 April 2005. The law defines an electronic signature as data in a data message used to identify the signer and to indicate the signer's approval of the content; a data message that can be displayed in tangible form and retrieved at any time can satisfy the writing requirement, and can satisfy the "original" requirement when conditions such as integrity are met.

The 2005 Measures for the Administration of Electronic Authentication Services then brought third-party authentication services — which verify the authenticity and reliability of electronic signatures — under licensing and regulation.

Sources:
- Cyberspace Administration of China, Electronic Signature Law of the People's Republic of China, 2004-08-28: https://www.cac.gov.cn/2004-08/28/c_126468489.htm
- Ministry of Justice, Measures for the Administration of Electronic Authentication Services, 2005-04-12 (the measures took effect 2005-04-01): https://www.moj.gov.cn/pub/sfbgw/flfggz/flfggzbmgz/200504/t20050412_143906.html

**Grade:** A — original text of a law / departmental rule.

But the law itself also makes clear that `electronic form` is only a form that may be recognized, and does not mean that every document and every setting is automatically digitalized.

---

## 4. 2005: an early version of the expansionary future — "one day a contract may not have to wait for a person to come back"

### 4.1 A very staged signing event actually preserved the real uncertainty of the time

In the early hours of 1 April 2005, the day the Electronic Signature Law took effect, Pan Shiyi signed two electronic contracts. The contemporaneous report in Internet Weekly itself pointed out that the event had an obvious demonstrative/showcase character.

What is more valuable is not the promotional label of "the first", but the questions Pan Shiyi kept asking at the time:

- could he use it to sign documents with a bank;
- what if the password were cracked;
- what if the electronic seal were lost;
- could he later sign this way with home buyers, builders and banks alike.

Source:
- Internet Weekly, republished, Electronic Signature: Farewell to Armchair Talk, 2005-05-11: https://finance.sina.com.cn/chanjing/b/20050511/16411578910.shtml

**Grade:** B — contemporaneous industry report; the "first" claim and the reported application effects belong to journalistic/vendor narrative and are not treated as absolute fact.

This is very good material on how contemporaries imagined the future. It shows that the sense of expansion in 2005 is not a summary produced by looking back today: the participants themselves were already imagining a future —

> **if banks, home buyers and suppliers all accepted this system, the place of signing might no longer be tied to where a person's body was.**

### 4.2 The same report also supplied a counter-proof: the law appeared, but the market did not immediately take off

The same report also records that some e-commerce enterprises were still watching and waiting, for reasons including cost, that the degree of marketization of CAs was limited, and that informatization penetration and the credit environment also constrained adoption.

This satisfies the repository's methodological requirement exactly:

```text
law exists
!= CA easily available
!= browser/device usable
!= counterpart accepts
!= ordinary user adopts
```

The "expansion" of 2005 was first of all **a future route being opened**, not that route having already become everyone's daily life.

---

## 5. The real friction of the old web: signature functions often depended on browsers, certificates, controls and keys

Today's mobile experience makes it easy to read electronic signing backwards as "you just tap once". The PC web era was not like that.

Microsoft's official legacy note on InfoPath Forms Server 2007 states explicitly that a digital signature in a browser requires an ActiveX-capable web browser, and therefore Windows Internet Explorer must be used; the first signing also requires installing and enabling two ActiveX controls, and then selecting a certificate before the signature can be completed.

Source:
- Microsoft Support, `Add a digital signature to a browser-enabled form` (applies to Forms Server 2007/InfoPath): https://support.microsoft.com/en-US/infopath/add-a-digital-signature-to-a-browser-enabled-form

**Grade:** A/B — official product documentation, still hosted today; it can establish the technical requirements of a legacy product, but it is not a 2007 web capture.

This means "signable remotely" has to be broken down further into:

```text
have a computer
+ have a network connection
+ a compatible browser
+ ActiveX/plugins can be installed
+ a certificate exists
+ the private key is usable
+ the page can load
+ the signature control can run
+ the server accepts it
```

So after the Internet arrived, the fact that **the body no longer had to go to the counter** did not mean infrastructure friction disappeared; the friction may simply have moved into browsers, USB keys, certificates and technical support.

---

## 6. "Online filing" is not one thing: the 2008 housing online contract filing is the best counter-example

When Beijing introduced online filing for existing-home transactions in 2008, contemporaneous material shows that free service windows were still provided, where buyer and seller could go to a service venue to complete the online filing; on the first day some halls had few applicants at all.

This kind of material is very well suited to blocking a common misreading:

**`online contract filing (wangqian) != cryptographic electronic signature != remote signing`**.

"Online filing" may mean:

- property information entering a government database;
- contract text generated or recorded online;
- counter staff operating through a system;
- both parties still meeting in person and signing on paper.

So the appearance of the two words "online filing" in a historical source must not be written straight up as "in 2008 ordinary home buyers could already sign electronically remotely from home".

> Housing online filing already has its own dedicated topic; this section serves only as a counter-example for the concept of a signature, and does not repeat the housing history.

---

## 7. 2015–2019: the congested future — signing became faster, but contracts also began to become platform affairs

### 7.1 2015: remote rental contracts were still first of all an advertised future

In 2015 Wan Min, founder of Shangshangqian, described an ideal scenario to The Beijing News: when renting, you and the landlord quickly sign a safe and valid contract online; the report also acknowledged that "online signing" had not really developed yet at that time.

Source:
- Xinhua, republishing The Beijing News, Shangshangqian Makes Online Signing Reliable, 2015-10-08: https://www.xinhuanet.com/politics/2015-10/08/c_128294214.htm

**Grade:** B — contemporaneous founder/product narrative, not used to establish mass adoption.

This material preserves the 2015 imagination of the future:

> transactions could already find the other party online and pay online; the next step was the hope that even the "formal commitment" would not have to fall back to paper and meeting in person.

### 7.2 Internet finance exposed the problem of "the platform holds the transaction, but the individual holds no evidence"

A contemporaneous 2015 report on P2P recorded that many transactions took place entirely inside the platform and investors often had no paper contract; once a platform absconded or the back-end evidence disappeared, an individual might be left with nothing but payment records. The industry therefore began to emphasize third-party electronic contracts and the fixing of evidence.

Source:
- People's Daily Online, republishing Guangzhou Daily, Introducing Electronic Contracts to Solve the P2P "Absconding" Problem, 2015-04-27: https://finance.people.com.cn/money/n/2015/0427/c42877-26908888.html

**Grade:** B — contemporaneous media plus industry figures; it cannot be used to prove that electronic contracts in themselves necessarily protect investors.

What appears here is `contract custody`:

**if a contract exists only in the trading platform's own database, then when the platform fails the contract may lose its executability along with it.**

### 7.3 2019: labour contracts began to go directly onto the phone

In 2019 Haier and the Qingdao human-resources and social-security department launched an electronic labour-contract model. Contemporaneous reporting describes it: the system sends a signing invitation to the employee's phone; after face-recognition real-name authentication the employee can sign with one tap, and can query, print and store the contract online; the promotional material at the same time stressed that it solved the problem of renewals or amendments being late because the person was away on business.

Sources:
- China Daily, 2019-06-04: https://sd.chinadaily.com.cn/a/201906/04/WS5cf62a43a31011d294da9fa7.html
- Qingdao Daily, republished, 2019-06-04: https://news.iqilu.com/shandong/shandonggedi/20190604/4285044.shtml

**Grade:** B — contemporaneous enterprise and government-enterprise project reporting; it proves the workflow existed, not that all workers were already signing this way.

By the time of the 2020 Beijing rollout, reporting also looked back and said that Baidu had already used an enterprise electronic seal for campus recruitment in the second half of 2019; JD.com's experience was to replace paper procedures that had previously taken several hours per employee during batch onboarding with operations on the employee's phone, so that people outside Beijing no longer had to mail contracts back and forth.

Source:
- People's Daily Online Beijing channel, 2020-04-22: https://bj.people.com.cn/n2/2020/0422/c14540-33967522.html

**Grade:** B — a near-contemporaneous 2020 reconstruction of 2019 enterprise practice.

This means the process of "starting a job" became decoupled:

```text
receive the offer
→ remote identity verification
→ read the contract on the phone
→ sign electronically
→ enterprise/platform storage
→ start work
```

A person could complete part of the formalities of an employment relationship before ever being physically in the same place as HR.

---

## 8. But the same period had another reality: many gig workers never entered the "contract" track at all

A contemporaneous 2019 report on food-delivery riders noted that many riders had no traditional labour contract and had their relationship defined only by a crowdsourcing service platform agreement in an app or by an offline oral arrangement, which brought difficulties in establishing the employment relationship and in defending rights.

Source:
- People's Daily Online public welfare channel, "Gig" Riders Face Many Difficulties Defending Their Rights, 2019-07-26: https://gongyi.people.com.cn/n1/2019/0726/c151132-31257711.html

**Grade:** B — contemporaneous report.

This is one of the most important counter-examples in this topic:

> **electronic signatures make the people who are already willing to sign a formal contract sign faster; they do not automatically bring in the people who were never covered by a formal labour contract.**

So we cannot write:

> "once electronic contracts spread, employment relationships became more formal."

At most we can write:

> "for the subset of relationships where a written contract has already been chosen or required, electronic signing lowered the cost of completing the formalities across distance."

---

## 9. 2019: electronic contracts turned "did you sign or not" from a question about a sheet of paper into a question about an evidence chain

In 2019 Legal Daily reported on a bank that fell into evidentiary difficulty in litigation because key logs of an electronic contract were missing, and in the end needed forensic-examination experts to rework the data before evidence could be formed.

Source:
- People's Daily Online, republishing Legal Daily, 2019-04-29: https://money.people.com.cn/n1/2019/0429/c42877-31056448.html

**Grade:** B — contemporaneous judicial/media report.

This shows that while electronic contracts reduce paper custody, they add another kind of "archival infrastructure" requirement:

```text
contract PDF
+ identity record
+ signature verification data
+ time / log
+ delivery record
+ version history
+ audit trail
```

**keeping only the final PDF is not necessarily the same as keeping all the conditions needed to prove it in the future.**

---

## 10. 2020–2022: the occasional future — when people could not meet, remote commitment became a fallback

### 10.1 The pandemic turned "must labour contracts be signed face to face" into a practical problem

In March 2020, answering a request for instruction concerning epidemic prevention and control, the Ministry of Human Resources and Social Security stated explicitly: an employer and a worker may, by agreement, conclude a written labour contract in electronic form, but must use data messages that can be treated as writing under the Electronic Signature Law and reliable electronic signatures, and must ensure that generation, transmission and storage are complete, accurate and untampered with.

Source:
- General Office of the Ministry of Human Resources and Social Security, Letter on Issues Concerning the Conclusion of Electronic Labour Contracts, 2020-03-04: https://www.mohrss.gov.cn/xxgk2020/fdzdgknr/ldgx_4234/ldyg/202003/t20200310_362037.html

**Grade:** A — original official document.

Beijing then explicitly linked online recruitment and the online signing of electronic labour contracts to returning to work and employment during the epidemic.

Source:
- People's Daily Online / Workers' Daily, 2020-04-23: https://acftu.people.com.cn/n1/2020/0423/c67502-31685166.html

**Grade:** B — contemporaneous report.

The occasional future appears here in a very typical form:

> a capability normally used mainly to save errands suddenly became, at a time when bodies temporarily could not conveniently meet, the fallback infrastructure that kept recruitment, onboarding and renewal running.

### 10.2 2022: an ordinary person's "15-minute remote counter signing" proved that multi-party co-presence could also be taken apart

In 2022 People's Daily Overseas Edition reported that when Ms Yan in Beijing was buying a home, her husband was out of town and could not return to Beijing, so the couple, the seller, the loan bank's account manager and the agent each logged into the system from different locations and completed the online counter signing in about 15 minutes.

Source:
- Cyberspace Administration of China, republishing People's Daily Overseas Edition, Let Information Run More and the Public Run Less: "Cloud Signing" Is Really Convenient, 2022-11-30: https://www.cac.gov.cn/2022-11/30/c_1671446738694677.htm

**Grade:** B — a contemporaneous individual case of an ordinary person; it does not mean all housing transactions nationwide could already be completed remotely.

The significance of this material is not that "housing finally went online", but that:

**a co-presence that originally had to be scheduled across five kinds of people can now be split into being online at the same time without being in the same room.**

---

## 11. 2023–2026: the defensive future — the focus began shifting from "can we sign electronically" to "how do we guarantee that we can still prove we signed"

### 11.1 2023: a job applicant could genuinely "complete a labour contract before ever meeting"

On 1 March 2023, job applicant Cheng Fangyuan entered the Inner Mongolia government-services app on her phone, reviewed the contract, then confirmed, submitted and entered her password, and completed what local reporting called the first electronic labour contract there via face recognition / electronic signature. In a contemporaneous interview she said there was no need to meet and no need to run back and forth, and it could be done in a few minutes.

Sources:
- China Employment Network / People's Daily Online, 2023-03-07: https://chinajob.mohrss.gov.cn/c/2023-03-07/371436.shtml
- China Youth Daily / China Workers' Network, 2023-03-10: https://news.cyol.com/gb/articles/2023-03/10/content_bmqWLoILjq.html

**Grade:** B — contemporaneous media plus an ordinary person's first-person account; "first" is the local agency's/report's framing.

This is a very clear change in life path:

```text
the job applicant is in place A
the enterprise is in place B
→ read the contract on the phone
→ remote identity / intent confirmation
→ the labour contract comes into existence
```

Formalizing an employment relationship no longer inherently requires one physical meeting.

### 11.2 Defence one: the contract must be something the worker can take away

A 2025 public question-and-answer from the human-resources and social-security authorities explicitly requires that the employer notify the worker that the electronic labour contract has been concluded, prompt them to download and save it in good time, and guarantee that the worker can view, download and print the complete content at any time on commonly used devices without charge; where the worker needs a paper text, the employer must provide at least one copy free of charge.

Source:
- Tianjin Economic-Technological Development Area, republishing the Ministry of Human Resources and Social Security WeChat account, Is There a Charge for Viewing an Electronic Labour Contract?, 2025-04-22: https://www.teda.gov.cn/contents/220/85970.html

**Grade:** A/B — official question-and-answer republished by government.

This means the maturity of digitalization cannot be judged only by the "signing completion rate"; we should also ask:

> **after a worker leaves the enterprise, changes device or loses an account, do they still hold a text that they themselves can keep and take to defend their rights?**

This is `contract custody right`.

### 11.3 Defence two: a document bearing an "electronic signature" may still fail to prove that the two parties reached agreement

In 2025 Workers' Daily reported a case in Karamay: the enterprise could not prove that the online-filed labour contract constituted a meeting of minds, and the court ultimately handled it as no written labour contract having been signed. The case is a reminder that an electronic-contract dispute is not as simple as whether the file exists; it requires further verification of who operated it, whether they were authorized, whether it was delivered, and whether agreement was genuinely expressed.

Source:
- Workers' Daily, republished, 2025-02-20: https://www.thepaper.cn/newsDetail_forward_30199347

**Grade:** B — contemporaneous judicial report.

This counter-example sets a very important bottom line:

**`real-name data / old signature image / electronic file != voluntary assent`**.

### 11.4 2026: contracts begin turning from "a document" into machine state in public service systems

By the time of the 2023 official introduction in Inner Mongolia, electronic labour contracts were already planned to be connected through to systems for labour-employment filing, employment and unemployment registration, social insurance, and labour-dispute mediation and arbitration; in 2026 many places continue to push electronic labour-contract data through platforms into employment, social-security and talent-service processes.

This means a future labour contract may carry two identities at once:

```text
a document for a person to read
+
a structured state for institutional systems to consume
```

For an ordinary person, this will further change the way one proves "I once worked here".

But the boundary must be kept:

**`contract data synced != every downstream right automatically recognized`**.

---

## 12. A comparison of four kinds of "future time"

| Period | Dominant sense of time | Role electronic signing plays in it | Conclusion that must not be substituted |
|---|---|---|---|
| 2005–2012, expansionary | more and more affairs seemed able to detach from place | opens the future route of "remote formal commitment" | law in force ≠ public already using it |
| 2015–2019, congested | more and more affairs online, and signing also pressed into platform workflows | phone/cloud signing raises the speed of onboarding and transactions | fast ≠ understood ≠ equal bargaining |
| 2020–2022, occasional | face-to-face processes may suddenly become unavailable | remote signing becomes the fallback for recruitment, counter signing and administrative procedures | fallback ≠ accessible to all groups |
| 2023–2026, defensive | attention begins to turn to evidence, custody, exit and mistaken-signing risk | download/print, paper copies, real name/intent/logs, public platforms | having an electronic file ≠ agreement established |

---

## 13. Consequences for the "standard life script"

The traditional standard script is often written as:

```text
graduate
→ report to the company
→ handle onboarding in person
→ sign the labour contract
→ start work
```

After digital signing, the actual order can become:

```text
be in another place
→ interview online
→ receive the offer
→ remote real-name authentication
→ sign the labour contract on the phone
→ then migrate / then report for duty
```

This adds a very concrete life path:

> **a person can first fix part of their future institutional status, and only then decide when their body will move there.**

This matters especially for graduates, people job-hunting in another city, business travellers and cross-city families.

But another life path still exists:

```text
start working
→ no formal labour contract
→ only a platform agreement / oral arrangement remains
→ prove the relationship after a dispute arises
```

So electronic signatures do not mean "the standard life script becomes more standard"; they mean **the formal path becomes easier to execute remotely for some people, while the people outside the formal path are not eliminated.**

---

## 14. Connections to the core matrix

### Education / employment
- campus recruitment can complete part of the signing while the student is still at school or in another city;
- the start of employment and the first physical reporting are further decoupled.

### Housing
- a distinction must be kept between "online filing for the record", "online counter signing", "reliable electronic signature" and "final registration";
- a database state must not be treated as the completion of the whole housing transaction.

### Migration
- a job or transaction can be locked in first, and the move made afterwards;
- it reduces trips between cities made specially in order to sign.

### Informal labour
- technical availability does not automatically give riders, cleaners or day labourers a formal labour contract.

### Documents and records
- the contract turns from paper into a combination of data message, signature certificate, logs, time records and account permissions.

### Communication
- post, fax and telephone were not replaced in an instant;
- the web, apps, SMS, email and face recognition gradually came together to form the signing chain.

### Future expectations
- the future of 2005 was "one day contracts may all be remote";
- the future of 2015 was "payment is already online, so signing should be online too";
- the reality of 2020 was "we can keep signing when we cannot meet";
- the defence of 2025 is "after signing, can I still obtain, prove and contest this contract".

### Online / offline identity
- real-name authentication is not consent itself;
- being able to identify "who this is" is not the same as being able to prove "which version of the text they agreed to".

### Platform disappearance and memory preservation
- electronic contracts should not exist only in an enterprise's internal account;
- future research should examine how account closure after leaving a job, platform migration and certificate expiry affect the verifiability of contracts.

---

## 15. Historical visibility bias

Electronic contracts are very dangerous for historians, because what is easiest to see today is:

- the law;
- vendor websites;
- promotion of "the first electronic contract";
- success stories;
- screenshots of e-signature pages;
- a final PDF.

What is hardest to see is:

- whether the user actually read it;
- whether the browser/ActiveX actually worked at the time;
- who actually controlled the private key;
- whether the SMS/verification code actually arrived;
- which version was agreed to;
- whether the enterprise gave the individual a complete copy;
- whether it can still be retrieved years after leaving the job;
- why the people who had no contract never entered the system.

Therefore:

**`archive-visible contract != lived agreement`**.

---

## 16. Hindsight risks

### Risk A: writing "the Electronic Signature Law took effect" as mass adoption of electronic contracts

Wrong. The law settles only part of legal recognition and of the institutional framework.

### Risk B: reading every "online filing" as a digital signature

Wrong. Many online filings are database-recording or online-generation processes, and the two parties may still sign on paper at the counter.

### Risk C: equating phone real-name authentication with the person's own free consent

Wrong. Identity, device control, presentation of the text, authorization and declaration of intent must be kept separate.

### Risk D: equating saved time with expanded freedom

Wrong. Signing faster can also mean less time to read, stronger pressure to tap, and a more one-directional enterprise workflow.

### Risk E: equating broader electronic-contract coverage with protection of informal labour

Wrong. Whether the employment relationship is recognized and whether there is a willingness to sign a contract are different institutional questions.

---

## 17. What we still do not know

1. How low was the share of ordinary individuals who actually used a CA/USB key to sign non-bank contracts in 2005–2010?
2. What were the failure rates for browser, control and certificate installation in early electronic contracts?
3. How long does an enterprise's internal electronic-contract platform usually retain an individual's access after they leave?
4. Did phone signing shorten the time ordinary workers actually spend reading a contract?
5. Did electronic labour contracts reduce the situation of "signed, but the employee never got their own copy"?
6. After a third-party e-signature platform shuts down, migrates or changes its certificate system, how is a contract from ten years ago still verified?
7. Which groups of informal workers remain systematically absent from the spread of electronic contracts?
8. Once electronic-contract data is connected to social-security/employment systems, how can an ordinary person correct an error in the data?

---

## 18. What this round changed in our understanding

In the past, a formal future often required the body to arrive first:

> go to the company, go to the bank, go to the agency, finish signing on paper, then come back and wait for the next step.

What electronic signatures genuinely added is not "one less pen", but:

> **before a person's body has reached the next stop, part of their future in institutional terms can arrive first.**

A job applicant can sign a labour contract in another city; someone on a business trip can complete a renewal; two parties who cannot meet during an epidemic can keep the procedures moving. This change makes migration, work and transactions more separable into parts.

But digitalization also pulled apart the questions that paper signing had once compressed into a single action:

> Who signed? What credential did they control? Which version did they see? Did they really agree? Did the other party receive it? Can it still be produced ten years later?

So the sign that electronic contracts have matured should not be merely "signed in a few seconds", but that an ordinary person can still answer these questions many years later.
