# Website-Visitor Identification (RB2B, IntentStream, Factors AI)

Turning anonymous website traffic into LinkedIn outreach — de-anonymize who visited, then push ICP-matching visitors into a HeyReach campaign while intent is fresh. HeyReach's framing: "Most companies obsess over driving traffic, then do nothing with it," and this inverts the raise-your-hand model by reaching people who showed intent by *visiting*, before they consciously engage — "That timing advantage is significant" (source: "How to turn website visitors into leads using RB2B and HeyReach"). This article covers RB2B (the primary partner), IntentStream, Factors AI, and the routing/enrichment/privacy mechanics. All sources are HeyReach's own blog/webinar (COI); the numbers are self-reported and often small-sample. This is the wiring companion to the campaign-side [[website-visitor-outreach]].

## RB2B (person-level de-anonymization)

RB2B places a tracking script that matches a visitor session to a real person — name, company, LinkedIn profile, business email — normally into a Slack channel; the play is to push them to HeyReach instead (source: "How to integrate HeyReach with RB2B and reach your website visitors on LinkedIn automatically"). **Two build options** (source: "How to turn website visitors into leads using RB2B and HeyReach"):
1. **Native RB2B→HeyReach integration** — push identified visitors straight into ONE LinkedIn campaign, no middleware, fast, but no intent segmentation (everyone gets the same message).
2. **n8n workflow** — a webhook listens for RB2B events; a **switch node routes by tag** to different HeyReach campaigns with intent-calibrated messaging.

**Intent layering** drives the routing: define **hot-lead** criteria (job title, company size, seniority) AND flag **hot pages** (pricing, demo, case studies); three segments result — hot lead only, hot page only, and hot lead + hot page (highest priority) (source: "How to turn website visitors into leads using RB2B and HeyReach").

**Setup via Zapier** (the simplest bridge): grab the RB2B webhook URL → Zapier "Webhooks by Zapier" trigger → HeyReach "Add Lead to Campaign" action (needs the HeyReach API key) → map fields (name, company, title, LinkedIn profile, and the page visited → a HeyReach custom field for personalization) → a simple campaign, e.g. "Hey [Name], I noticed you visited our website. Let's connect!" (source: "How to integrate HeyReach with RB2B and reach your website visitors on LinkedIn automatically"). RB2B focuses on **US visitors only**. First-test numbers (April 2024, unoptimized, small sample): 336 connection requests to identified visitors → 72 accepted (21% acceptance) → 10 replied on follow-up (14%) — "I'm not going to pretend these results are mind-blowing" (same).

## Adding email + enrichment to the RB2B routing

Extend RB2B routing with the native HeyReach↔Instantly two-way integration and FullEnrich (source: "How to turn website visitors into leads using RB2B and HeyReach"):
- **Business email** → Instantly campaign (same tag-based switch); **Gmail/personal** → skip email, route to LinkedIn ("hitting a personal inbox about a B2B offer damages trust"); **no email** → enrich first.
- **FullEnrich** takes the LinkedIn URL (RB2B almost always has it), processes async, and fires a webhook back with the enriched contact (incl. phone).
- **Data persistence:** enrichment loses the original tag data, so store incoming leads in n8n's built-in **Data Tables via UPSERT** (unique key = LinkedIn URL), then re-query and merge the tags back so the branches reunite at the switch node with context intact.

## The RB2B × HeyReach webinar plays

