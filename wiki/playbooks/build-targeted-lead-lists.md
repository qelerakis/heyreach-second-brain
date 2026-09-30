# Building Targeted LinkedIn Lead Lists

How to build the list your whole campaign rests on: define a high-resolution ICP, translate it into Sales Navigator filters (with Boolean and the "posted recently" filter doing the heavy lifting), source from the right places, and clean ruthlessly before launch. The corpus is unanimous that **list quality sets the ceiling** — "your list decides how hard the message has to work," and "copy can amplify list quality, but it can't compensate for a bad one" (source: "How to turn post reactors into a high-converting lead list in 30 minutes"). For intent-triggered lists (job changes, funding, website visitors) see [[signal-based-outreach]]; for enriching a raw list at scale see [[ai-personalization-at-scale]].

## Start with a high-resolution ICP, not a description

Get specific before opening any tool. Nadiya's course frames it as aiming for **80–90% of your network = ICP** and defining not "sales professionals" but "founders/sales pros in early-stage startups moving from founder-led to sales-led" (source: "Full LinkedIn Lead Generation Course (1+ Hour)"). Guest Stan pushes tighter: not "CMO in B2B SaaS" but "CMOs in B2B SaaS that raised Series A ≥6 months ago, hiring 5 SDRs + 2 marketers, active on LinkedIn" (source: "LinkedIn Outreach is About to Change Forever (and nobody even realises)"). HeyReach's prospecting guide recommends writing the ICP as **selection criteria, not a description** — each element auto-checkable — and using **keyword-based functional targeting** ("sales," "revenue," "growth") over fixed titles ("VP Sales") plus hard disqualifiers (source: "How to use Linkedin for B2B lead generation"). The Deal Lab's named targeting index (market → segment → persona → angle, with the persona as "the CEO of the problem") is the framework version — see [[icp-and-targeting-systems]] (source: "How I Generate $11M in LinkedIn Pipeline Using This Exact System").

## The Sales Navigator method

The Sales Navigator masterclass builds a "scrapable persona" offline first, then filter-by-filter (source: "LinkedIn Sales Navigator Full Masterclass 2026 - How to Generate Leads on LinkedIn"):

- **Account search first, then lead search.** Find qualifying *companies*, save them to an account list, then find people at those accounts — cleaner than a giant lead blast (source: "How to Get Clients on LinkedIn in 2026 (30+ Clients Per Month)"; source: "LinkedIn Outreach Strategy to Book More Sales Calls (2026)").
- **Headcount as a revenue proxy** (~$100K revenue/employee); prefer **person location** over company HQ location; **industry is unreliable** (creator-defined, no "SaaS" — use "software development" plus a keyword like "platform").
- **Function vs job title:** use exact job title when known (most specific), else filter by department/function and leave title empty; include (CEO/founder) AND exclude (interns/junior).
- **Years in current role:** target recent switchers (<1 year — "fresh blood... willing to experiment").
- **Boolean strings** for ICPs with no clean industry: AND narrows, OR expands, NOT excludes, "quotes" for exact phrases, () to combine; **capitalize operators** and use **straight (not curly) quotes**. Example that cut 1,000,000 → 4,000: `agency AND lead generation NOT branding` — "this is going to be your gold mine" (source: "LinkedIn Sales Navigator Full Masterclass 2026 - How to Generate Leads on LinkedIn"; source: "8 rules for safe and scalable outreach with the best LinkedIn connection automation tool").

### The single highest-leverage filter

Nearly every practitioner names **"Posted on LinkedIn" (in the last 30 days)** as the filter that matters most, because messaging inactive profiles wastes your scarce weekly quota. Amon calls it "the very first thing I tell my clients to do" and claims it "increases acceptance rates by 2 to 4X"; a 10K list often trims to ~1,500–2,000 active profiles (source: "How I made $5 Million with LinkedIn Outreach (1 Hour Masterclass)"; source: "LinkedIn DM Strategy: What Works After 5,000,000 Messages"). Other intent filters to layer: "Changed jobs" (last 90 days), "Following your company," "Viewed your profile."

### Import without a scraper

