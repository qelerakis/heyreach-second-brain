# Personalization & message experiments — what actually moves the numbers

Several campaigns in the library are explicit **A/B experiments**, and their findings are often counterintuitive: heavy personalization can *lower* reply volume while *raising* meetings; segmentation and a curiosity hook can beat both volume and hyper-personalization; a blank connection request can out-accept a noted one; and a personalized *asset* (a page or a deck) delivered as the first touch can lift replies. These are the most decision-useful case studies for anyone tuning copy. All numbers are self-reported (COI noted); several are single-client or small-sample.

## GenPage — personalized pages lowered replies but *doubled* meetings

**Who:** **Valentin and Samy Barbier** of **GenPage** (genpage.ai), testing **their own** personalization product — a COI (source: "Personalized landing pages that book meetings").

**Context & tactic:** A side-by-side A/B of personalized landing pages vs standard pages in LinkedIn outbound, using only 3 tools. Clay built a 1,000-company list (size 2–10; Marketing Services; Canada/NZ/UK/USA/Australia; keywords "lead generation, growth marketing") with LinkedIn URLs → GenPage generated a unique personalized page per prospect → HeyReach ran the campaign (View Profile → Connection Request 3 hours later → on accept, wait 3 hours → DM → 2 follow-ups; for non-accepters, a "three likes in eight days" nudge). The two parallel campaigns differed **only** in whether the message/page was personalized (source: "Personalized landing pages that book meetings").

**Numbers (self-reported):** Overall **9 meetings from 69 conversations**; the **personalized-pages campaign booked 6 of the 9 meetings (~2×)** — even though the **non-personalized** version got **more total and positive replies** (source: "Personalized landing pages that book meetings").

**The finding to preserve:** personalized pages **lowered reply volume but doubled meetings** (the actual goal) — "people actually appreciate it when you try harder," and reply volume ≠ meeting volume. **Do not** cite this as "personalization → more replies." Small sample (69 conversations → 9 meetings) (source: "Personalized landing pages that book meetings").

## Tim Jacobsen (B2B Boosted) — 2,400 messages, and why segmentation beat everything

**Who:** **Tim Jacobsen**, founder of **B2B Boosted** + Unlock Courses — his agency/courses are the COI. (Same practitioner as "Tim Yakubson" in [[lead-magnet-and-audience-growth-campaigns]].) The teardown names a real firm, **Cooley LLP**, as a live example (source: "I Sent 2,400 LinkedIn Messages in 30 Days (Real Results + What Actually Worked)").

**Context & tactic:** A 30-day teardown built as controlled A/B experiments (isolate one variable per campaign). Thesis: "volume is not the thing that made this work" — half the campaigns failed. The head-to-head used the **same ICP** (decision-makers at law firms), the **same 90-day window**, and two 3-message campaigns whose messages 2 and 3 were **identical** (source: "I Sent 2,400 LinkedIn Messages in 30 Days (Real Results + What Actually Worked)").

**Numbers (self-reported):**

*30-day totals:* **2,422 messages sent, 142 replies, 73 real conversations, 19+ booked calls; ~1,500 accepted connection requests (~21%); 25% reply rate; 6% email reply rate on ~300 emails.**

| | Campaign A (worst ever) | Campaign B (winner) |
|---|---|---|
| Targeting | 83,000 followers of Cooley LLP, partners only (scraped via scrapely.io) | In-house lawyers only, companies 50–150 employees |
| Hook | "Guessing you used them in the past?" | Curiosity trigger: "Guessing you heard about the redundancies over that company?" |
| Connection requests | 793 | 458 |
| Accepted | 28% | 134 (29.3%) |
| Replies | 4 | 47 |
| Positive / calls | **0 positive** | **12+ sales calls booked** |

(source: "I Sent 2,400 LinkedIn Messages in 30 Days (Real Results + What Actually Worked)")

