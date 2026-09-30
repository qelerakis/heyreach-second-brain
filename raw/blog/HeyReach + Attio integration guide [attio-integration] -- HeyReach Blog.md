# HeyReach + Attio integration guide

Source: https://www.heyreach.io/blog/attio-integration

Summary: Integrating HeyReach with Attio keeps your LinkedIn CRM in sync — outreach activity updates automatically, contacts flow into campaigns, and your pipeline stays current in real time without spreadsheets or repetitive data entry.

If you're using Attio to manage your pipeline, you've probably felt the friction of manually logging LinkedIn activity or copy-pasting contacts across tools. It's slow, it's error-prone, and it means your CRM is always a step behind what's actually happening in your outreach.

That changes with the **HeyReach–Attio integration**. Through a dedicated Attio app, you get a genuine two-way sync: LinkedIn activity from HeyReach flows into Attio automatically, and you can push contacts from Attio directly into HeyReach campaigns and lists. **No middleware required. No manual exports.**

I’ll walk you through setting it up – from installing the app to running your first workflow.

## **The building blocks: What's what?**

[**HeyReach**](https://www.heyreach.io/blog/heyreach-review) — A LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every connection request, message, and reply. Whether you're an agency managing dozens of client accounts or a sales team running [high-volume prospecting,](https://www.heyreach.io/blog/outbound-sales-automation) HeyReach handles the LinkedIn side — safely, efficiently, and at scale.

**Attio** — A modern, highly flexible CRM built around your data model. Attio lets you structure contacts, companies, and deals however your team actually works — with custom objects, powerful filtering, and real-time collaboration. It's become a go-to for GTM teams that want a CRM that adapts to them, not the other way around.

### **What they solve together:**

* LinkedIn activity (connection requests sent/accepted, messages, replies) is logged in Attio automatically.
* New LinkedIn contacts who don't exist in Attio yet get created automatically when HeyReach events come in.
* You can bulk-add Attio contacts directly into HeyReach campaigns or lists without leaving Attio.
* All HeyReach event data — LinkedIn URL, message body, campaign name, company, tags — is captured as structured Attio attributes.
* You stay in control of which events you want to track and sync, so your CRM doesn't fill up with noise.

## **Part 1: Setting up the Attio app and connecting HeyReach**

### **Step 1: Install the HeyReach app in Attio**

1. **Navigate to the app installation URL** — Contact the app developer for the direct install link (details in the Attio community or via the developer's email).
2. **Click Install** to begin the installation process.
3. **Review the permissions** — The app needs read/write access to records and lists (for logging and syncing contact data) and webhook permissions (for receiving real-time events from HeyReach). These are the minimum required to make the integration work.
4. **Click Install App** to confirm.

💡 **About the app:** This is a community-built Attio app, not a native HeyReach product. It's available on any Attio tier — free, Plus, or Pro — because it uses standard Attio lists and webhooks.

### **Step 2: Connect your HeyReach API key**

1. Inside the installed app, go to the **Connections** tab.
2. Click **Connect**.
3. **Paste your HeyReach API key** into the field provided.
   * To find your API key: go to HeyReach → **Integrations** → **Get API Key**.
4. Click **Add Connection**.

✅ Once connected, the app will automatically create up to 12 webhooks in HeyReach — one for each supported activity event type. You'll see these appear in your HeyReach **Integrations** panel.

> ⚠️ **Watch out:** The app also creates a dedicated **HeyReach Events** list in your Attio workspace automatically. This list is pre-configured with all the relevant data attributes from HeyReach payloads — LinkedIn URL, message body, campaign name, company, tags, and more. Don't delete this list; it's the backbone of the sync.

### **Step 3: Configure which events to track**

Not every HeyReach event needs to land in your CRM. The app lets you choose which events trigger activity in Attio.

1. Inside the app settings, review the **active webhook events**. By default, the app enables the events most likely to be meaningful — such as connection request accepted and message replied.
2. **Toggle events on or off** based on what you actually want to capture. For example, many users prefer not to create Attio records for "profile viewed" events.

> 💡 **Pro tip:** If a LinkedIn contact doesn't already exist in Attio when an event fires, the app will automatically create a new person record for them. This is powerful — but worth being aware of if you have a tightly controlled CRM. Adjust your active events accordingly.

### **Step 4: Create a list view for your HeyReach Events**

The HeyReach Events list is created automatically, but you'll want to configure a view to make it useful.

1. In Attio, navigate to the **HeyReach Events** list.
2. Click **Create View** and give it a name (e.g., "Campaign Activity" or "LinkedIn Events").
3. Add the columns you want to see — campaign name, event type, LinkedIn URL, message body, and any other attributes relevant to your workflow.

✅ Your Attio workspace is now set up to receive real-time activity from all your HeyReach campaigns.

## **Part 2: Pushing contacts from Attio into HeyReach**

This is where the bidirectional sync earns its place. Instead of exporting CSVs or switching between tools, you can add contacts to HeyReach campaigns or lists directly from Attio.

### **Step 5: Bulk-add contacts to a HeyReach campaign**

1. In Attio, go to **People** and select the contacts you want to add to a campaign.
2. Click the **More** menu (or right-click the selection).
3. Choose **Add to HeyReach Campaign** or **Add to HeyReach List**.
4. In the dialogue that appears:
   * **Select your LinkedIn account** — if you have [multiple accounts connected in HeyReach,](https://www.heyreach.io/blog/manage-multiple-linkedin-accounts) they'll all appear here.
   * **Select the campaign** you want to add people to.
5. Click **Add to Campaign**.

✅ You'll see a results summary showing how many contacts were successfully added, how many were updated (already in the campaign), and any that failed.

> 🚨 **Important:** HeyReach does not accept old-style LinkedIn URLs containing /pub/ in the path. If any contacts have this URL format in Attio, they'll appear in the failure count. Update those LinkedIn URLs to the standard format before re-adding.

### **Step 6: Add an individual contact to a campaign or list**

For one-off additions, you don't need to go through bulk selection.

1. Open any individual person record in Attio.
2. Look for the **HeyReach** section in the record panel.
3. Choose **Add to HeyReach Campaign** or **Add to HeyReach List**.
4. Select the LinkedIn account and target campaign or list.
5. Review the pre-filled contact details — you can edit any of the data fields before submitting if needed.
6. Click **Add to Campaign** or **Add to List**.

> 💡 **Pro tip:** The contact's details from their Attio record are pre-populated automatically. If you need to update or override any field (e.g., personalise the first message), you can do so right here before adding them.

## **Common workflows**

**Workflow 1: Auto-log LinkedIn replies to Attio** HeyReach sends a message → prospect replies on LinkedIn → the reply event fires a webhook → Attio logs the event in the HeyReach Events list with the full message body, LinkedIn URL, and campaign name. Your team sees it in real time, without touching HeyReach.

**Workflow 2:** [**ICP list**](https://www.heyreach.io/blog/outbound-channel) **→ LinkedIn campaign** You build a filtered view of target accounts in Attio → bulk-select the contacts → push them directly into a HeyReach campaign. Your LinkedIn outreach starts within minutes, no CSV needed.

**Workflow 3: New connection → CRM record** A prospect accepts your [connection request](https://www.heyreach.io/blog/linkedin-connection-message) in HeyReach → the event fires → if they don't exist in Attio yet, a new person record is created automatically with their LinkedIn URL, company, and tags populated.

**Workflow 4: Warm leads → priority campaign** You filter your Attio contacts by a custom attribute (e.g., "Opened > 3 emails" or "Stage = Warm") → push that segment into a dedicated HeyReach [follow-up campaign.](https://www.heyreach.io/blog/follow-up-email-and-linkedin-message) Targeted LinkedIn outreach to your warmest prospects, triggered directly from your CRM data.

## **Troubleshooting**

* **Some contacts failed to add to the campaign** **Solution:** Check whether their LinkedIn URLs contain /pub/ in the path — this is an older URL format that HeyReach doesn't accept. Update the LinkedIn URL field in Attio to use the standard linkedin.com/in/username format, then retry.
* **No webhooks appeared after connecting** **Solution:** Double-check that the API key was pasted correctly with no trailing spaces. Disconnect and reconnect. If webhooks still don't appear in HeyReach Integrations, rotate your API key in HeyReach and reconnect with the new one.
* **The HeyReach Events list was created but isn't populating** **Solution:** Confirm that at least one webhook event is toggled on in the app settings. Then trigger a test event in HeyReach (e.g., send a campaign with a test contact) and wait a few seconds for the data to appear.
* **Multiple LinkedIn accounts aren't appearing in the dropdown** **Solution:** All LinkedIn accounts must be connected to the same [HeyReach workspace](https://help.heyreach.io/en/articles/11980482-how-to-create-a-workspace-in-heyreach) tied to the API key you used. If some accounts are under a different workspace, they won't appear. Use the correct API key for the workspace containing all relevant accounts.
* **I removed the app — will it delete my Attio data?** **Solution:** No. Disconnecting the workspace connection removes the webhooks from HeyReach, but your HeyReach Events list and all records in Attio remain intact. Nothing is deleted on the Attio side.

## **Quick-start checklist**

**Setting up the HeyReach → Attio sync (inbound events):**

* Install the HeyReach app in Attio via the install URL
* Go to Connections → Connect and paste your HeyReach API key
* Confirm 12 webhooks were created in HeyReach Integrations
* Review and configure which events to track (toggle off events like "profile viewed" if not needed)
* Open the HeyReach Events list in Attio and create a custom view with your preferred columns

**Pushing contacts from Attio → HeyReach (outbound):**

* In Attio People, select the contacts you want to add
* Use More → Add to HeyReach Campaign or Add to HeyReach List
* Select the LinkedIn account and campaign/list
* Check the results summary and fix any contacts with legacy LinkedIn URL formats

🎯 HeyReach and Attio are now working together — LinkedIn activity flowing in, contacts flowing out, and your CRM finally as live as your outreach.
