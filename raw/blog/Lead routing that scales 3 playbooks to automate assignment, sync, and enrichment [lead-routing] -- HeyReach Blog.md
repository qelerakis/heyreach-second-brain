# Lead routing that scales: 3 playbooks to automate assignment, sync, and enrichment

Source: https://www.heyreach.io/blog/lead-routing

Summary: Lead routing that scales: 3 playbooks to automate assignment, sync, and enrichment

You’re juggling 5–15 LinkedIn seats, 3+ lead sources, at least 2 outbound tools, plus marketing automation you can barely keep up with. And instead of building a proper lead routing system, you’re left duct-taping spreadsheets, ignoring service agreements, battling sync issues, and guessing who should send what, when.

Your problem isn’t the messaging; it’s the routing system. Basically, the lack of one.

That’s what we fix in this article. We'll give you three modular playbooks: each built to automate a critical part of your lead routing engine using HeyReach + Make.

These follow lead routing best practices to ensure each incoming lead reaches the right rep at the right time. Get ready to move faster, scale safely, and never guess what goes where again.

## Why lead routing breaks most outbound systems (and how to fix it)

Outbound doesn’t always break because of bad messaging… sometimes it breaks earlier, when an effective lead routing strategy isn’t in place.

Things start to fall apart before your message even lands, because the lead assignment rules that decide who gets what, when, and *from whom* isn’t built to scale — and there’s no system for account matching to ensure fit.

Here’s how that happens:

* **You’re still assigning senders manually (with no lead assignment rules or round robin setup):** Even with automation tools, teams end up using spreadsheets and Slack threads to decide who sends what.
* **One account gets flagged while others sit idle:** Overused seats hit limits. Underused ones waste the budget. Outreach gets lopsided and risky.
* **Leads fall through the cracks:** This delay kills speed to lead and hurts conversion rates, especially when there’s no clear account owner or fallback. Inbound leads wait in Google Sheets. Enrichment gets skipped. CRM syncs fail silently. Nobody (can) follow up in time.
* **Campaigns trigger too late, or from the wrong sender:** Messages go out cold, mismatched to persona, timing, or funnel stage.

### These playbooks fix that. One link at a time.

We reverse-engineered all these failure points into modular workflows you can drop into your stack today.

* Playbook #1: Account Rotation
  → Fixes overused/inactive sender problem with smart lead distribution and seat rotation logic
* Playbook #2: CRM-to-Outreach Sync
  → Fixes timing and delay problems — leads are added to the right campaign instantly
* Playbook #3: Enrich Before You Outreach
  → Fixes message mismatch by qualifying and routing leads based on enriched persona data.

