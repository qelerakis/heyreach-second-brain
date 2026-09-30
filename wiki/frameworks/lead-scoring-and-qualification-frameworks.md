# Lead Scoring & Qualification Frameworks

This article collects the frameworks HeyReach's content uses to **rank, qualify, and route leads** — the classic B2B qualification acronyms, the first-party Hot/Warm/Cold intent-scoring model, the fit-plus-signal tiering systems, the anti-ICP qualification gate, and the SDR daily-prioritization matrix. It follows [[icp-and-targeting-systems]] (build the list) and feeds [[signal-based-outbound-framework]] (route by signal). The recurring thesis: **quality beats quantity, and qualifying *upstream* protects both pipeline and sender health** — "We shouldn't care about the total number of free trials... [but] the total number of qualified free trials" (source: "This lead scoring system doubled our conversion rate"). Scores and thresholds are self-reported/illustrative and era-bound (2026).

## Classic B2B qualification frameworks

HeyReach repeatedly lists the standard acronyms and notes **any of them can be automated** by mapping the criteria to the stack (source: "Streamlining success: lead qualification process that gives 20% more conversions"; source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline"; source: "LinkedIn lead generation strategy for 60%+ reply rates"):

| Framework | Expansion |
|---|---|
| **BANT** | Budget, Authority, Need, Timeline |
| **CHAMP** | Challenges, Authority, Money, Prioritization |
| **MEDDIC** | Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion |
| **ANUM** | Authority, Need, Urgency, Money |
| **GPCTBA** | HubSpot's inbound qualification framework |

The mapping to HeyReach's "deadly combo" stack: HeyReach reaches decision-makers, Clay enriches needs/criteria, Trigify surfaces intent/timing (source: "Streamlining success: lead qualification process that gives 20% more conversions"). The Five Pillars system also names BANT/CHAMP/MEDDIC/ANUM as its qualifying layer (source: "LinkedIn lead generation strategy for 60%+ reply rates").

## First-party Hot/Warm/Cold intent scoring

Rather than buying third-party intent data ("prediction, not proof"), HeyReach scores **your own campaign data** into Hot/Warm/Cold using acceptance × reply, because acceptance→positive reply→meetings *are* the buyer journey (source: "Find high-intent leads hiding in your campaign data"):

| Tier | Rule (starting points) | Owner |
|---|---|---|
| **HOT** | Acceptance ≥30% AND Reply ≥10% | AEs (SLA: engage within 2 hours of the HOT tag) |
| **WARM** | Acceptance ≥20% AND Reply ≥5% | SDRs convert |
| **COLD** | Acceptance <20% OR Reply <5% | automation nurtures |

The thresholds derive from the Belkins 2024 study (20M+ campaigns → ~30% acceptance, ~10% reply healthy — see [[linkedin-outreach-benchmarks]]). Add a **decay check** (a 3-week-old HOT lead needs re-activation, not standard AE handoff), and segment by role/company size (illustrative: SDRs 40% acceptance/9% reply = easy connect, rarely reply → downgrade HOT unless a meeting is booked; Founders 18%/10% = harder but higher-quality → AE ownership). **HOT >7 days with no meeting → review; COLD >60 days → remove from active campaigns.**

## Fit + engagement + intent tiering

The general model is to **score on fit, engagement, and intent, then tier** (source: "Streamlining success: lead qualification process that gives 20% more conversions"): Tier 1 (high-intent: ICP + high engagement), Tier 2 (moderate, needs nurture), Tier 3 (low-intent) — Tier 1 & 2 to human-led onboarding/CS, Tier 3 to marketing nurture. The signal-led version scores on **3 dimensions — ICP fit × signal strength × potential value** — and ties ownership to signal strength and funnel position (source: "Signal-led GTM engine: Playbook to turn signals into sales").

## ABM 1–5 scoring & the "Triple Threat"

For ABM, a 1–5 lead score with engagement weighting (source: "From ICP to ROI: Your step-by-step LinkedIn ABM playbook"):
- **Score 1–2 (monitoring)** — perfect ICP, zero intent → NO direct outreach; keep in awareness ads/organic.
- **Score 3–4 (warming)** — clicking ads / visiting pages → soft touch (blank invite / low-pressure email).
- **Score 5 ("Triple Threat")** — great ICP + high engagement + a real-world trigger → priority-one immediate personalized follow-up.

**Engagement weighting:** Noise (email opens, likes = low), Interest (multiple case-study clicks, guide download = medium), Intent (pricing/demo visits, positive replies = high). The 4-persona buying committee this scores against is in [[icp-and-targeting-systems]].

## Automated / GPT lead scoring & the lead decision matrix

Build a scoring + routing system with AI rather than rigid rules (source: "Lead scoring automation: stop letting good leads die in a spreadsheet"): **score on fit with GPT** ("rank this lead's likelihood to be a good fit... Output: High, Medium, or Low"), add an **urgency modifier** (site visit in 48h or 2+ email opens = Urgent). A 0–100 variant (via Origami's no-code GPT scoring): "+20 pts pricing-page visit in 7 days; +10 opened 3+ emails; +15 HubSpot/Salesforce in stack; −30 off-ICP industry; fallback missing field → default 50 or manual review." Combine with Factors real-time intent: **High + job change = demo-ready; Medium + tech install = nurture; Low + no signals = deprioritize.** The routing table is the **"lead decision matrix" / "lead scoring matrix"** (if/then): ≥90 → DEMO_01, 60–89 → NURTURE_01, <60 → SKIP/HOLD, missing → ENRICH. "Scoring alone tells you which qualified leads to target. Intent signals tell you when." Re-score every 7 days.

## Anti-ICP qualification (the upstream gate)

The disqualification-first framework: **qualify at the data level, before the first message**, because unqualified volume trains LinkedIn to see you as a spammer (source: "Outbound lead qualification: Turn tough leads into unstoppable growth"). Define **anti-ICP** red flags to remove immediately: stagnant/shrinking headcount, recent down-round or 18+ months without funding, legacy tech stack with no API path, recently locked into a competitor contract, and "professional evaluators" engaging across 5+ competing tools.

- **4-point logic gate:** Firmographic fit (**The Body**), Technographic synergy (**The Brain**), Timing & tenure (**The Heart** — "most underused filter"), CRM deduplication (**The Memory**).
- **Pre-outbound checklist (5 gates, all must be yes):** headcount flat/growing, tech stack compatible, decision-maker at ~7-month tenure, ≥1 active intent signal ("A lead with no intent signal is just a contact"), CRM clearance/dedup.
- **Scoring blueprint (1 pt each):** Sales Ops/RevOps hiring in last 30 days, champion migration, funding in last 90 days, LinkedIn activity in last 30 days, ~7-month tenure → **4–5 pts = Tier A, 2–3 = Tier B, <2 = don't enter.**
- **Tier A "sniper" sequence:** 5–7 touches over 3–4 weeks, deep personalization, manual video/voice on touch 3–4, slower pacing. **Tier B "nurture":** 3–4 touches over 5–6 weeks, content-forward, multichannel, no hard CTA until a micro-signal upgrades it.

## The Sales Prioritization Matrix (SDR daily workflow)

A three-tier matrix for how an SDR spends the day — **conversation-led, not inbox-led** — and explicitly **not** the Eisenhower urgent/important matrix (source: "Sales prioritization matrix: a 3-step workflow for SDRs to set daily priorities"):

- **Tier 1 — Campaign priority:** before touching a reply, rank campaigns by acceptance rate, reply rate, ICP relevance, and recent trends; open campaigns scoring well on ≥2 of the 4 first.
- **Tier 2 — Reply priority:** a **4-tag system — Interested / Warm / Not Now / Not a Fit** (doubling as an SLA); handle Interested first, then Warm, schedule Not Now, archive Not a Fit. Tag-clarity rule of thumb: "if a new SDR can't tag a reply correctly in 10 seconds, it's not clear enough."
- **Tier 3 — Task priority (SLA by tag):** Interested → same-hour action; Warm → same-day; Not Now → scheduled nurture; Not a Fit → clean and move on.

Daily loop: "Review Tier 1 campaigns → Respond Interested → Respond Warm → follow-ups/cleanup. No inbox hopping." The speed rationale (third-party stats): replying to interested leads within 5 minutes boosts conversions 391% (ChiliPiper); after 15–30 minutes they're 21x less likely to convert (RevenueHero).

## HeyReach's own qualification result (first-party)

HeyReach's internal free-trial qualification system: qualify every signup → segment into tiers → Tier 1 & 2 to Customer Success (concierge), Tier 3 to self-serve marketing; data in HubSpot, enriched in Clay (run Apollo only for HubSpot-owned contacts to save credits; reach only Admins & Power Users, not Team Members) (source: "This lead scoring system doubled our conversion rate"). Claimed result: **free-trial-to-paid conversion doubled from 10% to 20%+** — a sibling source states the same result as **"from 9% to 21%"** (preserve both; the discrepancy is HeyReach's own) (source: "This lead scoring system doubled our conversion rate"; source: "Streamlining success: lead qualification process that gives 20% more conversions"). This also reveals HeyReach's own ICP tiers: lead-gen agencies, sales teams, and GTM experts.

## Summary

Lead scoring and qualification in the HeyReach canon runs on three layers: the **classic acronyms** (BANT/CHAMP/MEDDIC/ANUM/GPCTBA) as the deal-qualification vocabulary; **fit + engagement + intent tiering** operationalized as first-party **Hot/Warm/Cold** scoring (HOT ≥30% acceptance & ≥10% reply), the ABM **1–5 / Triple Threat** model, or GPT/Origami scoring feeding a **lead decision matrix**; and an **anti-ICP upstream gate** (4-point logic gate, 5-gate checklist) that disqualifies before the first message to protect deliverability. The **Sales Prioritization Matrix** (Campaign → Reply → Task tiers, 4-tag reply SLA) turns those scores into an SDR's daily order of work. Every threshold and result is self-reported.

## Related
- [[icp-and-targeting-systems]]
- [[signal-based-outbound-framework]]
- [[linkedin-outreach-benchmarks]]
- [[campaign-audit-and-diagnostics]]
- [[linkedin-follow-up-frameworks]]
- [[multichannel-outreach-architecture]]
