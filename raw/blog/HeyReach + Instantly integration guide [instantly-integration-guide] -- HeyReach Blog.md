# HeyReach + Instantly integration guide

Source: https://www.heyreach.io/blog/instantly-integration-guide

Summary: Connect HeyReach and Instantly to automate multi-channel outreach. Send LinkedIn prospects to email sequences automatically when they don't respond. Setup guide + workflows included.

You're crushing it on LinkedIn—sending connection requests, following up with messages, building pipeline. But some **prospects don't respond on LinkedIn alone**. They're busy, they miss notifications, or they simply prefer email. Meanwhile, you're manually tracking who needs email follow-up, copying data between platforms, and watching hot leads go cold because you couldn't reach them fast enough.

The solution? Automated multi-channel outreach that follows prospects from LinkedIn to their inbox—without hiring a data engineer or drowning in spreadsheets.

## **The building blocks: What's what?**

### **HeyReach**

HeyReach is a LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every connection request, message, and reply. Whether you're an agency managing dozens of accounts or a sales team running high-volume prospecting, HeyReach handles the LinkedIn side—safely, efficiently, and at scale.

### **Instantly**

Instantly is an email outreach platform that automates cold email at scale. It handles unlimited email accounts, keeps your messages out of spam with built-in warmup, manages deliverability across multiple inboxes, and tracks replies in one unified dashboard. If you need to send thousands of personalized emails without tanking your sender reputation, Instantly is the engine that powers it.

### **What they solve together**

Here's the problem: prospects split their attention between LinkedIn and email. If you only hit one channel, you're leaving meetings on the table. But managing both manually is a nightmare—tracking who responded where, remembering who needs follow-up, syncing data between platforms.

**The HeyReach + Instantly integration solves this with bidirectional automation.**

LinkedIn message goes unanswered? That lead hits your email sequence.

Cold email campaign finishes with no reply? That prospect gets added to LinkedIn outreach.

Warm email responder? Push them to LinkedIn for relationship building.

You set the rules once, and the integration handles the rest—no manual exports, no forgotten follow-ups, no leads slipping through the cracks.

You get to double the touchpoints with half the effort, and prospects get reached on whichever channel they actually check their inboxes.

## **Setup instructions: Connect HeyReach + Instantly in 5 minutes**

## **Part 1: Connect HeyReach to Instantly**

### **Step 1: Generate your Instantly API Key**

1. Open Instantly and go to **Settings → Integrations → API Keys**
2. Click **Create a new key**
3. **Select all scopes** (this ensures everything works—missing scopes cause errors)
4. Click **Generate** and copy the key

### **Step 2: Connect Instantly to HeyReach**

1. In HeyReach, go to **Integrations → Instantly**
2. Click **Connect Now**
3. Paste your Instantly API key when prompted
4. Hit save

You'll see the integration status change to **Connected ✅**

## **How to send leads from HeyReach to Instantly**

HeyReach gives you **two ways** to send leads into Instantly:

### **Option 1: Send leads directly to Instantly campaigns (Recommended)**

Use this when you want leads to **immediately start receiving email sequences**. No extra steps—they go straight into an active campaign.

**How it works:**

1. Add the **"Add to Instantly"** action in your HeyReach campaign sequence
2. Select **"Instantly Campaigns"**
3. Pick the campaign you want leads sent to from the dropdown

**Important:** The campaign must already exist in Instantly. Only then will it appear in HeyReach.

### **Option 2: Send leads to Instantly lists**

Use this when you want to **collect leads first, then decide which campaign to run them through later**. Perfect for:

* Leads that need email enrichment before sending
* Building segmented lists over time
* Manual review before activation

**How it works:**

1. Add the **"Add to Instantly"** action in your HeyReach campaign sequence
2. Select **"Instantly Lists"**
3. Choose which Instantly Lead List you want leads sent to

> **⚠️ Important:** Lead Lists must be created in Instantly first. Once created there, they'll automatically appear in HeyReach.

## **Understanding email types in HeyReach**

HeyReach handles two types of emails:

### **Enriched email**

