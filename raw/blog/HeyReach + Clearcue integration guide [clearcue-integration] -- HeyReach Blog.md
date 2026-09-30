# HeyReach + Clearcue integration guide

Source: https://www.heyreach.io/blog/clearcue-integration

Summary: Pair HeyReach with Clearcue to run intent-driven campaigns, personalize outreach at scale, and increase reply rates — without extra effort or busywork.

Most outbound campaigns start with a list. Someone builds it, someone cleans it, someone loads it into a sequence. But by the time those messages actually go out, half the leads have gone cold, changed jobs, or already bought from a competitor.

The better approach is to **catch people in motion.** Leads who just posted about a pain point. Companies that suddenly started hiring for a role your solution replaces. Decision-makers who've been consuming content in your category for the past 30 days. These aren't just better leads – they're a different category of lead entirely.

That's the problem[**HeyReach + Clearcue solves.**](https://www.heyreach.io/integration/clearcue) This guide walks you through exactly how to set that up.

## **The building blocks: What's what?**

**HeyReach** – A LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every connection request, message, and reply. Whether you're running a lean [GTM motion](https://www.heyreach.io/blog/scalable-gtm-automation-systems) or managing outreach across a full sales team, [HeyReach handles the LinkedIn side](https://www.heyreach.io/blog/heyreach-review) — safely, efficiently, and at scale.

**Clearcue** – An AI-powered signal intelligence platform that tracks real-time buying intent across LinkedIn and other digital channels. It monitors signals like job changes, hiring patterns, tech stack mentions, and keyword triggers, then uses signal stacking to layer multiple intent indicators and surface only the leads showing the strongest buying behavior. The result: a prioritized shortlist of people who are actively in-market, not just demographically similar to your ICP.

### **What they solve together**

On their own, each tool does one job well. Together, they close the gap between knowing who to reach and actually reaching them:

