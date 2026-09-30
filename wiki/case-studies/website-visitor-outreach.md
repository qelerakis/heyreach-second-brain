# Website-visitor de-anonymization → LinkedIn outreach

Two HeyReach playbooks turn anonymous website traffic into named LinkedIn outreach using **RB2B**, which maps individual (not just company-level) **US** visitors to their LinkedIn profiles and pushes them, via webhook, into a HeyReach campaign. The pitch is that a pricing- or case-study-page visit is a fresh, high-intent signal you can act on the same day. Both pieces are HeyReach's own content and are as much a walkthrough of the RB2B ↔ HeyReach integration as a measured case study — hard campaign-result numbers are thin, and the reply rates that do appear are from the author's *prior* campaigns. RB2B is **US-only** due to GDPR/global privacy constraints. Treat everything as self-reported.

## Taylor Haren — tiered intent-based outreach for RB2B

**Who:** **Taylor Haren**, who runs "creative outbound to generate consistent revenue for RB2B (his client)." Because RB2B is his client and the featured tool, **RB2B is the COI**; the reply rates quoted are from his prior RB2B work, not this exact template. HeyReach narrates in the first person around his method (source: "Identify high-value website visitors").

**Context & tactic:** RB2B identifies individual US visitors and enriches contact details (incl. email) via "waterfall enrichment"; on a match it webhooks the data to **Clay**, which segments/enriches by action + buying intent and routes to LinkedIn (HeyReach) + email (Smartlead). Data is enriched **twice** — once in RB2B, again in Clay — "giving you a unique outreach advantage." Taylor's worked example (an events/certifications/memberships org) tiers visitors by the pages they saw:

| Tier | Trigger | Email cadence |
|---|---|---|
| Tier 1 (High-value) | Event, Certification, or Membership/Teams pages (or target-account sponsors) | 3 emails |
| Tier 2 (Medium) | Any 'other' page **and** Enterprise Target Account / on Sponsors list | 2 emails |
| Tier 3 (Low) | Any 'other' page | 1 email |

The LinkedIn arm (HeyReach): like a recent post → view profile → **blank** connection request → first message (+ optional follow-up) → if not accepted, view profile once more, then stop ("so I don't spam people"). Tier 2 runs through Smartlead cold email; subject-line pattern "[FIRST NAME] Visited [YOUR COMPANY NAME]" (source: "Identify high-value website visitors").

**Numbers (self-reported):** **40% and 54% reply rates** — explicitly from the author's **prior** RB2B campaigns, not this specific template. The final campaign results were shown in a linked webinar and are **not quantified in the text** ("Cha-ching!") (source: "Identify high-value website visitors").

**Their conclusion / limits:** Tier by intent rather than blasting everyone; double enrichment is the edge. But this is a how-to workflow with an example org's tiers, not a single measured case; RB2B is US-only.

## HeyReach's own RB2B integration walkthrough

**Who:** **HeyReach** (first-party), promoting its **native RB2B ↔ HeyReach** integration — a double COI, and the sample messages literally pitch the integration (source: "Send personalized LinkedIn messages to your website visitors").

**Context & tactic:** RB2B identifies the LinkedIn profiles of your visitors in real time (and can push them to Slack). In RB2B, filter by company size, job titles, pages visited, company revenue, and region, then fire a **webhook** on a qualifying lead so it flows straight into a HeyReach campaign (the author runs two campaigns for two ICPs). HeyReach sequence: connection request with a personalized note ("Thanks for visiting HeyReach. Let's connect if you are interested to learn about this integration") → on accept, a message 3 hours later pitching the RB2B integration. A planned refinement: if the request isn't accepted, view the profile + engage a recent post to appear in notifications "without breaking any LinkedIn limits whatsoever" (source: "Send personalized LinkedIn messages to your website visitors").

**Numbers:** **None given** — the page refers to "instant results like this" shown in an image but records no metrics. "Without breaking any LinkedIn limits whatsoever" is a HeyReach **safety claim**, not a measured result (source: "Send personalized LinkedIn messages to your website visitors").

**Their conclusion / limits:** Website-visitor identification is framed as "one of the quickest and most profitable inbound-led strategies." Qualify before reaching out. No benchmark numbers; US-only under GDPR.

## Note
Website-visitor de-anonymization also appears inside a broader multichannel stack: Gilbert Kralinger uses RB2B alongside HubSpot job-change monitoring and Teamfluence — see [[multichannel-linkedin-email-campaigns]]. HeyReach's blog also lists de-anonymized visitors (via Midbound) as one of its "Big 5" buying signals — see the buying-signal framework (source: "Outbound ICP signals: How to spot high-intent leads before your competitors").

## Related
- [[buying-and-intent-signal-campaigns]] — visitor de-anon as one intent signal among many
- [[multichannel-linkedin-email-campaigns]] — RB2B inside a fuller LinkedIn + email stack
- [[heyreach-first-party-campaigns]] — other HeyReach-run campaigns
- [[personalization-and-message-experiments]] — blank connection requests and no-ask openers
