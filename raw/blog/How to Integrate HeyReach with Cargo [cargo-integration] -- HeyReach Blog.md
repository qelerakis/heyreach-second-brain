# How to Integrate HeyReach with Cargo

Source: https://www.heyreach.io/blog/cargo-integration

Summary: Learn how to connect HeyReach with Cargo to automate LinkedIn outreach. Set up plays, add HeyReach as a connector, and run campaigns directly from Cargo.

Smooth workflows are what separate scrappy outreach from scalable outbound. With HeyReach + Cargo, you can connect your CRM, datasets, or marketing stack directly to your LinkedIn campaigns — no extra steps, no manual uploads. Cargo acts as the bridge, pushing leads straight into HeyReach so your outreach engine runs the moment new data appears. In this guide, I’ll walk you through setting it up step by step so your sales plays move from data to action automatically.

## **The Building Blocks: What’s What?!**

Before jumping into the setup, let’s get clear on what each tool does:

* **HeyReach** – Your LinkedIn automation engine. It manages connection requests, rotates across multiple accounts, handles follow-ups, and keeps everything safe while scaling outreach.
* **Cargo** – A workflow automation platform designed for B2B teams. It connects data sources (like HubSpot, CRMs, or datasets) with tools like HeyReach, making sure leads move automatically through your sales and marketing stack.

With these roles in mind, let’s connect them. 👇

## **Step 1: Create a Play in Cargo**

1. Log into your **Cargo dashboard**.
2. Click **New Play** (or open the **Plays tab**).
3. Choose **Create from Blank** and hit **Start** – this marks the beginning of your workflow.
4. Select a trigger source:
   * **Datasets** (for list-based triggers)
   * **Integrations** (e.g., HubSpot, Salesforce, etc.)

👉 Example: Let’s say you choose **HubSpot** as your trigger. If it’s not connected yet, set up your HubSpot connector in Cargo first. Once connected, you’ll see your Play ready to build.

## **Step 2: Add HeyReach to the Play**

1. From your Play canvas, drag a connector from the trigger step.
2. Choose **HeyReach** from Cargo’s integration list.
3. Name the connector and slug (defaults will be filled in, but you can customize for clarity if you’re using multiple HeyReach actions).

**Step 3: Get the API Key from HeyReach**

1. Open your **HeyReach dashboard** → **Integrations tab**.
2. Find **API Key** and click **Get API Key**.
3. Copy the generated key.
4. Paste it into Cargo’s HeyReach connector setup.

Once pasted, the connector is ready for use. ✅

## **Step 4: Configure Actions**

On the right-hand side of your Cargo Play, you’ll see a configuration table. Define:

* **Object type** – What data you’re passing.
* **Action** – What HeyReach should do (e.g., add to campaign, add to list).
* **Campaign** – The HeyReach campaign you want to connect.
* **LinkedIn campaign** – If relevant, specify which one.

## **Step 5: Run the Play**

When everything is configured, simply hit **Play**. 🚀
 Cargo will now automatically pass leads to HeyReach, triggering LinkedIn outreach with zero manual effort.

And there you have it. With Cargo feeding leads directly into HeyReach, you’ve built a workflow that reacts instantly, scales safely, and keeps your outreach pipeline always in motion. From HubSpot triggers to enriched datasets, every source can now fuel your LinkedIn campaigns without a single copy-paste. If you ever get stuck or want to optimize further, our support team is just a click away. 🚀

‍
