# The LinkedIn Outreach Benchmark Framework (96,051 Campaigns)

HeyReach's benchmark framework is built on its own aggregate campaign data — most prominently a **96,051-campaign dataset** — and turns raw acceptance/reply numbers into a diagnostic funnel with "typical / warning / strong" bands. The core insight repeated across every source: **getting accepted is not the hard part; turning an acceptance into a reply is** — "The sharpest performance drop occurs after acceptance" (source: "How to manage multiple LinkedIn accounts without getting flagged"). This article collects the benchmark numbers, the KPI definitions and formulas, and the reference ranges. **Every figure below is self-reported by HeyReach or its featured practitioners and is not independently audited** — cite it as HeyReach benchmark data, not neutral fact, and note that LinkedIn limits and rates drift year to year (all figures are current as of 2026).

## The 96,051-campaign funnel

HeyReach's headline dataset ("96,051 HeyReach campaigns," sometimes rounded to "96,000") produces a three-stage funnel where roughly **1 in 5 converts at each stage** (source: "LinkedIn Growth Strategy: 8 Steps That Turn Connections Into Conversations (Backed by 96,000 Campaigns)"):

| Metric | Typical (median) | "Warning" band | "Strong" band |
|---|---|---|---|
| Connection acceptance rate | 20.75% (~21%, "1 in 5") | below 13% | above 31.78% (~32–33%) |
| Reply rate | 22.22% (~22%, "1 in 5") | below 13% | above 33% |
| Reply-to-acceptance conversion | 18.1% (~18%, "1 in 5") | below 9.62% | above ~28% |

