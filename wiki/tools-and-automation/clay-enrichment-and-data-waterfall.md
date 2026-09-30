# Clay Enrichment & the Data Waterfall

Clay is the enrichment "control layer" or "GTM command center" that HeyReach pairs with most often — the reasoning/data half of the [[ai-outreach-agent-architecture]] that decides *who* to contact and supplies the *data* to personalize, while HeyReach executes. HeyReach's core enrichment thesis: outreach failure "is not a messaging issue. It usually turns out to be a data problem," so shift from "list → sequence → hope" to "data → signals → automated outreach → real conversations" (source: "Automated data enrichment: Fueling high-scale LinkedIn outreach"). This article covers the data-waterfall pattern, Clay as the control layer, the native Clay→HeyReach integration and its variable rules, Claygent, and credit control. Clay is a HeyReach integration partner (COI on both sides).

## The data waterfall

Because no single provider has full coverage, you **sequence multiple providers** as a waterfall. HeyReach's five steps (source: "Automated data enrichment: Fueling high-scale LinkedIn outreach"):

1. **Source** — raw lead input (LinkedIn profile, Sales Nav export, or a trigger-based lead like a new hire/funding).
2. **Validate** — clean/verify basics (valid LinkedIn URL? company exists? key fields present?) to avoid wasting credits.
3. **Enrich** — layer sources: one for firmographics, another for tech stack, another for hiring/growth signals.
4. **Qualify** — filter on signals (only keep companies hiring SDRs / using a specific tool / with a key signal).
5. **Route** — push the qualified lead straight into a HeyReach campaign (no manual export).

The waterfall recurs everywhere in the stack: Bitscale chains "email finder → phone → tech stack → firmographics" skipping to the next provider on empty (source: "HeyReach + Bitscale: Turn signals into LinkedIn outreach, automatically"); the enrichment-tools roundup calls waterfall enrichment the "recurring technique" (source: "Your CRM is only as good as your data: Best B2B data enrichment tools in 2026"). See [[data-enrichment-tools-and-providers]].

## Clay as the control layer

Build the enrichment engine in Clay: start with a table (Sales Nav profiles, trigger-captured leads, existing data); **each column is a waterfall step**; connect 50+ data sources in one workflow; add **conditional logic** (only enrich if it matches ICP / a field is missing / a signal is detected — "hiring SDRs → continue; if not → stop") to save credits and keep the pipeline high-intent; **run expensive steps last** (email finding, phone, AI summaries only after a lead qualifies); and enable **auto-update** for always-on enrichment (source: "Automated data enrichment: Fueling high-scale LinkedIn outreach"). Its rule: "Enrichment without qualification is just more data – not better targeting." The GTM-agents roundup profiles Clay at $167/mo with 150+ data providers, Claygent Builder/Navigator, Sculptor natural-language workflows, and MCP server support, with teams reporting "80–90% time savings on pre-outreach prep" (vendor claim) (source: "The Best AI Agents for GTM Engineering (Your 2026 Stack Guide)"). In trigger-based outreach Clay is the **"bouncer"** — a pre-qualification gate filtering revenue/headcount/tech stack before drafting (source: "The ultimate guide to trigger-based outreach").

## Connecting Clay → HeyReach (native)

The native integration means no CSV/Sheets: in a Clay table, Add column → Add enrichment → search HeyReach → **"Add Lead to Campaign"**; Manage accounts → Add connection → generate a **Clay-specific API key** in HeyReach (Integrations → HeyReach API) → paste into Clay (source: "How to integrate HeyReach with Clay?"). Prep the HeyReach campaign first (create campaign, empty lead list, LinkedIn senders, sequence). Then map fields (first name, last name, LinkedIn URL) plus custom variables; with auto-update on, Clay keeps pushing new qualified leads.

