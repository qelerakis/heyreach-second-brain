# Campaign Audit & Diagnostic Frameworks

These are HeyReach's frameworks for **reading a campaign's numbers and deciding what to fix or whether to scale** — the diagnostic counterpart to the reference numbers in [[linkedin-outreach-benchmarks]]. The unifying principle: **a low reply rate is a "blended number" that hides *which layer* broke, so scaling a weak campaign multiplies the damage** — "you have not scaled anything. You have spread the same silence across four reputations" (source: "Stop scaling too soon: a campaign audit framework that actually works"). Below are the named diagnostic models, from the simplest three-metric tree to full pre-scale audits. All thresholds are HeyReach's own 2026-era guidance and self-reported.

## The three-metric diagnostic tree

The foundational diagnostic maps each of the three core metrics to one broken layer (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"):

- **Low acceptance + low reply → wrong people → fix the LIST** (targeting).
- **High acceptance + few replies → targeting is fine → fix the FIRST MESSAGE.**
- **Positive reply rate flat after a change → fix the OFFER.**

So **acceptance rate reflects targeting, reply rate reflects the message, and positive reply rate reflects the offer/interest** — a "fix-diagnostic tree" repeated across the strategy videos (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"; the acceptance-then-message-then-offer split also appears in source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline"). See [[linkedin-outreach-benchmarks]] for the exact bands (<13% acceptance = targeting; reply-to-acceptance <9.62% = messaging).

## RTA and its three patterns

**Reply-to-Acceptance rate (RTA = Replies ÷ Accepted × 100)** exists specifically to separate targeting from messaging, and is read **per campaign, not blended** (source: "Low reply rate on LinkedIn? Use RTA to find exactly what's broken"). Read it only with enough volume (patterns stabilize at ~100 accepted per campaign; A/B needs ~50 accepted per variation). Benchmarks: ~18% typical, below ~10% weak, above ~28% strong. **Three RTA patterns and their fixes:**

1. **Low & flat RTA (below ~15%) across all campaigns** → the opening message is failing after connection → rewrite Step 1 to anchor on one specific problem (not a value prop or meeting ask); make the CTA near-zero-commitment.
2. **RTA drops across campaign duration** → the follow-up sequence is too weak → check sequence depth (fewer than 3 steps after acceptance is the likely gap; follow-ups must add a new angle).
3. **RTA varies significantly across campaigns** → an ICP–message fit problem → sort campaigns by RTA, compare audience filters between top and bottom performers, rewrite the opener's problem per ICP.

**Priority order:** fix targeting first if acceptance is low (get it above ~25% before using RTA), then Pattern 1 (highest-probability), then Pattern 3, then Pattern 2 last (source: "Low reply rate on LinkedIn? Use RTA to find exactly what's broken").

## The 6-point sequence diagnostic

A more granular "fix one place" tree for a broken sequence, keyed to the 96,051-campaign benchmarks (source: "Sales sequence automation: Fewer steps, more replies"):

| Symptom | Broken layer | Fix |
|---|---|---|
| Acceptance <13% | list quality / sender profile / connection note | fix targeting first |
| Reply-to-acceptance <9.62% with healthy acceptance | the first message after connection | extend delay to 24–48h; less pitch/ask too early |
| Low reply rate, reasonable reply-to-acceptance | volume / list | (campaigns <30 days underperform) |
| Low positive vs total reply | targeting/relevance | audit the AI icebreakers |
| Sharp drop after step 2 | weak follow-up | rewrite so it stands alone |
| Runs to completion, ~no replies | input/list problem | tighten the segment |

## The 5-point pre-scale audit

Validate a campaign **before scaling** with a 5-point score (0–2 each, out of 10; if total <8, fix the weak links first) (source: "Stop scaling too soon: a campaign audit framework that actually works"):

1. **Proof of conversion** — 0 no replies/meetings; 2 consistent replies + reliable booked calls. Benchmarks: 15%+ acceptance, 20%+ reply-to-acceptance, 1+ meeting per 50–75 sends.
2. **Angle resonance** — do replies show intent/pain vs ghosting/brush-offs (tag reply tone).
3. **CTA strength** — soft early (a question), firm later ("Book a 15-min call"); measure **Click-to-Book = (Booked calls ÷ link clicks) × 100**; A/B test.
4. **Segment fit** — compare across segments; enrich weak ones; run small batches first.
5. **Scalability readiness** — warmed/approved senders, reply-management system, clean handoffs, reusable messaging.

**Red flags = do not scale:** <15% acceptance (poor targeting), reply-to-acceptance <20% (messaging off — "gold" above 30%), <1 meeting per 50 sends. "Scaling at this stage is like stepping on the gas with your check engine light on." Clean-scale setup: 2–3 senders max, simple logic, add more senders only after the first batch works, review replies in batches of 10–15.

## The 15-minute 3-band audit

A repeatable weekly audit that turns acceptance + reply into next-week actions (source: "Stop guessing which outreach campaigns work: Audit campaign performance and decide what to scale in 15 minutes"):

- **4-step system:** (1) export clean CSV from the dashboard; (2) apply the **3-band framework — Scale (green) / Optimize (yellow) / Pause (red)**; (3) optionally let Claude/ChatGPT compare via MCP with copy-paste prompts; (4) automate with n8n for 10+ campaigns (structure: **Trigger → Fetch → Logic → Slack**).
- **Decision thresholds:** **≥30% acceptance = scale; <20% = pause;** bonus rule adds reply ≥10%. The momentum prompt flags an acceptance/reply drop >5 points or improvement >10 points.
- Advice: run it manually 3–4 weeks before automating; adjust thresholds to your ICP/industry. "Automation ≠ autopilot. That's how AI outreach gets its bad rep (and how LinkedIn accounts end up in timeout)."

## The Green/Yellow/Red outbound-drift model

A health model for catching "outbound drift" before it burns pipeline (source: "Why automation fails in sales sequences: 8 early-warning signs of outbound drift"):

- 🟢 **Green** — within baseline; monitor weekly, don't tweak.
- 🟡 **Yellow** — 1–2 signals slipping; optimize mid-sequence, refresh the opener, clean data before adding volume.
- 🔴 **Red** — multiple signals stacking; pause affected campaigns/senders, fix the root cause, resume with safeguards.

This mirrors the per-sender **Account Health Matrix** used for deliverability in [[safe-linkedin-sending-limits]].

## Baseline-band monitoring at scale

For agencies monitoring many senders (source: "LinkedIn campaign monitoring that scales"): the **Baseline band method** sets a per-metric baseline as **Median / −10% / −20%** and flags deviations; an **Account Health Scorecard** (Google Sheet) tracks Client, Seats, Acceptance trend, Reply trend, Invite backlog, and a Flag (OK/Watch/Action) with an owner and next action. External benchmarks it cites: the Belkins LinkedIn outreach study and the HubSpot 2024 Sales Trends Report.

## When to scale (the consolidated rule)

Across the audit sources the "green light to scale" thresholds cluster (all self-reported, era-bound):

- **Acceptance ≥30%** (Scale) / **<20%** (Pause) (source: "Stop guessing which outreach campaigns work: Audit campaign performance and decide what to scale in 15 minutes").
- **Acceptance 15%+, reply-to-acceptance 20%+ (gold >30%), ≥1 meeting per 50–75 sends** (source: "Stop scaling too soon: a campaign audit framework that actually works").
- **Don't scale if acceptance <20% or reply <5%** (source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline").
- "Think signal-first, not sender-first" — a weak campaign scaled just spreads the damage (source: "Stop scaling too soon: a campaign audit framework that actually works").

## Summary

Diagnose before you scale: use the **three-metric tree** (acceptance = list, reply = message, positive reply = offer), isolate messaging with **RTA and its three patterns**, run the **6-point sequence diagnostic** against the 96k benchmarks for step-level fixes, and gate scaling behind the **5-point pre-scale audit** and the **15-minute 3-band (Scale/Optimize/Pause)** review — with a Green/Yellow/Red drift model and baseline-band scorecards for ongoing monitoring. The consistent thresholds: acceptance ~30% and reply-to-acceptance ~20%+ before scaling; below ~13–15% acceptance means fix targeting first.

## Related
- [[linkedin-outreach-benchmarks]]
- [[safe-linkedin-sending-limits]]
- [[outreach-sequence-architecture]]
- [[linkedin-message-formulas]]
- [[lead-scoring-and-qualification-frameworks]]
- [[linkedin-follow-up-frameworks]]
