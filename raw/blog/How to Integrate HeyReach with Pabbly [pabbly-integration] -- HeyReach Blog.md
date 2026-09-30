# How to Integrate HeyReach with Pabbly

Source: https://www.heyreach.io/blog/pabbly-integration

Summary: Learn how to connect HeyReach with Pabbly to push LinkedIn outreach data into Slack, HubSpot, Google Sheets, and more. Step-by-step setup with webhooks explained.

Outreach doesn’t stop at LinkedIn — the real efficiency comes when every reply, connection, or lead event flows straight into the tools your team already lives in.

That’s where **HeyReach + Pabbly** comes in. By linking the two, you can instantly send activity from your HeyReach campaigns into Slack, HubSpot, Google Sheets, Gmail, or just about any other app — all without touching a line of code.

I’ll walk you through setting up that connection step by step, so your outreach data moves automatically to where it matters most.

## **Building blocks: What’s what?!**

* **HeyReach** – LinkedIn outreach automation platform that lets you run campaigns across multiple accounts.
* **Pabbly Connect** – a no-code workflow automation tool that connects apps via triggers and actions.
* **Webhook** – a URL where HeyReach sends event data (e.g., reply received, connection accepted).

Together, these let you automate data flow from HeyReach → Pabbly → your tool of choice (Slack, HubSpot, Google Sheets, etc.).

## **Step 1: Create a Workflow in Pabbly**

1. Log into your Pabbly dashboard.
2. Click **Create Workflow**.
3. Name your workflow (e.g., “HeyReach → Slack”).
4. Choose **HeyReach** as your **Trigger App**.
5. Select a **Trigger Event** (e.g., “New Reply Received,” “Connection Accepted”).

For this example, we’ll push replies from HeyReach campaigns into **Slack**.

## **Step 2: Create a Webhook in HeyReach**

1. In HeyReach, go to **Integrations** → **View/Create Webhooks**.
2. Click **Create Webhook**.
3. A right-side panel will open. Fill in the following:
   * **Webhook Name** (e.g., “Slack Notification”)
   * **Webhook URL** (provided by Pabbly when you create the workflow)
   * **Campaign** (select the campaign you want to connect)
   * **Event Type** (e.g., “Reply Received”)
4. Click **Save**.

Congrats! Your webhook is now live. You can test it inside your Pabbly workflow.

## **Step 3: Create the action in Pabbly**

1. In your Pabbly workflow, choose the **Action App** (e.g., Slack, HubSpot, Google Sheets).
2. Select an **Action Event** (e.g., “Send Channel Message” for Slack).
3. Connect your Action App account.
4. Map the incoming data fields from HeyReach (like name, LinkedIn profile, message) into your Action App.
5. Click **Connect**.

## **Step 4: Test & Run**

* Perform a test action in HeyReach (e.g., trigger a reply).
* Check your Action App (e.g., Slack) to confirm the workflow is working.
* Once verified, turn the workflow **ON** in Pabbly.

Now every time the selected HeyReach event happens, Pabbly will automatically push it to your chosen app. 🚀

## **Example use cases**

* **HeyReach → Slack**: Send a Slack notification when a prospect replies.
* **HeyReach → HubSpot**: Push new leads or replies into HubSpot CRM.
* **HeyReach → Google Sheets**: Log all new connections or replies into a spreadsheet automatically.
* **HeyReach → Gmail**: Trigger a personalized follow-up email when someone accepts your LinkedIn request.

That’s all it takes. With HeyReach and Pabbly working together, every action in your LinkedIn outreach can trigger something meaningful elsewhere in your stack — whether that’s a Slack ping, a HubSpot update, or a fresh row in Google Sheets. Once you flip the workflow on, the manual copy-paste days are behind you.

If you need help fine-tuning your setup, our team’s always here to back you up. 🚀