**Three differences that mattered:** (1) far better **list segmentation** (in-house vs firm lawyers), (2) a **curiosity-driven** question, (3) **timing** (B sent 8am–1pm Mon–Fri vs A's 8am–6pm daily — flagged by him as possible correlation, not causation). **What did NOT matter:** AI personalization, long messages, many data points, over-engineered hooks — "we didn't even research their zodiac sign or the name of their dog." Takeaway: "it's far better to reach out to half a thousand people… with a better segmented message" than to 2,000 with a generic one (source: "I Sent 2,400 LinkedIn Messages in 30 Days (Real Results + What Actually Worked)").

## Automated pitch decks — a claimed 44% higher reply rate

**Who:** An **unnamed guest practitioner** writing in the first person on HeyReach's blog, who appears to **sell this exact deck service** (a calendar-booking CTA is baked into the decks) — a COI (source: "Scaling personalized LinkedIn outreach with automated pitch decks (44% higher reply rate)").

**Context & tactic:** Deliver fully personalized **pitch decks** at scale as the LinkedIn first touch. Ampify scrapes the Meta Ads Transparency Suite → Clay enriches and (ICP filter: **20–1,000 active Meta ads** as a spend proxy) runs a **GPT-4.1** landing-page analysis returning structured JSON → the **Gamma API** generates a ~7-card deck per company (title / summary / what's working / what to improve / recommended changes / CTA with a calendar link). HeyReach sends: **blank** connection request → first message verbatim "[First name], ran a performance analysis on one of your meta ad landing pages. Cheers, [First name]." (the embedded URL does the talking, no ask) → wait **three weeks** → one minimal follow-up "Managed to take a look?". A fallback generic note triggers <1% of the time (source: "Scaling personalized LinkedIn outreach with automated pitch decks (44% higher reply rate)").

**Numbers (self-reported):** A claimed **44% higher reply rate for one client** (source: "Scaling personalized LinkedIn outreach with automated pitch decks (44% higher reply rate)").

**Caveat to preserve:** "44% higher reply rate" is a **single-client, self-reported** figure repeated from the title into the body with **no baseline or sample size** — treat as a claim, not a benchmark. "The absence of a CTA in the message signals confidence." Era: names GPT-4.1 and the Gamma API; costs quoted in GBP (source: "Scaling personalized LinkedIn outreach with automated pitch decks (44% higher reply rate)").

## Data point: blank vs noted connection requests

A recurring micro-test across the library favors the **blank** (no-note) connection request. One guest masterclass cites HeyReach's own data: **a blank connection request got 27% acceptance vs 22% with text** (source: "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)"). Multiple campaigns adopt the empty note as "best practice" (e.g. Linkunity in [[simple-and-direct-campaigns]], and HeyReach's own campaigns in [[heyreach-first-party-campaigns]]). The frameworks deliverability rules also note that a connection *note* now carries a punitive LinkedIn cap (~10/month), which reinforces going note-free at scale.

## What the experiments agree on
- **Targeting/segmentation and offer beat wording.** Both GenPage and Tim Jacobsen found that message micro-tweaks and hyper-personalization moved the numbers far less than list quality and the concept/asset.
- **Optimize for meetings, not replies.** GenPage's personalized pages won on meetings while *losing* on replies — the metric you optimize changes the verdict.
- **Personalized *assets* (pages, decks) can outperform personalized *text*** as the first touch.

## Related
- [[simple-and-direct-campaigns]] — segmentation + blunt copy; blank-note practice
- [[engagement-signal-campaigns]] and [[buying-and-intent-signal-campaigns]] — the targeting layer these experiments say matters most
- [[lead-magnet-and-audience-growth-campaigns]] and [[event-led-outreach-campaigns]] — Tim Jacobsen / B2B Boosted's other campaigns
- [[aggregate-creator-claims]] — the $5M masterclass this blank-vs-noted stat comes from
