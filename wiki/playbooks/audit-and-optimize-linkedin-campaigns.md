# Auditing & Optimizing LinkedIn Campaigns

How to diagnose *why* a campaign underperforms and decide what to fix, scale, or kill — before you multiply a broken campaign across five accounts. The governing principle across the corpus: read the funnel top-down (acceptance → reply → positive reply → meeting) to isolate whether the problem is your **list**, your **message**, or your **offer**, and never scale a campaign that hasn't proven it converts, because "scaling a weak campaign doesn't fix it. It multiplies the damage" (source: "Stop scaling too soon: a campaign audit framework that actually works"). The benchmark numbers referenced here are HeyReach's own 96,051-campaign dataset (vendor-sourced, not independently audited) — see [[linkedin-outreach-benchmarks]].

## Track three pipeline metrics, ignore vanity metrics

Stop optimizing connections sent, profile views, messages sent, or likes. Track three metrics tied to pipeline entry (source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline"):

- **Connection acceptance rate** = Accepted ÷ Sent → tells you about **targeting**.
- **(Positive) reply rate** = Replies ÷ Accepted → tells you about the **message**.
- **Meeting-booked rate** = Meetings ÷ Positive replies → tells you about the **CTA/offer and speed**.

Note HeyReach doesn't track booked meetings natively — pull them from tagged Unibox replies or a CRM sync (source: "Stop guessing which outreach campaigns work: Audit campaign performance and decide what to scale in 15 minutes").

## The diagnostic tree

The most repeated diagnostic maps a symptom to the layer to fix (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"; source: "LinkedIn sales strategy: How to turn LinkedIn into your team's #1 pipeline channel"):

| Symptom | Root cause | Fix |
|---|---|---|
| Low acceptance + low reply | Wrong people | Fix the **list/targeting** first |
| High acceptance + few replies | Targeting fine, message weak | Fix the **first message** |
| Decent replies, few *positive* replies | Offer doesn't land | Fix the **offer** |
| Good acceptance + good reply + few meetings | Conversion problem | Clearer/lower-friction **CTA + faster response** |
| Everything decent but volume too low | Infrastructure problem | Add sender accounts (safely) |

Order matters: "get acceptance above ~25% before using [reply metrics]," and "never change copy until you've ruled out targeting and enrichment" (source: "Low reply rate on LinkedIn? Use RTA to find exactly what's broken"; source: "AI outbound workflows break after launch? Here's how to fix them"). Guest Stan's quick check: manually click through 50–100 people who accepted and verify their titles actually match your offer, since "99% of LinkedIn-based databases" return off-target role variations (source: "LinkedIn Outreach is About to Change Forever (and nobody even realises)").

## Use Reply-to-Acceptance (RTA) to separate targeting from messaging

Reply rate is a "blended number." **RTA = (Replies ÷ Accepted connections) × 100** isolates messaging from targeting; calculate it per campaign (Dashboard → select campaign → Export CSV; `=B2/A2*100`), and only read it with enough volume (~100 accepted for a stable signal, ~50 accepted per A/B variation) (source: "Low reply rate on LinkedIn? Use RTA to find exactly what's broken"). Three RTA patterns: low-and-flat across all campaigns (~<15%) = the opening message is failing → rewrite step 1 to anchor on one specific problem with a near-zero-commitment ask; RTA drops across a campaign's duration = weak follow-up sequence; RTA varies wildly across campaigns = an ICP-message fit problem (compare the audience filters of your top vs bottom performers). HeyReach's RTA benchmarks: ~18% typical, <10% weak, >28% strong.

## The 15-minute weekly audit (scale / optimize / pause)

A repeatable weekly audit turns raw percentages into next-week actions with a **3-band framework** — Scale (green), Optimize (yellow), Pause (red): export the CSV, note acceptance % and reply % per campaign, assign a band, add an action column. Decision thresholds used: **≥30% acceptance = scale; <20% = pause;** a bonus rule requires acceptance ≥30% AND reply ≥10% to scale (source: "Stop guessing which outreach campaigns work: Audit campaign performance and decide what to scale in 15 minutes"). "Stop funding losers because 'we need more time to see'" — run it manually for 3–4 weeks, then automate for 10+ campaigns via n8n.

## The 5-point pre-scale audit

Before scaling any campaign, score it 0–2 on five points (out of 10; **fix weak links before scaling if total <8**): (1) proof of conversion (benchmarks: 15%+ acceptance, 20%+ reply-to-acceptance, 1+ meeting per 50–75 sends), (2) angle resonance (do replies show intent/pain?), (3) CTA strength (soft early, firm later; measure click-to-book), (4) segment fit, (5) scalability readiness (warmed senders, reply system, clean handoffs) (source: "Stop scaling too soon: a campaign audit framework that actually works"). Red flags that mean "do not scale": <15% acceptance, reply-to-acceptance <20%, <1 meeting per 50 sends — because scaling then is "like stepping on the gas with your check engine light on," and you've just "spread the same silence across four reputations."

## Read the benchmarks correctly

HeyReach's 96,051-campaign benchmarks (median): **acceptance ~20.75% (weak <12.97%, strong >31.78%), reply ~22.22% (weak <13.37%, strong >33.33%), reply-to-acceptance ~18.1% (weak <9.62%, strong >28.89%)**, with **10.7%** of campaigns getting accepted connections but zero replies (source: "LinkedIn Message Automation: The 2026 Guide to Automated LinkedIn Messaging"). Two structural findings to fold into any audit: campaigns using **6–20 sender accounts** show the strongest reply rates, and **campaigns under 30 days consistently under-perform** — so give a campaign time and adequate sender spread before judging it (source: "LinkedIn company expansion strategy: Grow and scale your outreach"). External benchmarks differ (Belkins ~26% acceptance / 6–9% reply; ~30% acceptance / ~10% reply "healthy"), so calibrate thresholds to your own ICP rather than treating any number as absolute (source: "LinkedIn campaign monitoring that scales"; source: "Find high-intent leads hiding in your campaign data").

## Set baselines and catch drift early

Optimization is continuous, and outbound "doesn't break all at once. It drifts" — degrading gradually over 2–3 weeks with no error or alert (source: "AI outbound workflows break after launch? Here's how to fix them"). Build per-client/per-tier baselines from the last 4–8 weeks (Median / −10% watch / −20% action bands) and watch four leading metrics weekly: acceptance rate, reply rate, pending requests, daily send volume (source: "LinkedIn campaign monitoring that scales"). The 8 early-warning signs of drift and their fixes: acceptance drop → tighten ICP; reply *quality* declines (rising "not relevant") → ICP fix, (rising "not now") → timing/offer fix; message fatigue → rotate openers; pending-invite backlog → withdraw + lower pacing; sequence stalls early → warm-up steps consuming shared limits; reply latency spikes → daily Unibox routine; sender imbalance → normalize limits; CRM↔tool drift → one source of truth (source: "Why automation fails in sales sequences: 8 early-warning signs of outbound drift"). Use a green/yellow/red health model and "don't interrupt green" (source: "Why automation fails in sales sequences: 8 early-warning signs of outbound drift").

## For AI-driven campaigns: diagnose the right layer

When Clay/AI/HeyReach are stacked, "symptoms appear in HeyReach. Root causes live in Clay and MCP." Acceptance moves → check targeting/enrichment (Clay); replies move → check the AI's *inputs* (stale enrichment), not the copy — "healthy acceptance with low reply rate is almost never a copy problem"; personalization breaks (fallback/`{variable}` showing in Unibox) → check field mapping between the enrichment layer and HeyReach (source: "AI outbound workflows break after launch? Here's how to fix them"). A/B test one variable at a time with the winning metric defined upfront.

## Mine your own data for high-intent leads

Optimization isn't only fixing losers — it's harvesting winners. Your campaign data *is* first-party intent: acceptance = awareness, positive reply = interest, meetings = evaluation. Export, score leads Hot/Warm/Cold against benchmarks (Hot = acceptance ≥30% AND reply ≥10%), add a decay check (a 3-week-old "Hot" needs re-activation, not a standard handoff), and route AEs to Hot / SDRs to Warm / automation to Cold — first-party intent is "proof," not the "prediction" you buy from third-party intent tools (source: "Find high-intent leads hiding in your campaign data"). Routing and scoring detail is in [[qualify-and-prioritize-leads]].

## Related
- [[book-meetings-on-linkedin]]
- [[build-linkedin-campaign-sequences]]
- [[build-targeted-lead-lists]]
- [[write-cold-outreach-copy]]
- [[qualify-and-prioritize-leads]]
- [[manage-replies-and-inbox-at-scale]]
- [[scale-linkedin-outreach-safely]]
- [[linkedin-outreach-benchmarks]]
