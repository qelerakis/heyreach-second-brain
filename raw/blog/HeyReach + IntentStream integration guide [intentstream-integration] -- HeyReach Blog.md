# HeyReach + IntentStream integration guide

Source: https://www.heyreach.io/blog/intentstream-integration

Summary: Learn how to connect HeyReach with IntentStream to turn anonymous website visitors into high-intent LinkedIn leads and automate outreach at scale.

You've built solid LinkedIn outreach sequences. Your messaging is tight. Your targeting is decent. But you're still sending cold connection requests to people who have never heard of you and have no immediate reason to care.

What if you could reach out to prospects who are already on your website, actively researching solutions like yours — before your competitors do?

That's the gap IntentStream closes. It identifies the anonymous companies and decision-makers visiting your site, resolves their identities, and gives you a way to reach them directly. Connect it to HeyReach, and your most engaged website visitors become your next LinkedIn conversations — automatically.

This guide walks you through setting up the HeyReach + IntentStream integration from scratch.

## **The building blocks: what's what?**

**HeyReach** is a LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every connection request, message, and reply. Whether you're an agency managing dozens of client accounts or a sales team running high-volume prospecting, HeyReach handles the LinkedIn side — safely, efficiently, and at scale.

**IntentStream** is a B2B advertising and activation platform that resolves anonymous website visitors into known buyers. It taps into a 200M+ B2B identity graph and uses real-time behavioral and firmographic signals to build high-intent audience segments — the people actively showing purchase intent right now. Those audiences can be activated across paid channels through IntentStream's own DSP, or pushed directly into HeyReach for LinkedIn outreach.

### **What they solve together**

* **Turn anonymous traffic into named prospects.** IntentStream identifies the people behind your website visits and resolves them into actionable LinkedIn-ready profiles.
* **Reach high-intent leads before they go cold.** Timing is everything in outreach — IntentStream feeds HeyReach with prospects while their interest is at its peak.
* **Eliminate manual list-building.** No more downloading CSVs from a data vendor, enriching them elsewhere, and manually uploading them to campaigns. The integration handles the handoff automatically.
* **Run truly multichannel outreach.** IntentStream can activate the same high-intent audiences across paid social, programmatic ads, and LinkedIn outreach simultaneously — so your prospects see you everywhere, not just in their inbox.
* **Keep campaigns fresh without lifting a finger.** With continuous sync enabled, newly identified intent signals flow into your HeyReach campaigns on an ongoing basis — no manual refreshes needed.

## **Prerequisites**

Before you start, make sure you have:

