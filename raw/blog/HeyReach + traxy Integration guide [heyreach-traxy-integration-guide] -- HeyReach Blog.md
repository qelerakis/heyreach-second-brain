# HeyReach + traxy Integration guide

Source: https://www.heyreach.io/blog/heyreach-traxy-integration-guide

Summary: Low acceptance rates? traxy feeds HeyReach with leads who are already active on LinkedIn — so your campaigns reach the right people at the right time.

Here's a frustrating pattern: you build your LinkedIn outreach campaign, you get your sequences right, your copy is solid — and your acceptance rate is still sitting at 20–25%. Not because your messaging is bad. Because your list is wrong.

Most HeyReach users pull their lead lists from LinkedIn Sales Navigator, which is great for filtering by title, company, or location. But it tells you nothing about who's *actually active* on LinkedIn right now — who's engaging with posts, responding to competitors' content, or showing real buying signals in the feed.

That's where traxy comes in. traxy is a LinkedIn intelligence layer that monitors engagement across your own content, your competitors', and key influencers in your space. It identifies who's already active and interested — and with the HeyReach integration, sends those leads directly into your campaigns automatically.

This guide walks you through exactly how to set it up, step by step.

### 🍿 Watch the full integration walkthrough

## The Building Blocks: What's What?

**traxy** is a LinkedIn listening and lead qualification tool built for B2B outbound. It monitors LinkedIn engagement across your content, competitors' posts, and influencer conversations — then identifies the people showing real buying signals. Rather than prospecting from static filters, traxy gives you a continuously refreshed list of leads who are already active and relevant to your space.

**HeyReach** is a LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every connection request, message, and reply. Whether you're an agency managing dozens of accounts or a sales team running high-volume prospecting, HeyReach handles the LinkedIn side — safely, efficiently, and at scale.

### What they solve together

The problem with most LinkedIn outreach isn't the tool — it's the list. traxy and HeyReach together fix that:

* **Signal-based targeting:** traxy surfaces leads who are actively engaging on LinkedIn, so your HeyReach campaigns reach people who are already warm — not just people who match a job title.
* **Fully automated list-to-campaign flow:** traxy pushes qualified leads directly into your HeyReach campaigns as they're identified — no manual exports, no CSV uploads.
* **Better acceptance and reply rates:** Reaching active LinkedIn users means your connection requests land when people are in the app. Ben, the founder of Traxxi.ai, reported acceptance rates climbing from 20–25% to 45–58% after switching to traxy-powered targeting.
* **Competitor audience targeting:** traxy can track who's engaging with your competitors' content — letting you launch timely outreach before those leads go further down someone else's funnel.
* **Continuously refreshed lists:** As new people engage with tracked content, traxy automatically routes them into the right HeyReach campaigns — keeping your outreach evergreen without manual intervention.

## Setting Up the Integration

The traxy → HeyReach integration is set up entirely inside your traxy account. You'll need:

* An active traxy account
* An active HeyReach account
* Your HeyReach API key
* A HeyReach campaign (existing or new) to send leads into

💡 **Note:** Setup takes only a few minutes. Once it's live, traxy will automatically push qualified leads into HeyReach on an ongoing basis — no further action required on your end.

### Step 1: Get your HeyReach API key

**Locate your API key in HeyReach.**

1. Log into your HeyReach account.
2. Navigate to **Settings** → **Integrations** (or **API**). [VERIFY exact menu path]
3. Copy your API key.

🚨 **Keep your API key private.** Don't share it or commit it anywhere publicly. If it gets compromised, regenerate it from the same settings page.

### Step 2: Connect HeyReach inside traxy

**Open the Integration tab in traxy.**

