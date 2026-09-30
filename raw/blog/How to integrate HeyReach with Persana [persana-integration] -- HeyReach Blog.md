# How to integrate HeyReach with Persana

Source: https://www.heyreach.io/blog/persana-integration

Summary: Learn how to integrate HeyReach with Persana to automate lead imports, sync variables, and run personalized LinkedIn outreach at scale.

The real power of outbound comes when personalization meets automation. That’s why connecting **HeyReach** with **Persana AI** is such a game-changer: Persana captures and enriches leads straight from your website, while HeyReach puts those leads into motion with smart, sequenced LinkedIn outreach. In this guide, I’ll show you how to stitch the two together so every visitor-turned-lead flows seamlessly into your campaigns — no manual uploads, no missed opportunities.

## **The building blocks: What’s what?!**

* **HeyReach** – Your LinkedIn outreach automation engine. It manages connection requests, follow-ups, and runs campaigns safely across multiple LinkedIn accounts with rotation and scaling features.
* **Persana** – An enrichment and data orchestration platform. It helps you pull verified, enriched data about prospects (emails, company info, signals) and keep your lead lists updated.
* **Webhook**  – The “bridge” that lets HeyReach send prospect engagement data (like replies, connections accepted) into Persana, or vice versa—enriched data flowing from Persana into HeyReach for better targeting.

Together, these tools make sure you’re not just blasting messages, but reaching the *right* people, with the *right* context, at the *right* time.

## **Step 1: Create a campaign in HeyReach with an empty lead list**

The first step is setting up your campaign in HeyReach.

1. Go to [**Create a Campaign** in HeyReach](https://help.heyreach.io/en/articles/9877952-how-to-launch-your-first-campaign).
2. Name it (e.g., *Persana Campaign*).
3. Create a **new, empty lead list** — this is where Persana will push leads from your website.
4. Choose excluding options if needed.

Next, assign a **Sender**.

> 💡**Pro tip:** Use a sender not tied to other campaigns to ensure their limits are dedicated to Persana-synced leads only.

Now, build your **sequence**:

* Best practice: Create a **conditioned sequence** using *If connection*.
* If the lead is connected → send them a message right away.
* If not → add other actions (connection request, engagement, etc.) before sending the message.

> ⚠️ Don’t forget to define **variables** in your message templates and set a **fallback message** in case Persana can’t populate a variable.

At this point, you can launch the campaign — but since the lead list is empty, it won’t run yet.

## **Step 2: Locate connection spot in Persana**

1. In Persana, go to **Dashboard → Settings → Integrations**.
2. Find **HeyReach Integration**.
3. You’ll be asked to provide your HeyReach API key.

## **Step 3: Get your API Key from HeyReach**

1. In HeyReach, go to **Integrations → HeyReach API**.
2. Click **Get API Key** and copy it.
3. Paste it into Persana’s integration field.

✅ Now, Persana and HeyReach are connected.

## **Step 4: Configure variables in Persana for HeyReach**

1. In Persana, go to your **use case** for the campaign.
2. In the table, click **Add Column → Enrichment**.
3. Search for **HeyReach → Add Lead to Campaign (HeyReach)**.

A setup window will appear on the right side:

* Select the **campaign or lead list** in HeyReach to push leads to.
* Assign the correct **Sender** in HeyReach.
* Map **all variables** from Persana to HeyReach.

‍

> ⚠️ You can add both predefined and **custom variables/fields**. Just make sure variable names match exactly in Persana and HeyReach — otherwise, fallback messages will trigger.

Finally, click **Save & Run for All**.

## **Step 5: Verify lead import**

Go to your HeyReach **Lead List** to double-check that leads from Persana are flowing in correctly.

That’s it — your outreach is now automated, personalized, and ready to scale 🚀.

And you’re done. With Persana feeding fresh, enriched leads directly into HeyReach, you now have an always-on system that reacts instantly to your website traffic and scales your outreach with precision.

If you run into any bumps along the way, we’re just a message away — but once this is live, you’ll wonder how you ever managed without it. 🚀
