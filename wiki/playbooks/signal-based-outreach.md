# Signal-Based Outreach

How to run outreach triggered by what a prospect just *did* rather than who they statically *are* — job changes, funding, hiring, tech-stack shifts, content engagement, and website visits. The premise repeated across the corpus: at any moment only a small slice of your market is in-market, "so instead of relying on who someone is, it focuses on what they are doing," and buying intent decays fast, so **speed and timing beat volume** (source: "How to use Linkedin for B2B lead generation"; source: "Route buying intent signals into LinkedIn campaign before they decay"). This is the "reach people while the window is open" playbook; the list-building basics are in [[build-targeted-lead-lists]] and the automation wiring is in [[partner-integrations-directory]].

## Why signals, and why now

HeyReach frames the shift as timing, not lead volume — "Most teams don't have a lead problem. They have a timing problem" (source: "Inbound-led outbound: Turn inbound signals into a predictable pipeline"). Warm, signal-driven leads convert far better than cold: HeyReach's lead-type table (from its 96,051-campaign dataset; vendor-sourced) puts **cold at 1–3%, warm at 5–15%, hot at 15–30%** (source: "Warm Leads: What They Are & How to Convert Them Fast"). Intent decays within roughly **24–48 hours**, which is why signals must route into live campaigns fast (source: "Route buying intent signals into LinkedIn campaign before they decay").

## The signals that work (and one that doesn't)

HeyReach's "Big 5" high-intent signals (source: "Outbound ICP signals: How to spot high-intent leads before your competitors"):