1. Log into your traxy account at [traxxy.ai](https://traxxy.ai).
2. Navigate to the **Integration** tab in the left-hand sidebar. [VERIFY label]
3. Click on **HeyReach** from the list of available integrations.
4. Paste your HeyReach API key into the designated field.

✅ Once connected, traxy will be able to read your existing HeyReach campaigns and lists.

### Step 3: Select your target HeyReach campaign

**Choose where qualified leads should go.**

1. After connecting your API key, traxy will display your existing HeyReach campaigns.
2. Select the campaign you want traxy to send leads into — or create a new one directly in HeyReach first, then return here to select it.
3. Select the lead list or sequence you want to use within that campaign. [VERIFY if list vs. campaign is a separate selector]

💡 **Pro tip:** Set up a dedicated HeyReach campaign specifically for traxy-sourced leads. This makes it much easier to track performance and compare results against your standard Sales Navigator campaigns.

### Step 4: Set delivery to Auto

**Enable automatic lead delivery.**

1. In the traxy integration settings, find the **Delivery** option.
2. Set it to **Auto**.
3. Click **Save settings**.

That's it. traxy will now monitor LinkedIn engagement in your tracked audiences and push qualified leads directly into your selected HeyReach campaign as they're identified — in real time.

✅ You're connected. From this point on, traxy handles lead qualification and delivery. HeyReach handles the outreach.

## Common Workflows

### Workflow 1: Warm up competitor audiences before they convert

**Trigger:** Someone engages with a competitor's LinkedIn post**Action:** traxy identifies and qualifies the lead → pushes to HeyReach campaign → HeyReach sends a timely connection request and message sequence

This is one of the highest-signal plays you can run. People engaging with competitor content are already aware of the problem you solve — they just haven't found you yet.

### Workflow 2: Activate your own content's warm audience

**Trigger:** Someone likes, comments on, or shares your LinkedIn content**Action:** traxy captures and qualifies the lead → routes to HeyReach → HeyReach follows up with a personalized outreach sequence

Your content is already doing the warming. This workflow closes the loop by moving engaged viewers into a structured outreach sequence automatically.

### Workflow 3: Monitor influencer conversations in your niche

**Trigger:** A buyer-fit prospect engages with a key LinkedIn influencer in your industry**Action:** traxy identifies them against your ICP → qualifies and pushes to HeyReach → outreach launches while engagement is fresh

Timing is everything on LinkedIn. Reaching someone shortly after they've engaged with relevant content dramatically increases the chance of a reply.

### Workflow 4: Evergreen prospecting without manual list refreshes

**Trigger:** Ongoing LinkedIn engagement activity across tracked accounts**Action:** traxy continuously surfaces new qualified leads matching your ICP → auto-pushes to HeyReach → campaigns stay populated without you lifting a finger

Rather than running periodic list-building sessions, you get a live, self-refreshing pipeline that works in the background.

## Troubleshooting

**The API connection isn't working.**Double-check that you've copied the full API key from HeyReach without any leading or trailing spaces. If the issue persists, regenerate your API key in HeyReach and reconnect in traxy.

**traxy isn't finding my existing campaigns.**Make sure your HeyReach campaigns are active (not paused or archived) when you connect. If you created a new campaign after connecting, you may need to refresh the campaign list in traxy's integration settings. [VERIFY if a refresh option exists]

**Leads are not being added to my campaign.**Check that your delivery setting is set to **Auto** in traxy's HeyReach integration settings. Also confirm your HeyReach campaign is not paused or at capacity.

**I'm seeing the same leads appear multiple times.**traxy's deduplication should prevent this, but if you're running the same ICP across multiple tracked sources (your content + a competitor's), the same lead could qualify from both signals. [VERIFY traxy's deduplication behavior — flag for review]

**My acceptance rates aren't improving after connecting.**Give it a full campaign cycle before drawing conclusions. traxy learns and improves its qualification over time — the longer it runs, the more accurately it identifies your highest-converting leads. Make sure your HeyReach message sequences are also optimized; even the best list won't rescue poor copy.

## Quick-Start Checklist

**Setting up traxy → HeyReach**

* Create or log into your traxy account at traxxy.ai
* Log into HeyReach and copy your API key from Settings → Integrations [VERIFY path]
* In traxy, open the Integration tab and select HeyReach
* Paste your HeyReach API key and connect
* Select the target HeyReach campaign for qualified leads
* Set Delivery to **Auto**
* Save settings
* Confirm traxy is tracking the right LinkedIn sources (your content, competitors, influencers)
* (Recommended) Set up a dedicated HeyReach campaign for traxy-sourced leads to benchmark performance separately

🎯 You're live. traxy is now routing qualified, active LinkedIn leads straight into your HeyReach campaigns — so you spend less time building lists and more time booking meetings.
