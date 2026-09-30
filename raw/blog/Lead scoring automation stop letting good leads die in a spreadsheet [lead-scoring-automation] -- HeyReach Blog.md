# Lead scoring automation: stop letting good leads die in a spreadsheet

Source: https://www.heyreach.io/blog/lead-scoring-automation

Summary: Lead scoring automation turns enriched data into booked meetings. Score on fit, read intent for timing, and route leads into HeyReach with GPT, no dev needed.

Your team spent real money enriching these leads. You know their job titles, company size, tech stack, and even the content they clicked. And then the whole thing just sits there.

No score. No priority. No routing. The data piles up while your reps keep working off gut feel and whoever shouted loudest in the last pipeline meeting.

This is the **execution bottleneck**, the quiet gap between knowing who a lead is and actually doing something about it. Most teams never close it. Leads get enriched but never scored, scored but never prioritized, prioritized but still [routed](https://www.heyreach.io/blog/lead-routing) by hand.

Lead scoring automation is how you close that gap. I’ll show you how to build **lead-scoring** **system** that scores every lead on fit, reads real-time intent, and routes the right people to the right HeyReach campaign automatically. No developer, no CSV gymnastics, about thirty minutes to a working version.

## Step 1: Score leads using a predictive model and real-time signals

Turn flat enrichment into decision-ready leads with an automated, predictive lead scoring model.

We will use a simple logic layer powered by GPT plus real-time intent signals to [score leads](https://www.heyreach.io/blog/make-integration) based on context, not guesswork.

### Why this lead scoring logic works

Instead of relying on rigid, rules-based scoring (think: if job title contains VP, add 10 points), GPT evaluates the full lead context: title, company size, tech stack, and engagement behavior.

Then it outputs a relevance score your sales team can act on, which shortens sales cycles and improves conversion rates.

**Example:**

* Marketing Manager at a 500-person SaaS using HubSpot, with a spike in website visits or a webinar registration. Score: **High**
* Founder at a 2-person agency using Mailchimp, no recent activity. Score: **Low**

### Prompt logic, in plain English

*“Based on company size, industry, job title, and tech stack, rank this lead’s likelihood to be a good fit for our [ICP]. Output: High, Medium, or Low.”*

**Add a modifier for urgency:**

*“If they have visited the site in the past 48 hours or opened 2 or more emails, mark as Urgent.”*

### How does this lead scoring model plug into your system?

You do not need a developer. This can run in:

* **Airtable:** store enriched lead data plus scoring output.
* **Sheets:** prompt GPT to score directly via a GPT extension or [Make](https://www.heyreach.io/integration/make).
* **Slack:** push High and Urgent leads to sales reps in real time.
* **HeyReach:** auto-segments leads into outreach campaigns based on score to sharpen targeting.

**With Origami plus Factors, it is even easier:**

* **Origami** handles prompt execution and scoring logic in the background.
* **Factors** pulls in enrichment plus real-time activity (visits, opens, clicks).

Let us break down how this combo works.

### Score with Origami

Origami takes the heavy lifting out of scoring by letting you run **no-code GPT** **prompts on your enriched data**. No custom scripts. No developer needed. Set the logic once, and Origami scores every new lead automatically in the background.

### Why automated lead scoring with Origami works

You can build scoring rules that are as simple or as advanced as you want.

* For example, give each lead a score from 0 to 100 based on persona fit, engagement recency, and ICP match.

Origami looks at everything you feed it (job title, seniority, company size, industry, tech stack, behavioral data, past activity) and applies your scoring logic instantly to surface [high-intent leads](https://www.heyreach.io/blog/high-intent-leads) and real opportunities.

### How to set up lead scoring in Origami

1. Pick your scoring inputs, for example, title, seniority, company size, industry, demographic information, ICP keywords, and recent engagement.
2. **Write your GPT prompt in plain English. Examples:**
   1. *“Score this lead from 0 to 100 based on how closely they match our ideal customer profile. Prioritize VP or C-level roles at SaaS companies with 200 to 1000 employees.”*
   2. *“If the lead visited our pricing page in the last 7 days, add 20 points. If they opened 3 or more emails in the last 14 days, add 10 points.”*
   3. *“If their tech stack includes HubSpot or Salesforce, add 15 points. If their industry is not on our ICP list, subtract 30 points.”*
3. Add fallback logic, for example: if any required field is missing, assign a default score of 50 or send to manual review.

**Pro tip:** Origami plays nicely with Factors, Airtable, and HeyReach, so once a score is generated, High leads can be routed instantly to the right campaign, rep, or workflow without you lifting a finger.

### Add intent triggers using Factors

Factors gives you [real-time buyer intent signals](https://www.heyreach.io/playbook/real-time-buying-signals): things like job changes, tech installs, new hires, social engagement, and other activity that screams “something is happening over here.”

These are not nice-to-have data points. They are urgency flags that tell you when to move now versus when to hold back.

### Why intent matters for lead scoring

Scoring alone tells you **which** qualified leads to target. Intent signals tell you **when**. When you combine Factors’ [signal-based](https://www.heyreach.io/blog/signal-based-outbound) data with Origami’s AI lead scoring, you get a logic layer far more dynamic than traditional lead scoring tools or basic marketing automation.

It shows your team where to direct effort next based on real touchpoints, which speeds up conversion and leads to better [prioritization](https://www.heyreach.io/blog/lead-prioritization) and more accurate pipeline forecasting.

### Example logic for lead scoring

* **High score plus job change**: tag as Demo-ready. Trigger instant outreach.
* **Medium score plus tech install**: tag as Nurture. Keep them warm until the timing is right.
* **Low score plus no signals**: tag as Deprioritize. Do not waste time here.

#### How it works together

* Origami scores leads based on fit.
* Factors monitors them in real time for urgency signals.
* The combined logic routes leads into the right bucket automatically: your hot-lead campaign, a nurture sequence, or the back burner.

When your scoring system understands both fit and timing, you finally stop chasing ghosts.

### Create a lead decision matrix

Once you have fit from Origami’s scoring and timing from Factors’ intent signals, you need a clear way to decide where each lead goes next. That is your lead decision matrix, sometimes called a **lead scoring matrix**.

Think of it as your if/then routing table, the brain of your system.

Without it, you are just collecting scores and signals without a plan to act on them, leaving your sales process reactive.

Here’s a simple reference of lead decision matrix you can model:

### How the lead decision matrix works

* **High score plus signal**: strike while the iron is hot. Send straight to your HeyReach demo-ready sequence.
* **Medium score plus signal**: stay on their radar. Move into your nurture campaign.
* **Low score plus no signal**: do not waste cycles. Log them for later review or enrichment.

This keeps your routing clean and aligned with the entire customer journey.

## Step 2: Build a filterable lead queue in Sheets or Airtable

This is where scored and tagged leads turn into a clean, organized queue, so ops teams can quickly filter, sort, and kick off outreach. Picture it as an execution layer, the bridge between your scoring logic and your campaign triggers.

### Use Smart Views to segment leads

Smart Views make it simple to surface the right leads at the right time. By filtering on score and intent signals, you can instantly see who to route, who to nurture, and who to enrich. This is a [lead qualification](https://www.heyreach.io/blog/lead-qualification-process) you can run at a glance.

**There are three Smart Views you can set up:**

**High Priority**

* **Filters:** Score 90 or higher AND a signal present (job change, tech install, or new hire).
* **Next step:** Route immediately to your demo-ready HeyReach campaign to engage sales-ready leads.

**Campaign-Ready**

* **Filters:** Score 60 to 89 (signal optional).
* **Next step:** Add to your nurture sequence to [keep them warm](https://www.heyreach.io/blog/warm-leads) until they show stronger intent.

**Needs Enrichment**

* **Filters:** Score missing or under 60, OR missing firmographic fields such as company size or industry.
* **Next step:** Hold for enrichment, add missing data, or send to manual review before routing.

### Map leads to campaign destinations

Before you flip the automation switch, you need a clear, pre-baked routing plan for every lead in your queue. The easiest way? Add a Campaign ID column to your Sheet or Airtable base. That column tells your automation tool exactly where each lead should go, with no guessing and no manual sorting later.

### Why it matters

When routing logic is built into the queue itself, your team does not stop to decide on campaigns one lead at a time. That keeps qualification consistent and prevents the bottlenecks that pop up between sales and marketing. It also makes integrations with tools like Pabbly smoother, since you are passing clean, pre-assigned campaign IDs straight into the automation flow, and it makes routing decisions easy to tie back to downstream metrics.

### How to set it up

1. Add a Campaign ID column next to your score and signal columns.
2. Use simple rules to assign campaign IDs automatically:
   * Score 90 or higher to DEMO\_01 (demo-ready campaign).
   * Score 60 to 89 to NURTURE\_01 (nurture campaign).
   * Score under 60 to SKIP or HOLD (no outreach).
3. For leads missing a score or an ICP match, tag them ENRICH so they get reviewed before going anywhere.

**Pro tip:** Lock these rules into your team’s workflow so everyone uses the same scoring criteria. Consistency here means less cleanup later and a faster automation handoff.

With Campaign IDs assigned, your queue is automation-ready. All that is left is connecting it to [Pabbly](https://www.heyreach.io/blog/pabbly-integration), so let us dive into that.

## Step 3: Route leads into HeyReach via Pabbly

Once you have a filterable lead queue with campaign tags, it is time to put that logic into motion. The goal is simple: automatically send the right leads to the right HeyReach campaign without touching a single row by hand.

Pabbly connects directly to Google Sheets or Airtable, integrates with HeyReach through native triggers and webhooks, and supports if/then routing rules with its built-in filters and path routers.

### Pabbly routing flow

Here is a simple lead management flow you can set up and replicate:

1. **Trigger:** a new row is added (or a tag is updated) in your Sheet or Airtable.
2. **Filter:** score at or above your threshold AND a signal present.
3. **Action:** send the lead to HeyReach.
4. **Assign campaign:** use the Campaign ID from your queue.
5. **Assign seat:** route to the right rep’s HeyReach seat.
6. **Tag for reporting:** add tracking tags so you can monitor performance by campaign and lead source.
7. **Fallback logic:** if a lead is tagged ENRICH or HOLD, stop the flow and send it to a review list instead.

## Step 4: Add fallback logic to handle uncertain leads

Not every lead slides neatly into your routing logic. Some land in the maybe zone: medium fit, weak intent signals, or missing data. Others look good on paper but reveal a mismatch once outreach starts. Fallback logic keeps these edge cases from slipping through the cracks and protects outreach quality at scale.

### Handle gray-zone leads before sending

Before a lead ever hits a campaign, use GPT logic (via Origami or similar) to answer one question: should I route, skip, or hold?

**Example decision rules:**

By standardizing these gray-zone decisions, you avoid random routing and keep your outreach clean and focused.

### Classify replies and trigger smart actions

Once replies start coming in, automation can help decide the next move. Using GPT (via Origami, for instance), classify responses into categories like:

* **Interested**: pause campaigns and send high-value leads straight to an [AE for handoff](https://www.heyreach.io/blog/sales-handoff).
* **Objection**: route to an AE for follow-up.
* **Not now**: move to a nurture campaign.
* **Referral**: enrich with new contact details and restart scoring.

**Note:** This classification logic typically runs outside of HeyReach using tools like Origami, Zapier, or even manual tagging. Done right, it closes the loop between scoring, routing, and follow-up so every lead gets the right next step.

## Build the full routing system in 30 minutes, start to finish

Let us make this real. Here is your quick-start blueprint, a six-step walkthrough that connects every tool and logic layer into one executable sales funnel workflow.

**Use this routing system to:**

* Build your MVP version in under 30 minutes.
* Clarify sequencing across tools (Origami to Factors to Sheets/Airtable to Pabbly to HeyReach).
* Hand off to a teammate or use it as your ops checklist.
* Plug in templates (Sheet/Airtable base, GPT prompt, fallback matrix) for an even faster setup.

### Step 1: Score leads in Origami using GPT logic

* Use enriched fields like job title, seniority, company size, and ICP keywords.
* Prompt GPT to return a score between 0 and 100.
* Tag this as Score in your Sheet or Airtable base.
* Optional: add fallback logic, tagging as HOLD if any key fields are missing.

### Step 2: Check real-time buyer signals via Factors

* Look for intent signals like job changes, tech installs, or hiring alerts.
* Tag as Intent based on signal type.
* Example: Job Change equals high urgency, No Signal equals low urgency.

### Step 3: Send scored and tagged leads to Airtable or Sheets

* **Include these key columns:** Lead Name, Score (from Origami), Intent (from Factors), Campaign ID (based on routing logic).
* **Sample mapping:** Score 90 or higher plus Intent to DEMO; Score 60 to 89 to NURTURE; Score under 60 or incomplete to ENRICH or HOLD.
* Use a downloadable base with pre-set filters, views, and mock data to speed this up.

### Step 4: Set up Pabbly automation to route leads

* **Trigger:** a new row added or updated in Airtable/Sheets.
* **Filter:** score at or above your threshold AND intent present.
* **Action:** send to a HeyReach campaign (based on Campaign ID), assign an available seat, and add tracking tags.
* Optional: add a fallback branch so that if Campaign ID equals HOLD, routing is skipped.

### Step 5: Launch the campaign in HeyReach

* Leads now enter the assigned campaign automatically.
* No CSV uploads, no manual sorting. Just filtered, tagged, and routed.

### Step 6: Monitor replies and act based on classification

* Pause the campaign for leads showing strong interest.
* Route objections to an AE for follow-up.
* Move Not now responses into a nurture sequence.
* Use a GPT workflow (via Origami) to classify replies and flag them in Sheets or Airtable for review.

## What to build next

Once your MVP is live and running smoothly, you can layer in upgrades that make the system smarter, faster, and more dynamic. A few high-impact next steps:

* **Re-score leads every 7 days**: keep scores fresh by pulling in new activity, firmographic updates, and engagement data. A lead that was cold last week could be hot today.
* **Sync CRM stages to HeyReach campaigns**: automatically move leads between campaigns based on pipeline stage changes using [lead status synchronization](https://www.heyreach.io/blog/lead-status-synchronization).
* **Trigger re-engagement when warm signals fire**: if a cold lead visits your pricing page or starts hiring again, route them into a fresh sequence with [trigger-based outreach](https://www.heyreach.io/blog/trigger-based-outreach).
* **Send Slack alerts for hot leads**: push instant notifications to sales when high-priority leads enter the queue or show strong intent.
* **Post-call automation**: after a rep logs a call in your CRM, automatically update the lead’s status, trigger follow-ups, or kick off the next outreach step.

The goal is to take your [rock-solid base system](https://www.heyreach.io/blog/sales-tech-stack) and evolve it into a fully connected growth engine in which scoring, routing, and re-engagement all run on autopilot.

## Turn lead scoring into a growth lever

[Smart outbound](https://www.heyreach.io/blog/make-integration) needs the right mix of signals, filters, predictive scoring, and a few well-structured GPT prompts. With Origami scoring, Factors intent signals, a filterable lead queue, Pabbly routing, and HeyReach campaigns, you have everything you need to move from static data to live, revenue-ready conversations.

Package these elements into a simple toolkit alongside your other [lead scoring tools](https://www.heyreach.io/blog/lead-generation-tools), and you have a repeatable, automated system anyone on your team can run. When every step is connected, your outbound machine runs faster, hits harder, and wastes zero time on anything but your best leads.

[Schedule a 1:1 strategic call](https://cal.com/nadjakomnenic/discovery) to walk through your setup, fine-tune your scoring logic, or explore how to take this framework even further.
