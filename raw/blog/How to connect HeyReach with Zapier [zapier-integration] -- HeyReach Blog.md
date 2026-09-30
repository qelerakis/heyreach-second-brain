# How to connect HeyReach with Zapier

Source: https://www.heyreach.io/blog/zapier-integration

Summary: Learn how to connect HeyReach with thousands of apps using Zapier integration. Automate workflows, sync leads, and get notified in Slack or HubSpot effortlessly.

You can integrate HeyReach with thousands of tools via **Zapier**. While HeyReach doesn’t yet have a native Zapier app, you can connect the two using **Webhooks**. This allows you to either **send data from HeyReach to Zapier** (when something happens in HeyReach) or **send data into HeyReach** (from your other apps).

## **Option 1: Send Data from HeyReach → Zapier**

Use this if you want HeyReach events (e.g. new reply, connection accepted) to trigger workflows in Zapier.

### **Step 1: Create a Zap in Zapier**

1. Log in to Zapier.
2. Click **Create Zap**.
3. For the trigger, select **Webhooks by Zapier**.
4. Choose **Catch Hook** as the trigger event.
5. Zapier will generate a unique **Webhook URL**. Copy it.

### **Step 2: Add the Webhook in HeyReach**

1. Open **HeyReach**
2. Go to **Integrations → Webhooks**.
3. Click **Add New Webhook**.
4. Paste the Zapier Webhook URL you copied.
5. Select the event(s) you want to send (e.g. “Reply received”, “Connection request accepted”).

### **Step 3: Test the Connection**

1. Perform the chosen action in HeyReach (e.g. send a test message).
2. In Zapier, click **Test trigger**. You should see data from HeyReach

### **Step 4: Add Your Action**

Now choose what happens next:

* Send a Slack/Teams notification.
* Update your CRM (HubSpot, Salesforce, Pipedrive).
* Add a row in Google Sheets.

**Option 2: Send Data from Zapier → HeyReach**

Use this if you want to push leads into HeyReach when something happens in another app (e.g. Calendly booking, new row in Google Sheets).

### **Step 1: Create a Zap in Zapier**

1. Log in to Zapier.
2. Click **Create Zap**.
3. Choose your trigger app (e.g. Calendly, Typeform, Google Sheets).

### **Step 2: Set HeyReach as the Action**

1. For the action, select **Webhooks by Zapier**.
2. Choose **POST** as the event.
3. Enter HeyReach’s **API endpoint** for creating a lead or updating a campaign (found in **HeyReach → Settings → API**).

### **Step 3: Add Authentication**

1. In the request header, add:
   * Key: Authorization
   * Value: Bearer YOUR\_API\_KEY (replace with your HeyReach API key).

### **Step 4: Map Your Fields**

Map the trigger app’s fields (like firstName, lastName, LinkedInProfileUrl, email) to HeyReach’s required fields.

### **Step 5: Test and Activate**

1. Send a test from Zapier.
2. Check HeyReach — the lead should appear in your campaign.
3. Turn on your Zap.

## **Example Use Cases**

* **Calendly → HeyReach**: Every new meeting adds the contact into a LinkedIn outreach sequence.
  **HeyReach → Slack**: Get notified in Slack when a prospect replies.
* **Google Sheets → HeyReach**: Upload new rows of leads into campaigns automatically.

**HeyReach → HubSpot**: Sync outreach replies into HubSpot for your sales team.