Copy the Sales Navigator search URL and paste it into HeyReach (Leads → Add leads → Sales Navigator leads → paste URL → select senders → Start importing) — no separate scraper or CSV needed; it uses your logged-in account and imports in ~2–3 minutes (source: "The NEW Way to Get Clients on LinkedIn in 2026"; source: "How I Generate $11M in LinkedIn Pipeline Using This Exact System").

### Sales Navigator limits worth knowing (era-sensitive, 2026)

Search results viewable up to **2,500 lead results / 1,000 account results**; up to **10,000 saved leads**; **InMail up to 50/month** on Core; profile views 2,000/day on Sales Nav vs 500/day free (source: "How to Use LinkedIn Sales Navigator: 6 Lead-Gen Tactics (2026)"). Free LinkedIn people search caps at ~1,000 profiles/month; HeyReach can bypass this by combining multiple accounts' searches and de-duplicating (source: "I reviewed and ranked 40+ best LinkedIn automation tools of 2026").

## Lead sources beyond Sales Navigator

HeyReach imports from: LinkedIn free search bar (weak filters, free), Sales Navigator, LinkedIn Recruiter, **LinkedIn Groups** (scrape members), **Events** (scrape attendees), **post reactors/commenters** (scrape a competitor's or thought-leader's engagers), and **CSV** (needs profile URL + first/last name) (source: "I Sent 5,000,000 LinkedIn DMs: here's what you need to know"; source: "The ONLY LinkedIn Lead Generation Video You Need"). Lookalike/competitor plays: "rent your competitor's audience" via the "Followers of" field, and lookalike modeling via tools like Ocean.io (source: "5 LinkedIn best practices to accelerate growth"; source: "LinkedIn prospecting: The only guide you’ll ever need").

**Hard-to-find local/service businesses** that Apollo and Sales Navigator miss (they often have no LinkedIn company page) can be scraped with a Google Maps Scraper on Apify — one clinic yielded 41 doctors vs ~2 on Apollo, and 19,220 London clinics via Maps vs 1,300 on Apollo (source: "How to Find Anyone’s Contact Data for B2B Lead Generation").

## Rank your list by warmth

List warmth is set before any copy. HeyReach ranks its native import sources warmest → coldest: **Tier 1 Post Reactors** (warmest — they saw your content, recognized your name, self-selected the topic), **Tier 2 Event Attendees** (shared context), **Tier 3 Sales Navigator** (precision cold, tightest ICP), **Tier 4 free Search Bar** (broad cold, most cleanup). Warm math beats cold: a 150-person warm list at 32% acceptance ≈ 48 accepted, close to a 500-person cold list at 12% ≈ 60 — very different quality (source: "How to turn post reactors into a high-converting lead list in 30 minutes").

## Clean the list before launch

- **Manual review (~10 min):** remove title/company non-fits; pull out people you know personally (they get a direct DM, not a sequence) (source: "How to turn post reactors into a high-converting lead list in 30 minutes").
- **Exclude the wrong leads:** already-contacted-in-another-campaign, messaged-by-other-senders, contacted-by-you-before, existing clients (import as an exclude list), 1st-degree connections on cold campaigns, and profiles with no photo (source: "How to re-engage lost customers [67% reply rate]"; source: "The Best LinkedIn Lead Generation Strategy for 2026").
- **Combine and intersect lists** to dedupe and cross-match (e.g. event attendees AND group members) (source: "LinkedIn message automation: the playbook that got us a 42% reply rate").
- **AI list cleaning:** connect Claude to HeyReach (MCP) and have it read the whole list and remove everyone who doesn't match the ICP — HeyReach reports cleaning a 23k-lead list "in minutes," and notes Sales Nav exports "can contain 20-30% irrelevant contacts" (source: "The Laziest Way to Book Meetings on LinkedIn"; source: "The new baseline for LinkedIn outbound"). The stack wiring for enrichment/qualification (Clay, Trigify, RB2B) is in [[ai-personalization-at-scale]] and [[qualify-and-prioritize-leads]].

## Related
- [[signal-based-outreach]]
- [[ai-personalization-at-scale]]
- [[qualify-and-prioritize-leads]]
- [[write-cold-outreach-copy]]
- [[book-meetings-on-linkedin]]
- [[build-linkedin-campaign-sequences]]
- [[icp-and-targeting-systems]]
- [[icp-and-targeting-systems]]