Each playbook comes with prebuilt [Make scenarios](https://www.heyreach.io/make-scenarios), campaign-level routing logic, and dynamic field mapping. Your team can launch fast, scale safely, and stop relying on brittle manual processes.

## 3 plug-and-play workflows to fix outbound’s biggest lead routing gaps

Think of these like cheat codes for [scaling outbound](https://www.heyreach.io/blog/outbound-sales-automation) ops. Built from scratch, battle-tested, and ready to plug in. Let’s go!

### Playbook #1: Distribute leads across multiple LinkedIn accounts automatically

screenshot of the sender seat setup panel]

**Running outbound across 5+ LinkedIn accounts?** You’ve probably seen this:

* One inbox gets flooded, others stay idle
* Leads pile up unevenly
* Some senders hit limits while others go untouched

That’s not just inefficient, it’s risky. Overused accounts trigger flags. Underused seats waste the budget. Campaigns stall.

This playbook fixes that with an automated lead routing system using **HeyReach + Make**, designed to keep outreach safe, balanced, and scalable.

#### How it works (high-level)

Here’s the core flow:

* A lead enters via form, CRM, or Google Sheet
* The system checks who was used last and applies round robin logic for balanced lead assignment
* It assigns the lead to the next sender in the list
* Adds them to your HeyReach campaign under that sales rep or account owner
* Updates the sender log for next time

Simple logic. Smart scaling. Plus, this logic follows proven lead distribution strategies to keep the pipeline flowing evenly across team members. 😀

> 💡**Pro tip: Add persona-based lead routing**
>
> Here’s how:
> → Add a persona column to your intake Google Sheet (e.g., “PM”, “Sales”, “RevOps”)
> → Use Make’s **Router module** to match personas to specific senders
>
> Example:
> If persona = “Sales” → assign to Sender A
> If persona = “RevOps” → assign to Sender B
>
> This unlocks even safer scaling — especially when paired with your lead scoring system or CRM-defined customer profile, and when each sender specializes in a specific audience or handles leads with distinct needs.

#### What you’ll need

* A **Make account** (Free or Pro)
* A **Google Sheet** with preformatted fields
* Your **HeyReach API key** + campaign ID
* **HeyReach sender\_account\_ids** (one per active seat)
* Optional: Slack or Gmail module for alerts

#### Grab the setup pack

* ✅ [Copy the [Lead Rotation Sheet](https://docs.google.com/spreadsheets/d/1cgr1dq68HcMbZUbXILUMnr6rPxlCqkKQTuQiV-Lx-WY/edit) – with persona lead routing field]
* ✅ [ [Setup Guide – Walkthrough in Notion](https://heyreach.notion.site/Playbook-1-Distribute-Leads-Across-Multiple-LinkedIn-Accounts-Automatically-22609c3bcad38049a1a8e78926b5b4b3)]
* ✅ [Clone the Make Scenario – with Round-Robin + persona lead routing]

You’ll get a ready-to-copy Google Sheet inside the Rotation Pack with all required fields (like first\_name, linkedin\_url, campaign\_id, and sender\_account\_id) already set up — so there’s no guesswork.

**Default setup** uses:
 → Google Sheets as lead intake
 → Make Router + HeyReach API

### **Customize This for Your Stack:**

**🛠 Using Airtable instead of Google Sheets?** Swap the **Google Sheets module** for the **Airtable “Watch Records”** module.
 Everything else — rotation logic, sender assignment, and HeyReach API call — stays exactly the same.

[Bonus] Want to trigger this from a form instead? Connect Typeform or Tally via Make's webhook or native module, then pipe responses into the same rotation logic.

This way, the logic remains modular, only the lead source changes.

### Playbook #2: Trigger outreach directly from your CRM or form tool

Automatically routes incoming leads from CRMs or forms using proven lead routing tools to the right HeyReach campaign, helping sales teams follow up in real-time, improving lead response time.

#### What this solves:

* No more waiting on weekly CSV exports
* Instant outreach the moment someone fills a form or enters a pipeline stage
* Ensures CRM status + outreach campaigns stay in sync for a better customer experience and reduced handoff delays
* Cleaner lead management during your sales cycle, ensuring smoother handoffs

#### How it works (high-level):

1. A lead submits a form (or enters a CRM pipeline stage)
2. Make picks it up immediately
3. It maps key data (name, LinkedIn URL, tags)
4. The lead is added to a specific HeyReach campaign
5. (Optional) A Slack alert is sent to notify your team

#### What you’ll need:

* A Make account (Free or Pro)
* CRM or form tool (e.g. Pipedrive, HubSpot, Airtable)
* Your HeyReach API key
* HeyReach Campaign IDs
* Optional: Slack or Gmail module for alerts

#### Grab the setup pack (Optional):

→ Clone the “[Pipedrive → HeyReach” Make Scenario](https://www.heyreach.io/make-scenarios/pipedrive-to-heyreach)  (Includes: prebuilt Make flow, field mapping, campaign routing logic)

→ [Access the full Setup Guide in Notion](https://www.notion.so/heyreach/Playbook-2-CRM-to-Outreach-Sync-22609c3bcad38092a586f5b8725d6f0a)

> 💡Pro Tip: Add lead routing logic by persona or eam
> Want to route leads from CRM into different [HeyReach campaigns](https://help.heyreach.io/en/articles/9877952-how-to-launch-your-first-campaign) based on their persona or role?
>
> Use **Make’s Router module** like this:
>
> If persona = **Sales** → Send to Campaign A
> If persona = **Marketing** → Send to Campaign B
> If team\_size = **Growth** → Send to Campaign C
>
> This works especially well when your CRM has prefilled fields from form submissions or enriched data.
> You’ll avoid blasting the same message to all, and instead match the right campaign to the right lead.

#### ⚠️ Notes for HeyReach users

* Campaigns can be pre-tagged for each persona
* Sender rotation is optional — You can use default or advanced assignment logic
* Always test and turn on your scenario in Make after cloning

### **Customize This for Your Stack:**

**🛠 Using HubSpot instead of Pipedrive?**Swap the **Pipedrive “New Deal” or “Deal Stage Changed”** trigger with the **HubSpot “New Contact”** or “Deal Stage” trigger in Make.
 Field mapping logic stays the same. Just match fields like first\_name, linkedin\_url, campaign\_id.

**🛠 Using Airtable Forms or Webflow Forms?**Connect your form using Make's native Airtable/Webflow module (or a webhook), then map the fields to your HeyReach campaign just like in this guide.

(Optional: add a toggle or snippet link to example field mapping for HubSpot or Webflow.)

### Playbook #3: Enrich before you outreach

Sending messages without context? That’s a fast way to land in “Who dis?” territory.

This playbook enriches your leads before they ever enter a HeyReach campaign, so you can [personalize at scale](https://www.heyreach.io/playbook/rb2b-workflow), route them by persona, and optimize lead qualification through better contact information (skipping the “guess their job title” phase.)

#### What this Solves:

* Avoids pushing low-scoring or incomplete leads into your campaign
* Enables persona-based lead routing (e.g. PM vs. Head of Sales) . Plus, it helps match each potential customer to the right rep, improving engagement and [personalization](https://www.heyreach.io/playbook/rb2b-workflow).[‍](https://www.heyreach.io/blog/linkedin-lead-generation-strategy)
* [Boosts reply rates](https://www.heyreach.io/blog/linkedin-lead-generation-strategy) through better targeting and personalization

#### How it works (high-level):

1. A lead enters your system (e.g. signup form, webhook, CRM)
2. Make calls an enrichment tool to get persona/firmo data
3. Router module checks: Is the lead ICP-fit based on your lead scoring and customer profile?
4. If YES → Send to the right salesperson or SDR campaign
5. If NO → Drop into a fallback campaign or alert queue

#### What you’ll need:

* A Make account (Free or Pro)
* An enrichment tool (e.g. Clay, Clearbit, Dropcontact, etc.)
* Your HeyReach API key
* Your HeyReach campaign\_id(s)
* Optional: Slack/Gmail for alerts

> 💡 Pro tip: Route enriched leads by persona
> Once your [enrichment tool](https://www.heyreach.io/blog/best-data-enrichment-tools) fills in firmographic fields (e.g. job title, team size, vertical), you can route leads automatically:
>
> If job\_title = Head of Sales → Send to Campaign A  
> If company\_size > 200 → Send to Campaign B  
> If enrichment fails → Add to “Needs Review” queu
>
> This avoids sending [generic cold messages](https://www.heyreach.io/blog/linkedin-cold-messages), improves your overall sales process.and makes sure each lead lands in the right outreach flow (instantly.)

#### ⚠️ Notes for HeyReach users:

* All leads must have a LinkedIn URL
* Make’s Router module works best after enrichment is complete
* You can build a fallback path: no data → low-touch campaign or alert
* Test your flow and turn on the scenario in Make

#### Grab the setup pack:

* ✅ [[Clone enrichment + Routing Make Scenario]](https://www.heyreach.io/make-scenarios/enrich-qualify-free-trial-signups-using-make-heyreach)
* ✅ [[Access the setup guide in Notion](https://heyreach.notion.site/Playbook-3-Enrich-Before-You-Outreach-22609c3bcad380d48017ee5751b034ee)]

**Default setup** uses:
 → Clay or Clearbit for enrichment
 → Make + HeyReach campaign API
 → Persona-based routing with Router module

### **🛠 Customize This for Your Stack:**

**🛠 Using Dropcontact or Apollo for enrichment?** Swap the enrichment module with your tool’s Make module or webhook.
 As long as your enrichment tool returns persona/firmographic data (job title, company size, etc.), the routing logic remains the same.

**🛠 No enrichment tool yet?** Use LinkedIn profile scraping via Clay or a fallback queue:
 → If persona = blank → Add to “Review Later” campaign

⚠️ Don’t skip enrichment entirely — it powers the persona-based logic in this playbook.

You can also offer links to enrichment fallback templates (e.g., Clay + fallback path).

> ▶️ Feeling bold. [Steal all three playbooks](https://heyreach.notion.site/Outbound-Ops-Stack-22609c3bcad380c99318d33fc6927033) 😀

## How to plug these playbooks into a scalable outbound system

So now what? You’ve got the playbooks, how do you start?

Here’s how to layer the playbooks based on your current workflow, lead sources, and team setup:

### If you’re running multi-seat outbound, start with Playbook #1 (Account rotation)

Distribute leads evenly across multiple LinkedIn accounts, avoid sender overload, and keep campaigns moving without manual reassignment.

### If you’re syncing from forms or CRMs, start with Playbook #2 (CRM-to-outreach sync)

Trigger campaigns the moment someone signs up, with no CSVs or lag. Ideal for inbound flows or teams relying on HubSpot, Pipedrive, or Airtable.

### If you need targeting before outreach, start with Playbook #3 (Enrich before you outreach

Qualify, segment, and route leads using firmographic/persona data before adding them to any campaign. Best for leaner teams or high-volume inbound.

Here’s a “what to use when” mini-decision matrix:

### Most ops teams end up using all three

They [enrich first](https://www.heyreach.io/blog/best-data-enrichment-tools) → route based on persona (using structured lead routing rules and synced lead generation triggers) → then assign and sync to HeyReach. This gives you complete control over who gets what, when, and how.

## Next Steps: Launch a workflow that fits your funnel

Start with the playbook that solves the clearest pain in your funnel right now — and [scale outbound](https://www.heyreach.io/blog/outbound-sales-automation) from there.

Here’s a role-based starting guide:

* **RevOps leaders:** Start with **Playbook #1: Lead Rotation** → Fix overloaded accounts, distribute leads evenly, and reduce risk across multi-seat setups.
* **Inbound marketers or demand gen teams:** Start with **Playbook #2: CRM-to-Outreach Sync** → Trigger LinkedIn outreach automatically when someone fills a form or enters your pipeline.
* **Founders or lean GTM teams:** Start with **Playbook #3: Enrich Before You Outreach** → Qualify signups automatically and route them into the right campaign — no manual research needed.

👉 Once you’ve launched one, you can layer in the others to build a complete system that supports marketing teams and sales representatives working together.

Each playbook is modular (designed to plug into the next), so you can scale safely and tailor outreach at every stage of the funnel.

## Your lead routing fix → revenue engine starts here

Your lead routing process is your biggest ally when it comes to scaling safely. Replace broken spreadsheets with these real lead routing tools, sync your stack, and unlock repeatable outbound motion. Start with the one that fixes your biggest gap. Launch it. Test it. Once it’s live, layer in the rest.

The trick is to stop treating lead routing as admin work and start treating it like the ops engine it really is. Because when you route right, you not only reduce risk, but also improve conversion rates, response times, and overall customer experience.

Especially when lead routing routes match the salesperson to the potential customer. Use cases vary, from webinar signups to pricing page visitors,  smart lead routing optimizes every touchpoint.

👉 Want help plugging these into your stack? [Schedule a 1 on 1 strategic call.](https://cal.com/nadjakomnenic/discovery)
