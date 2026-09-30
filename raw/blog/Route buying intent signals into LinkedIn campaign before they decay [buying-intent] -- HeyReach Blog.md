# Route buying intent signals into LinkedIn campaign before they decay

Source: https://www.heyreach.io/blog/buying-intent

Summary: Turn buying intent signals into LinkedIn outreach within 24 hours. Detect, enrich, filter, and execute before signals decay using Clay, RB2B, n8n, and HeyReach.

You already have more buyer intent data than you can act on. Website visits, LinkedIn engagement, job changes, product signups – all of which your systems capture.

And yet, the execution stage is where most teams get stuck

You’ve seen it happen. Countless times.

A prospect downloads your guide, visits your pricing page, maybe even replies to your sales outreach with “we’ll circle back soon 🔥.”

The sales team is excited for a week and then…. silence.

Two weeks later, your dashboard still says “high intent.”

But in reality, that lead has already moved on, probably talking to your competitor or back to ignoring vendors altogether.

That’s how fast purchase intent decays.

 It doesn’t wait for your next sync. It doesn’t care that marketing is “still testing new campaigns” or that sales “haven’t uploaded the list yet.”

Every extra day between signal and action bleeds revenue. And we’re not letting that happen anymore.

This piece is about fixing that lag.

So instead of watching interest fade, you’ll learn how to automatically route potential customers into live LinkedIn campaigns while they’re still curious, still clicking, still in the market, and while buying intent is still fresh.

## **Why buying-intent signals lose impact after 24–48 hours**

Most buying intent decays within the 24–48-hour lag between detection and action because many sales teams still struggle to operationalize execution.

When someone visits your pricing page, comments on a post you made, or updates their job title, that signal isn’t a long-term indicator of interest.

