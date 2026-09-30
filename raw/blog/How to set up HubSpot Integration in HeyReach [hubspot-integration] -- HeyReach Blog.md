# How to set up HubSpot Integration in HeyReach

Source: https://www.heyreach.io/blog/hubspot-integration

Summary: Learn how to connect HeyReach with HubSpot in just a few steps. Our easy guide makes HubSpot integration simple, even if you’re not a tech expert.

Getting a HubSpot integration up and running doesn't have to be complicated. With HeyReach, you can connect your CRM in just a few simple steps and start managing leads more efficiently — no tech wizardry required.

I'll show you exactly how I connect [officially approved HubSpot integration](https://app.hubspot.com/marketplace/24004400/listing/heyreach), grab the access token, and export leads from HeyReach. Along the way, I'll explain how I map lead stages and handle multiple leads at once, making my workflow smoother and saving time.

## **Native HubSpot Integration (OAuth)**

### **Step 1: Connect your HubSpot account**

1. Open HeyReach and navigate to Integrations.
2. Click Connect Account under HubSpot.
3. Sign in to HubSpot and select the correct account.
4. Click Choose Account and confirm.

### **Step 2: Configure contact update triggers**

Once connected, set up your triggers under the Update Contacts in HubSpot section. When a trigger fires, HeyReach finds the matching HubSpot contact and starts syncing their activity.

**Currently supported triggers:**

* **L**ead Added to Campaign
* First Reply Received

### **Step 3: Set up field mapping**

In the Field Mapping section, select which HubSpot property contains LinkedIn URLs.

> ⚠️ This is critical. If the wrong property is selected, lead imports will fail. You can also map additional HubSpot properties to HeyReach fields and configure custom variables for campaign personalization.

### **Step 4: Enable activity sync**

Under Activity Mappings, enable the activities you want synced back to HubSpot — such as message replies and other LinkedIn engagement. These will appear directly on the HubSpot contact's activity timeline. HeyReach also logs conversation notes on the contact record so your team can follow the full exchange.

### **Step 5: Auto-find missing LinkedIn URLs**

This setting is enabled by default. If a HubSpot contact is missing a LinkedIn URL, HeyReach uses their email to find the matching LinkedIn profile. If found, the lead imports normally. If not, the lead is marked as failed and won't be imported.

### **Step 6: Monitor activity in Logs**

The Logs section shows a full history of sync activity, including date and time, lead name and email, connected HubSpot account, activity performed, and sync status. Filter by status to quickly spot any failures or confirm successful updates.

✅ Your HubSpot integration is now set up and ready to use.
