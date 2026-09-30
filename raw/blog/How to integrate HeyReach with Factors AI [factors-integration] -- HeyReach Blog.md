# How to integrate HeyReach with Factors AI

Source: https://www.heyreach.io/blog/factors-integration

Summary: Learn how to connect HeyReach with Factors to automatically add enriched leads to your HeyReach campaigns or lists using workflows and Apollo data.

When you’re building a serious outbound engine, the magic isn’t in any single tool — it’s in how they talk to each other. That’s exactly what this guide is about: connecting **HeyReach** (your LinkedIn outreach powerhouse) with **Factors** (your growth automation brain) so your leads move from signal to action without manual work.

I’ll walk you through the setup step by step. No fluff, no jargon, just a clear path to get your data flowing, your leads enriched, and your outreach firing on all cylinders.

## **The building blocks: What’s what?!**

Let’s quickly break down what each tool does before we dive into the integration:

* **HeyReach** – Your LinkedIn automation engine. It handles sending connection requests, rotating across multiple accounts, managing follow-ups, and keeping everything safe and in sync.
* **Factors** – A B2B growth automation platform. It lets you trigger workflows based on website visitor behavior, CRM updates, or product usage data, and then push those leads directly into your sales and marketing tools.
* **Apollo** – Provides enrichment data (emails, company info, etc.) so that every lead sent to HeyReach is complete and ready for outreach.

Now that we know who does what, let’s move to the process. 👇

## **Step 1: Set up a workflow in Factors**

⚠️There are two workflow options in Factors, and both also include **Apollo enrichment**, so every lead comes with richer context.

1. Open your **Factors dashboard** and navigate to **Workflows**.
2. Click **+ New Workflow**.
3. You’ll see templates that include HeyReach:
   * **Add leads to HeyReach List**
   * **Add leads to HeyReach Campaign**

4. Click on your preferred template and hit **Use this workflow**.

## **Step 2: Connect HeyReach**

1. Inside the workflow, click **Connect HeyReach**.
2. Enter your **HeyReach API Key**:
   * Go to **HeyReach dashboard → Integrations → Get API Key**.
   * If none exists, click **New API Key**.
   * Copy it using the double-page icon.

⚠️ **Note:** This key is private — don’t share it.

3. Paste it into Factors.Choose whether to add leads to a **Lead List** or a **Campaign** in HeyReach.
4. Pick the event type that will trigger the workflow:
   * **Performs an event**
   * **Enter a segment**
   * **Exit a segment**

Then configure the event details by selecting the app, event, and any filters you want to apply.

## **Step 3: Configure Apollo**

Follow the exact steps in [Factors’ Apollo Integration guide](https://help.factors.ai/en/articles/10031572-apollo-integration) to complete the enrichment setup.

## **Step 4: Launch your workflow**

That’s it! 🎉 Once launched, your workflow will:

* Capture leads in Factors
* Enrich them with Apollo
* Push them straight into HeyReach campaigns or lead lists for automated outreach

And that’s it, you’re all set. With HeyReach and Factors working together (plus Apollo for enrichment), you’ve now got a lean, automated system that does the heavy lifting for you. If anything feels unclear or you hit a snag, don’t worry — our team’s here to help you get it running smoothly.

Now go put your outreach on autopilot. 🚀