* An active HeyReach account with at least one campaign or lead list set up
* An active IntentStream account with tracking installed on your website
* Your HeyReach API key (you'll need this to connect the two platforms)

## **Setting up the integration**

### **Part 1: Connect HeyReach to IntentStream**

**Step 1: Get your HeyReach API key**

Log in to HeyReach and navigate to **Settings → API**. Copy your API key and keep it handy — you'll paste it into IntentStream in the next step.

> 💡 **Pro tip:** If you don't see an API section in your settings, check that your HeyReach plan includes API access. Reach out to HeyReach support if you're unsure.

**Step 2: Add HeyReach as a connected platform in IntentStream**

Inside IntentStream, navigate to **Integrations** (or **Connected Platforms** and locate HeyReach in the list of available integrations. Click **Connect** and paste in your HeyReach API key when prompted.

✅ Once connected, you should see a confirmation that IntentStream has successfully authenticated with your HeyReach account.

**Step 3: Verify the connection**

IntentStream will pull a list of your existing HeyReach campaigns and lead lists to confirm the integration is working. If you can see your campaigns listed inside IntentStream, you're good to go.

> ⚠️ **Watch out:** If the connection fails, double-check that you've copied the full API key without any trailing spaces. API key errors are the most common cause of failed integrations.

### **Part 2: Build your intent audience and push it to HeyReach**

**Step 4: Define your intent audience in IntentStream**

In IntentStream, navigate to **Audiences** and create a new segment. You'll filter by a combination of:

* **Behavioral signals** — pages visited, time on site, repeat visits, content consumed
* **Firmographic filters** — company size, industry, geography, job title

> 💡 **Pro tip:** Start with a tighter audience rather than a broad one. Prospects who visited your pricing page or a product-specific page are significantly more likely to respond than general blog visitors. Narrow = higher intent = better reply rates in HeyReach.

**Step 5: Choose your HeyReach destination**

Once your audience is defined, click **Activate** and select where you want these profiles to land:

* **Option A: Push to a HeyReach campaign** — Profiles are added directly as leads in an active campaign and will enter your outreach sequence immediately.
* **Option B: Push to a HeyReach lead list** — Profiles are added to a list, which you can review and manually add to a campaign when ready. Good if you want to QA intent audiences before they hit your sequences.

**Step 6: Choose your sync mode**

After selecting your destination, choose how you want the data to flow:

* **On-demand push** — Send the current audience snapshot to HeyReach once. Use this for a one-time campaign targeting a specific moment in time (a product launch, an event, a promotional window).
* **Continuous sync** — IntentStream monitors your audience criteria in real time and automatically sends newly identified profiles to your HeyReach campaign or list as they're resolved. This is the "set it and forget it" option — your HeyReach campaigns stay perpetually fresh with high-intent leads.

> 🚨 **Critical:** If you're using continuous sync with a live HeyReach campaign, make sure your campaign sequence has appropriate delays and connection limits set. Flooding a campaign with too many new leads at once can affect your LinkedIn account's health. Work with your IntentStream account representative if you're unsure how to pace the flow.

**Step 7: Confirm and activate**

Review your settings — audience criteria, destination campaign or list, sync mode — and click **Activate**. IntentStream will begin resolving and pushing profiles based on your configuration.

✅ You should see new leads appearing in your selected HeyReach campaign or list within a short window, depending on the volume of visitor traffic being resolved.

## **Common `workflows`**

### **Workflow 1: Warm-up outreach to high-intent pricing page visitors**

IntentStream detects a company visiting your pricing page multiple times in 48 hours → resolves the decision-maker profiles → continuously syncs them into a HeyReach campaign → HeyReach sends a personalized LinkedIn connection request with a message that acknowledges the prospect's likely evaluation stage (e.g., "Hey [Name], noticed [Company] has been exploring solutions in [category]...").

This workflow is ideal for SaaS or services companies where pricing page visits are a strong purchase signal.

### **Workflow 2: Event-based outreach surge**

Your company runs a webinar or attends a conference → you push a dedicated tracking link for event follow-up → IntentStream captures attendees or registrants visiting your site in the following days → on-demand push sends the resolved profiles to a dedicated HeyReach campaign built around the event context.

Use the on-demand push mode here so you're working with a clean, time-boxed audience.

### **Workflow 3: Multichannel squeeze**

IntentStream identifies a high-intent segment → pushes them to HeyReach for LinkedIn outreach → simultaneously activates the same audience across LinkedIn Ads and IntentStream's DSP for programmatic ads → your prospect receives a LinkedIn connection request, sees retargeting ads, and gets a LinkedIn message in their inbox.

This is the full multichannel play. Same audience, three touchpoints, coordinated timing — without you having to manage each channel separately.

### **Workflow 4: Agency managing multiple client accounts**

Agency sets up separate IntentStream audience segments for each client, each mapped to a specific HeyReach campaign under the relevant client's LinkedIn account → continuous sync runs independently per client → agency reviews performance centrally in IntentStream and optimizes segments based on reply rates in HeyReach.

> 💡 **Pro tip:** Use IntentStream's account representative support to help structure multi-client audience logic from the start. Getting the segmentation right early saves a lot of cleanup later.

## **Troubleshooting**

* **Integration won't authenticate with HeyReach API key:** Ensure you copied the full key with no extra spaces and that your HeyReach plan includes API access. If needed, regenerate the key and try again.
* **Can't see HeyReach campaigns in IntentStream:** Disconnect and reconnect the integration. Confirm campaigns are active (not paused or archived).
* **Profiles pushed to HeyReach but leads aren't entering sequences:** Make sure the campaign is active. Verify the selected lead list or campaign matches the intended destination. Leads in a list may require manual assignment to a campaign.
* **Continuous sync sending too many leads:** Contact your IntentStream rep to configure pacing and throttling. Check HeyReach daily sending limits to stay within safe LinkedIn limits.
* **Some resolved profiles missing LinkedIn URLs or mismatched:** Identity resolution isn't perfect. Review a sample of pushed leads in HeyReach before running high-stakes campaigns.

## **Quick-start checklist**

**In HeyReach:**

* Confirm your HeyReach plan includes API access
* Copy your HeyReach API key from Settings → API
* Set up at least one campaign or lead list as your push destination
* Review and configure daily sending limits in your target campaign

**In IntentStream:**

* Confirm tracking is installed and firing on your website
* Connect HeyReach using your API key
* Verify the connection (your campaigns should appear in IntentStream)
* Build your intent audience using behavioral and firmographic filters
* Select your HeyReach destination (campaign or lead list)
* Choose your sync mode (on-demand or continuous)
* Activate the integration

**Before going live:**

* Do a small-scale test push and confirm leads appear correctly in HeyReach
* Review sample profiles for accuracy
* Confirm your HeyReach sequence messaging is relevant to an intent-based audience

And that’s it! Your LinkedIn outreach is now powered by real buying intent, running on autopilot.