A joint webinar with RB2B's founder Adam Robinson and HeyReach's Nick (CEO) and Ilia (Head of Revenue) adds tactics (attribute to the named speakers; vendor co-marketing) (source: "Send personalized LinkedIn messages to your website visitors [HeyReach - RB2B Webinar]"):
- **Ilia's flow** — run ONE campaign across ~4 LinkedIn accounts (round-robin), and don't message from the top: start with a profile **FOLLOW → 3h later a connection request** ("hey [first name] thanks for visiting HeyReach let's connect") → if accepted, 3h later a short message; add **2 pre-touches (follow, then next-day like)** before the connection request → "around 55% more people accept"; re-engage visitor audiences within 3–5 days. Setup: RB2B pixel → RB2B fires to Slack + a HeyReach campaign webhook (HeyReach campaign → Integrations → RB2B → select campaign → copy URL → paste into RB2B → test → 200).
- **RB2B "hotlist"** — label by company size / role so only matching visitors enter the LinkedIn campaign; Ilia's "RB2B seniority" campaign hit ~65% reply rate (single sender, ~15–20 responders — small sample).
- **Adam's 60-day "parasocial" play** (via his consultant Alec) — build a 2–3 year TAM, send 10/day scaling to 20–30 connection requests/day, no-pitch "how's it going at [company]?" on accept, post daily so they see your content, then ask for the call after ~60 days / 15–20 touches → "~80% accept rate."
- **Messaging rules** — Nick: connection requests get NO note; first message = quick intro + how-I-found-you + pain + solution + a "how can I help / hop on a call" CTA. Ilia: never copy email copy to LinkedIn; make it **challenge-oriented** ("this is a challenge we solve… is this a problem for you?").

RB2B billing: 1 credit per uniquely resolved profile per monthly period (unresolved visits free); it can map ~70% of visitors (source: "Send personalized LinkedIn messages to your website visitors [HeyReach - RB2B Webinar]").

## IntentStream (identity resolution + DSP)

IntentStream resolves anonymous visitors via a **200M+ B2B identity graph** and activates the same audience across paid social, programmatic (its own DSP), and LinkedIn — a "multichannel squeeze" (source: "HeyReach + IntentStream integration guide"). Setup: HeyReach → Settings → API → copy key (plan must include API access) → IntentStream → HeyReach → paste key → build an **Audience** filtering behavioral signals (pages, time on site, repeat visits) + firmographics → Activate → choose destination (Push to campaign = immediate entry; Push to lead list = QA first) → choose sync mode (On-demand snapshot vs Continuous). Pro tip: start narrow — pricing/product-page visitors respond far better than blog visitors; it cautions continuous sync can flood LinkedIn account health, and identity resolution "isn't perfect" (review a sample first).

## Factors AI (intent-triggered, Apollo-enriched)

Factors triggers workflows on website-visitor behavior, CRM updates, or product-usage data, with Apollo supplying enrichment (source: "How to integrate HeyReach with Factors AI"). Setup: Factors → Workflows → New → pick a HeyReach template ("Add leads to HeyReach List" or "…Campaign," both include Apollo enrichment) → Connect HeyReach (API key) → choose Lead List or Campaign → pick a trigger event ("Performs an event" / "Enter a segment" / "Exit a segment") → configure Apollo → launch. Flow: Factors captures → Apollo enriches → pushes into HeyReach.

## Privacy & compliance

Visitor tracking requires a **privacy-policy update and an opt-out** (source: "How to integrate HeyReach with RB2B and reach your website visitors on LinkedIn automatically"). Don't email personal/Gmail addresses about a B2B offer, and treat continuous-sync volume against LinkedIn's daily limits — see [[safe-linkedin-sending-limits]]. Other de-anonymization tools named in HeyReach content: Clearbit Reveal, Leadfeeder, and Warmly (source: "Outbound automation tools: What works and what you’re probably doing wrong"; source: "Your CRM is only as good as your data: Best B2B data enrichment tools in 2026").

## Related
- [[website-visitor-outreach]]
- [[signal-and-intent-integrations]]
- [[data-enrichment-tools-and-providers]]
- [[multichannel-email-and-ai-copy-integrations]]
- [[n8n-automation-workflows]]
- [[zapier-albato-and-other-orchestrators]]
- [[automation-workflow-templates]]
- [[ai-outreach-agent-architecture]]
- [[safe-linkedin-sending-limits]]
- [[signal-based-outreach]]
