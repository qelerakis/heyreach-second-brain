# Signal-Based / Trigger-Based Outbound Framework

Signal-based (a.k.a. trigger-based) outbound is HeyReach's most-developed framework family: instead of demographic guessing, you reach out **because something just changed** — "from 'who fits my ICP' to 'who fits my ICP and something just changed in their world'" (source: "Outbound ICP signals: How to spot high-intent leads before your competitors"). This article covers the signal taxonomies, the qualification gate, the decay/speed rules, and the routing/orchestration frameworks that decide which signal fires which campaign. The recurring warning: **"Most outbound teams don't have a signal problem. They have an orchestration problem"** (source: "Signal-based outbound: build a safe, scalable routing engine for LinkedIn outreach"). The tool-wiring (Clay/Trigify/RB2B → n8n/Make → HeyReach) lives in tools-and-automation; this is the decision logic. All figures are self-reported/illustrative and era-bound (2026).

## What counts as a signal (the taxonomies)

Three overlapping taxonomies appear across sources:

**The 3-type taxonomy** (source: "The ultimate guide to trigger-based outreach"): **Direct intent** (pricing-page time, webinar registration), **Social connectivity** (a power user changes companies = highest-converting trigger, call within the first 90 days; thoughtful competitor-post comments), **Silent signals** (usage drops, renewal/contract expirations, tech-stack shifts, hiring sprees).

