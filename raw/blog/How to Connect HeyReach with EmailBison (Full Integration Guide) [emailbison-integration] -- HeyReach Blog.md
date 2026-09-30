# How to Connect HeyReach with EmailBison (Full Integration Guide)

Source: https://www.heyreach.io/blog/emailbison-integration

Summary: When LinkedIn outreach doesn't convert, email should pick up automatically. Here's how to connect HeyReach and EmailBison for a seamless multichannel follow-up system.

You've sent the connection request. You've waited. You've followed up with a message. Still nothing. LinkedIn isn't converting — but that doesn't mean the lead is dead.

The problem most outreach teams run into is that their LinkedIn and email efforts live in completely separate worlds. When a lead goes cold on LinkedIn, there's no automatic hand-off to email. Instead, you're manually exporting lists, uploading them somewhere else, and hoping nothing gets lost in the process. That's friction — and friction kills pipeline.

The HeyReach x EmailBison native integration fixes exactly this. Leads that don't respond on LinkedIn flow directly into EmailBison email sequences, and leads that warm up via email can be pulled back into HeyReach LinkedIn campaigns. One connected system, zero manual exports.

This guide walks you through every step: connecting the two platforms, configuring defaults, mapping fields, pushing leads manually or automatically, and the best workflow sequences to run once everything's set up.

## The building blocks: What's what?

**HeyReach** — A LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every connection request, message, and reply. Whether you're an agency managing dozens of accounts or a sales team running high-volume prospecting, HeyReach handles the LinkedIn side — safely, efficiently, and at scale.

**EmailBison** — A cold email platform built for high-deliverability outreach. It handles email sequences, sending schedules, reply tracking, and automation workflows — giving you a reliable second channel to reach leads who didn't respond on LinkedIn.

**What they unlock together:**

* Push unresponsive LinkedIn leads directly into EmailBison email sequences — manually or automatically
* Set up conditional multi-channel workflows: if no connection accepted → email follow-up; if connected but no reply → email follow-up
* Pull warm email leads back into HeyReach LinkedIn campaigns via the API
* Configure per-campaign or per-workspace defaults so every push goes to the right place automatically
* Map custom fields between platforms so personalisation carries over seamlessly

## Part 1 — Connecting EmailBison to HeyReach

This connection lets you push leads from HeyReach into EmailBison.

🍿 Video walkthrough connecting EmailBison to HeyReach

### Step 1 — Get your EmailBison API token

1. **Log into EmailBison** and go to your account settings.
2. **Open Developer API** in the settings menu.
3. **Click New Token**, give it a recognisable name (e.g. "HeyReach"), and click **Generate**.
4. **Copy the token** — you'll need it in the next step.

### Step 2 — Connect EmailBison in HeyReach

1. **Open HeyReach** and navigate to **Integrations** in the left sidebar.
2. **Find the EmailBison card** and click on it.
3. **Paste your API token** into the field provided.
4. **Click Update API Token.**

✅ If the token is valid, you'll see a success confirmation — the integration is now live for that workspace.

## Part 2 — Connecting HeyReach to EmailBison

This connection lets you push leads from EmailBison into HeyReach campaigns using EmailBison's automation workflows.

🍿 Video walkthrough for connecting HeyReach to EmailBison

### Step 1 — Get your HeyReach API key

1. In HeyReach, go to **Integrations → HeyReach API → Get API Key.**
2. **Copy the API key.**

### Step 2 — Connect HeyReach in EmailBison

1. In EmailBison, go to **Integrations** in the sidebar.
2. **Find HeyReach** and click **Connect Now.**
3. **Paste your HeyReach API key** into the field.
4. **Copy the Destination URL** shown and paste it into the corresponding field.
5. **Click Save.**

✅ EmailBison will confirm the connection and display your connected HeyReach workspaces.

## Configuring workspace defaults in HeyReach

Before pushing any leads, set your workspace defaults. These settings apply automatically every time a lead is pushed from that workspace to EmailBison — so getting this right upfront saves you a lot of manual configuration later.

**To configure defaults:**

1. On the **EmailBison integration page** in HeyReach, scroll down to **Workspace Defaults.**
2. **Select the default EmailBison campaign** that leads will be pushed to. Use the dropdown (which pulls from your EmailBison API token) or enter a campaign ID manually.

> 💡 **Just created a new campaign in EmailBison and it's not showing up?** Click **Refetch Campaigns** to refresh the list — HeyReach doesn't pull updates automatically.

## Setting up field mapping

Below the campaign selector, you'll find the **Default Mapping** section. This controls which HeyReach lead fields map to which EmailBison fields when a lead is pushed.

**Required fields:**

> 🚨 **LinkedIn Profile URL is required by EmailBison.** If this field isn't mapped, leads will fail to push. Create a custom variable in HeyReach — for example, `linkedinUrl` — that contains the LinkedIn profile URL for each lead, then map it to the LinkedIn Profile URL field here. Don't skip this step.

**Optional fields:**

All other EmailBison fields and custom variables are optional. Map as many or as few as your EmailBison campaign setup requires.

## Pushing leads manually

There are two ways to push individual leads to EmailBison on demand.

### Option A — From the Leads page

1. Go to the **Leads screen** in HeyReach.
2. Find the lead and click **Manage.**
3. Click **Actions → Push to EmailBison.**
4. A modal appears with the lead's information pre-filled from your default mapping. **Review and update any fields** if needed.
5. **Select or confirm the target EmailBison campaign.**
6. Click **Push.**

