# LinkedIn Outreach Sequence Architecture

This article covers how HeyReach teaches you to **structure a LinkedIn sequence** — the steps, the conditional branches, the delays, the warm-up actions, and the built-in templates — as distinct from the copy inside each step ([[linkedin-message-formulas]]) and the LinkedIn+email version ([[multichannel-outreach-architecture]]). The governing thesis: **automating a weak sequence just fails faster at higher volume** — "Get the architecture right first. Then automate it" (source: "How to design LinkedIn and email outreach sequences that work together"; source: "Sales sequence automation: Fewer steps, more replies"). All timing/threshold numbers reflect the 2026 LinkedIn state and are HeyReach's own guidance.

## The 4-step high-converting sequence

HeyReach's canonical structure gives each step exactly one job (source: "Sales sequence automation: Fewer steps, more replies"):

1. **Connection request** — one job: a low-friction, credible reason to accept. **Not** the place to pitch or qualify. A personalized note usually beats a *generic* one, but an **empty request can beat a generic one** when the profile is strong / there's a mutual connection / shared community.
2. **Opener** — formula **[Specific observation] + [Relevant pain] + [Low-friction ask]**; the observation must be real (a hire, a post, a company announcement, a tech signal).
3. **Follow-up** — always add something **new** (a data point, a different angle, an insight); avoid "just checking in" / "circling back."
4. **Graceful exit** — say it's the last message, give an easy out, leave the door open; "generates more replies than expected."

The length rule: **longer ≠ better** — "A fifth extra step rarely recovers what a weak second step lost" (source: "Sales sequence automation: Fewer steps, more replies"). Break up after **2–3 unanswered follow-ups** (source: "How to set up LinkedIn drip campaigns that actually generate leads").

## Delays and pacing

Timing is a first-class design variable, not an afterthought:

