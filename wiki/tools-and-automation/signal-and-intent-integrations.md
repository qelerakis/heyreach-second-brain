# Signal & Intent Integrations (Trigify, Bitscale, Jungler, Clearcue, traxy)

The "brain" partners that detect *who is in-market now* and feed those leads into HeyReach while intent is warm — the listening/qualification layer of the [[ai-outreach-agent-architecture]]. HeyReach's trigger-based guide names the split as **"Brain & Muscle"**: Brain = a listening layer (Trigify) + a verification layer (Clay); Muscle = HeyReach execution — with the warning "If you've got the muscle without the brain, you're just a sophisticated spammer" (source: "The ultimate guide to trigger-based outreach"). This article covers the engagement/intent-signal partners and the shared signal→enrich→outreach pattern. Website-visitor de-anonymization tools (RB2B, IntentStream, Factors AI) are in [[website-visitor-identification]]. All sources are HeyReach's own guides (COI); acceptance/reply lifts are the partners' or practitioners' self-reported claims.

## The signal → enrich → outreach pattern

The recurring architecture: a signal tool *listens*, Clay *enriches/qualifies*, HeyReach *executes* — "Trigify listens → Clay enriches/qualifies → HeyReach kicks off sequence" (source: "The ultimate guide to trigger-based outreach"). HeyReach's outbound-automation model generalizes it into five steps with a tool set per step — signal detection (Trigify, RB2B, Clay, Clearbit Reveal, Leadfeeder) → enrichment & segmentation → outreach activation → AI personalization → multichannel nurture (source: "Outbound automation tools: What works and what you’re probably doing wrong"). The **5-minute rule** ("speed is strategy") and an **80/20 personalization formula** (80% reusable value prop, 20% "why now" hook referencing the trigger) come from the same brain-and-muscle guide (source: "The ultimate guide to trigger-based outreach").

## Trigify (real-time social signals)