- **Career move / new role** — the most cited. There is a ~90-day proving window; Morgan J Ingram's "Sweet Spot Window" (attributed) says **3–6 months in** they see what's broken and **7–10 months in** they want impact before the one-year review — the **7-month mark** is the sweet spot (source: "How to finally make buyer intent signals work for your outbound"). A champion from an existing customer who moves companies is a warm "executive migration" lead.
- **Tech-stack shift** — added/dropped a tool (especially a competitor's); capture *recency* (last 30 days = live; 8 months = irrelevant).
- **Growth trigger** — funding rounds + aggressive dept hiring; specificity matters ("posted 4 SDR roles and a RevOps manager in the last 3 weeks"). A "ghost-job" signal (hiring Sales Ops / RevOps / GTM Engineering) means they're building infrastructure for a tool.
- **Content engagement** — likes/comments on authority, competitor, or your own posts.
- **De-anonymized website visit** — a pricing-page visit is the warmest signal.

The consistent warning: **a post-like alone is not intent.** HeyReach: "please don't chase people... just because they liked your post" — a like doesn't mean they need what you offer (source: "The Best AI LinkedIn Lead Generation Strategy for 2026"). Halen Youles of Scalemate (agency, disclosed HeyReach partnership, COI) frames a **two-tier buying-intent** model: Tier 1 = action on *your* company (site visit, demo request — highest but low volume for no-brand startups); Tier 2 = action on *your industry* (engaged a competitor/influencer — the scalable play) (source: "How I’d Generate LinkedIn Leads From Zero (No Network, No Warm Leads)").

## The signal-message blueprint

Keep it to two sentences: **[The Signal] + [The Relevant Problem] + [The Low-friction Ask]** — "One signal, one problem, and one ask. Everything else is noise" (source: "Outbound ICP signals: How to spot high-intent leads before your competitors"). Anchor the opener in the signal via a variable like `{{engagement_type}}` ("liked"/"commented") — "the signal does most of the work. The message simply needs to carry it forward" (source: "How to use Linkedin for B2B lead generation"). Crucial nuance: **don't call out an invasive signal.** "I saw you on our pricing page" feels invasive — use the visit for timing and tone, not as the opening line (source: "Outbound ICP signals: How to spot high-intent leads before your competitors"; source: "Send personalized LinkedIn messages to your website visitors [HeyReach - RB2B Webinar]").

## Play 1 — Post-engagement outreach

Scrape everyone who engages with a chosen thought leader's or competitor's posts, qualify to ICP, then reach out warm. The stack pattern (wiring in [[partner-integrations-directory]]): a listening tool (Trigify) captures likers/commenters → Clay enriches and scores fit → qualified leads flow into a HeyReach campaign referencing the engagement ("saw your like/comment on [X]'s post…") (source: "The Best LinkedIn Outreach Strategy for 2026"; source: "How to use Linkedin for B2B lead generation"). Halen's fully automated influencer-engagement campaign self-reported **49% acceptance, 31% reply, no email** — but he explicitly warns those numbers reflect an unusually active founder/tech market (source: "How I’d Generate LinkedIn Leads From Zero (No Network, No Warm Leads)"). A comment-to-lead funnel from your *own* posts (capture commenters → enrich → outreach) is a warm variant (source: "Full Guide to Engaging & Commenting on LinkedIn (Best Growth Strategy)"). Gunner Park of Brij self-reported a 60% reply rate on a 90-message Trigify + Clay + Smartlead campaign (source: "Perfecting your LinkedIn cold messages: Proven tactics for higher engagement and shorter sales cycles").

## Play 2 — Website visitors (de-anonymization)

Put a pixel (RB2B, or Midbound/others) on the site to match visitors to real LinkedIn profiles, then route them into LinkedIn outreach. From the HeyReach × RB2B webinar (co-marketing, vendor claims): Adam Robinson (RB2B/retention.com) treats the first move as a connection request because "most people accept all of their LinkedIn connection requests"; HeyReach's Ilia recommends **not messaging from the top** — start with a profile follow, then 3 hours later a connection request, then a short message on accept — and reports adding two pre-touches (follow, then next-day like) makes "around 55% more people accept," plus a ~65% reply rate on a single-sender RB2B-seniority campaign (small sample, vendor-reported) (source: "Send personalized LinkedIn messages to your website visitors [HeyReach - RB2B Webinar]"). Route by intent: hot-page-only vs hot-lead-only vs both, into different campaigns; **don't cold-email a personal/Gmail address** they never opted in with — send those to LinkedIn instead (source: "How to turn website visitors into leads using RB2B and HeyReach"). Steven Brady self-reported **$49,000 in 8 weeks** via HeyReach + Trigify (source: "Outbound ICP signals: How to spot high-intent leads before your competitors").

Adam Robinson's 60-day "parasocial" play (attributed to him via his consultant Alec): build a 2–3-year TAM, send 10/day scaling to 20–30 connection requests/day with a no-pitch "how's it going at [company]?", post daily so they get served your content, and after ~60 days and 15–20 touches ask for the call — he claims "~80% accept rate" (source: "Send personalized LinkedIn messages to your website visitors [HeyReach - RB2B Webinar]").

## Play 3 — YouTube comments and event attendees

YouTube commenters are a strong intent signal (they discovered you, consumed content, and engaged publicly): scrape comments (Apify), enrich profiles for LinkedIn URLs, dedupe in a sheet, and push LinkedIn-having commenters into a connection campaign with a contextual note (source: "How to Turn YouTube Comments Into High-Intent Leads"; source: "YouTube lead generation: How to turn comments into high-intent LinkedIn leads"). Event attendees are similar — scrape a LinkedIn event's attendee list and open with the shared context ("are you at [event]?"), a "super underused" non-awkward opener (source: "I Built a Clay to HeyReach Pipeline That Books 12 Meetings Per Month (Full Breakdown)"; source: "The Best LinkedIn Outreach Strategy for 2026").

## Route signals before they decay

Because signals decay in 24–48h, route them into live campaigns fast — HeyReach recommends first touch live within 24h (and within ~1h for ultra-high-intent like a pricing-page visit) (source: "Route buying intent signals into LinkedIn campaign before they decay"). Not all signals are equal: HeyReach weights **Funding = 3, Re-Entry (job change) = 2, Website Visit = 1**, and estimates funding events reply ~15% vs website visits ~4% (author "expected ranges," not verified) (source: "Route buying intent signals into LinkedIn campaign before they decay"). The signal-led GTM model layers three intent tiers — ICP-with-signals (higher volume), intent-first signals (timing-sensitive), and first-party/inbound signals (highest urgency, route straight to sales) — with the rule "Signals determine entry points. Capacity determines feasibility. Intent strength determines escalation" (source: "Signal-led GTM engine: Playbook to turn signals into sales"). The routing/orchestration engineering (validate → dedupe → prioritize → route → pace) is the [[signal-based-outbound-framework]] framework and the [[partner-integrations-directory]] stack.

## Speed is the moat

Once a signal fires, respond fast. HeyReach and its guests cite third-party stats that contacting within 5 minutes vs an hour makes leads far more likely to convert, and re-entry (job-change) leads respond 2–3× the rate of cold (source: "Route buying intent signals into LinkedIn campaign before they decay"; source: "How I’d Generate LinkedIn Leads From Zero (No Network, No Warm Leads)"). Managing that inbound speed at scale is [[manage-replies-and-inbox-at-scale]].

## Related
- [[build-targeted-lead-lists]]
- [[book-meetings-on-linkedin]]
- [[ai-personalization-at-scale]]
- [[qualify-and-prioritize-leads]]
- [[manage-replies-and-inbox-at-scale]]
- [[multichannel-linkedin-email-sequencing]]
- [[write-cold-outreach-copy]]
- [[signal-based-outbound-framework]]
- [[website-visitor-identification]]
- [[signal-and-intent-integrations]]
