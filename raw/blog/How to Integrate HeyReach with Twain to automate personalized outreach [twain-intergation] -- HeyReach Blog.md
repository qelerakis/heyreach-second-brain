# How to Integrate HeyReach with Twain to automate personalized outreach

Source: https://www.heyreach.io/blog/twain-intergation

Summary: earn how to connect HeyReach with Twain in just 5 steps. Automate LinkedIn outreach with AI-powered personalization—without losing quality or compliance.

Building sequences can sometimes be scary, just because you don’t know how to manage your outreach strategy. What to write? When? How not to sound blant or repetitive?

Twain integration helps you out with it. Follow this tutorial, add Twain to your toolkit together with HeyReach and unfreeze your outbound.

## **The building blocks: What’s what?!**

Let’s start with a quick breakdown of what each tool does:

[**HeyReach**](https://www.heyreach.io/blog/heyreach-review) – Your main automation engine. HeyReach handles LinkedIn outreach at scale—sending connection requests, managing follow-ups, and rotating across multiple LinkedIn accounts—all while staying compliant with platform limits.

**Twain** – Twain is your AI-powered personalization layer. It helps you write highly personalized messages based on lead data, conversations, or web activity—and then sends those messages directly to outreach platforms like HeyReach.

Now that you know what each tool does, let’s walk through how to connect them in five easy steps.👇

## **Why connect HeyReach and Twain?**

By integrating Twain with HeyReach, you unlock scalable yet hyper-personalized LinkedIn outreach. Twain ensures every message feels tailor-made, while HeyReach ensures it gets delivered at the right time, using the right sender, and on the right account—without manual effort.

This combo is ideal for:

* SDRs who want better reply rates without sacrificing speed.
* Marketing teams automating lead nurturing on LinkedIn.
* GTM teams aiming to convert inbound or website leads into live sales conversations.

Ready to start? You can follow our Success magician Umer on the video walkthrough or read written instructions bellow 👇🏼

## **Step-by-step guide: How to connect HeyReach and Twain**

### **Step 1: Create a campaign in HeyReach (with an empty lead list)**

1. Log into your HeyReach dashboard.
2. Click **Create New Campaign**.

3. Name it (e.g., “Twain Campaign”) and assign an **empty** lead list — Twain will fill it later.

4. Choose a sender — ideally, one not involved in other campaigns so you don’t hit seat limits.

5. Set up a **conditional sequence**:
   * If the lead is connected → send message
   * If not → add steps like a connection request or post engagement
6. **Leave all message fields blank** for now — Twain will fill those via variables later.

7. Launch the campaign.

 Don’t worry, it won’t start running yet because there are no leads in the list (yet).

### **Step 2: Export personalized leads from Twain to HeyReach**

1. In Twain, go to the personalization screen for the leads you want to export.

2. Click **Export Last Saved** and choose **HeyReach**.

3. Click the three-dot menu (⋯) to open a pop-up asking for your HeyReach API key.

### **Step 3: Grab your HeyReach API key**

1. Head back to HeyReach.
2. Open the **Integrations** tab.

3. Find the **API section** and click **Get API key**.
4. Copy it. Keep it safe.

### **Step 4: Complete export from Twain**

1. Paste your HeyReach API key into the Twain export popup.

2. Choose the lead list you created in Step 1.
3. Name your custom variables (e.g., {{JobTitle}}, {{Company}}, etc.).
4. Click **Export Leads**.

That’s it! The leads (with personalized variables) are now in your HeyReach list.

⚠️ Double-check the import in HeyReach to confirm the leads landed where expected.

### **Step 5: Map Twain variables inside HeyReach**

1. Go to your campaign in HeyReach.
2. Navigate to the **Messages** section.
3. Click into the message fields and select Twain’s custom variables.
4. Add **fallback text** in case a variable is missing (e.g., {{FirstName | there}}).
5. Save your sequence.

Your personalized campaign is now ready to launch. 🎯

## **Final thoughts**

By combining Twain’s advanced personalization with HeyReach’s automation power, you can run outreach that feels one-on-one—but scales like one-to-many.

Whether you're converting traffic from your website or crafting ABM campaigns, this setup helps you automate like a machine and sell like a human.
