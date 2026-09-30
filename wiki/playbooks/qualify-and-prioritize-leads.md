# Qualifying, Scoring & Routing Leads

How to decide who deserves outreach, in what priority, and who acts on them — before and around the campaign. The recurring principle: **qualify upstream, at the data level, before the first message** — because unqualified volume doesn't just waste effort, it "trains LinkedIn's algorithm to see you as a spammer" and burns sender accounts you don't get back (source: "Outbound lead qualification: Turn tough leads into unstoppable growth"). This covers pre-outreach qualification, lead scoring, routing/assignment, and the sales handoff; reply-triage inside the inbox is [[manage-replies-and-inbox-at-scale]] and campaign-level prioritization is [[audit-and-optimize-linkedin-campaigns]].

## Qualify before you send, not after

"Most teams optimize the wrong end of outbound" — the fix is a qualification layer upstream, so "a lead with no intent signal is just a contact. Don't send to contacts" (source: "Outbound lead qualification: Turn tough leads into unstoppable growth"). Start with the **anti-ICP** — define who to *exclude*. Red flags to remove immediately: stagnant/shrinking headcount (cost-cutting), a recent down-round or 18+ months without funding, a legacy tech stack with no integration path, a company recently locked into a competitor's contract, and "professional evaluators" engaging across 5+ competing tools (source: "Outbound lead qualification: Turn tough leads into unstoppable growth"). Quality over volume is the mindset — HeyReach's CMO Vuk: "we shouldn't care about the total number of free trials... [but] the total number of *qualified* free trials" (source: "Streamlining success: lead qualification process that gives 20% more conversions").

## Qualification frameworks (any of them can be automated)

The corpus repeatedly names the classic frameworks and maps them onto the stack: **BANT** (Budget, Authority, Need, Timeline), **CHAMP** (Challenges, Authority, Money, Prioritization), **MEDDIC** (Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion), **ANUM** (Authority, Need, Urgency, Money), plus HubSpot's **GPCTBA** for inbound — each automatable with HeyReach (reach decision-makers) + Clay (enrich needs/criteria) + Trigify (surface intent/timing) (source: "Streamlining success: lead qualification process that gives 20% more conversions"; source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline"). Qualification "shouldn't slow buyers down — it should speed them up" (source: "Streamlining success: lead qualification process that gives 20% more conversions").

## A 4-point pre-outbound gate

Run every lead through four checks before it enters a sequence (source: "Outbound lead qualification: Turn tough leads into unstoppable growth"):

1. **Firmographic fit** (headcount flat/growing — check Clay/Prospeo).
2. **Technographic synergy** (compatible tech stack).
3. **Timing & tenure** ("the most underused filter") — target decision-makers at the ~**7-month tenure** mark; Morgan J Ingram's "sweet spot window" (3–6 vs 7–10 months) is the framework version (source: "How to finally make buyer intent signals work for your outbound").
4. **CRM deduplication** — not already an open opp or worked by an AE (HubSpot/Pipedrive/Salesforce).

## Score leads on fit + engagement + intent

Score on more than firmographics — combine **fit** (ICP match), **engagement** (pricing-page visits, feature use, webinars) and **intent** (buying signals) into a tier (source: "Streamlining success: lead qualification process that gives 20% more conversions"). GPT-based scoring beats rigid rules — prompt an LLM to rank High/Medium/Low or 0–100 "based on company size, industry, job title, and tech stack," with an urgency modifier (site visit in 48h → Urgent), rather than "if job title contains VP, add 10 points" (source: "Lead scoring automation: stop letting good leads die in a spreadsheet"). Route by tier:

- **Tier A "sniper"** (great ICP + high engagement + a real trigger — the "Triple Threat"): 5–7 touches over 3–4 weeks, deep signal personalization, a manual video/voice note on touch 3–4, slower pacing (source: "Outbound lead qualification: Turn tough leads into unstoppable growth").
- **Tier B "nurture":** 3–4 touches over 5–6 weeks, content-forward, multichannel, no hard CTA until a micro-signal upgrades them.
- **Tier C:** hold/enrich; tag "check back in 6 months" and re-activate on a new signal.

HeyReach reports its own inbound qualification (HeyReach + Clay + Trigify, "capture then qualify") more than doubled free-trial-to-paid conversion — stated as both **10%→20%** and **9%→21%** across posts (note the internal inconsistency; a self-reported vendor result) (source: "Streamlining success: lead qualification process that gives 20% more conversions"; source: "LinkedIn lead generation strategy for 60%+ reply rates").

