# How to connect HeyReach with Slack

Source: https://www.heyreach.io/blog/slack-integration

Summary: Learn how to connect HeyReach with Slack to get instant notifications for connection requests, message replies, and campaign updates. Step-by-step guide included.

Staying on top of your LinkedIn outreach just got easier. By connecting HeyReach with Slack, you’ll receive real-time notifications every time a connection request is accepted, a message or email reply arrives, or a campaign completes. This guide walks you through setting it up so you never miss a conversation, all without leaving your Slack workspace.

## **The building blocks: What’s what?!**

**HeyReach** – Your LinkedIn outreach automation engine. It handles connection requests, follow-ups, and campaign tracking across multiple accounts.

**Slack** – The messaging platform where you want to receive notifications for HeyReach activity.

**Incoming Webhook** – The bridge that lets HeyReach send activity updates (like replies or connection acceptances) directly to a Slack channel.

Together, HeyReach + Slack ensures you’re always in the loop without checking multiple apps — perfect for managing campaigns efficiently.

## **Step 1: Go to HeyReach Integrations**

1. Open the [HeyReach integrations page](https://app.heyreach.io/app/integrations/public-api/slack):
2. Find and click **Connect with Slack**.
3. Name your integration (e.g., HeyReach Activity).

## **Step 2: Open Slack Admin Panel**

1. Go to your [Slack Admin panel:](https://heyreach.slack.com/admin/settings)
2. Make sure you’re in the correct workspace — this is where notifications will be sent.

## **Step 3: Configure Incoming WebHooks in Slack**

1. Click **Configure Apps** in the admin panel.
2. Select **Custom Integrations** → **Incoming WebHooks**.
3. Click **Add to Slack**.
4. Choose the channel where you want notifications (e.g., HeyReach Activity) and confirm.
5. Slack will generate a webhook URL — **copy this URL**, you’ll need it for HeyReach.

## **Step 4: Connect Slack to HeyReach**

1. Go back to HeyReach.
2. Paste the Slack webhook URL into the **Slack URL** box.
3. Click **Create Connection**.

> 💡 **Pro tip:** You can add multiple Slack notifications by repeating this process with different channels or webhooks.

## **Step 5: Test your connection and add multiple notifications**

1. Use the **Test Connection** button in HeyReach to ensure notifications are working.
2. Once confirmed, every time an event occurs (connection accepted, reply received, campaign completed), a notification will appear in your Slack channel.

That’s it! With HeyReach feeding activity updates directly into Slack, you’ll always stay on top of your campaigns without juggling apps. If you run into any issues, HeyReach support is just a click away — but once this is live, you’ll wonder how you ever managed without it .🚀
