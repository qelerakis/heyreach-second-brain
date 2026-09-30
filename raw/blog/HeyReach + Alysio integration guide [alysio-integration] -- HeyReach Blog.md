# HeyReach + Alysio integration guide

Source: https://www.heyreach.io/blog/alysio-integration

Summary: Connect HeyReach and Alysio to discover prospects, push leads directly into LinkedIn campaigns, and manage outreach from one place.

You know the drill. You open your data provider — ZoomInfo, Apollo, whatever you're using — filter down to your ICP, export a CSV, clean it up, upload it to HeyReach, create a list, add the leads to a campaign, and finally hit send. By the time you've done all that, you've spent 20 minutes on what should have taken two.

Now multiply that across your team. Across dozens of campaigns. Across multiple data sources. The friction adds up fast — and it's not the kind of work that moves pipeline.

That's the problem [Alysio + HeyReach](https://www.heyreach.io/integration/alysio) solves. Instead of bouncing between tools to build and launch outreach, you stay in one place, use natural language to find the right people, and push them directly into an active HeyReach campaign — no CSV, no tab-switching, no wasted time.

This guide walks you through how to set it up and what you can do once it's running.

## **The building blocks: What's what?**

[**HeyReach**](https://www.heyreach.io/blog/heyreach-review) is a LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every [connection request,](https://www.heyreach.io/blog/linkedin-connection-automation-tool) message, and reply. Whether you're an agency managing dozens of accounts or a sales team running high-volume prospecting, HeyReach handles the LinkedIn side — safely, efficiently, and at scale.

**Alysio** is a GTM AI workspace that connects all of your revenue tools — your CRM, data providers, engagement platforms, conversation intelligence tools, and more — into a single real-time interface. Instead of logging into five different platforms to piece together a picture of your pipeline, you ask Alysio in plain language and it pulls the answer from wherever the data lives. It's built for CROs, RevOps, VPs of Sales, AEs, and BDRs who need to move fast without losing context.

### **What they solve together?**

The standard prospecting workflow has a lot of unnecessary steps between "who should I talk to?" and "I'm sending them a LinkedIn message." HeyReach + Alysio collapses that gap:

* **Find prospects with natural language** — Use your connected data providers (ZoomInfo, Apollo, etc.) inside Alysio to filter by ICP criteria without ever leaving the platform.
* **Skip the CSV entirely** — Build and curate lead lists inside Alysio and push them directly into HeyReach. No exports, no uploads, no reformatting.
* **Add leads to live campaigns in seconds** — Whether you're spinning up a new campaign or fueling an existing one, Alysio writes directly back to HeyReach via API.
* **Manage campaigns from your** [**GTM**](https://www.heyreach.io/blog/signal-led-gtm-engine) **workspace** — View campaign status, pause or resume campaigns, check lead activity, and pull [performance metrics](https://www.heyreach.io/blog/linkedin-campaign-monitoring) — all from within Alysio.
* **Work across your full stack** — HeyReach sits alongside your CRM, Gong calls, [Slack](https://www.heyreach.io/integration/slack), Salesforce, and every other connected tool in one unified context, so your outreach decisions are informed by the full picture.

Here's how it all looks in action:

## **Setting up the integration**

### **Step 1: Connect HeyReach to Alysio**

**Authenticate via OAuth in the Alysio platform.**

1. Log into your Alysio workspace.
2. Navigate to **Integrations** or **Connected Tools** in your settings.
3. Find **HeyReach** in the integration list and click **Connect**.
4. You'll be redirected to a HeyReach OAuth screen. Log in with your HeyReach credentials and authorize the connection.
5. Once authorized, you'll be returned to Alysio with HeyReach listed as a connected integration.

✅ **You're connected.** Alysio can now read from and write to your HeyReach account in real time.

> 💡 **Note:** The integration uses HeyReach's API via OAuth, which means Alysio respects your existing HeyReach permissions. If you're managing [multiple LinkedIn accounts in HeyReach,](https://www.heyreach.io/blog/manage-multiple-linkedin-accounts) all of them will be accessible through Alysio after authentication.

### **Step 2: Connect your data provider(s)**

**Link the sources you use to find prospects.**

Alysio supports a wide range of data providers and [GTM tools,](https://www.heyreach.io/blog/best-gtm-tools) including ZoomInfo, Apollo.io, Salesforce, HubSpot, Salesloft, Outreach, and more.

1. In your Alysio **Integrations** settings, connect whichever data sources you use for prospecting.
2. Authenticate each one following the same OAuth or API key flow.
3. Once connected, Alysio's AI layer can query these sources directly when you're building prospect lists.

> 💡 **Pro tip:** The more data sources you connect, the richer the context Alysio can pull from. Connecting your CRM alongside your data provider lets Alysio cross-reference existing contacts, open opportunities, or accounts already in motion — so you're not accidentally re-targeting someone who's already in a deal cycle.

### **Step 3: Find prospects using natural language**

**Ask Alysio to build your list — no filters, no exports.**

This is where the workflow changes fundamentally. Instead of navigating ZoomInfo's filter UI and exporting to CSV, you describe who you're looking for in plain English.

Some examples of what you might say:

* *"Find me 50 VP of Sales at Series B SaaS companies in the US with 50–200 employees, not in our CRM."*
* *"Show me heads of RevOps at companies using Salesforce and Gong."*
* *"Pull 30 prospects from ZoomInfo matching our ICP in the fintech vertical."*

Alysio queries your connected data provider, surfaces the results, and lets you review and curate the list before doing anything with it — all in the same window.

> ⚠️ **Watch out:** Like any data provider, results quality depends on your source data. Spot-check a few records before pushing a list to a live campaign, especially for contact accuracy and LinkedIn profile availability.

### **Step 4: Push leads into HeyReach**

**Add your curated list directly to a HeyReach campaign or list.**

Once you're happy with your prospect list in Alysio:

1. Select the leads you want to push.
2. Choose **Add to HeyReach** and select one of the following: 
   * **Add to an existing campaign** — Pick a live or paused HeyReach campaign from the dropdown.
   * **Add to a lead list** — Push leads into a HeyReach list for later use or bulk campaign assignment.
   * **Create a new list** — Set up a new empty list in HeyReach and populate it in one step.
3. Map any custom fields if prompted (e.g., first name, company, LinkedIn URL).
4. Confirm and push.

✅ **Leads will appear in HeyReach immediately.** You can verify by opening your campaign or list in HeyReach and checking the lead count.

> 💡 **Pro tip:** If you're adding leads to an active campaign, HeyReach will begin sequencing them according to your existing campaign settings. Make sure your campaign's sending limits and LinkedIn account assignments are configured the way you want before pushing a large batch.

### **Step 5: Manage campaigns from Alysio**

**You don't need to open HeyReach to check in on what's running.**

Once the integration is live, Alysio can surface HeyReach data directly in your workspace. You can:

* **View all campaigns** — See a full list with status, filtering by active/paused/completed or by keywords.
* **Get campaign details** — Pull up sequence info, lead counts, connected LinkedIn accounts, and more for any specific campaign.
* **Pause or resume campaigns** — Control campaign state without leaving Alysio.
* **Check lead status** — Look up where a specific lead is in a sequence, what campaign they're in, or their full message history.
* **Pull performance metrics** — Get overall stats filtered by LinkedIn account, campaign, or date range.

This is particularly useful if you're already in Alysio reviewing Gong call data or CRM pipeline and want to cross-reference what outreach is actively running to a given account — without opening another tab.

## **Common workflows**

### **Workflow 1: ICP Prospecting → LinkedIn campaign in under 5 minutes**

**The core use case.**

You need to launch a LinkedIn campaign targeting a new vertical or account segment. Instead of exporting from your data provider and uploading to HeyReach manually:

1. Ask Alysio to find 40 prospects matching your ICP from ZoomInfo.
2. Review and trim the list.
3. Push directly into an existing HeyReach campaign.
4. Done.

No CSV. No tab-switching. No reformatting. The leads are in your campaign and sequencing starts according to your existing settings.

### **Workflow 2: Account-based list building across tools**

**When you want to go after specific accounts and need full context before reaching out.**

Say you have a list of target accounts in your CRM and want to add LinkedIn outreach to your sequence:

1. In Alysio, ask for contacts at those accounts from your connected data provider.
2. Cross-reference with your CRM to exclude existing contacts or open opportunities.
3. Push the clean list into a new HeyReach lead list.
4. Assign the list to an account-specific LinkedIn campaign.

**The result:** a tight, de-duped prospect list built from two [data sources,](https://www.heyreach.io/blog/best-data-enrichment-tools) loaded into HeyReach without a single export.

### **Workflow 3: Mid-campaign refueling**

**When an active campaign is running low on leads.**

You're two weeks into a campaign and your lead pool is thinning. Rather than pausing the campaign and rebuilding:

1. Open Alysio and ask for 30 new prospects matching your original ICP criteria.
2. Review the results.
3. Add them directly to the live campaign.

HeyReach picks up the new leads and sequences them automatically. Your campaign keeps running without interruption.

### **Workflow 4: Pipeline-informed outreach**

**When you want LinkedIn activity to be aware of what's already in motion.**

Before launching outreach to a new batch of accounts, check your CRM and conversation data inside Alysio:

* Are any of these accounts already in a deal stage?
* Did any of them show up in a recent Gong call?
* Are they already being worked by another rep?

With all your GTM tools connected in one place, Alysio can surface this context before you push to HeyReach — so your LinkedIn outreach doesn't undercut an active deal.

## **Troubleshooting**

* **Leads aren't appearing in HeyReach after I push them from Alysio.** Check that the OAuth connection is still active. Go to your Alysio integrations settings and confirm HeyReach shows as connected. If the connection has expired, re-authenticate and try again. Also verify the campaign or list you targeted is accessible under your HeyReach account permissions.
* **I can see campaigns in Alysio but can't push leads to some of them.** Alysio respects HeyReach's API permissions. If a campaign is owned by a sub-account or has restricted access, it may appear in read-only mode. Check the campaign's settings in HeyReach directly to confirm write access.
* **My data provider isn't surfacing results that match my prompt.** Natural language queries depend on how well Alysio can interpret your ICP criteria against your provider's data model. Try being more specific — include job title, seniority level, company size, industry, and geography as separate criteria rather than one long sentence.
* **Leads are being added to HeyReach but some are missing LinkedIn URLs.** HeyReach requires a valid LinkedIn profile URL to enroll a lead in a LinkedIn outreach campaign. If your data provider returns contacts without LinkedIn URLs, those leads may be skipped or fail to sequence. Check your data source for LinkedIn URL coverage, or supplement with a LinkedIn-enriched data provider.
* **The campaign I want to target doesn't appear in the dropdown inside Alysio.** Alysio pulls campaign data via the HeyReach API. If a campaign was created very recently, try refreshing the connection or waiting a moment for the data to sync.

## **Quick-start checklist**

**To get HeyReach + Alysio running:**

* Log into Alysio and navigate to Integrations
* Connect HeyReach via OAuth and authorize the connection
* Connect your data provider(s) (ZoomInfo, Apollo, Salesforce, etc.)
* (Optional) Connect your CRM for cross-referencing during list building
* Test the connection by asking Alysio to list your active HeyReach campaigns
* Run a small prospect query and push a test list to a HeyReach lead list
* Verify the leads appear in HeyReach
* Push your first real batch to an active campaign

You made it – from ICP filter to LinkedIn sequence, without leaving your GTM workspace.
