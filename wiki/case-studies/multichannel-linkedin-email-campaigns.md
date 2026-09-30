# Multichannel campaigns (LinkedIn + email together)

These three playbooks run LinkedIn and cold email as one coordinated motion, usually with HeyReach as the LinkedIn arm and Smartlead as the email arm, orchestrated through Clay and (via Make/Zapier) de-duplicated so a prospect isn't hit twice. Two of the three lean on lookalike/de-anonymization sourcing; all three are heavy-stack builds. Each is on HeyReach's own playbook library and features a practitioner using their own tool or agency (COI noted). Numbers are self-reported and unverified.

## Vicky (Ocean.io) — 41 meetings from a lookalike-account motion

**Who:** **Vicky**, a self-described "former BDR" associated with **Ocean.io** (Ocean and HeyReach "share many mutual users") — Ocean is her tool/COI (source: "41 meetings booked with lookalike company search").

**Context & tactic:** Foundation = a targeted account list + 2–3 contacts per company. Take your top 5 customers in a niche (with case studies/testimonials) → generate **lookalike accounts** in **Ocean.io** → find 2–3 contacts each. Her manual cadence combines channels: connection request without a note → on accept, a LinkedIn **voice** message → next day a **2-minute personalized video** tailored to the company → if the connection isn't accepted, the video goes first via email (HubSpot cadence) → follow-up email with another video → phone call → final email. HeyReach's automated version: Ocean → Clay + GPT to fill a self-updating `[DREAM OUTCOME]` tag → HeyReach LinkedIn campaign (voice **converted to a text note**, multiple copy variations A/B'd) → Smartlead for email, routed via Make/Zapier to avoid duplicate messaging (source: "41 meetings booked with lookalike company search").

**Numbers (self-reported):** **41 meetings booked from 97 replies; 173 connection requests → 97 accepted & engaged (~56% acceptance).** The video step is a 2-minute personalized video. LinkedIn was her most effective channel (source: "41 meetings booked with lookalike company search").

**Their conclusion / limits:** Video wins because "I can convey tone, emotion, and enthusiasm." **Product limitation noted:** voice notes can't be automated in HeyReach, so they're converted to a text note. The automated build-out is HeyReach's recommendation layered onto Vicky's manual method.

## Gilbert Kralinger (Enablement.ch) — 8% conversion via "4 golden rules"

**Who:** **Gilbert Kralinger**, COO of **Enablement.ch**, which helps sales teams scale revenue with AI/automation "without hiring more people" — his firm is the COI (source: "How Gilbert achieved 8% conversion rate in B2B outreach").

**Context & tactic:** His "4 golden rules": (1) **Targeting** — Sales Navigator + Ocean.io + Bardeen + Apify, plus Claude AI to create/repurpose LinkedIn posts and LinkedIn Ads to amplify winners; (2) **Timing** — catch high-intent moments via RB2B (visitor de-anon), HubSpot (job changes), and Teamfluence + its "Lead Harvest" (network engagement); (3) **Qualification** — every trigger webhooks into Clay, enriched with Apollo + Clearbit and waterfall email, then gated by an "ICP?" column **and** a "Persona fit?" check — outreach launches only when both are positive; (4) **Personalization** — LinkedIn via HeyReach, email via Smartlead, with AI turning signals into personalized sentences (and translating into local languages, e.g. German) (source: "How Gilbert achieved 8% conversion rate in B2B outreach").

**Numbers (self-reported):** **8% conversion rate**, stated as "significantly outperforming the industry standard of 1-3%." This is the **only** metric given (source: "How Gilbert achieved 8% conversion rate in B2B outreach").

**Benchmark caveat to preserve:** "8% vs 1–3% industry standard" is a practitioner claim with **no supporting volume or denominator** — treat it as a claimed conversion figure, not a verified benchmark. Very heavy multi-tool stack.

## Gunner Park (Brij) — 60% reply rate in ecommerce/CPG

**Who:** **Gunner Park** of **Brij** (brij.it), which builds ecommerce/CPG "digital experiences" (rebates, sweepstakes, product education) — his company is the COI. Campaigns run off the posts of Brij's CEO **Kait Stephens**, and Brij's inbox is managed as her (source: "How Gunner from Brij uses multichannel outbound to hit a 60% reply rate").

**Context & tactic:** An eight-step ecommerce workflow. **Trigify** captures people engaging with Kait Stephens's posts (a warm audience) → **Clay** cleans/qualifies (ClayAgent + OpenAI eligibility check; a revenue hack that Google-scrapes company ZoomInfo profiles instead of paying ZoomInfo; waterfall email via Apollo) → **RB2B** adds US website visitors enriched with growth signals → three segments (**CPG, Durable Goods, Baby Goods**) each with dynamic same-vertical social proof ("We've helped brands like [Carawa] and [Canopy]"). LinkedIn runs as **three parallel HeyReach campaigns**, one per segment, with three connection-note templates (Industry Focus / Event-Based / Collaboration); one follow-up sends the same copy whether accepted (as a DM) or not (as an InMail). Cold email runs through Smartlead. HeyReach's **Unibox** is heavily featured — Gunner replies to every lead **as Kait, from one place**, "without having to log in and out of different LinkedIn accounts" (source: "How Gunner from Brij uses multichannel outbound to hit a 60% reply rate").

**Numbers (self-reported):** **Reply rates of 60% and 23% across two campaigns.** Email proof points cited are **Brij's client results, not HeyReach results:** Chamberlain Coffee brought in over $50,000 via in-store sweepstakes; Health-Ade captured 40,000+ emails through paid-media sweepstakes (source: "How Gunner from Brij uses multichannel outbound to hit a 60% reply rate").

**Their conclusion / limits:** Warm, engagement-sourced audiences + dynamic same-vertical social proof drive the high reply rates; the lookalike feedback loop makes it "an infinite loop." The page carries an explicit "register free, no card required" CTA (vendor promotion), and the 60%/23% are from a warm audience.

## Cross-study notes
- **Dedupe across channels** (Make/Zapier, or Clay/CRM blacklists) is a recurring must so LinkedIn and email don't double-hit a prospect.
- **Warm sourcing recurs:** Vicky (lookalikes of existing customers) and Gunner (the CEO's engagers) both start warm, which lifts the reply/acceptance numbers.
- The **Unibox** is the multichannel reply-management layer — covered in the product-and-positioning category's unified-inbox notes.

## Related
- [[engagement-signal-campaigns]] — Trigify engagement sourcing (Gunner starts here)
- [[website-visitor-outreach]] — RB2B de-anon (used by Gilbert and Gunner)
- [[buying-and-intent-signal-campaigns]] — the timing/trigger layer
- [[personalization-and-message-experiments]] — personalized video/deck first touches
- [[heyreach-first-party-campaigns]] — HeyReach's own multichannel free-trial work