**The "Big 5" high-intent signals** (source: "Outbound ICP signals: How to spot high-intent leads before your competitors"): (1) **Career move** — new hires/promotions (~90-day proving window; 3–6 months in they see what's broken, 7–10 months they can buy); (2) **Tech-stack shift** — capture *recency* (last 30 days = live; 8 months = irrelevant); (3) **Growth trigger** — funding + aggressive hiring, with specificity ("posted 4 SDR roles and a RevOps manager in the last 3 weeks"); (4) **Content signal** — engagement on authority/competitor/own posts; (5) **De-anonymized visitor** — pricing-page visit is the warmest, but "don't call it out" ("I saw you on our pricing page" feels invasive) — use it for timing/tone.

**The three-layer funnel** (by intent strength + urgency) (source: "Signal-led GTM engine: Playbook to turn signals into sales"): **Layer 1** ICP-driven outbound with signals layered on top (hiring, funding, expansion; higher volume, moderate urgency; email supported by LinkedIn); **Layer 2** intent-first signals (signal precedes ICP validation — content/event/ad/competitor engagement; higher urgency, timing-sensitive); **Layer 3** first-party/inbound (pricing visits, CRM reactivation, product-usage changes, trials; lowest volume, highest urgency → direct sales).

## The qualification gate

A signal alone doesn't justify outreach. **Gate every trigger with 3 questions** — real buying momentum? fits ICP? clear "why now?" — all yes, or don't fire (source: "The ultimate guide to trigger-based outreach"). The action-level mapping from the same source:

| Signal strength | Example | Action |
|---|---|---|
| Noise | generic "Monday Motivation" like | ignore |
| Low intent | follows company page | low-friction nurture |
| High intent | comments on a competitor's "bad service" post | immediate personalized outreach |
| Direct intent | visits "Book a Demo" and leaves | 5-minute "helpful peer" follow-up |

The recurring rule: **qualify ICP fit *before* drafting** — "Clay as the bouncer" filters revenue/headcount/tech stack first; "A lead with no intent signal is just a contact. Don't send to contacts" (source: "The ultimate guide to trigger-based outreach"; source: "Outbound lead qualification: Turn tough leads into unstoppable growth").

## Decay and speed

Intent **decays within 24–48h**, so route signals into live campaigns fast (source: "Route buying intent signals into LinkedIn campaign before they decay"). The "death zone" — a 24-hour delay between buyer intent and outreach — loses **up to 60% of potential lead value**; aim to hit the inbox within a **5-minute window** ("speed is strategy") (source: "The ultimate guide to trigger-based outreach"). Timing playbook: detection + enrichment 2–6h; import to HeyReach <12h; first touch live <24h (<1h for pricing-page visitors) (source: "Route buying intent signals into LinkedIn campaign before they decay"). Re-entry (job-change) leads respond at **2–3x the rate of cold** (same source).

## Brain & Muscle (execution design)

The "Brain & Muscle" framework (source: "The ultimate guide to trigger-based outreach"): the **Brain** (detect/qualify/decide) = a listening layer (Trigify) + verification layer (Clay); the **Muscle** (execute/scale/stay safe) = HeyReach's multi-seat auto-rotation + Unibox. "If you've got the muscle without the brain, you're just a sophisticated spammer." Paired rules from the same source: the **80/20 personalization formula** (80% muscle stays the same, 20% hook = the "why now"; see [[linkedin-message-formulas]]); the **"Big Brother vs Helpful Peer" tone rule** (position as a resource, not an observer); and the safety math **"100 messages from 1 account = likely ban; 10 messages from 10 accounts = safe"** (see [[safe-linkedin-sending-limits]]).

The **signal-message blueprint** ties it to copy: **[The Signal] + [The Relevant Problem] + [The Low-friction Ask]**, under two sentences — "One signal, one problem, and one ask. Everything else is noise" (source: "Outbound ICP signals: How to spot high-intent leads before your competitors").

## The Signal-to-Campaign 4-Tier framework

The end-to-end pipeline (source: "Route buying intent signals into LinkedIn campaign before they decay"): **Detect → Orchestrate → Filter → Execute.**
- **Tier 1 Detect:** Trigify (LinkedIn engagement + job changes), RB2B (website actions, strongest for US traffic), Clay (enrichment + freshness).
- **Tier 2 Orchestrate:** Make/Zapier for 1–2 signal types, n8n for complex multi-signal (conditional routing, scheduling, alerts, error handling).
- **Tier 3 Filter:** Claude connected to HeyReach via MCP classifies **QUALIFIED / NURTURE / REJECT**.
- **Tier 4 Execute:** HeyReach campaign management, seat rotation, tag analytics, Unibox.

The same source ships a **signal-to-action map** with four standardized tags (**Funding Event, Re-Entry Lead, High Intent Visit, Stale Signal**), per-workflow campaign configs, and **signal priority weights (Funding = 3, Re-Entry = 2, Visit = 1)**. It also gives a **3-layer noise filter**: Layer 1 Clay rules (firmographics, freshness reject >180 days, dedupe); Layer 2 optional MCP+Claude for gray-zone titles ("Lead"/"Manager") → QUALIFIED/NURTURE/REJECT + logged reason; Layer 3 HeyReach execution gates (includes/excludes, recency cooldown, seat rotation avoiding same-domain-to-same-seat, daily caps, auto-pause on reply). Signal-conversion example: Funding Event ~15% replies vs Website Visit ~4% (author "expected ranges," not verified).

## The routing engine (orchestration-first)

The most systematized version reframes signals as an orchestration problem: build a **unified control layer BEFORE LinkedIn execution** that must **Validate / Dedupe / Prioritize / Route / Pace / Monitor** — "Put your decisions upstream and your execution downstream" (source: "Signal-based outbound: build a safe, scalable routing engine for LinkedIn outreach"). Five orchestration applications:

1. **Signal Routing Matrix** (ICP × signal type → campaign) with priority + merge rules — the **highest-scoring signal wins** (a pricing-page visit outranks funding; "a demo request outranks a LinkedIn post comment every time").
2. **Validation & Dedupe "Quality Gate"** — check CRM for active opp/recent reply; enforce hygiene; dedupe vs active campaigns; gate leads missing required fields to a "Manual Review" bucket.
3. **Safety controls & throttling** — "execution capacity, not signal volume, determines your send rate"; release bursts in small randomized batches; per-seat daily limits; overflow-sender fallback.
4. **Queueing & orchestration** — buffer leads, check capacity at intervals, release only what's safe.
5. **KPI & monitoring** — tag every lead with its "Source Signal" to close the loop; track routing accuracy, time-to-contact, reply rate by signal, seat utilization.

Recommended architecture: **SIGNAL layer (Clay/Factors detect) → ORCHESTRATION layer (Make/n8n apply rules) → HeyReach layer (deliver safely) → FEEDBACK layer (Slack/CRM report).** "Automating a bad process only makes it fail faster"; "Scale follows control, never the other way around."

### Gatekeeper logic (the 4-check version)
A compact routing rule repeated in two sources: **Validate (usable data) → Dedupe (against active HeyReach sequences + CRM) → Prioritize (commercial intent decides intro) → Route (territory first, load second)** — the four checks before a lead reaches a sender (source: "Outbound ICP signals: How to spot high-intent leads before your competitors"; source: "LinkedIn company expansion strategy: Grow and scale your outreach").

## ILO, capacity budgeting, and build-your-own signals

- **ILO model (Identify → Leverage → Outreach)** for turning inbound signals into pipeline; success metrics = signal-to-first-touch time, reply rate by signal type, meeting rate per enriched signal (source: "Inbound-led outbound: Turn inbound signals into a predictable pipeline").
- **Per-signal capacity budgeting** — budget infrastructure *per signal*, not per campaign (5 signals × 200 accounts/mo = 1,000 accounts); email capacity from safe per-mailbox limits (15–20/day/mailbox); if a signal exceeds LinkedIn bandwidth, email becomes the primary entry with LinkedIn supporting (source: "Signal-led GTM engine: Playbook to turn signals into sales").
- **Build your own signals** for differentiation — combine public + first-party data (e.g. "companies that raised funding AND are hiring for the exact operational role your product supports" + behavioral confirmation) into a proprietary, hard-to-replicate signal set (source: "Signal-led GTM engine: Playbook to turn signals into sales").
- **Orchestration across teams** — tie ownership to signal strength + funnel position (first-party → sales within a window; Layer 1 → outbound teams); score leads on **3 dimensions (ICP fit × signal strength × potential value)** — see [[lead-scoring-and-qualification-frameworks]] (source: "Signal-led GTM engine: Playbook to turn signals into sales").

## Summary

Signal-based outbound reaches out *because something changed*: classify signals (direct/social/silent, or the Big 5, or the three-layer funnel), **gate each with "real momentum? fits ICP? why now?"**, act inside the 24–48h decay window (5-minute window for hot ones), and route via a **signal routing matrix** where the highest-scoring signal wins — all through an orchestration layer that Validates → Dedupes → Prioritizes → Routes → Paces → Monitors before HeyReach safely executes. The frameworks insist the hard part is orchestration and governance, not collecting more data; every conversion number is a self-reported "expected range."

## Related
- [[icp-and-targeting-systems]]
- [[lead-scoring-and-qualification-frameworks]]
- [[linkedin-message-formulas]]
- [[safe-linkedin-sending-limits]]
- [[multichannel-outreach-architecture]]
- [[campaign-audit-and-diagnostics]]
- [[linkedin-outreach-benchmarks]]