* **Intent-first targeting**: Every lead entering your HeyReach campaign has been pre-qualified by Clearcue's signal stack. You're not blasting a list; you're contacting people who've already signaled they might need what you offer.
* **Zero manual handoff**: Via [MCP,](https://www.heyreach.io/blog/beginners-guide-heyreach-mcp) Clearcue and HeyReach connect through an AI assistant like Claude. Signals get detected, leads get pushed, campaigns get launched — without anyone copying and pasting a spreadsheet.
* **Timing that actually matters**: You reach leads when signals are fresh, not days later after they've already responded to someone else.
* **Personalization at the signal level:** Because you know *why* a lead surfaced (a job change, a hiring spike, a keyword cluster), your [outreach](https://www.heyreach.io/blog/signal-based-outbound) can reference the actual trigger.
* **Reply rates that move the needle**: Teams using intent-based targeting through Clearcue and HeyReach see 35–45% reply rates compared to the 5–10% cold outbound average.

## **Setting up the integration**

Clearcue and HeyReach connect in two ways. The first is a **direct native integration** — you can sync leads from Clearcue directly into HeyReach lists and receive outreach events back into Clearcue as signals. The second is through **MCP**, a protocol that lets [Claude](https://help.heyreach.io/en/articles/12123398-how-to-integrate-heyreach-mcp-with-claude) use both platforms as external tools, so you can orchestrate the entire workflow from a single AI interface.

Here's what you'll need before you start:

* A HeyReach account with at least one active LinkedIn sender
* A Clearcue account with at least one signal filter configured
* Access to an AI assistant that supports MCP tool connections (Claude is recommended)
* Your HeyReach API key and Clearcue API key

### **Part 1: Connect HeyReach's MCP server**

**Step 1: Get your HeyReach API key**

* Log into your HeyReach account.
* Go to **Settings → API**.
* Copy your API key. Keep this somewhere safe — you'll need it in the next step.

**Step 2: Add HeyReach as an MCP server in Claude**

* Open Claude (claude.ai or the Claude desktop app).
* Navigate to **Settings → Integrations** (or your MCP connections panel, depending on your setup).
* Add a new MCP server with the following details:
  + **Name:** HeyReach
  + **API key:** paste your HeyReach API key from Step 1
* Save the connection. Claude should confirm that the HeyReach tools are now available.

> ✅ **You'll know it's working when** Claude can list your HeyReach campaigns or sender accounts in response to a plain-language prompt like *"show me my active HeyReach campaigns."*

### **Part 2: Connect Clearcue's MCP server**

**Step 3: Get your Clearcue MCP URL or API key**

* Log into Clearcue and go to Settings → Integrations → Clearcue MCP
* Copy the MCP URL — this handles authentication automatically
* Prefer a static token? Click Generate Key instead and copy the API key (starts with clc\_, shown only once)

**Step 4: Add Clearcue as an MCP server in Claude**

* In the MCP connections panel, add a new server
* Paste your MCP URL or API key and save

> ✅ You'll know it's working when Claude can query your Clearcue signals and return a list of leads with their associated intent signals.

### **Part 3: Build the signal-to-outreach workflow in Claude**

With both MCP servers connected, Claude becomes the orchestration layer between them. You can now describe what you want in plain language and Claude will execute across both tools.

**Step 5: Create or confirm your Clearcue signal**

Before running the workflow, make sure you have at least one signal filter set up in Clearcue. A signal filter defines which intent signals you're monitoring — for example, a company announcing a seed funding round, a company hiring for a Head of Sales role, or a prospect interacting with your content or a competitor's on LinkedIn.

> 💡 **Pro tip:** The more specific your signal stack, the higher your reply rates. Clearcue's signal stacking lets you combine 2–4 signals for tighter targeting. If you're just getting started, try combining one behavioral signal (e.g. a LinkedIn post keyword) with one contextual signal (e.g. hiring for a relevant role).

**Step 6: Create your HeyReach campaign**

Before running the workflow, you'll also need a live campaign in HeyReach ready to receive leads:

* In HeyReach, go to **Campaigns → New Campaign**.
* Set up your sequence (connection request + [follow-up messages](https://www.heyreach.io/blog/sales-follow-up)).
* Write your outreach copy. Since you'll know the intent signal that triggered each lead, you can reference it directly — e.g. *"Noticed your team is scaling the SDR function — curious if LinkedIn outreach is part of that push."*
* Set the campaign status to **Active** (or to a draft/paused state if you want to review leads before they enter the sequence).

> ⚠️ **Don't add leads manually at this stage.** The workflow will handle that automatically via Claude.

**Step 7: Run the workflow via Claude**

Now the setup pays off. Open Claude and give it a prompt like:

*"Pull the top 20 leads from my [signal filter name] filter in Clearcue, then add them to my [campaign name] campaign in HeyReach."*

Claude will:

* Query Clearcue for leads matching your filter
* Return a list with intent context (which signals each lead triggered)
* Push each lead into the specified HeyReach campaign
* Confirm how many leads were added successfully

> ✅ **After running, go to your HeyReach campaign and verify the leads appear under the Leads tab with correct data.**

**Step 8: Schedule or automate the workflow (optional)**

For a fully automated pipeline, you can prompt Claude on a recurring basis — or, if your team uses an automation layer like n8n or Make, set up a trigger that runs the Claude MCP workflow on a schedule (e.g. every morning at 8am, pull fresh signals and push to HeyReach).

> 💡 **Pro tip:** Pair this with HeyReach's smart sending limits to stay within LinkedIn's safe activity thresholds. Don't push 500 leads at once — drip them in batches of 20–50 per sender per day.

## **Common workflows**

* **Workflow 1: Hiring signal → LinkedIn outreach.** Set a signal in Clearcue to scan for companies with open SDR job listings, stacked with a signal detecting companies or people interacting with a competitor's page or profile. Create a list in Clearcue with both signals stacked at the company level and add your ICP filters (location, company size, industry, position). Claude pulls the list each morning and pushes it to a HeyReach campaign referencing the hiring spike in the connection request.
* **Workflow 2: Job change trigger → warm intro sequence** A contact in your [ICP](https://www.heyreach.io/blog/linkedin-outreach-template) just started a new VP role → Clearcue surfaces them as a fresh signal → Claude pushes them into a HeyReach "new role" campaign within 48 hours of the change while they're still in "making decisions" mode.
* **Workflow 3: Keyword cluster → content-aware outreach** Clearcue detects leads posting about a pain point your product solves (e.g. "LinkedIn outreach doesn't scale") → Claude pulls the shortlist and pushes to a HeyReach campaign with messaging that references the specific topic they've been engaging with.
* **Workflow 4: Weekly intent refresh** Every Monday morning, Claude pulls the top 50 fresh people(matching your ICP) detected via signals from Clearcue and distributes them across 3–5 HeyReach sender accounts, keeping daily activity balanced and outreach volume high without triggering LinkedIn's spam filters.

## **Troubleshooting**

* **Claude can't find the HeyReach or Clearcue MCP server** → Double-check that the MCP server URL and API key are entered correctly in your connections panel. Confirm with both HeyReach and Clearcue support that the MCP server endpoint is active on your account tier.
* **Leads are being added to the wrong campaign** → When prompting Claude, use the exact campaign name as it appears in HeyReach. Partial or mistyped names can cause Claude to match the wrong campaign. You can ask Claude to "list all my HeyReach campaigns" first to confirm the exact name.
* **Duplicate leads appearing in HeyReach →** HeyReach will flag leads that already exist in a campaign. If you're running the workflow daily, configure Clearcue to only return new leads since the last pull, or use a date filter in your Claude prompt: "Pull leads that triggered the signal after [date]."
* **Leads added but not receiving messages** → Check that your HeyReach campaign is set to Active, that the sender accounts are healthy and connected, and that the leads' LinkedIn profiles are publicly accessible. Leads with restricted profiles may be silently skipped.

## **Quick-start checklist**

**Setup**

* HeyReach API key copied from Settings → API
* Clearcue API key copied from your account settings
* HeyReach MCP server added to Claude with correct URL and API key
* Clearcue MCP server added to Claude with correct URL and API key
* Both connections verified by running a test prompt in Claude

**Before running the workflow**

* At least one Clearcue signal configured and active
* HeyReach campaign created with outreach sequence and copy
* [ ] Campaign set to Active (or staged for review)
* [ ] Sending limits checked across HeyReach sender accounts

**Running the workflow**

* Claude prompt specifies the signal filter name and HeyReach campaign name
* Leads confirmed in HeyReach Leads tab after first run
* Recurring workflow scheduled (optional — via n8n, Make, or manual cadence)

🎯 You're all set. Your intent-driven LinkedIn outreach machine is live — every lead that enters your campaign is there for a reason.