In my experience, and supported by data, businesses that make fast initial contact within the first few minutes of a fresh intent signal close between 35% and [50% of sales](https://www.heyreach.io/blog/sales-follow-up).

In fact, calling a lead within the first minute can boost your conversion rate by [up to 391%](https://www.chilipiper.com/article/speed-to-lead-statistics#:~:text=But%20how%20fast%20is%20fast,just%20a%20few%20minutes%20longer), largely because [78% of potential clients](https://voiso.com/articles/lead-response-time-metrics/) would buy from the company that contacts them first.

So, speed is really your moat here.

Within the first 24 hours, the [buyer intent signal](https://www.heyreach.io/blog/buyer-intent-signals) is hot.
The buyer is still in problem-solving mode, open to new tools, actively researching, and emotionally invested in fixing the issue that made them click.

By 48 hours, that signal has already cooled.

The urgency fades, their attention splits, and even your most relevant message now competes with a dozen others in their inbox or feed.

Across teams I’ve seen, the main issue is figuring out: what happens after a signal fires?

Here is where most teams lose momentum:

* **Signal routing friction:** Intent data surfaces in one tool, say, Clay, but outreach happens in another. Without real-time orchestration, those signals sit idle while ops teams have to manually sync or enrich.
* **Approval or enrichment delays:** Before outreach begins, someone wants to “verify” or perform lead scoring. By the time they’re done, it’s tomorrow and the buyer’s already moved on.
* **Campaign lag:** Even when the signal is valid, it can take hours to import, tag, and queue prospects if there’s no live integration or campaign tagging setup.

By the time all this processing is done, the signal’s no longer fresh, it’s just data.

The fix isn't for your sales reps to collect more data.

It’s building a real-time operational layer that moves from detection → enrichment → outreach automatically, without execution gating or manual approvals slowing things down.

* If your system can recognize a pricing-page visitor at 10:02 a.m. and enroll them in a personalized [LinkedIn outreach](https://www.heyreach.io/blog/linkedin-outreach-campaign) sequence by 10:05, you’ve beaten signal decay.
* If your system can spot a job change, re-score the contact, push them into a re-engagement workflow, and tag it for analytics tracking, you’ve beaten signal decay.

This is what speed-to-lead looks like in practice.

And when some signals inevitably slip through, build a fallback orchestration plan: a light-touch reactivation workflow that warms up stale signals without spamming. Over time, that simple layer alone will help you outperform most of your competitors.

## **How to act fast on buying intent data and automate it**

You can set up buying-intent detection to happen in tools like [Clay](https://www.heyreach.io/integration/clay), [RB2B](https://www.heyreach.io/integration/rb2b), and [Trigify](https://www.heyreach.io/integration/trigify) and move to execution by triggering an automated action in [HeyReach](https://www.heyreach.io/blog/heyreach-review) within minutes, not hours.

If you want to shorten your speed-to-lead, follow one golden rule: Treat buying intent signals as triggers for instant action.

When one tool detects a signal, another must act on it instantly.

**You need two connected layers:**

* **Detection Layer** → where signals originate (Clay, RB2B, Trigify, Crunchbase).
* **Execution Layer (HeyReach)** → where those signals are routed into live LinkedIn outreach, enriched, tagged, and tracked automatically.

This is how your team moves from “we know who’s interested” to “we’re already in their inbox.”

> For reference, Heyreach already integrates with some of your most used detection tools so connecting your stack takes minutes. See [the full HeyReach integration ecosystem](https://www.heyreach.io/integrations).

### **The signal-to-action map**

This table turns the four most common buying-intent use cases into immediate actions so you see how to connect the dots between intent data providers and execution in HeyReach.

**Detection =** External tools (Clay, Trigify, RB2B, Crunchbase)
**Execution =** HeyReach (import, tag, assign, rotate)
**Standardized tags =** Funding Event, Re-Entry Lead, High Intent Visit, Stale Signal

Each workflow uses standardized tags to keep analytics clean, speed routing decisions, and support multi-campaign orchestration inside HeyReach.

Your goal: move from **signal → action → analytics** in minutes, not days.

### **1. Funding signals → prioritize high-value outreach**

**Detection:** Clay + Crunchbase
**HeyReach action:** Import → Tag “Funding Event” → Push to high-priority campaign

When a company announces a new funding round, they’re flush with budget and urgency but also flooded with vendor outreach. Your edge is time.

Use Clay to identify companies that match your ideal customer profile and have recently raised funds through Crunchbase. The moment that the record updates, send it directly into HeyReach via API or webhook.

Inside HeyReach:

* Tag those leads as Funding Event
* Route them to your high-priority campaign
* Enable multi-sender rotation to distribute outreach evenly and safely

**Operational tip:** Funding signals lose freshness quickly. Build a dedicated “Funding Event” campaign with tight pacing caps so your team engages those leads first.

### **2. Job-change signals → Re-engage in the new role**

**Detection:** Trigify or Clay
**HeyReach action:** Remove from old campaign → Retag “Re-Entry Lead” → Trigger new sequence

Job changes are one of the strongest buying-intent signals, especially when the contact moves into a decision-making role.

With Trigify or Clay, set triggers to detect title or company changes from your CRM or LinkedIn data.

As soon as a change is detected, remove them from their previous campaign.

In HeyReach:

* Tag them as ”Re-Entry Lead”
* Enroll them in a context-aware LinkedIn outreach sequence acknowledging the new role

**Operational tip**: Track re-entrylead conversions separately using tag-based analytics. These leads typically respond at two to three times the rate of cold outreach. See how tags and analytics work in Heyreach’s Unibox in following video.

https://www.youtube.com/watch?v=ote3FBiMFqM

### **3. Website visits → Trigger same-day warm nurture**

**Detection:** RB2B
**HeyReach action:** Import → Tag “High Intent Visit” → Assign to nurture campaign

Website visits are your clearest sign of active intent.
With [RB2B integration](https://www.heyreach.io/integration/rb2b), identify which companies and users visited your pricing or demo pages.

HeyReach will:

* Import the lead
* Apply the ”High Intent Visit” tag
* Route them to a same-day nurture campaign managed by your SDRs

This ensures anyone who visits your site today receives outreach within 12–24 hours, while interest is still warm.

**Operational tip:** Combine website visits with recent LinkedIn engagement for compound intent scoring. Route only leads above a set threshold to reduce noise.

### **4. Signal decay (>30 Days) → Move to long-term nurture**

**Detection:** Clay freshness filter
**HeyReach action:** Pause campaign → Retag “Stale Signal” → Move to long-term nurture

Every buying signal has a half-life. If a lead hasn’t engaged after 30 days, it’s not necessarily a dead lead, it could be a stale signal.

Use Clay freshness filters to flag these leads.

Once flagged, HeyReach can automatically:

* [Pause active campaigns](https://help.heyreach.io/en/articles/10493626-how-to-pause-resume-my-campaign) for those leads
* Retag them as “Stale Signal“
* Move them to a long-term nurture sequence with lighter, value-led touchpoints

### **Why this system works**

When your detection and execution layers communicate in real time: Clay → Trigify → RB2B → HeyReach — you create a [live GTM orchestration loop](https://help.heyreach.io/en/articles/10493626-how-to-pause-resume-my-campaign).

Every signal that fires triggers the right action instantly.

Every lead is tagged consistently: ***Funding Event, Re-Entry Lead, High Intent Visit, Stale Signal*,**

This gives your RevOps team clean, tag-based analytics to measure lead response time and pipeline velocity.

The result is a data source that routes, enriches, personalizes, and executes automatically, long before your competitors even finish exporting their CSVs.

To implement this, make sure your integrations between detection tools and HeyReach are live. The HeyReach integrations library supports [Clay](https://help.heyreach.io/en/articles/9910966-how-to-integrate-heyreach-with-clay), [RB2B](https://www.heyreach.io/blog/rb2b-integration), [HubSpot](https://www.heyreach.io/blog/hubspot-integration), and [n8n](https://www.heyreach.io/integration/n8n), so you can automate the entire signal-routing cycle.

## **The signal-to-campaign framework (4 Tiers)**

This 4-tier framework shows precisely how buying-intent signals move from detection to LinkedIn execution, so you can select the right setup level for your stage before building marketing automations.

Your speed depends on how tightly these layers connect: Detect → Orchestrate → Filter → Execute.

### **Tier 1: Detect**

Everything starts with clean, contextual signal detection.
This is where your system captures buying intent across digital touchpoints, including social media, website visitors, and job changes. Your whole workflow depends on how clean this layer is.

**Your core tools here are:**

* **Trigify**: detects LinkedIn engagement and job changes so you instantly see when someone in your ICP starts interacting or moves companies.
* **RB2B**: watches high-intent website actions like pricing, demo pages visits. It’s strongest for US traffic.
* **Clay:** handles enrichment and freshness confirming that your contact data is still valid and flagging leads that have gone cold or changed roles.

In my experience, most setups start here with one or two of these tools feeding fresh, contextual signals into the stack before scaling up. But detection alone doesn’t create a pipeline, orchestration does.

### **Tier 2: Orchestrate**

Once a signal fires, you need a way to route it cleanly, automatically, and safely to your execution platform. That’s where orchestration lives.

For light setups, you can use [Make](https://www.heyreach.io/integration/make) or [Zapier](https://www.heyreach.io/integration/zapier) to move one or two signal types.

For example; RB2B → HeyReach.
For complex multi-signal orchestration, use n8n, which supports conditional routing, scheduling, Slack alerts, and error handling.

**Example flow:**

Clay detects a “Funding Event” → n8n receives it → routes it to HeyReach → Slack notifies SDR channel → lead appears tagged and ready to engage.

Orchestration ensures signals are acted on instantly without the need for manual intervention.

### **Tier 3: Filter**

When signal volume grows, manual filtering becomes a bottleneck. That’s when you add intelligence.

Connect **Claude to** [**HeyReach via MCP**](https://www.heyreach.io/mcp) to automatically classify incoming signals as **QUALIFIED**, **NURTURE**, or **REJECT**, with context for each decision.

**Example logic:**

* A visit from a verified ICP company → **QUALIFIED**
* A non-ICP or early-career visitor → **NURTURE**
* Duplicate or student accounts → **REJECT**

This classification happens before leads reach active LinkedIn campaigns in HeyReach, ensuring only high-quality signals enter your outreach queue.

Keep your basic rule-based filters like job title, region, freshness  inside Clay or n8n, but let [Claude connected via MCP](https://www.heyreach.io/blog/beginners-guide-heyreach-mcp)  handle nuance when scale grows.

### **Tier 4: Execute**

This is where HeyReach turns signals into a real pipeline.

Once leads pass through orchestration and filtering, HeyReach handles execution to convert these raw signals into structured, trackable outreach:

* **Campaign management:** Organize leads by tag (Funding Event, Re-Entry Lead, etc.) and automatically route them to LinkedIn sequences.
* **Seat rotation:** Distribute outreach evenly across SDRs to boost coverage while staying within safe daily send limits.
* **Tag-based analytics:** Track which signal types generate the highest reply and conversion rates.
* **Unified inbox:** Manage all LinkedIn conversations from one dashboard for full RevOps visibility inside HeyReach Unibox.

Here’s what a modern GTM automation stack looks like when fully connected:

**Trigify / RB2B / Clay → n8n / Make → HeyReach**

This system ensures:

* Every new signal is detected in real time
* Every lead is enriched and filtered
* Every qualified contact is instantly routed into the right LinkedIn campaign
* Every SDR stays within pacing and seat rotation limits

This is how you operationalize intent data, not just collect it.

Your setup can be as simple or advanced as your pipeline volume demands.

### **Choosing your path**

This table helps you decide the right setup level based on your team’s size and signal volume.

**Note**: For some setups, you can add an AI orchestration layer like Claude connected via MCP to classify or enrich data automatically across tools like Clay, and HeyReach. However, MCP itself isn’t a tool. It’s the connection layer that lets your AI agent communicate with these tools in real time.

## **Route signals into LinkedIn in 24–48h — 4 proven workflows**

Most high-intent signals have a 24–48h shelf life but if you can route it fast through a clean enrichment → filtering → execution pipeline, you increase the chance of conversion.

I will show you proven workflows to turn fresh buying signals into [automated LinkedIn outreach](https://www.heyreach.io/blog/linkedin-message-automation) within a day. Each one shows the stack, timing, and HeyReach setup to keep response velocity high and decay low.

**To start, use this timing guidance as your operating playbook.**

* Detection + enrichment/filtering = aim for 2–6 hours
* Import to HeyReach = aim for less than 12 hours
* First touch or message live = aim for less than 24 hours (aim for less than 1 hour for ultra-high intent, e.g., pricing-page visitors with enrichment-aside).

**For tools:**

* Use n8n when orchestration requires branching, scheduling, or Slack alerts.
* Use Make/Zapier for simple single-signal flows.
* Use Clay for enrichment, deduplication, and strict rule-based filtering (e.g., job title, company size, or region).
* Use Claude via MCP connection during filtering to automatically classify borderline leads once volume scales. MCP links Claude directly to tools like HeyReach or Clay, so it can apply logic tags such as: QUALIFIED / NURTURE / REJECT (+reason)

### **Workflow 1: Website visit — Engage warm but anonymous traffic**

**When to use:** When a lead or account visits your pricing, demo, or “request a quote” pages especially from target accounts.

**Signal strength:** Strong intent. Active buyer behavior within a buying session.

**Tools required:** RB2B (visit detection) → Clay (enrichment & dedupe) → n8n or Make (routing)→ HeyReach (execution).

**Workflow (Trigger → Enrich → Filter → Execute)**

* **Trigger:** RB2B detects a visit to the pricing/demo page and emits a webhook with company & IP meta.
* **Enrich:** n8n pulls the visitor’s company and possible user info into Clay to append role, company size, ICP flag, tech stack, and CRM ID.
* **Filter**: Apply ICP + freshness rules. For high-volume or uncertain cases, you can use Claude, connected via MCP to auto-classify leads into QUALIFIED / NURTURE / REJECT categories with reasons.
* **Execute**: Qualified leads are pushed via webhook/API to HeyReach with the tag ”High Intent Visit” and enrolled immediately in a campaign.

**How to configure this in HeyReach**

1. **Campaign name format:** WI-HighIntent-YYYY-MM (WI = Website Intent)
2. **Tags**: High Intent Visit, Source: RB2B, Page: Pricing
3. **Seat count:** 2–4 SDR seats for moderate volume; scale to 6+ if the number is greater than 100 leads/week
4. **Cadence timing & sequence structure:**

* Day 0: Connection + DM (value hook)
* Day 2: Case study/question
* Day 5: Social proof / ask
* Day 12: Final value + CTA

5. Use seat rotation + safe pacing caps to keep daily sends per seat at safe limits.

**Message template you can use:**

Hi {first\_name}, I noticed a visit from {company} to our {trigger\_page}.
Was there a specific feature you were evaluating? Depending on what you’re looking to achieve, I’d be happy to show how this could streamline processes and deliver results for your team — let me know if a 10-minute walkthrough would be helpful.

**Expected results (ranges)**

* Connection acceptance: **30–55%**
* Reply rate: **8–18%**
* Booking rate (meeting scheduled): **2–6%**

**Troubleshooting (cause → fix)**

1. **Issue***:* Low replies → **Possible cause**: Generic message. **Fix***:* Mention the specific visited page.
2. **Issue***:* Low booking rates → **Possible cause:** No immediate value add. **Fix***:* Add follow-up with micro-value, for example a case study link of a business in a similar industry.
3. **LinkedIn limits/throttling** — **Possible cause:** aggressive multi-sender cadence. **Fix**: reduce per-seat daily sends; implement pacing caps in HeyReach.

**Bonus tip**: You can set up an automation to ping your account executive (AE) in Slack the moment a pricing visit is detected. A human follow-up in the loop multiplies conversion.

### **Workflow 2: Job change / Re-entry lead**

**When to use:** When a previously contacted lead changes role or company. An opportunity to re-open dialogue in a fresh context. Perfect time to re-engage quickly.

**Signal strength:** Medium-high — timing is emotional and high-change + potential new budget or authority.

**Tools required:** Trigify or Clay + n8n + HeyReach

**Workflow:**

* **Trigger:** Trigify detects job change (title or company update).
* **Enrich:** Use Clay to pull new company details (size, industry, region).
* **Filter:** Use Claude (via MCP connection) to auto-classify leads into QUALIFIED / NURTURE / REJECT categories with reasons. . For example, QUALIFIED = ICP match, NURTURE = wrong fit but promising company.
* **Execute:** n8n routes QUALIFIED to “Re-Entry Leads” campaign in HeyReach.

**HeyReach config:**

* **Campaign**: Re-Entry Lead
* **Tags**: Re-Entry Lead, New Role, Warm
* **Seat count:** 1–3 SDR seats per account team
* **Cadence timing & sequence structure:**

* Day 0: Congrats + re-intro message acknowledging move
* Day 3: Relevance message

* Day 7-8: Case study or sync request

**Messaging template you can use:**

**Option 1:** Congrats on the new role, {first\_name}! Noticed you moved to {new\_title} at {new\_company}. We chatted back when you were at {old\_company} about {topic} — would love to share what’s changed and how teams like yours are approaching {pain\_point}. Open to a 10-minute sync?

**Option 2:** Congrats on your move to {new\_company}!
Curious — are you planning to carry over some of the {previous\_tool\_or\_motion} playbook from {old\_company}? We’ve seen a lot of leaders tweak that motion in the first 90 days.

**Expected results (ranges)**

* Connection acceptance (if not connected): **45–70%**
* Reply rate: **12–30%**
* Booking rate: **3–10%**

**Troubleshooting**

1. **Issue**: Old title still in data

**Fix**: Re-enrich via Clay’s LinkedIn URL refresh.

2. **Issue**: Unqualified industry

**Fix**: Add Clay filter by company sector

3. **Issue**: Low replies

**Fix**: Soften opener tone; make the message about them, not you.

4. **Issue**: Flooded campaign.

**Fix**: Pause seat rotation; queue next 24h batch.

**Bonus tip:** If they moved to a company that just raised funding, stack the signals and make them double priority.

### **Workflow 3: Funding event → priority outreach**

**When to use:** When a target account raises a funding round. This typically opens immediate budget windows and strategic hiring or GTM expansions.

**Signal strength:** Very high — company-level trigger of buying readiness.

**Tools required (stack):** Tools required (stack): Clay + Crunchbase feed (funding detection) → n8n (priority routing + Slack + CRM update) → HeyReach

**Workflow (Trigger → Enrich → Filter → Execute)**

* **Trigger:** Clay/Crunchbase feed detects a funding event for a matched ICP account and emits a company-level update.
* **Enrich:** Clay appends revenue band, likely budget window, and relevant stakeholders.
* **Filter**: If the funding amount passes the threshold and matched stakeholders exist → QUALIFIED. If no contacts are found, Claude via MCP can analyze the company and suggest ideal roles to hunt.
* **Execute**: Qualified accounts are mass-imported to HeyReach as “Funding Event” leads.

**HeyReach config**

* **Campaign name format:** FP-Funding-{RoundType}-{MM} (FP = Funding Priority)
* **Tags:** Funding Event, Round:{Series}, Priority: High
* **Seat count:** 4–10 SDRs (rotate aggressively to hit multiple contacts); consider AM+SDR pairing.
* **Cadence timing & sequence structure:** Day 0 — personal outreach to known stakeholder → Day 1 — secondary touch from different sender (multi-sender rotation) → Day 3 — case study or ROI note → Day 7 — ask to meet. Use tighter pacing and higher touch density for the first 72 hours.

**Messaging template you can use:**

Congrats on the {round\_size} at {company\_name}!

Saw you’re scaling the {function\_team} — we’ve helped similar teams tighten outbound right after raising. Worth a 10-minute chat this week to share what’s working for them?

**Expected results**

* Connection acceptance: **25–45%**
* Reply rate: **10–20%**
* Booking rate: **3–9%**

**Troubleshooting**

1. **Issue:** No contacts found for the funded company — **cause**: incomplete enrichment. **Fix**: Enrich via Clay.
2. **Issue**: Duplicate leads entering campaign → **Fix**: Enable deduplication in Clay
3. **Issue**: Message feels generic → **Fix**: Add funding-specific hook (“post-raise hiring” or “expanding go-to-market”).
4. **Issue**: Too many leads at once → **Fix**: Use HeyReach seat rotation to spread the load.

**Pro tip:** Momentum dies fast. Aim to have outreach start within 12 hours of announcement.

### **Workflow 4: Decay / Inactive Signal — Recycle leads after 30+ days of inactivity**

**When to use:** When leads have gone inactive for 30+ days. Recycle into low-touch nurture instead of deletion.

**Signal strength:** Low but valuable for keeping your pipeline fresh.

**Tools required:** Clay + n8n + HeyReach

**Workflow:**

* **Trigger:** Clay identifies leads with “Last Signal >30 days.”
* **Enrich:** Pull any new activity or updates (company move, post engagement).
* **Filter**: Use Claude connected via MCP to auto-classify leads — NURTURE = keep light, REJECT = suppress.
* **Execute**: n8n routes NURTURE group into HeyReach’s “Long-Term Nurture” campaign.

**HeyReach config:**

* **Campaign**: Long-Term Nurture - {Quarter}
* **Tags**: Stale Signal, Reactivation, Low Priority
* **Seat count:** 1–2 SDRs (low volume)
* **Cadence:** 1-touch check-in every 30–45 days
* **Sequence structure:** Casual reconnect → Offer light value → Open door

**Message template you can use:**

**Option 1:** Hey {first\_name}, not sure if the timing's better now — saw {company\_name} has been quiet on {topic}. We’ve made a few updates since last time that might be relevant if {pain\_point} is still top of mind.”

**Option 2:** Hi {first\_name}, sharing a recent note on {topic} that has been helpful for teams at {peer\_company}. No pressure — thought it might be useful given your role at {company}. (link)

**Expected results:**

* Acceptance: 15–20%
* Reply: 10–12%
* Booking: 3–5%

**Troubleshooting:**

* **Old profiles** → *Fix:* Re-enrich quarterly.
* **Low conversion** → *Fix:* Test casual tone; don’t push for a call too soon.

**Pro tip:** If they later show a new signal, like a job change, funding, or pricing visit,  re-route them right back into a high-priority flow immediately.

**Note:** MCP doesn’t run automations by itself. It’s the protocol that allows an AI agent like Claude to plug into your GTM tools and act on your prompts; classifying leads, enriching data, or triggering outreach across multiple systems, without you doing it manually.

> *Deep dive:* [How to automate LinkedIn messaging at scale](https://www.heyreach.io/blog/linkedin-message-automation)

## **Personalize by signal to lift replies: 4 plug-and-play openers**

Personalization is how you turn a buying signal into a real conversation.

Each signal gives you context and that’s your edge.

Your goal is to show an understanding of timing and relevance:

“I saw this, I understand what it means for you, and I have something that can help right now.”

I have written four ready-to-use openers you can drop directly into HeyReach campaigns to [scale your outbound motion](https://www.heyreach.io/blog/outbound-sales-automation).

Each follows three rules:

1. Reference the specific signal that triggered your outreach.
2. Tie it to an opportunity or pain that comes with that event.
3. Keep the tone human, conversational, and brief.

### **1. Funding round**

**When to use:** Right after Clay, Trigify, or Crunchbase detects a new round size announcement from a company that fits your ICP.

**Signal context:** Fresh funding means hiring, scaling, and tool evaluation. This is when buyers are most open to new conversations.

**Opener template:**

“Congrats on the {round\_size} raise, {first\_name}! Most teams we talk to start scaling ops and outbound right after a round — are you already building that motion out at {company}?”

**Why this works:** It acknowledges their big moment (funding) and subtly connects your value to their next logical step which is growth enablement.

**Pro tip:** Pair this opener with a “**Funding Event**” tag in HeyReach and use a “fast-track” campaign cadence (3 touches over 5 days) to ride the momentum wave.

### **2. Job change**

**When to use:** When your detection tools flag that a previous lead or prospect just moved to {new\_company}, especially if they’re now in a more senior or decision-making role.

**Signal context:** A new role is a natural reset point. They’re evaluating tools, rebuilding processes, and are open to familiar solutions that make them look good early.

**Opener:**

“Congrats on joining {new\_company}, {first\_name}! Those first 90 days are all about quick wins — are you rethinking your {function} stack or keeping what worked from your last role?”

**Why this works:** It celebrates the milestone, signals awareness, and invites them to talk about their priorities without pressure. You’re showing up at a moment when they’re forming new vendor opinions or comparing options.

### **3. Website visit**

**When to use:** When RB2B or your site tracking tool shows multiple visits from the same company to key pages like your pricing page or demo pages.

**Signal context:** Someone’s comparing options or convincing internal stakeholders. You are top of mind right now. Speed matters here.

**Opener:**

“Hey {first\_name}, noticed {company} checking out the {page\_visited} page a few times. Happy to share how teams like yours usually approach {specific\_pain\_point} once they hit that stage — want a quick walkthrough?”

**Why it works:** It frames the outreach as helpful and time-sensitive. It’s a “we can make your next step easier.” move which most prospects are likely to be open to.

**Pro tip:** Use the “**High Intent Visit**” tag in HeyReach and trigger a same-day “Warm Nurture” sequence. Combine this with a Slack alert for the assigned AE so they can follow up manually within hours.

### **4. Signal decay**

**When to use:** When Clay shows a lead has gone quiet for 30+ days or missed multiple touches in your outreach sequence.

**Signal context:** Silence doesn’t mean disinterest. Most of the time, timing just wasn’t right. Bringing them back with context keeps your brand warm.

**Opener Template:**

“Hey {first\_name}, popping back up since it’s been a bit — looks like we last connected around  {last\_touch\_date}. A lot’s changed since then. Want me to send a quick update on what’s new in {your\_product}?”

**Why this works:** It reopens the door politely, shows awareness of history, and resets the relationship without sounding desperate.

**Pro tip:** Each of these openers can live as reusable templates inside HeyReach.

Tag by signal type: ”**Funding Event, Re-Entry Lead, High Intent Visit, Stale Signal”** and compare reply, acceptance, and booking rates across campaigns.

Over time, you’ll see which signal delivers the highest return and double down on what works.

## **Noise blockers: filters that keep low-value signals out of campaigns**

One of the biggest hidden drains on SDR capacity and sender reputation in high-volume outbound or demand gen operations is noise; weak, stale, or irrelevant signals that slip through into campaigns.

These low-fit contacts distract your reps, inflate bounce rates, and erode deliverability over time.

In practice, you cannot trust every signal to be “hot” or right enough to pursue.

Your goal is to have only high-fit, fresh signals ever hit your campaign engine. Everything else is tagged, suppressed, or routed away. And yes, failed signals are not deleted. You tag & route them to review or long-term nurture.

I’ve seen teams double their response rates just by enforcing this three-layer model:

* Clean detection,
* Intelligent filtering, and
* Tight execution gates.

These filters act as guardrails that help you turn a noisy signal system into a revenue machine.

### **Filter layer 1 — Clay: rules-based ICP & hygiene guardrails**

This is your baseline “screening funnel.” At this stage, you want to drop the obvious mismatches and preserve SDR time and goodwill. These should be implemented at ingestion or just before campaign injection.

**Typical filters/rules:**

* **Firmographics & size**: Only pass leads whose company size, revenue band, and number of employees match your ICP.
* **Industry / vertical include/exclude**: Allow industries you target; block those you never serve (e.g., “education,” “nonprofit,” etc.).
* **Title/seniority includes & excludes**: e.g. include “VP, Director, Head, C-level”; exclude junior roles like “Associate,” “Intern,” etc.
* **Geography**: Only allow countries/regions you operate in.
* **Tech fit/tech stack**: (If available) require the presence of certain tools to assure compatibility.
* **Freshness**: Reject leads whose last touch or signal is older than a threshold (For example, greater than 180 days).
* **Dedupe & suppression lists**: Exclude people you’ve already closed, blacklisted domains, or known non-buyers.
* **Rejected reason tagging**: When a lead is blocked, tag it with the reason (e.g. SizeMismatch, NotICPIndustry, TitleExcluded)  for analytics and review later.

If a lead fails any of these, flag it as “Rejected at Layer 1” and route out to review or nurture. Only those passing all rules proceed to Layer 2.

### **Filter layer 2 — MCP + Claude (optional intelligence layer for edge cases/volume)**

Once your rules-based layer is solid, you can add a lightweight AI-powered classification step for signals that don’t clearly pass or fail. This is especially useful when volumes are high or when titles are ambiguous.

**What you do here:**

* For any lead that passed Layer 1 but still sits in a “gray zone” — e.g. borderline cases. For example, titles like “Lead,” “Manager,” “Consultant” or when rule-based filters are too noisy, unusual company profile, or limited behavioral signals.
* The model should output **one of three classes**:

* **QUALIFIED** — passes to execution
* **NURTURE** — not fit now; route to a nurture track
* **REJECT** — discard from active campaigns

* Also log the reason/decision text so you can later audit or retrain (e.g. “model: low engagement score,” “model: title ambiguous,” etc.)

This layer is optional if your volume is low, you might skip it.

But in high-volume operations, an intelligent layer can reduce false positives and avoid over-filtering. It is also helpful for giving nuance beyond rigid rules, especially for edge signals like “Head of Ops,” “Strategy,” or ambiguous industry tags.

### **Filter layer 3 — HeyReach execution gates & pacing controls**

Once a lead passes Layer 1 and (optionally) Layer 2, execution filtering protects your sending infrastructure, SDR capacity, and campaign integrity.

**Execution gates & controls in HeyReach:**

* **Campaign includes/excludes:** Don’t allow a lead to enroll in a campaign if they match an exclude tag (e.g. Stale Signal) or already exist in a conflicting campaign.
* **Tag-based routing with exact casing**: e.g. “Funding Event, Re-Entry Lead, High Intent Visit”. Use consistent tag names to direct campaign logic cleanly.
* **Recency gate**: Prevent touching the same lead more than once within a defined cooldown window (e.g. 14 days).
* **Seat rotation & assignment rules**: Spread leads evenly across SDRs to avoid saturation, and avoid assigning multiple leads in the same domain to the same seat.
* **Daily send caps/pacing limits**: Each seat has a safe daily limit; campaign pacing must not exceed thresholds.
* **Auto-pause on reply/engagement**: If a lead replies, unsubscribes, or books, auto-pause further touches in that campaign.

This layer ensures that even qualified leads don’t overwhelm your SDRs or violate sending best practices.

### **Why filtering matters in scaling outbound**

As reported in multiple “speed-to-lead” studies, B2B teams average 42 42-hour response time to new leads, and at [least 38% of those leads never respond](https://www.chilipiper.com/article/speed-to-lead-statistics) at all. Meanwhile, leads contacted within the first few minutes are [21× more likely to qualify](https://timetoreply.com/blog/lead-response-time/) than those delayed 30 minutes or more.

If you don’t filter, you overload SDRs and they become slower.

### **How to manage fail-safe/fallback routing**

No signal should ever be deleted silently. If a lead is filtered out at any layer, move it to a **Review** or **Long-Term Nurture** queue:

* Tag it (e.g. Rejected: TitleMismatch, Nurture: LowConfidence)
* Record metadata (reason, timestamp)
* Allow re-promotion if a stronger signal triggers later (funding, job change, pricing visit)

This preserves lead equity and ensures you don’t lose out on someone who becomes eligible later.

## **Track results by signal and optimize what works**

By tagging every sequence with its source signal, measuring KPIs per tag, and running tight “if-then” iteration loops, your team can move from guessing to precision GTM ops.

You’ll know exactly:

* Which signals convert fastest,
* Which need better targeting, and
* When to pull back or double down.

### **What to track by system**

Each tool in your stack gives a different lens into signal quality.

**HeyReach — Track reply health, engagement & sender performance:**

* **Replies/acceptance/meetings by signal tag**: This is your bread and butter. For example, you may find that a ”Funding Event” triggers 15% replies, while a “Website Visit” only generates 4%. That tells you where to focus SDR energy.
* **Sender health metrics**: monitor bounce rates, unsubscribe rates, and seat rotation utilization. A healthy sender reputation ensures your high-value signals actually reach inboxes.

**Clay — signal quality & hygiene:**

* **Freshness**: Were signals acted on quickly enough? Typically, signals older than 24–48 hours decay rapidly.
* **Enrichment rate**: Are you collecting all the personalization fields (title, company, size, recent activity) needed for effective outreach?
* **Pass-through rate**: How many signals actually make it through your filters and get sent to HeyReach? A high pass-through but low reply rate means the data is clean, but the signal might be weak. A low pass-through means you need to tighten enrichment logic or expand data sources.

**Alerts/notifications:**

* Use Slack pings for high-value triggers especially for high-value signals such as new funding, tech change, and leadership hire. This keeps GTM teams close to intent as it happens and lets reps jump in fast while the signal is still warm.

### **Test and iterate by signal: A/B examples**

Find what combination of timing and messaging actually drives replies and meetings and track each variant by signal tag, not just by campaign.

Two simple examples:

**A/B for Funding Events → Tone test**

* **Variant A:** Congratulatory openers — “Congrats on the {round\_size} raise, {first\_name}! Scaling fast? Here’s how teams like yours accelerate outbound.”
* **Variant B:** Straight to value openers — “Nice work on {round\_size}! Building a pipeline from scratch? Let’s chat about ways to move fast.”

Compare reply rates and meetings booked per variant.

**A/B for High-Intent Visits → Timing test**

* Variant A: Trigger send within 1 hour of visit
* Variant B: Wait 24 hours and reference their visit context

The faster trigger usually wins but tracking per tag helps you confirm, not assume.

### **KPI table: track signal-specific performance**

This table gives you a template you can create for your team to have:

* A signal-by-signal scoreboard of performance and data hygiene.
* Clear SLA expectations for how fast each type of signal should trigger.
* A base for automation: if a signal falls below its SLA or KPI, trigger a workflow to fix it.

## **How to turn metrics into fast iterations**

Iteration speed is the moat. Discipline beats creativity here.

You don’t need fancy dashboards, just simple “if-then” rules tied to the metrics above:

1. If reply <5% for 2 weeks → tighten ICP filters. Exclude marginal titles, old leads, or irrelevant industries, or change messaging angles.
2. If the meeting rate is <3% for 2 weeks → adjust your sequence cadence or revise your message template for each signal.
3. If conversion <0.5% for 2 weeks → revisit value proposition; consider testing new personalization variables (e.g., {recent\_funding}, {page\_visited}).
4. If freshness >12h for high-intent visits → shorten automation delay or review Clay-to-HeyReach sync.
5. If enrichment rate <85% → adjust enrichment sources or update Clay recipe logic.
6. If sender health drops → reduce volume for 24h and warm domains back up before continuing.

Each rule keeps iteration predictable, not reactive, and gives you a repeatable way to measure, analyze, and optimize without getting lost in guesswork.

### **Pro tips for fast iteration**

* **Weekly review cycles:** Check metrics by signal weekly. Small intentional tweaks compound fast.
* **Tag consistently:** Keep your tag casing exact (Funding Event, Re-Entry Lead) so reporting is clean and actionable.
* **Log changes:** Record adjustments to filters, messaging, and cadence. Over time, this builds a “playbook of what works.”
* **Automate alerts:** Turn on Slack notifications for high-value triggers to make sure no signal goes unacted upon.

## **Avoid the common pitfalls in signal automation**

Most signal automation setups fail because operators automate noise. The fix is discipline: set thresholds, enforce SLAs, and layer filters so only high-value signals trigger actions.

Even the best signal workflows can fail if you fall into predictable traps such as:

1. **Dumping every “like” or click into campaigns**

Every signal is not equal. Some teams dump all website visits, LinkedIn likes, or social engagement events straight into campaigns. This floods SDRs and dilutes focus.

One SaaS team added every product page visit to their outreach list. SDRs spent hours chasing low-intent visitors. Replies dropped below 5%.

**How to fix:**

* Set minimum engagement thresholds before triggering a workflow (e.g., 2+ pricing page visits or a funding announcement).
* Route only high-value signals to active campaigns; low-value signals go to a long-term nurture queue.

### **2. Skipping ICP or title filters**

A frequent operator mistake is sending signals directly to outreach without revalidating the ICP.

Without filtering by company size, industry, or role, leads may look active but aren’t decision-makers.

Example: a “Funding Event” trigger sends every employee from a newly funded company including interns.

**How to fix:**

* Layer Clay rules for strict inclusion/exclusion. Always apply a title or seniority filter in Clay (e.g., “Head of Growth,” “CTO,” etc)
* Use Claude via MCP connection for edge cases when volume is high or roles are ambiguous. It analyzes signals and context, then returns a classification tag.
* Always tag rejected leads with reasons (TitleExcluded, IndustryMismatch) so they can be revisited if the criteria change.

### **3. Acting too late after the 24–48h window**

Intent has a half-life.  Wait more than 48 hours, and even the strongest signals will fade.
For example: a prospect viewed your pricing page on Monday but got your outreach on Thursday. By the time your SDR contacts the lead, they have likely moved on or set up a meeting with a competitor.

**How to fix:**

* Enforce SLA: Trigger → enrich  → filter → execute within 24 hours.
* Use n8n, Make/Zapier, or direct webhooks to automate the handoff from detection to HeyReach campaigns.
* Build alerts in Slack when delays exceed SLA so ops can fix bottlenecks fast.

### **4. Treating all signals equally**

Not all signals deserve equal attention. A “Funding Event” usually converts 2–3x better than a “Website Visit.”
**How to fix:**

* Assign weight or priority scores to each tag (Funding = 3, Visit = 1, Re-Entry = 2).
* Route high-weight signals to your best senders or faster sequences.
  This ensures SDR capacity goes where ROI is highest.

### **5. Ignoring data decay**

Enriched data doesn’t stay valid forever.
Example: a contact’s job title changed two weeks ago, but your system still shows “VP Sales.”

**How to fix:**

* Re-enrich key signals weekly in Clay.
* Auto-retire signals older than 14 days unless revalidated.
  This prevents SDRs from sending stale or inaccurate messages.

### **6. Over-automating without QA**

Automation can easily spiral if you never spot-check.
Example: an automation loop mistakenly sends 30 “Congrats on your funding” messages to the same founder because of duplicate signals.

**How to fix:**

* Add a QA step; one person reviews signals daily before the final push.
* Use Clay’s deduplication and tagging to detect repeats.

### **7. Ignoring execution limits**

Overloading SDRs or violating daily send limits can hurt sender health and deliverability.

**How to fix:**

* Use HeyReach execution gates: pacing caps, recency thresholds, seat rotation, and auto-pause on replies.
* Keep campaigns balanced; high-intent signals move faster, low-intent signals slower.

## **Put this signal-to-campaign playbook into action**

Here’s a realistic roadmap to take your buying-intent signals from detection to LinkedIn execution within 1–2 weeks:

### **Week 1 — Setup & signal mapping**

1. **Map your signals**: List all high-value signals (Funding, Job Change, High-Intent Website Visits, Signal Decay).
2. Assign detection tool (Clay, Trigify, RB2B) and HeyReach campaign.
3. **Define your filters**: Layer Clay rules for ICP, titles, industry, geo, and enrichment.
4. **Set SLAs & execution gates**: Decide recency thresholds, seat rotation, daily send limits, and pacing caps. Ensure **Trigger → Enrich → Filter → Execute** can happen within 24–48h.
5. **Create personalization templates**: One opener per signal with variables ready for HeyReach merge fields.

### **Week 2 — Automation & early testing**

1. **Build your workflows**: Use n8n or Make/Zapier to automate the handoff from detection tools to HeyReach campaigns. Include Slack alerts for high-priority triggers.
2. **Test & iterate**: Run a small batch of each signal type through the workflow. Track reply, meeting, and conversion rates by tag (**Funding Event, Re-Entry Lead, etc.).**
3. **Refine filters & messaging**: Adjust thresholds, sequence cadence, or opener templates based on early performance.
4. **Document & repeat**: Keep a log of changes, decisions, and results to make the system repeatable and scalable.

**Pro tip:** Start small. A reliable 50-lead workflow beats a messy 500-lead automation every time. Scale as your workflows prove reliable.

## **Turn those signals into action today**

Don’t wait for another lead to slip through the cracks. Your SDR team can stop chasing noise and start engaging leads while the signals are still hot.

Use this playbook to:

* Detect buying intent signals early.
* Route high-value leads into real-time LinkedIn campaigns.
* Personalize outreach with signal-specific templates.
* Measure, iterate, and optimize by signal tag.

[**Test this yourself on a free trial**](https://app.heyreach.io/account/register)and put your signal-to-campaign workflows into action.

‍