This is the email address found through HeyReach's internal enrichment systems. You **cannot manually edit** this email—it's automatically discovered and populated.

### **Custom email**

This is an email you import or manually add yourself. HeyReach doesn't populate this value—you control it entirely.

**To edit a custom email:**

1. Click on the lead's full name in any list
2. The Lead Profile card opens on the left
3. Click the pencil icon next to Custom Email
4. Edit and hit Save

## **Email rules when sending from HeyReach to Instantly**

### **For leads sent to campaigns:**

* **Leads WITHOUT email → will fail** (error message shown)
* **Leads with enriched email only** → Enriched email is sent
* **Leads with custom email only** → Custom email is sent
* **Leads with both** → Custom email takes priority

### **For leads sent to lists:**

* **Leads without email → still added** (you can enrich them later in Instantly)
* **Leads with Enriched email only** → Enriched email is sent
* **Leads with Custom email only** → Custom email is sent
* **Leads with both** → Custom email takes priority

**Pro tip:** Custom emails always win when both exist. Use this to override enriched emails when you have better data.

## **Using the *Find Email* action in HeyReach campaigns**

You can discover professional email addresses directly inside your HeyReach campaigns using the **Find Email** action.

**How it works:**

1. Add the **Find Email** action anywhere in your campaign sequence
2. Click Continue to agree to use Credits for emails found
3. The sequence branches based on results:
   * **Email Found** → route to Instantly or continue LinkedIn outreach
   * **Email Not Found** → continue with LinkedIn-only approach

> **⚠️ Important:** Find Email can only be added **once per sequence** and will trigger **once per lead per campaign**.

### **Example workflow 1: Find email first**

* Find Email → Email Not Found → Send Connection Request
* Find Email → Email Found → If Not Connected → Add to Instantly Campaign
* Find Email → Email Found → If Connected → Send LinkedIn Message

### **Example Workflow 2: LinkedIn first, Email fallback**

* Send Connection Request → Not Accepted → Find Email → Email Found → Add to Instantly
* Send Connection Request → Accepted → Send LinkedIn Message

