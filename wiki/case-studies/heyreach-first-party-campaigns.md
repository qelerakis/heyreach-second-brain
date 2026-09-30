# HeyReach's own campaigns (first-party, double COI)

These four case studies are campaigns **HeyReach ran on itself**, using HeyReach — so they carry a double conflict of interest (the vendor is both the subject and the promoter) and every number is self-reported by the HeyReach team. They are still useful: they reveal HeyReach's internal GTM (free-trial qualification, activation, and win-back), and several are co-built by the same Clay operator, **Macklin Buckler**. Treat all figures as claimed; samples are small; two of the four give **different framings of the same free-trial conversion result**, which is preserved below rather than reconciled.

## Free-trial lead-scoring system — doubled conversion 10% → 20%+

**Who:** **HeyReach** (first-party), built by its Clay expert **Macklin Buckler**, with the CEO and CMO setting the strategy in summer 2024 (source: "This lead scoring system doubled our conversion rate").

**Context & tactic:** The insight: "we shouldn't care about total number of free trials… [but] the total number of **qualified** free trials." Design: qualify every signup → segment into user tiers → **Tier 1 & 2 → Customer Success campaigns** (human-led/concierge onboarding), **Tier 3 → Marketing campaigns** (self-serve). Data lives in HubSpot → pushed to Clay for enrichment (run Apollo **only** for contacts with a HubSpot Account Owner to save credits; reach only **Admins & Power Users** on multi-user teams to avoid duplicate messages; a job-title-formatting GPT prompt). Outreach is multichannel — Smartlead (email) + HeyReach (LinkedIn) — with an if-connected split and an InMail fallback. A standout feature: **HeyReach API sender assignment**, where the sender automatically matches each lead's HubSpot owner ("One campaign, three senders, all automated") (source: "This lead scoring system doubled our conversion rate").

**Numbers (self-reported):** **Doubled free-trial → paid conversion from 10% to 20%+.** The LinkedIn arm: **99 requests, 47 accepted, 20 responses.** Cold email: **48 messages sent, 6 replies** (from one CS account; opens/clicks not tracked) (source: "This lead scoring system doubled our conversion rate").

**Notable / limits:** This piece also reveals HeyReach's own ICP tiers (lead-gen agencies / sales teams / GTM experts) and that larger agencies get concierge CS to discuss whitelabeling and custom API. Dates to summer 2024 (source: "This lead scoring system doubled our conversion rate").

## Free-trial activation campaign — conversion 8% → 16%

**Who:** **HeyReach** (first-party); colleague **Mrki / Nikola Siljanoski** QA'd and uploaded the list; **Vuk** contributed copy help (source: "LinkedIn outreach campaign targeting inbound leads (from 8% to 16% CR increase)").

**Context & tactic:** An activation campaign to convert free-trial signups. Upload only qualified signups → automated connection request **exactly one day after signup, with no note** → split on reaction: not accepted → wait 7 days, auto-like their freshest post, wait 4 more days, stop; accepted → wait 4 days (let them explore the tool) then a casual message "Hey hey {FIRST_NAME}, thx for accepting me! How's your HeyReach experience so far?" → on reply, the author personally converses to uncover pain points. Why it worked: didn't message brand-new signups; a personal account "put a face to the product"; didn't sell right away (source: "LinkedIn outreach campaign targeting inbound leads (from 8% to 16% CR increase)").

**Numbers (self-reported):** **162 connections sent; 104 accepted (64.1%); 83 messages sent; 21 replies (25.3%); conversion boost from 8% (December) to 16% (February)** — a doubling over two months (source: "LinkedIn outreach campaign targeting inbound leads (from 8% to 16% CR increase)").

**Caveats to preserve:** the author explicitly states "we deployed one or two conversion optimization strategies elsewhere," so the **8% → 16% lift is not solely attributable to this campaign**. Small sample (83 messages / 21 replies). The high **64.1% acceptance reflects warm inbound** (own signups), not cold outreach (source: "LinkedIn outreach campaign targeting inbound leads (from 8% to 16% CR increase)").

