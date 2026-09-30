# How to Integrate HeyReach with n8n (and automate your LinkedIn workflows)

Source: https://www.heyreach.io/blog/n8n-integration

Summary: Unlock the power of HeyReach and n8n integration to improve LinkedIn outreach. Automate campaigns, sync leads, and make your outbound effortless.

## **How to Integrate HeyReach with n8n (and automate your LinkedIn workflows)**

Ever wished your LinkedIn outreach could just *run itself* while you sit back and focus on conversations that actually matter?

That’s exactly what you get when you connect **HeyReach** with **n8n**.

Together, they help you automate your outreach, sync data across tools, and trigger workflows based on real activity — no manual exporting, no CSV uploads, no chaos. Just a smooth, powerful setup for your outbound engine.

Let’s walk through how to set it up.

## **The building blocks: What’s what?**

Before we dive in, here’s what each tool brings to the table:

[**HeyReach**](https://www.heyreach.io/blog/heyreach-review) – Your LinkedIn automation powerhouse. It runs campaigns, connection requests, and follow-ups safely across multiple accounts — all in the cloud, with unified inboxes and smart account rotation. From recently powering the game with HeyReach MCP server, so you  can run everything from your favorite AI agent.

**n8n** – A no-code workflow automation tool that connects your favorite apps (like HeyReach, [Slack](https://www.heyreach.io/integration/slack), [HubSpot](https://www.heyreach.io/integration/hubspot), and more). It helps you build custom automations to sync data or trigger actions when things happen in HeyReach.

Together, they give your [sales stack](https://www.heyreach.io/blog/sales-tech-stack) superpowers.

### **Want to see it in action? 🎥**‍

Watch the HeyReach x n8n video tutorial 👇

## **Why connect HeyReach and n8n?**

Because [LinkedIn outreach](https://www.heyreach.io/blog/linkedin-outreach) doesn’t have to be manual or risky.

When you connect HeyReach and n8n, you can:

* Automatically trigger campaigns when a new lead comes in
* Sync leads and campaign data between apps in real time
* Push high-intent prospects directly into HeyReach sequences
* Set up advanced automations without coding

If you’re managing multiple client workspaces, teams, or outbound sequences, this combo is a must-have. You’ll go from *“we should add this lead manually”* to *“it’s already in the campaign.”*

Ready? Let’s connect the two. 👇

## **Step 1: Get your n8n key in HeyReach**

Each workspace in HeyReach comes with its own **MCP Server URL** and **MCP Key** — you’ll need these to authenticate n8n.

Here’s how to find them:

1. Go to **Integrations** in HeyReach.
2. Find **n8n** and hit **Connect Now**.

3. Click **Generate New n8n (API) Key** (if you don’t already have one).

4. Copy your **n8n Key** — you’ll need it in the next step.

> 💡 Each key is unique per workspace, which makes it easy to keep client or team setups separate.

## **Step 2: Add the HeyReach key to n8n (web version)**

If you’re using the **n8n Web Version**:

1. Log in to your n8n account.
2. Click **Add first step**.
3. Select **HeyReach API** as a trigger for your workflow.

4. Install the required nodes — you’ll get access to HeyReach actions like **Campaigns**, **Unibox**, **Lists**, **Stats**, and **Webhooks**.

5. Create a **Webhook** and select:

* **Credentials → Create New Credential**
* Paste the **HeyReach-generated n8n Key**
* Fill in **Resource**, **Operation**, **Webhook name**, **Webhook URL**, and **Event Type**

6. Hit **Execute step** and look for the green success confirmation. ✅

## **Step 3: Confirm the Connection in HeyReach**

Once your webhook is live, go back to HeyReach:

1. Navigate to **Integrations → Webhooks**.
2. If everything’s working, you’ll see your n8n trigger displayed there.

🎉 Congrats — your HeyReach Web Version integration is live!

## **Step 4: Using n8n desktop version (Community Node)**

Prefer to use the **n8n Desktop App** instead? No problem — here’s how:

1. Log in to your n8n desktop account.
2. Navigate to **Community nodes → Install a Community node**.
   Add this npm package:
    N8n-nodes-heyreach

3. and hit **I agree** to install it.
4. Once installed, check the **documentation** under the three-dot menu — it lists all available HeyReach actions.

## **Step 5: Create your first workflow (add leads to campaign)**

Now it’s time to put that integration to work:

1. Go back to **n8n Settings → Create Workflow**.

2. Click **Add first step** → select **HeyReach API**.

3. Scroll down to **Campaign Actions → Add leads to campaign**.

4. Connect your HeyReach credentials — paste your **n8n Key** to authenticate.
5. Set **Allow HTTP Requests Domain to All** (to make sure everything flows smoothly).
6. Hit **Execute step** to complete the workflow.

‍

And just like that — your n8n workflow can now automatically push leads straight into a HeyReach campaign. 🚀

## **Wrap-up**

The **HeyReach x n8n integration** is a dream combo for anyone running serious outbound.
 It’s perfect for sales teams, agencies, and founders who want to:

* Connect HeyReach with dozens of other apps (Slack, HubSpot, Notion, etc.)
* Automate LinkedIn outreach based on real-time events
* Eliminate manual imports and messy syncs

Whether you’re running one workspace or managing multiple clients, this setup turns HeyReach into a connected part of your GTM ecosystem — not just another outreach tool.

Now go build your first automated workflow — and let your outreach run itself.