**Variable naming rules (critical):** custom variables like `{complimentToTheProfile}`, `{websiteSummary}`, `{AI_Icebreaker_1}` must use **no spaces, only letters/numbers/`_`/`-`, and match EXACTLY between Clay and HeyReach** — mismatched names trigger the fallback message (source: "How to integrate HeyReach with Clay?"). If the LinkedIn account field is left blank, HeyReach randomly assigns a sender from that campaign. Custom variables only appear in HeyReach *after* you transfer at least one lead (source: "Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)"). Ready-made "Clay + HeyReach templates" live at heyreach.io/clay-templates.

## Claygent (AI web research)

Claygent is Clay's AI web crawler for enrichment beyond database fields. Practitioner (Tim Jacobson, B2B Boosted — COI) uses it to (a) visit a company site and categorize/confirm ICP, and (b) find a named contact + LinkedIn URL from a company name (source: "Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)"). A GTM engineer uses two Claygent signals: a job posting for ops roles (≤30 days old), and a "someone left the company" signal via Clay's past-experiences filter + an AI prompt returning the date left (source: "How to automate LinkedIn outreach using Clay, HeyReach and n8n"). Tip repeated across videos: switch the Claygent model from expensive "Neon" to a cheaper model (GPT-4o mini / GPT-5.1) and "sculpt" the prompt with Clay's generate button (source: "I Built a Clay to HeyReach Pipeline That Books 12 Meetings Per Month (Full Breakdown)").

## Controlling Clay credits

Clay "gets super expensive super fast" at scale, so cost control is its own discipline (Rob, HeyReach channel). A basic enrichment burns ~6 credits/row (scrape profile 3 + enrich person 1 + find email 1 + validate 1). Three methods (source: "How to Save Thousands on Clay Credits and GTM Tools (2026)"):
1. **Conditional run-settings (free)** — Clay AI formulas (no credit cost) split names/extract IDs; gate pricey enrichments with a condition (e.g. "only run if a validated email is present OR LinkedIn activity within 2 months").
2. **Claygent with your own OpenAI/Claude API key** — reach OpenAI usage-tier-2 (~$50), use GPT-4o mini; custom scrapes (e.g. Ofsted ratings at $0.001/row) replace paid tools.
3. **Third-party marketplaces** — Apify (LinkedIn scraper ~$5/1,000 rows vs 1 credit/row) and RapidAPI (buy just the SimilarWeb/Ahrefs API vs a full subscription).

That client's vacancies campaign reported 18% message reply rate and 30% connection acceptance (self-reported) (source: "How to Save Thousands on Clay Credits and GTM Tools (2026)"). Clay's Explorer tier (vs Starter) adds direct API integrations to HeyReach/Smartlead, webhooks, and HTTP-API access — worth it only at hundreds of thousands of enrichments/month (same). A cost angle HeyReach pushes: the native integration means "you don't have to spend money on multiple data enrichment tools (Apollo, Prospeo, Lusha, Cognism…)" — a vendor cost claim (source: "How to integrate HeyReach with Clay?").

## Personalization variables that convert

The stack passes AI-written openers as variables. HeyReach's outbound-automation model shows Clay pushing `{AI_Icebreaker_1}`, `{websiteSummary}` and SmartReach AI generating `{connection}`, `{follow_up_1}`, `{follow_up_2}` into a live HeyReach campaign (source: "Outbound automation tools: What works and what you’re probably doing wrong"). Always set a **fallback message** for when a variable can't populate. For the message-craft side (poke-the-bear questions, ≤12-word sentences), see [[ai-personalization-at-scale]] and [[linkedin-message-formulas]].

## Related
- [[data-enrichment-tools-and-providers]]
- [[ai-outreach-agent-architecture]]
- [[signal-and-intent-integrations]]
- [[n8n-automation-workflows]]
- [[make-automation-workflows]]
- [[heyreach-campaign-api-and-webhooks]]
- [[automation-workflow-templates]]
- [[build-targeted-lead-lists]]
- [[ai-personalization-at-scale]]
- [[signal-based-outbound-framework]]