**Discrepancy to preserve:** the lead-scoring piece frames HeyReach's free-trial conversion win as **10% → 20%+**, this activation piece as **8% → 16%**. These are two overlapping-but-distinct initiatives (a scoring/tiering system vs an activation sequence) reported with different baselines — keep both, don't merge into one number.

## "Prequalify, don't pitch" — a 42% reply rate campaign

**Who:** **HeyReach** (first-party); team members "Mrki" (Sales Nav tips), "Vuk" (copy), and an intern "Viki" (replies) are named (source: "LinkedIn message automation: the playbook that got us a 42% reply rate").

**Context & tactic:** Sequence: view profile → **empty** connection request → split on accepted/not (not accepted → +5 days profile view, +2 days auto-like a post if newer than 24h, +5 days stop; accepted → wait 1 day then message 1). The message **prequalifies instead of pitching**: "Tnx for connecting {FIRST_NAME}! I'm curious to know if you guys offer LinkedIn outreach as a service." — agency owners reply to an inbound question about a service they provide, thinking they're talking to a customer. Follow-up 1 is a single emoji "👋" ("feels superhuman"), follow-up 2 asks for an answer. Targeting used the "Posted on LinkedIn" active-user filter and Boolean strings (source: "LinkedIn message automation: the playbook that got us a 42% reply rate").

**Numbers (self-reported):** **This campaign: 42% reply rate + 7 qualified demos** (a prior version got 22.8% acceptance, 42.2% reply, 7 qualified leads) (source: "LinkedIn message automation: the playbook that got us a 42% reply rate").

**Notable / limits:** Small demo count (7). This post is also the home of HeyReach's **96,051-campaign aggregate benchmarks** (≈22% reply, ≈21% acceptance, ≈18% of accepted convert to replies, ~1-in-10 campaigns get zero replies, 6–20 senders and >30-day runtime as the sweet spot) — those belong to the frameworks benchmark article, not as this campaign's result (source: "LinkedIn message automation: the playbook that got us a 42% reply rate").

## Win-back campaign — 67% reply rate re-engaging lost customers

**Who:** **HeyReach** (author = Head of Growth @HeyReach), co-built with **Macklin Buckler of Harochi** (harochi.io) — Harochi is an external agency COI (source: "How to re-engage lost customers [67% reply rate]").

**Context & tactic:** A win-back triggered by a specific event (a previously-missing feature being added). Fireflies call transcripts seeded the templates; **exclusion filters** removed anyone previously messaged (across the org), 1st-degree connections, and profiles without a picture. The 2-sentence connection message reminds them of the prior interaction and asks an open question; the follow-up, in a casual/emoji tone, **reveals the outreach came from an integration** as a hook ("I maaaaayyyyy have created an integration that took our call transcript from Fireflies and our Clay to write you our last message 😋 Wanna see how?"). Stack: HubSpot (data) + Fireflies (transcripts) + Clay + HeyReach (source: "How to re-engage lost customers [67% reply rate]").

**Numbers (self-reported):** **67% reply rate (66.7%): 42 connections sent, 24 accepted (57.5%), 24 messages sent, 16 replies (66.7%).** Lost-lead conversion is cited at **15–20%** (much higher than cold) (source: "How to re-engage lost customers [67% reply rate]").

**Limits:** The 66.7% is substantiated in-body but on a **tiny sample** (42 connections / 24 messages). "Send countless messages… while staying within LinkedIn's limits" is a vendor claim (source: "How to re-engage lost customers [67% reply rate]").

## Related
- [[engagement-signal-campaigns]] — HeyReach's own Trigify + Clay campaign (54% reply)
- [[website-visitor-outreach]] — HeyReach's own RB2B integration walkthrough
- [[recruiting-and-candidate-sourcing]] — reply-processing + scoring pipelines (in a hiring context)
- [[personalization-and-message-experiments]] — the blank-note practice these campaigns use