- **Do not send the opener immediately after acceptance** — use a **24–48h delay**; "don't pitch slap" a new connection (a 3-day break is also cited) (source: "Sales sequence automation: Fewer steps, more replies"; source: "Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)").
- **3–5 days between follow-ups** (source: "Sales sequence automation: Fewer steps, more replies").
- A common post-acceptance move is a "thanks for connecting" message **~3 hours after acceptance** (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").
- Conditional logic gates each step: Step 2 fires only if accepted; Step 3 only if no reply after the window; the campaign auto-pauses on any reply (source: "Sales sequence automation: Fewer steps, more replies"; source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial").

## Warm-up actions inside the sequence

Because a send-only account is easy to flag ([[safe-linkedin-sending-limits]]), non-send actions are built into the sequence *before* the connection request so the account behaves like a human: **view profile → (optional) like/comment a recent post → follow → delay → connection request** (source: "How to CRUSH the New LinkedIn Algorithm in 10 Minutes"; source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool"). A frequently-shown "human-mimicking" order is **follow → like → blank connection request → 3h wait → message** (source: "Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)").

A documented example sequence produced 22.8% acceptance / 42.2% reply / 7 qualified leads (source: "5 LinkedIn best practices to accelerate growth"):
1. View profile (pop into notifications).
2. Send connection request (empty note).
3. If not accepted: re-view profile after 5 days, then auto-like most recent post 2 days later; if still not accepted, wait 5 more days and end.
4. If accepted: wait 1 day, send first message.
5. Emoji follow-up after 2 days if no reply.
6. Second follow-up 3 days after the first.

## Conditional branching

The core branch is **"If connection"**: HeyReach auto-detects whether the sender is already connected — if yes, send a message; if no, send a connection request (source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial"). From there, branches fork on **accepted / not accepted** and **replied / no reply**, with fallback actions (re-view, like, InMail, or hand off to email — see [[multichannel-outreach-architecture]]). Sequence type also matters: **connection-request-to-message performs best; InMail is for senior decision-makers** with lower acceptance (source: "Sales sequence automation: Fewer steps, more replies").

## Built-in templates and drip patterns

**Seven built-in sequence templates** (source: "How to set up LinkedIn drip campaigns that actually generate leads"): Partnership proposal, Engagement response sequence, Comment follow-up sequence, New connection nurture, Value-first outreach, Social proof sequence, Expand your network sequence.

**Three day-by-day drip templates** from the same source:
- **Template 1:** Day 0 connect w/ note → Day 1 strike conversation (pain point) → Day 3 light proof → Day 5 soft CTA → Day 8 follow-up.
- **Template 2 (active-on-LinkedIn):** Day 0 engage post → Day 1 connect → Day 2 continue → Day 5 add value → Day 8 proof + soft CTA → Day 12 follow-up.
- **Template 3:** Day 0 connect → Day 1 credibility → Day 4 relevance check → Day 7 soft CTA → Day 10 follow-up.

A widely-shared partner workflow (Sönke Venjacob, Platinum): **connection request → 2 days after acceptance like their recent post → 3 hours later send first message → 4 days later follow-up** (source: "The ultimate guide to drip campaigns").

Other named structures:
- **Connect / Value / Follow-Up blueprint + "Rule of 3"** (source: "LinkedIn Message Automation: The 2026 Guide to Automated LinkedIn Messaging").
- **Pattern-break sequence** — blank connection request → value-first, no-ask deck message → ~3-week gap → single minimal follow-up (source: "Scaling personalized LinkedIn outreach with automated pitch decks (44% higher reply rate)").

## Multi-sender relay

Sequences scale by distributing sends across multiple sender accounts (see [[safe-linkedin-sending-limits]]). Assign senders deliberately (source: "Sales sequence automation: Fewer steps, more replies"): by **seniority** (founder/VP → C-suite; SDR → director and below), **industry** (vertical-matched work history), and **region** (a UK sender → UK prospects). HeyReach dedupes and prevents overlapping sequences across senders at the campaign level. The "relay team" idea: each sender runs at human pace, but collectively they cover far more ground (source: "LinkedIn company expansion strategy: Grow and scale your outreach").

## Build-order rules

- **One goal per campaign** — don't stack onboarding + retain + upsell; space them into separate campaigns (source: "The ultimate guide to drip campaigns"; source: "How to set up LinkedIn drip campaigns that actually generate leads").
- **10–14 day timeline** for a multichannel drip (source: "The ultimate guide to drip campaigns").
- **A/B test one variable at a time** (connection note if acceptance is low; the post-connect message if reply is low) (source: "How to set up LinkedIn drip campaigns that actually generate leads").
- **Exclusions at campaign start** — exclude leads already contacted in another campaign, messaged by other senders, or previously contacted, so a lead never sits in two sequences (source: "How to set up LinkedIn drip campaigns that actually generate leads").

## The Sequence Builder

HeyReach's rebuilt canvas-based Sequence Builder starts with a choice of **"Build it your way" (blank canvas) or "Start with a template,"** shows delays visualized on the canvas, and includes a **live per-lead message preview with missing-data warnings** (so `{{first_name}}` doesn't render as "Hey there, ." in front of a dream account) (source: "Preview message + new Sequence Builder").

## Summary

A HeyReach LinkedIn sequence is a conditional, delay-paced tree: warm-up actions → connection request (blank by default) → a 24–48h pause → an observation-led opener → follow-ups that each add something new → a graceful breakup, branching on connected/accepted/replied and distributed across multiple rotated senders. Keep it short (a weak Step 2 can't be rescued by a fifth step), one goal per campaign, and exclude cross-campaign duplicates. The design principles are largely channel-agnostic; the vendor layer is that HeyReach executes and enforces them safely.

## Related
- [[linkedin-message-formulas]]
- [[multichannel-outreach-architecture]]
- [[linkedin-follow-up-frameworks]]
- [[safe-linkedin-sending-limits]]
- [[linkedin-outreach-benchmarks]]
- [[signal-based-outbound-framework]]
