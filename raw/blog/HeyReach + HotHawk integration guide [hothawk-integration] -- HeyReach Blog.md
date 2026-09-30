# HeyReach + HotHawk integration guide

Source: https://www.heyreach.io/blog/hothawk-integration

Summary: Unify your outbound replies in a single workspace with HeyReach + HotHawk — manage LinkedIn and email conversations, streamline follow-ups, and give clients a clean, shared inbox for full visibility.

You're running LinkedIn outreach in HeyReach and cold email in parallel. Replies are coming in [across both channels.](https://heyreach.io/blog/multichannel-outreach) Your team — or your client — is bouncing between inboxes, missing follow-ups, and losing context. Sound familiar?

That's the gap HotHawk fills. It's a shared team inbox designed for sales and lead generation workflows, purpose-built to consolidate all your outbound replies in one place. And with the HeyReach integration, your LinkedIn conversations flow directly into [HotHawk](https://www.heyreach.io/integration/hothawk) alongside your email replies. No more tab-switching, no more missed messages.

For agencies, this unlocks something even more valuable: you can give your clients a single, clean inbox to manage their replies without ever exposing your full HeyReach setup. One login, both channels, full visibility where it matters.

This guide walks you through connecting HeyReach to HotHawk – from generating your API key to seeing your first LinkedIn conversations appear in the inbox.

## **The building blocks: What's what?**

**HeyReach** – A LinkedIn automation platform built for scale. It lets you run personalized outreach campaigns across multiple LinkedIn accounts, manage sequences with smart delays and conditions, and track every connection request, message, and reply. Whether you're an agency managing dozens of accounts or a sales team running high-volume prospecting, [HeyReach](https://www.heyreach.io/blog/heyreach-review) handles the LinkedIn side — safely, efficiently, and at scale.

**HotHawk** – A shared team inbox built for sales, not support. It consolidates outbound replies from email and LinkedIn into a single, manageable interface, making it easy for teams to handle conversations, assign ownership, and never lose track of a hot lead. Agencies love it because they can give clients white-labeled inbox access without exposing campaign details or tooling.

### **What they solve together?**

* All LinkedIn replies from HeyReach appear in HotHawk alongside your email replies — one inbox for your entire [outbound motion](https://www.heyreach.io/blog/outbound-channel)
* Agencies can give clients a single set of login credentials to manage their own replies, without exposing HeyReach campaigns or sender accounts
* Lead tags sync bidirectionally — update a tag in HotHawk and it reflects in HeyReach, and vice versa
* Lead profile data from HeyReach is automatically linked to contacts in HotHawk's built-in CRM
* Your full LinkedIn conversation history is imported on first connection, so you're not starting from scratch

## **Setting up the integration**

The connection is straightforward: you generate an API key in HeyReach, paste it into HotHawk, and the platform handles the rest — including a one-time bulk sync of your existing LinkedIn conversations.

### **Step 1: Generate your HeyReach API key**

1. **Log in to HeyReach** and navigate to **Settings** → **Integrations** → **Public API**.
2. **Click "Generate API Key"** (or copy an existing key if you've already created one).
3. **Copy the key** and keep it somewhere handy — you'll paste it into HotHawk in the next step.

> 💡 **Pro tip:** If you manage multiple client workspaces in HeyReach, make sure you generate the API key from the correct workspace. Each HotHawk inbox connection maps to one HeyReach workspace.

### **Step 2: Connect HeyReach inside HotHawk**

1. **Log in to your HotHawk account** and go to **Settings** → **Integrations**.
2. **Find HeyReach** in the integrations list and click **Connect**.
3. **Paste your HeyReach API key** into the field provided and confirm.

> ✅ Once connected, HotHawk will automatically register webhooks for LinkedIn message replies, sent messages, and lead tag updates on your HeyReach account. You don't need to configure any webhooks manually in HeyReach.

### **Step 3: Let the initial sync complete**

As soon as the connection is confirmed, HotHawk kicks off a one-time bulk import of your existing LinkedIn conversations and [messages](https://heyreach.io/blog/automated-linkedin-messaging) from HeyReach.

Depending on your campaign volume, this can take anywhere from a few seconds to a few minutes. You'll see your conversation history begin to populate in the LinkedIn inbox inside HotHawk.

> ⚠️ **Don't disconnect or reconnect during this phase.** Wait for the sync to complete before making any changes to the integration settings.

### **Step 4: Verify your LinkedIn inbox**

1. In HotHawk, navigate to the **LinkedIn Inbox** view.
2. Check that your existing conversations have imported correctly — you should see lead names, message history, and timestamps from HeyReach.
3. Send a test reply to an existing LinkedIn conversation from inside HotHawk and confirm it delivers successfully.

> ✅ From this point on, all new LinkedIn activity in HeyReach — incoming replies, sent messages, tag updates — flows into HotHawk in real time via webhooks.

### **Step 5 (Agencies): Set up white-label client access**

If you're running campaigns on behalf of clients and want to give them inbox access without exposing your HeyReach setup:

1. In HotHawk, go to **Settings** → **Team & Access** (or your white-label configuration panel).
2. **Create a client user account** with access scoped to the relevant inbox.
3. **Share the HotHawk login credentials** with your client.

Your client can now view and manage their LinkedIn and email replies in one place. They see only what's in their inbox — not your HeyReach campaigns, sender accounts, or other clients' data.

> 💡 **Pro tip:** This is the main reason agencies integrate HotHawk. Instead of giving a client access to HeyReach (where they'd see everything), you give them a clean, branded inbox that shows only their conversations.

## **Common workflows**

**Workflow 1: Full multichannel inbox for a sales team**

Your team runs [LinkedIn outreach and cold email in parallel.](https://www.heyreach.io/blog/email-vs-linkedin-message) Rather than having reps check two separate inboxes, HotHawk becomes the single reply hub. A prospect replies on LinkedIn → the message appears in HotHawk alongside email replies → the rep handles everything from one screen and tags the lead as "Interested" → the tag syncs back to HeyReach automatically.

**Workflow 2: White-label client inbox for lead gen agencies**

Your agency runs LinkedIn campaigns in HeyReach on behalf of a marketing client. Instead of giving that client HeyReach access, you connect HotHawk, scope a client inbox to their campaigns, and hand over a single login. The client manages their own replies and sees leads marked with the right status — all without touching your HeyReach setup or seeing any other clients' data.

**Workflow 3: Lead qualification and CRM sync**

A prospect replies positively to a LinkedIn message. Your SDR updates the lead's tag to "Qualified" in HotHawk. That tag syncs back to HeyReach, where it can be used to pause the lead from receiving further outreach steps. Meanwhile, the lead's profile data (sourced from HeyReach) is already linked to the contact record in HotHawk's CRM — no manual data entry required.

**Workflow 4: Team inbox for high-volume outreach**

You're running campaigns across multiple LinkedIn sender accounts in HeyReach. All replies, regardless of which sender account they came from, surface in a shared HotHawk inbox. Team members can be assigned conversations, add internal notes, and mark threads as resolved — giving you a proper reply management [workflow without building it yourself.](https://www.heyreach.io/blog/customer-retention-automation)

## **Troubleshooting**

* **Existing LinkedIn conversations didn’t import:** Initial sync can take a few minutes. Refresh inbox after 10 minutes; if still missing, disconnect and reconnect to re-run bulk import.
* **New LinkedIn replies from HeyReach not appearing in HotHawk:** Check that your HeyReach API key hasn’t been regenerated or revoked. Reconnect with the current key if needed.
* **Tag updates not syncing between HotHawk and HeyReach:** Ensure tag names match exactly (including capitalization). Tags must exist in both platforms to sync.
* **Connected the wrong HeyReach workspace:** Disconnect, generate an API key from the correct workspace, and reconnect. Inbox will re-sync.
* **Clients seeing conversations that aren’t theirs:** Verify inbox scoping in HotHawk. Users should be scoped to specific inboxes, not the full workspace. Check permission settings.

## **Quick-start checklist**

**In HeyReach:**

* Navigate to Settings → Integrations → Public API
* Generate (or copy) your API key
* Confirm you're in the correct workspace

**In HotHawk:**

* Go to Settings → Integrations → HeyReach
* Paste your HeyReach API key and confirm the connection
* Wait for the initial conversation sync to complete
* Open the LinkedIn Inbox and verify historical conversations have imported
* Send a test reply to confirm outbound messaging works

**For agencies (optional):**

* Create a scoped client user account in HotHawk
* Confirm the client can only see their own inbox
* Share login credentials with your client

You did it all! Your LinkedIn and email replies are now in one place — and your clients have the clean, focused inbox they actually need.