## Route leads to the right sender/campaign automatically

Three modular routing playbooks (built on HeyReach + an orchestration tool; wiring in [[partner-integrations-directory]]) (source: "Lead routing that scales: 3 playbooks to automate assignment, sync, and enrichment"):

1. **Account rotation:** new lead → check who was used last → round-robin → assign to the next sender → add to that owner's HeyReach campaign → update the sender log. Add a persona column to route by role (Sales → Sender A, RevOps → Sender B).
2. **CRM-to-outreach sync:** a form submit or CRM stage change immediately maps the lead's fields and adds them to a specific HeyReach campaign, with a Slack alert.
3. **Enrich before you outreach:** enrich for persona/firmographics → check ICP fit → route qualified leads to the right rep's campaign, non-fits to a fallback/"needs review" queue. Always build a no-data fallback path.

Territory logic (validate → dedupe → prioritize → route) resolves "one prospect, one sender" conflicts *in the data*, not in HeyReach, and the `assigned_sender` value must match the account label exactly or routing breaks (source: "LinkedIn company expansion strategy: Grow and scale your outreach").

## Sync lead status as signals, not logs

Treat CRM sync as signals that drive workflows, not passive activity logs, and prefer **one-way sync** (HeyReach pushes engagement, the CRM reacts) over two-way (which creates competing sources of truth) (source: "Lead status synchronization: How to align your CRM and outbound stack without friction"). Map four signals: lead enters campaign → "contacted" (don't infer intent early); connection accepted → "connected/warm" (access, not interest); **reply received → "engaged"** (the only signal that should trigger action — task the AE, create a deal, Slack alert); intent tag (positive/neutral/negative) → qualification. The critical setup detail: enable "auto-find missing email addresses," because no email = no contact created = "the #1 reason teams think their sync is broken," and agencies must connect the CRM **per workspace** to avoid cross-client data bleed. The biggest funnel drop is after acceptance, so time-to-first-reply is the clearest buying signal (source: "Lead status synchronization: How to align your CRM and outbound stack without friction").

## Prioritize the SDR's day

Daily SDR priority should be conversation-led, not inbox-led. The "sales prioritization matrix" runs three tiers: **campaign priority** (scan campaign health, work the strongest campaigns first — see [[audit-and-optimize-linkedin-campaigns]]), **reply priority** (tag replies Interested/Warm/Not Now/Not a Fit and work Interested first — see [[manage-replies-and-inbox-at-scale]]), and **task priority** (SLA by tag) (source: "Sales prioritization matrix: a 3-step workflow for SDRs to set daily priorities"). Standardize tags so tightly that "if a new SDR can't tag a reply correctly in 10 seconds, it's not clear enough." Lead scoring tells you *who* to contact; triage tells you *which reply to handle first* — different jobs (source: "Lead prioritization on LinkedIn: Respond to high-intent leads first").

## Nail the handoff (RACI + SLA)

Deals die in the handoff, so define ownership and SLAs per handoff point rather than generic frameworks — "forget '3-3-3 rules' or '5Cs.'" A RACI/SLA template: MQL→SDR (touch within 15 min, tag in Unibox), SDR→AE on an interested reply (AE loops in within 24h, post to a Slack handoff channel), AE→CS on closed-won (same-day Slack, CS kickoff within 48h, include "promise notes" = pricing/stakeholders/timeline), CS→AM on onboarding complete (source: "Sales handoff workflows: ready-to-run RevOps playbooks for lifecycle orchestration"). Speed-to-lead SLA bands (first *human* touch): inbound form ≤5 min, LinkedIn reply ≤15 min, referral ≤60 min, with escalation timers — "the fastest responder gets the conversation, and usually the close" (source: "Sales follow-up workflows: Speed-to-lead benchmarks & SLA templates that win deals").

## Related
- [[manage-replies-and-inbox-at-scale]]
- [[audit-and-optimize-linkedin-campaigns]]
- [[signal-based-outreach]]
- [[build-targeted-lead-lists]]
- [[book-meetings-on-linkedin]]
- [[agency-client-onboarding-and-reporting]]
- [[ai-personalization-at-scale]]
- [[lead-scoring-and-qualification-frameworks]]