### Option B — From the Unibox

1. **Open the Unibox** and find the conversation with the lead you want to push.
2. Click **Lead Actions → Push to EmailBison.**
3. The same modal appears. Review the lead data and campaign selection.
4. Click **Push.**

> 💡 **Pushing from the Unibox is especially powerful** when you're reviewing replies. You can immediately push unresponsive leads to an email follow-up sequence without ever leaving your inbox.

> 🚨 **Push failing?** Scroll to the bottom of the push modal to see the error message. The most common cause: the target EmailBison campaign is still in **draft status.** Activate the campaign in EmailBison first, then retry.

## Pushing leads automatically

This is where the integration really earns its keep. HeyReach can automatically push leads to EmailBison when a campaign sequence ends and the lead hasn't responded — no manual effort required.

**To enable automatic pushing for a specific campaign:**

1. **Open the campaign** in HeyReach.
2. Go to **Settings** within the campaign.
3. Find the **Integration Settings** section.
4. **Enable Automatic Push to EmailBison.**

By default, leads are pushed to your workspace default EmailBison campaign. To route this campaign's leads somewhere different, check **Override workspace default** and select the specific campaign.

Once enabled, any lead whose sequence finishes without a reply within **3 days of the final step** is automatically pushed to the configured EmailBison campaign.

> ✅ **Recommended:** Enable automatic push on all active LinkedIn campaigns. This ensures no lead falls through the cracks — anyone who doesn't engage on LinkedIn gets moved to an email sequence without any manual effort on your part.

## Common workflows

Ready to put it all together? Here are the three most effective sequences to run with this integration.

**Workflow 1: Connection not accepted → Email follow-up**

Target leads who never accepted your connection request.

> `Follow profile → Like recent post → Send Connection Request
> Wait X days → If Not Accepted → Push to EmailBison ("Not Accepted" campaign)`

EmailBison message angle: *"Hey, I tried to connect on LinkedIn but didn't hear back — reaching out here instead."*

**Workflow 2: Connected but no reply → Email follow-up**

Target leads who accepted but never responded to your message.

> `Send Connection Request → Wait for acceptance
> Accepted → Send Message → Wait X days
> No reply → Push to EmailBison ("No Reply" campaign)`

EmailBison message angle: *"Thanks for connecting on LinkedIn — just wanted to follow up here as I didn't get a response."*

**Workflow 3: Find email first, then go multichannel**

Ideal when your lead list doesn't include email addresses. Use HeyReach's Find Email action to enrich leads before deciding their path.

> `Find Email
> ├── Email not found → Send Connection Request (LinkedIn-only path)
> └── Email found → Follow profile → Send Connection Request → Wait for acceptance
>     └── Not accepted → Push to EmailBison ("Email Found, Not Accepted" campaign)`

> ✅ This approach maximises reach — leads without an email get LinkedIn-only outreach, while leads with a verified email get a full multichannel sequence if LinkedIn doesn't convert them.

> 💡 For more on Find Email, see *How to use the Find Email action in HeyReach Campaigns* and *How do the Email Credits work in HeyReach?*

## Troubleshooting

**My push failed and I don't know why.**Open the push modal and scroll to the bottom — the error message is shown there. The most common culprits are: campaign in draft status (activate it first), LinkedIn Profile URL not mapped, or an expired API token (re-generate and re-enter from EmailBison).

**The EmailBison campaign I just created isn't showing in the dropdown.**Click **Refetch Campaigns** on the EmailBison integration page. HeyReach doesn't refresh the campaign list automatically.

**I want to push the same lead to different campaigns at different stages. Is that possible?**Yes. Each sequence branch can target a different EmailBison campaign. For example, a "Not Accepted" branch pushes to one campaign, and a "No Reply" branch pushes to another. Each push step in your sequence can have its own campaign destination.

**Does the integration need to be configured for each workspace separately?**Yes. The EmailBison API token is set per workspace. If you manage multiple workspaces in HeyReach, configure the integration — and set defaults and field mappings — in each one individually.

**I don't have email addresses in my HeyReach lead list. Can I still use this integration?**Yes. HeyReach pushes leads to EmailBison using the mapped fields (first name, last name, LinkedIn URL). EmailBison then handles email lookup and outreach on its end. If you want more control, use the Find Email action in your HeyReach sequence to enrich leads before pushing.

## Quick-start checklist

**Part 1 — HeyReach → EmailBison (push leads to email)**

* Generated an API token in EmailBison (Developer API settings)
* Pasted the API token into the EmailBison card in HeyReach Integrations
* Confirmed the success message appeared
* Selected a default EmailBison campaign in Workspace Defaults
* Created a custom variable in HeyReach for LinkedIn Profile URL
* Mapped LinkedIn Profile URL to the required EmailBison field
* Enabled Automatic Push on active campaigns (optional but recommended)

**Part 2 — EmailBison → HeyReach (pull leads into LinkedIn campaigns)**

* Copied the HeyReach API key from Integrations → HeyReach API
* Connected HeyReach inside EmailBison's Integrations section
* Pasted the Destination URL and saved the connection
* Confirmed connected HeyReach workspaces are visible in EmailBison

🎯 **You're all set.** Your LinkedIn outreach and email sequences are now one connected system — no lead left behind.

‍