Sources agree on these figures: the acceptance 20.75% / reply 22.22% / conversion 18.1% numbers and the below-13% / above-31.78% acceptance bands and below-9.62% reply-to-acceptance threshold come from (source: "Sales sequence automation: Fewer steps, more replies"); the 21% / 22% / 18% "1 in 5" framing from (source: "LinkedIn Growth Strategy: 8 Steps That Turn Connections Into Conversations (Backed by 96,000 Campaigns)"); and the "acceptance ~21% average, >30% great, <13% something is off, <10% = LinkedIn's first flag; reply ~22% typical, >33% awesome" restatement from (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes").

Two "silence after acceptance" stats recur: **10.7% of campaigns with accepted connections got zero replies**, and roughly **15% converted fewer than 1 in 10** accepted connections into replies (source: "LinkedIn Growth Strategy: 8 Steps That Turn Connections Into Conversations (Backed by 96,000 Campaigns)"; source: "Sales sequence automation: Fewer steps, more replies"). "Not low replies — zero" (source: "Low reply rate on LinkedIn? Use RTA to find exactly what's broken").

### How to read the bands (the diagnostic rule)

The framework maps each band to a broken layer, so the numbers tell you *what* to fix (see [[campaign-audit-and-diagnostics]] for the full method):

- **Acceptance below ~13% + reply below ~13%** → ICP / targeting problem (fix the list).
- **Reply/reply-to-acceptance low with healthy acceptance** → messaging problem (fix the first message).
- **~21–22%** = typical; **above ~32%** = strong (tighter ICP, better sender profiles, sharper first messages).

(source: "How to manage multiple LinkedIn accounts without getting flagged"; source: "Sales sequence automation: Fewer steps, more replies")

## Sender count: the "6–20" sweet spot

From the same 96,051-campaign dataset, HeyReach reports that **campaigns run across 6–20 sender accounts have the highest median reply rate at 25.00%**, versus **22.22% for single-sender** campaigns and **21.94% for 21–50 senders** — i.e. more senders help up to a point, then plateau (source: "How to manage multiple LinkedIn accounts without getting flagged"; source: "LinkedIn company expansion strategy: Grow and scale your outreach"). A sibling video frames the same dataset slightly differently as best-performing campaigns running **"between SIX and 27 accounts"** — preserve the discrepancy; it is the same underlying data with a different cut (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes").

**Single-account reply decay** (why volume alone backfires): the first 50 connections from one account reply at ~12%, the next 100 at ~6%, the next 200 at ~2% (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"). This is the empirical case for the sender rotation in [[safe-linkedin-sending-limits]].

## Time and list-size effects

- **Account age curve:** campaigns under 30 days consistently underperform; acceptance climbs from **13.33% in the first week to 26.99% at 180+ days** (correlation, not proven cause) (source: "How to manage multiple LinkedIn accounts without getting flagged"; restated as "campaigns under 30 days consistently underperform" in source: "Sales sequence automation: Fewer steps, more replies").
- **List-size effect:** acceptance declines with volume, from **21.43% at the 50–100-lead tier to 19.35% at 1,000+ leads**, while reply rates stay broadly flat (source: "LinkedIn company expansion strategy: Grow and scale your outreach").
- **Empty vs noted connection requests:** empty connection requests perform **~5% better** per the 96,000-campaign benchmark (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"); a practitioner cites HeyReach data of **27% acceptance blank vs 22% with text** (source: "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)"). See [[linkedin-message-formulas]].

## The "millions of messages" datasets (practitioner-reported)

Beyond the campaign dataset, HeyReach and its guests cite large message-volume analyses. These are separate, differently-sourced claims:

- **1,000,000 cold DMs analyzed:** top performers get **reply rates above 20%**; InMail reply rate cited at **~11.4%** (source: "Cold DMs That Actually Work in 2026 (1M Messages Analyzed)"). Attribute the six scripts in that source to their named authors (see [[linkedin-message-formulas]]).
- **5,000,000 LinkedIn DMs sent** (HeyReach's flagship claim): benchmarks include **400–800 connection requests/month** per account (by warmth), **800 free InMails/month** to open profiles (~20% of profiles are "open") = up to **1,600 cold touches/month**; the Sales Navigator "Posted on LinkedIn" active-profile filter gives **2–4x higher acceptance** (can cut a 10K list to 2K); warm-signal outreach gives **~10x response**; acceptance benchmark **15–30% average** (e-commerce sub-10%, hospitality ~40%) (source: "LinkedIn DM Strategy: What Works After 5,000,000 Messages"; source: "I Sent 5,000,000 LinkedIn DMs: here's what you need to know").

## KPI definitions and formulas

The framework insists on tracking **pipeline-entry KPIs, not vanity metrics** (connections sent, profile views, messages sent, likes are "vanity") (source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline").

| KPI | Formula | Source |
|---|---|---|
| Connection acceptance rate | (Accepted ÷ Sent) × 100 | "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline" |
| Positive reply rate | (Positive replies ÷ Accepted connections) × 100 | "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline" |
| Meeting booked rate | (Meetings ÷ Positive replies) × 100 | "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline" |
| Reply-to-Acceptance (RTA) | (Replies ÷ Accepted connections) × 100 | "Low reply rate on LinkedIn? Use RTA to find exactly what's broken" |
| Click-to-Book | (Booked calls ÷ link clicks) × 100 | "Stop scaling too soon: a campaign audit framework that actually works" |
| Conversion rate | closed deals ÷ people reached out to | "How to set up LinkedIn drip campaigns that actually generate leads" |

**RTA** is singled out as the metric "most tools miss": it isolates messaging from targeting because reply rate is a "blended number." RTA benchmarks: **~18% typical, below ~10% weak, above ~28% strong** ICP-message fit; read it only with enough volume (patterns stabilize at ~100 accepted connections per campaign; A/B tests need ~50 accepted per variation) (source: "Low reply rate on LinkedIn? Use RTA to find exactly what's broken").

### The KPI hierarchy

One agency source organizes KPIs into a hierarchy (source: "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)"):

- **Inputs:** connections sent, InMails sent — aim **400–800/month per account**.
- **Leading indicators:** acceptance rate, messages sent, message replies, email replies, meetings booked.
- **Lagging indicators:** deals closed, revenue.

Levers to move each layer: raise **acceptance** with a less-salesy headline (a documented headline test moved acceptance **14% → 20%**), better filters, and removing the connection note; raise **reply** with an irresistible offer or a non-salesy question; raise **meeting-book** rate by giving a reason for the call (free audit/roadmap) (source: "Complete Guide to LinkedIn Automation to Get 10+ Clients Per Month (2026)").

## Reference "rule-of-thumb" ranges (not from the 96k dataset)

These looser benchmarks appear as rules of thumb and should be treated as starting points, not measured results:

- Healthy acceptance **25–30%**; positive reply rate **aim 40%+**, below 20% "not ideal," below 8% signals weak messages; meeting-booked **20–30% of positive replies** (source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline").
- Do **not scale** if acceptance <20% or reply <5% (source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline").
- **≥30% acceptance = scale-worthy; <20% = pause** (source: "Stop guessing which outreach campaigns work: Audit campaign performance and decide what to scale in 15 minutes").

### First-party vs third-party intent, and external benchmarks

HeyReach argues your own campaign data is **first-party intent** ("prediction, not proof" is its knock on paid intent tools), and uses acceptance/reply/meetings as the buyer-journey stages for a Hot/Warm/Cold model (see [[lead-scoring-and-qualification-frameworks]]) (source: "Find high-intent leads hiding in your campaign data"). Where it cites outside numbers, it attributes them:

- **Belkins 2024 LinkedIn outreach study**, 20M+ campaigns → **~30% acceptance and ~10% reply** as healthy (source: "Find high-intent leads hiding in your campaign data").
- **emailsearch.io** — 30% "average acceptance rate across B2B and digital marketing outreach" (flagged as industry-variable) (source: "Stop guessing which outreach campaigns work: Audit campaign performance and decide what to scale in 15 minutes").
- LinkedIn message reply rates "up to 10.3%" vs average cold email 5.1% (Wpromote / general); healthy acceptance 50%+ per Leadloft, reply 30%+ (source: "How to set up LinkedIn drip campaigns that actually generate leads").
- 89% of B2B marketers use LinkedIn for lead gen; 62% say it produces leads (Sprout Social) (source: "How to manage multiple LinkedIn accounts without getting flagged").

## Title-only and hype numbers (do not record as results)

Per HeyReach's own extraction discipline, a figure that appears only in a title and is not substantiated in the body is not a benchmark. The clearest example: **"60%+ reply rates"** is title framing — the strongest in-body examples are 42.2% and 40%, and the nearest 60%+ figure (66.7%) belongs to a separately-linked re-engagement case study (source: "LinkedIn lead generation strategy for 60%+ reply rates"). Likewise "10x" appears only in demo-video titles and is unsubstantiated in-body.

## Summary

HeyReach's benchmark framework converts acceptance, reply, and reply-to-acceptance into a diagnostic funnel anchored on a 96,051-campaign dataset (typical ~21% / ~22% / ~18%, warning below ~13% / ~9.62%, strong above ~32%), layers on a 6–20-sender "sweet spot" (25% median reply) and a single-account reply-decay curve (12% → 6% → 2%), and defines clean KPI formulas that separate targeting failures from messaging failures. All numbers are HeyReach- or practitioner-reported and vendor-sourced; the value is the *structure* — knowing which metric names which broken layer — more than the exact percentages.

## Related
- [[campaign-audit-and-diagnostics]]
- [[safe-linkedin-sending-limits]]
- [[linkedin-message-formulas]]
- [[lead-scoring-and-qualification-frameworks]]
- [[outreach-sequence-architecture]]
- [[icp-and-targeting-systems]]
