# How HeyReach Reads Its Benchmarks

HeyReach leans on one recurring dataset — **its own ~96,051 LinkedIn campaigns** — to argue three interpretive points: getting *accepted* is easy but getting a *reply* is the hard part (only ~1 in 5 accepted connections replies), specific number bands tell you *what* is broken (targeting vs. messaging vs. offer), and there's a "6–20 senders" sweet spot for reply rate. This article is about how HeyReach *interprets* the numbers and where to be skeptical; the raw benchmark tables belong in [[linkedin-outreach-benchmarks]]. The essential caveat up front: this is **self-reported vendor data**, aggregated from HeyReach's own platform, not independently audited — and it's marshaled to support the exact behaviors (multi-account rotation, quality-over-volume) that HeyReach sells.

## The headline dataset (and its provenance)

Across the corpus the same figure recurs: "96,051 campaigns" (sometimes rounded to "96,000"). It anchors blog posts and videos alike — e.g., "Backed by 96,000 Campaigns" (source: "LinkedIn Growth Strategy: 8 Steps That Turn Connections Into Conversations (Backed by 96,000 Campaigns)") and the AI-agents deep dive (source: "Autonomous AI agents in B2B sales: What works and what quietly breaks"). One video even has the auto-caption garble the source as "Hiretual," almost certainly a mis-transcription of HeyReach naming its own data (source: "Is LinkedIn Outreach Worth It in 2026?"). Bottom line for readers: wherever a "96k-campaign" benchmark appears, it is **HeyReach's own aggregate**, credible as directional but not neutral.

## Reading #1: acceptance is easy, the reply is the wall

HeyReach's central interpretive claim is that the funnel breaks *after* acceptance. The typical campaign converts only "~1 in 5 (20%)" accepted connections into a reply, and "10.7% of campaigns with accepted connections got ZERO replies" (source: "Autonomous AI agents in B2B sales: What works and what quietly breaks"); the growth-strategy post frames the same funnel as acceptance ~21% / reply ~22% / reply-to-acceptance conversion ~18%, noting "80% of the people who say ’yes’ to connecting never hear from you again" (source: "LinkedIn Growth Strategy: 8 Steps That Turn Connections Into Conversations (Backed by 96,000 Campaigns)"). The reply-conversion figure is cited as 18% elsewhere too (source: "AI outbound workflows break after launch? Here's how to fix them"). The lesson HeyReach draws: stop celebrating acceptance and optimize the first message.

## Reading #2: the diagnostic bands — numbers tell you *what's* broken

HeyReach turns its benchmarks into a troubleshooting key rather than mere bragging. Its bands: acceptance ~21% average, >30% "great," <13% means "something is off," <10% is "LinkedIn's first flag"; reply ~22% typical, >33% "awesome" (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"). And crucially, the *combination* localizes the fault: under ~13% on both acceptance and reply signals an ICP/targeting problem, while a low reply rate with healthy acceptance signals a messaging problem (source: "LinkedIn Growth Strategy: 8 Steps That Turn Connections Into Conversations (Backed by 96,000 Campaigns)"), with "positive reply rate flat after a change → fix the OFFER" completing the triad. The KPI post adds pipeline-oriented targets — healthy acceptance 25–30%, positive reply aim 40%+ (below 8% signals weak messages), meetings 20–30% of positive replies — plus a scaling gate: "don't scale if acceptance <20% or reply <5%" (source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline").

## Reading #3: the "6–20 senders" sweet spot

The most-cited strategic interpretation is that reply rate peaks with a *moderate* pool of rotated senders. "6-20 senders with proper rotation = 25%" median reply, versus single-sender "22.22%" and "21-50 accounts = 21.94%" (source: "Autonomous AI agents in B2B sales: What works and what quietly breaks" and source: "How to manage multiple LinkedIn accounts without getting flagged"). This pairs with the single-account **reply-decay curve** — first 50 connections reply ~12%, next 100 → ~6%, next 200 → ~2% (source: "The Best AI LinkedIn Lead Generation Strategy for 2026") — to argue you should spread volume across accounts rather than push one. Note the range wobbles across sources: one video says the best campaigns run "between SIX and 27 accounts" rather than 6–20 (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes") — same dataset, slightly different cutoffs. HeyReach's "empty connection requests perform 5% better" also comes from this benchmark set.

## Reading #4: acceptance ≠ intent (don't trust vanity numbers)

A recurring interpretive warning is that a high acceptance rate can be meaningless. "LinkedIn acceptance rates don't equal buying intent," and "LinkedIn acceptance with no reply tells you nothing" (source: "Email vs LinkedIn message: Which one should you choose?"). This is the analytic backbone of the [[quality-over-volume-philosophy]] and the "chase pipeline, not activity" stance in [[is-linkedin-outreach-worth-it]] — the numbers to trust are positive-reply and meetings-booked, not connections-sent.

## Caveats HeyReach itself (partly) flags

- **Self-reported / not audited.** All 96k-campaign figures are HeyReach's own platform data. Where two sources disagree on the same metric, both are preserved here rather than reconciled.
- **Survivorship bias.** Older campaigns look far better — "<30 days = 13.33% acceptance / 14.29% reply; 180+ days = 26.99% / 28.26%" — but HeyReach concedes this is "partly survivorship bias" (bad campaigns get killed) and "correlation not cause" (source: "Autonomous AI agents in B2B sales: What works and what quietly breaks").
- **Internal inconsistency.** Sender-pool cutoffs (6–20 vs 6–27) and weekly limits (~100/week vs ~200/week) drift across HeyReach's own content — treat any single figure as approximate. See [[deliverability-and-ban-avoidance-beliefs]].
- **External corroboration exists but differs.** HeyReach also cites a Belkins study of "20M+ LinkedIn outreach" landing on ~30% acceptance / ~10% reply as "healthy" (source: "Find high-intent leads hiding in your campaign data") — a genuinely third-party benchmark, worth citing to Belkins rather than to HeyReach, and note its reply bar (~10%) sits below HeyReach's ~22% "typical."
- **Partner/agency numbers are testimonials.** Claims like "HeyReach partners report 35–40% average response rates" or "Tim Scheuer 45%" (source: "The only LinkedIn outreach agency checklist you actually need") are self-selected success stories, not the platform median.
- **Practitioner "millions analyzed" framings** (e.g., "1M Messages Analyzed," "5,000,000 DMs") are individual claims with undisclosed methodology (source: "Cold DMs That Actually Work in 2026 (1M Messages Analyzed)"; source: "LinkedIn DM Strategy: What Works After 5,000,000 Messages").

## Related
- [[linkedin-outreach-benchmarks]]
- [[quality-over-volume-philosophy]]
- [[signal-based-vs-spray-and-pray]]
- [[deliverability-and-ban-avoidance-beliefs]]
- [[is-linkedin-outreach-worth-it]]
- [[campaign-audit-and-diagnostics]]
- [[aggregate-creator-claims]]