> **⚠️** [**Credits**](https://help.heyreach.io/en/articles/12855506-how-do-the-email-credits-work-in-heyreach)**:** Each successful email found consumes HeyReach credits. You'll see a confirmation before running the campaign.

## **Common HeyReach → Instantly workflows**

### **Workflow 1: No connection acceptance**

* Send connection request → wait 10 days
* If not accepted → Find Email → Add to Instantly Campaign → start email sequence

### **Workflow 2: LinkedIn messages ignored**

* Send InMail or message → wait 5 days
* No reply → Add to Instantly List → enrich → move to campaign

### **Workflow 3: Warm but unresponsive**

* Connection accepted but no replies to messages → Add to Instantly Campaign
* Route to "Warm, No Reply" campaign with softer nurture emails

## **Part 2: Connect Instantly to HeyReach (Bidirectional Integration)**

### **Step 1: Generate Your HeyReach API Key**

1. Open HeyReach and go to **Integrations → HeyReach API → Get API Key**
2. Generate the API key and copy it

### **Step 2: Add HeyReach to Instantly**

1. Open Instantly and go to **Settings → Integrations**
2. Find **HeyReach** and click **Get New**
3. Paste your HeyReach API key
4. Click **Connect**

Once saved, Instantly will display your connected HeyReach Workspaces ✅

## **How to send leads from Instantly to HeyReach**

Inside Instantly, you'll create **Automation workflows** that trigger leads to move into HeyReach campaigns or lists.

### **Create an Automation Workflow**

1. In Instantly, go to **Automations**
2. Click **+ Add New** to create a workflow

### **Step 1: Add a trigger (what starts the workflow)**

1. From Built-In tools, select **Instantly**
2. Choose your trigger event from the dropdown:
   * **Lead interest status changed**
   * **Campaign finished for lead**
   * **Lead added to list**
   * **Lead replies**

**Example Trigger:** Campaign Finished for Lead

3. Select the specific Instantly campaign this workflow applies to

> **⚠️ Important:** Only one Instantly campaign per trigger event

4. Choose when the trigger should run:
   * Campaign ended and the lead did not reply
   * Campaign ended after the lead replied

**Example:** Campaign ended and the lead did not reply

5. Click Continue to test and save

### **Step 2: Add an Action (what happens next)**

1. Select **HeyReach** as your action
2. Choose your HeyReach workspace (account)
3. Select the Action Event:
   * **Add Lead to Campaign**
   * **Add Lead to List**

**Example Action:** Add Lead to Campaign

4. Select the HeyReach campaign where leads should be sent
5. The data fields will auto-map (LinkedIn profile, name, email, etc.)
6. Click **Continue**
7. Hit **Test Step** to verify data mapping is correct
8. Click **Save** to activate the workflow

## **Common Instantly → HeyReach Workflows**

### **Workflow 1: Cold email non-responders to LinkedIn**

* Trigger: Email campaign finishes with no reply
* Action: Add lead to HeyReach LinkedIn outreach campaign

### **Workflow 2: Warm email responders to LinkedIn relationship Building**

* Trigger: Lead replies to email
* Action: Add lead to HeyReach "Warm Nurture" campaign with softer LinkedIn messaging

### **Workflow 3: Interest signal routing**

* Trigger: Lead marked as interested in Instantly
* Action: Add lead to HeyReach list for manual review and personalized LinkedIn outreach

## **Troubleshooting**

### **Integration shows "Disconnected" or API errors**

**Problem:** Integration was working but suddenly stopped.

**Solution:**

1. Check if your API keys are still valid (they can expire or be regenerated)
2. Verify you selected **all scopes** when generating keys
3. Disconnect and reconnect with fresh API keys

### **Leads failing when sent to Instantly campaigns from HeyReach**

**Problem:** Leads aren't being added to Instantly campaigns.

**Solution:** Check if leads have email addresses. Leads without emails will fail when sent to campaigns. Use the **Find Email** action first or send to Instantly Lists instead.

### **Leads not appearing in HeyReach from Instantly automation**

**Problem:** Instantly automation runs but leads don't show in HeyReach.

**Solution:**

1. Check the automation test step—verify data fields are mapping correctly
2. Ensure the HeyReach campaign or list you selected still exists
3. Check if leads already exist in that HeyReach campaign (duplicates may be skipped)

### **New campaigns/lists not showing in dropdown**

**Problem:** Created a new campaign or list but don't see it in integration dropdowns.

**Solution:** Refresh the page. Both platforms pull available campaigns/lists on page load.

### **Find email action not working**

**Problem:** Find Email step shows errors or doesn't find emails.

**Solution:**

1. Verify you have enough HeyReach credits
2. Check if Find Email was already used once in this sequence (it can only trigger once per lead per campaign)
3. Some leads may not have discoverable emails—this is expected

### **How do I know which direction to send leads?**

Ask yourself:

* **LinkedIn cold, email warm?** → Instantly to HeyReach (build relationships on LinkedIn)
* **LinkedIn warm, email cold?** → HeyReach to Instantly (try email as secondary channel)
* **Both cold?** → Start wherever you have better data, use other channel as fallback

## **Quick-start checklist: Bidirectional setup**

### **HeyReach → Instantly Setup**

* Generate Instantly API key with all scopes
* Connect Instantly in HeyReach (Integrations → Instantly)
* Create at least one Instantly Campaign or List
* Add "Add to Instantly" action in HeyReach campaign
* Select Campaigns or Lists and pick destination
* Optional: Add Find Email action before sending to Campaigns

### **Instantly → HeyReach Setup**

* Generate HeyReach API key
* Connect HeyReach in Instantly (Settings → Integrations)
* Create at least one HeyReach Campaign or List
* Go to Instantly Automations → Add New
* Add Trigger (e.g., Campaign Finished for Lead)
* Add Action (Add Lead to HeyReach Campaign/List)
* Test and save automation

### **Test It**

* Run test leads through both directions
* Verify leads appear in correct destinations
* Check data mapping is accurate (emails, names, profiles)

### **Scale It**

* Activate campaigns on both platforms
* Monitor lead flow in both directions
* Adjust timing and routing based on results
