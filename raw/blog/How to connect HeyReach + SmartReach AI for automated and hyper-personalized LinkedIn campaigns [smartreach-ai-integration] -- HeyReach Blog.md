# How to connect HeyReach + SmartReach AI for automated and hyper-personalized LinkedIn campaigns

Source: https://www.heyreach.io/blog/smartreach-ai-integration

Summary: Learn how to integrate HeyReach with SmartReach AI to send hyper-personalized LinkedIn messages at scale. Step-by-step setup, prompts, and automation tips.

Want to scale outreach without sacrificing personalization? This SmartReach AI + HeyReach integration is built exactly for that. You’ll be able to craft AI-powered personalized LinkedIn connection requests and follow-ups—then send them automatically using HeyReach.

Let’s break down how to connect the two tools, build your campaign, and put everything on autopilot.

## **The building blocks: What’s what?!**

Let’s first look at what each tool does.

* **HeyReach** – Your outreach automation engine. It runs your LinkedIn campaigns across multiple accounts safely, handles follow-ups, manages limits, and makes sure your campaigns are always running.
* **SmartReach AI** – Your AI copy assistant. It personalizes your connection messages and follow-ups at scale based on your prompts. You define the ICP and messaging logic, and it auto-generates personalized messages for every lead.

Now let’s see how it all comes together. 👇

## **Step 1: Connect SmartReach AI with HeyReach**

Head to your **SmartReach AI account** → go to **Settings** → and paste your **HeyReach API key**.

To get your API key:

* Open HeyReach
* Go to **Integrations → HeyReach API**
* Copy the key
* Paste it into SmartReach AI and you’re connected!

## **Step 2: Build your LinkedIn campaign in HeyReach**

Time to set up your LinkedIn campaign.

Start by importing your list of prospects. (Pro tip: use Sales Navigator for better filters.)

Now build your outreach sequence. Let’s say you’ve got:

* 1 connection request message
* 2 follow-up messages

Here’s the key part: Add these special variables in your campaign messages to enable SmartReach AI to personalize them:

* {connection} → for your connection request

* {follow\_up\_1}, {follow\_up\_2}, etc. → for your follow-up messages

SmartReach AI will recognize these tags and replace them with custom copy tailored to each lead.

## **Step 3: Build your prompt engine in SmartReach AI**

Now switch over to **SmartReach AI** to create the prompts for your campaign.

You’ll define:

* **Description** – What your product does (your value prop in 1–2 lines)
* **Pain points** – What problems does your product solve?
* **Social proof** – Who has used your product and what were the results?
* **Strategic advantages** – What makes your offer unique vs. competitors?

💡 **Tip:** Leave “Keywords” and “Mandatory text” empty at first. Let the AI learn and optimize on its own.

Then select your list:

* Choose **Upload from HeyReach**
* Select the list you created earlier
* (Optionally rename it)

Click **Continue**.

On the **Settings** screen:

* Tick ✅ **HeyReach Campaign**
* Untick ❌ **Smart Link Campaign**

Choose your connection request setup:

* Use HeyReach’s default connection message, OR
* Use **Smart Link Connection Request** if you have a Sales Navigator license

Then pick:

* The LinkedIn Sender Account
* The HeyReach campaign to connect

Set **number of messages to generate** → this should match the number of follow-ups (excluding the connection message).

Customize the **call-to-action** and decide:

* ✅ Use Tone Optimizer → to experiment with tone variations
* ✅ Auto Upload to HeyReach → to send without review, or leave it unticked if you want to edit first

Click **Continue** and you're done!

If you chose not to auto-upload:

* Click **Edit Campaign** → edit individual messages if needed
* Then click the HeyReach icon to start sending

## **Step 4: Launch your campaign in HeyReach**

All set?

Just go back to **HeyReach**, select your campaign, and launch it.

You’re now sending AI-personalized LinkedIn messages automatically—across multiple accounts—without lifting a finger.