Trigify is the "if this, then that" engine reacting to LinkedIn/social signals in real time, and — importantly for safety — it does **not** use your LinkedIn account to scrape (source: "How to connect HeyReach & Trigify for smarter LinkedIn outreach"). Setup: HeyReach → Integration → HeyReach API → Get API key → paste into Trigify → Connect. Build a Trigify workflow (trigger: Connection accepted / User replied / Lead engaged with a post → HeyReach response), then "Save to → Export to HeyReach → choose campaign." Enrich with Clay before upload; run a sequence (connection request → follow-up #1 at +1 day → follow-up #2 at +3 days, firing #2 only if the person engages). Practitioner **Steven Brady** reported **$49,000 in 8 weeks** with this HeyReach + Trigify setup (his self-reported webinar result, COI) and praised HeyReach's safety limits: "the product limitations tell me you guys are thinking about keeping users safe from themselves" (source: "How to connect HeyReach & Trigify for smarter LinkedIn outreach"). Trigify also drives n8n post-engagement builds — see [[n8n-automation-workflows]] and [[automation-workflow-templates]].

## Bitscale (signal-driven GTM + BitAgent)

Bitscale is a signal-driven GTM platform for sourcing, enrichment, and outbound that pulls from 50+ sources and runs **waterfall enrichment** (fallback across providers), pushing signal-driven leads into a HeyReach campaign "while intent is still warm" (setup <5 min) (source: "HeyReach + Bitscale: Turn signals into LinkedIn outreach, automatically"). Setup: HeyReach API key → connect in Bitscale → build a "grid" from signal sources (Sales Nav, comment scrapers, job-board scrapers, CRM sync, webhooks) → run waterfall enrichments → generate a personalization line with **BitAgent** (AI opener referencing the trigger, "under 20 words") → push to HeyReach mapping First→`{first_name}`, Last→`{last_name}`, LinkedIn URL→profile [required], BitAgent col→`{personalization}` → set a **fallback** for `{personalization}` → run (campaign must be ACTIVE, not draft). Use **run conditions** so enrichment only fires on ICP-qualified rows (saves credits) and **exclude lists** to prevent cross-campaign duplicates. Its framing: "'All SaaS founders in the US' is a list. 'Founders whose company posted a Head of Sales role this week' is a signal."

## Jungler (LinkedIn engagement → meetings)

Jungler monitors LinkedIn engagement (a profile's posts or a specific post URL), backfills the last **31 days** on first run, enriches every engager, and pushes ICP-matched ones into a HeyReach campaign — running entirely **outside your LinkedIn account** (no login, cookies, or extension) (source: "HeyReach + Jungler: Turn LinkedIn Engagement Into Booked Meetings, Automatically"). Setup (<5 min): create a monitor → apply ICP filters → connect the HeyReach API key → select a HeyReach campaign that must be **EVERGREEN** (accepts new leads continuously) → map fields → activate. It positions itself as removing the "Clay middle step" — "No CSVs. No Clay detour" — with native HeyReach integration plus custom webhooks. Its highest-converting use case: engaging with a competitor's post = "actively in-market for your category."

## Clearcue (buying-intent intelligence)

Clearcue is an AI signal-intelligence platform tracking real-time buying intent across LinkedIn/digital channels; it connects to HeyReach **either natively or via MCP through Claude** (source: "HeyReach + Clearcue integration guide"). Setup: get the HeyReach API key + add HeyReach as an MCP server in Claude → get the Clearcue MCP URL/token (starts with `clc_`) → add Clearcue MCP in Claude → create a signal filter (funding round, hiring Head of Sales, engaging your/competitor content) → build a HeyReach campaign but don't add leads → prompt Claude "Pull the top 20 leads from my [filter] in Clearcue, then add them to my [campaign] in HeyReach." Its **"signal stacking"** = layering 2–4 intent indicators ("The more specific your signal stack, the higher your reply rates"). Vendor claim: intent-based targeting = 35–45% reply rates vs 5–10% cold. Drip in batches of 20–50 leads/sender/day across 3–5 accounts.

## traxy (LinkedIn listening layer)

traxy (traxxi.ai) is a "LinkedIn intelligence/listening layer" that monitors engagement on your content, competitors' posts, and influencers, qualifies against ICP, and auto-pushes active leads in real time — a fix for low acceptance from static Sales Navigator lists (source: "HeyReach + traxy Integration guide"). Setup (inside traxy): copy the HeyReach API key → paste in traxy → select a **dedicated** HeyReach campaign (to benchmark vs Sales-Nav campaigns) → set Delivery = Auto. Its founder **Ben** reported acceptance climbing from a typical 20–25% to **45–58%** after switching to traxy targeting (vendor-founder claim, COI). Its thesis: "The problem with most LinkedIn outreach isn't the tool — it's the list." (Note: the guide contains several "[VERIFY]" author placeholders on exact menu paths — draft-state doc.)

## Choosing a signal source

| Tool | Signal type | Connection | Runs on your LI account? |
|---|---|---|---|
| Trigify | LinkedIn/social engagement, if-this-then-that | API key | No |
| traxy | Engagement on your/competitor/influencer content | API key (Auto delivery) | No |
| Jungler | Engagement on a profile's or a post's activity | API key (evergreen campaign) | No |
| Clearcue | Multi-channel buying intent, signal stacking | Native or MCP (Claude) | n/a |
| Bitscale | Any signal source → enrich → outbound | API key | n/a |

The safe operating rule across all of them: drip in small daily batches per sender and gate on ICP fit so triggered systems don't "amplify silence." See [[signal-based-outbound-framework]] and [[safe-linkedin-sending-limits]].

## Related
- [[website-visitor-identification]]
- [[clay-enrichment-and-data-waterfall]]
- [[data-enrichment-tools-and-providers]]
- [[ai-outreach-agent-architecture]]
- [[n8n-automation-workflows]]
- [[make-automation-workflows]]
- [[automation-workflow-templates]]
- [[signal-based-outbound-framework]]
- [[signal-based-outreach]]
- [[safe-linkedin-sending-limits]]
