# Smarter outbound sales with AI agents: HeyReach + Make workflow

Source: https://www.heyreach.io/blog/ai-agents

Summary: Learn how to set up a no-code AI workflow using HeyReach and Make that scores and routes leads automatically.

AI agents are everywhere in outbound right now. The hype is real, but the execution? Still messy. Most teams are just bolting them onto broken workflows.

The real opportunity isn’t using artificial intelligence on top of outbound. It’s building AI into the outbound infrastructure. It's about [orchestration](https://www.heyreach.io/blog/sales-orchestration). Structuring how data flows, decisions are made, and actions fire in sync.

That’s where HeyReach + Make comes in. Make gives you a no-code way to run GPT logic, score leads, trigger campaigns via API, and build in fallbacks and safety checks. It’s where agent decisions happen. HeyReach is what acts on them.

Think: GPT → routes → HeyReach sends – only when qualified.

Still don’t get it? By the end of this article, you’ll have a plug-and-play workflow that scores leads and routes them safely to the right HeyReach sequence.

## **Why “send everything” workflows waste budget (and burn accounts)**

Unfiltered [automated outbound](https://www.heyreach.io/blog/outbound-sales-automation) kills performance.When every lead goes to the same campaign – no logic, no scoring – you get:

* Inboxes flooded fast
* Reply rates in freefall
* Accounts burned through rotation
* Platform limits hit by day three

It’s outbound without brakes. And it shows. It hurts **customer experience** by pushing irrelevant or untimely messaging to potential buyers.

That’s why HeyReach bakes in account protection from the start:

* **Paused lists** kick in when volume risks deliverability
* **Rotation logic** spreads sending load across accounts
* **Unified inbox** lets humans review hot leads before platforms flag you

Still, platform features alone aren’t enough. To stop sending everyone everything, we need a smarter system to streamline outbound.

And that’s where AI agents step in – **eliminating repetitive tasks** that slow your team down and hurt deliverability.

## **How AI agents work: real-world use cases and decision-making logic**

AI agents aren’t message chatbots. They function as learning agents aka decision engines – built to **complete tasks** like lead qualification and routing before a single message goes out.

Their job? Use customer data and intent signals to:

 → Route the right leads to the right HeyReach campaigns
 → Hold or flag leads that don’t meet intent or ICP fit

It’s the same logic used in support automation.

AI doesn’t answer every ticket. It routes based on urgency or topic.

Now apply that to sales: leads with strong signals go to Tier 1 campaigns. Weak or unclear ones get paused, reviewed, or enriched.

**Back to the flow:**

In real setups, we’re already using Clay’s GPT-based scoring to tag leads as Tier 1–3.

Those scores flow into Make, which then routes each lead to the right HeyReach campaign – or pauses them entirely.

* **Tier 1:** high-fit → priority campaign
* **Tier 2–3:** lower-fit → nurture, pause, or human review
* **No fit:** blocked automatically

This replaces what would otherwise require weeks of custom [software development agency](https://swovo.com/services/custom-software-development/) just to build a basic routing logic from scratch.

HeyReach then picks it up from there:

* Campaigns auto-trigger based on tag
* Leads can be held in queues
* No manual sorting needed

Let’s go through use cases in practice:

* Auto-assign campaigns by ICP tier
* Route based on job title, company size, or signals
* Pause leads with unclear data for review

One burns your sender limits. The other builds a pipeline – safely. See the difference?

## **Build this AI agent workflow to automate lead scoring and campaign triggers in HeyReach**

We’ve talked theory. Now let’s build.

This isn’t a black-box ‘AI assistant’ you can’t control. You choose which **types of AI agents** to deploy, set the logic, and define the fallback rules based on your specific goals for who gets into which campaign and why.

You’re building AI agents that follow yours, not someone else’s assumptions.

And with **Make + HeyReach**, you get full visibility – and the power to intervene at any step.

Here’s how to set up a fully functional, [agentic AI outbound system](https://www.heyreach.io/blog/outbound-sales-automation) in under 30 minutes.

### **What you’ll need?**

You don’t need to overhaul your entire stack. Just the parts of your business processes that block scale.

Here’s what will help:

* [A **Make** account](https://www.heyreach.io/blog/make-integration) (Free or Pro)
* Your **HeyReach API key + campaign IDs**
* The **OpenAI module** ( powered by LLM and built into Make)
* *(Optional)* Google Sheet or Slack fallback for paused/unqualified leads

### **Step-by-step:**

1. **Lead intake** → Form fill, webhook, or CRM sends data into Make
2. **Classification** → GPT module classifies the lead into Tier 1 (ideal), Tier 2 (okay), or Tier 3 (unfit)
3. **Routing logic (via Make’s router module):**
   * Tier 1 → Add to HeyReach Campaign A
   * Tier 2 → Add to Campaign B or put into self-serve queue
   * Tier 3 → Hold (pause, discard, or alert via Slack)
4. **Logging outcomes** → Optional Make module logs classifications to Google Sheets to help refine GPT logic over time

This becomes your internal **knowledge base** for tracking how decisions evolve, which inputs matter, and what to optimize next.

### **Use this sample GPT prompt:**

You are an AI assistant trained to qualify B2B leads for outbound campaigns.

**Input:**
*{{lead\_name}}, {{job\_title}}, {{company}}, {{company\_size}}, {{industry}}, {{LinkedIn\_profile}}, {{recent\_activity}}*

**Instruction:**Based on the following ICP criteria, classify this lead into one of the following Tiers:

* **Tier 1** – Ideal customer: matches target role, company size, and industry
* **Tier 2** – Good fit but not ideal: matches 2 out of 3
* **Tier 3** – Not a fit

**Output your response strictly in JSON format:**
 *{"tier": "Tier 1"} or {"tier": "Tier 2"} or {"tier": "Tier 3"}*

### **Skip the setup – copy this ready-made HeyReach Make template:**

 To make things easier, use this prebuilt Make + HeyReach scenario to:

* Score leads across 3 ICP tiers using GPT prompts
* Auto-route qualified leads into the right campaign or human-handled queue
* Mirror the exact structure described above (classification → action → fallback)

> ✅ This template is already aligned with HeyReach workflows, so you can clone it and get started fast.

If you want to build something similar, here’s step by step process:

1. **Start with a minimal form** → Use a simple form (e.g. HubSpot) that only asks for a **business email** → Less friction = more leads
2. **Detect new contacts** → Trigger Make when a new contact is added in HubSpot
    → This kicks off the entire automation chain**‍**
3. **Extract the domain from the email**
    → Use a small JavaScript module in Make to grab the domain from the email
    → Example: *john@acme.com → acme.com***‍**
4. **Enrich company data** → Use AI tools like Enrich.so (or any enrichment API) to pull:
        a. Company name, LinkedIn URL, description
        b. Industry type (SaaS, eCom, etc.
         c. Number of employees

5. **Classify company with AI** → Use Relevance or GPT-based prompts to check:
   * Is this a SaaS or eCom company?
   * Do they run outbound?
      → Return true, false, or unsure

6. **Enrich contact data** → Based on the email, pull:
   * First name, last name, job title, LinkedIn profile
   * Work history and current position
      → Rebuild this into a clean JSON object with **contact** and **company blocks**
7. **Update CRM (HubSpot)** → Use Make to create/update the contact in HubSpot
    → If company exists (based on domain): update it
    → If it doesn’t: create a new company record with enriched data

8. **Route to campaigns using Make's router module**
   * **If title contains “Marketing”, company >20 employees, and is SaaS** → Send to *HeyReach Campaign A*
   * **If title contains “Sales”, company >20, and does outbound** → Send to *HeyReach Campaign B*
   * **Else** → Log to fallback or send to a review queue (e.g. Slack, Google Sheet)
9. **Log or pause anything unqualified
    → Optional:** log Tier 3 leads to a fallback list
    → Avoid spamming contacts that don’t fit

This flow turns a single email input into:

* AI-powered enrichment
* Clean CRM updates
* Precision-routed outbound
* Safety-first execution logic

**The result?** No complex workflows. Just safer sends, and smarter outbound.

🎥 **Here’s a full video walkthrough of the setup in action**.

## **How to keep it safe: guardrails, human oversight, and failpoints**

You’ve built the flow – now it’s time to keep it safe.

Without the right guardrails, AI handling specific tasks like **routing or enrichment can burn accounts fast.**

Here’s how to add control, oversight, and fallback logic into your [cold messaging workflow:](https://www.heyreach.io/blog/linkedin-cold-messages)

### **Step 1: Verify confidence before sending**

Not every lead GPT touches is ready to go. Use score thresholds to gate your sends. If this is way too complex, consider investing in [AI courses](https://www.datacamp.com/category/artificial-intelligence) often gain a clearer framework for setting these thresholds and building safer outbound logic.

Inside Make’s router module, add logic like:

* Only route if GPT classifies the lead as **Tier 1** or **Tier 2**
* If **Tier 3** or classification is missing/uncertain → send to fallback

### **Step 2: Create a fallback queue for manual review**

Even **intelligent agents** won’t catch everything – some leads need a second look.

 Route those to:

* A shared **Slack channel** for quick human intervention and triage
* A **Google Sheet** where someone can batch-approve or discard them later

### **Step 3: Build in human checkpoints**

Automation ≠ autopilot.

Use HeyReach’s built-in safety layers to keep your domains, accounts, data privacy, and sender reputation protected:

* **Unified inbox**: Step in and manually review lead responses in real time
* **Sender rotation**: Distribute volume across multiple seats
* **Paused lists**: Automatically hold campaigns when lead flow spikes
* **Withdraw requests**: React quickly when someone wants out

## **Optimize your AI agent: real-time insights and prompt iteration**

Even well-tuned AI models drift over time. Markets shift. Job titles evolve. ICPs get tighter. So do the assumptions baked into most providers.

That’s why the smartest teams don’t “set and forget” their prompts. They’re solving a complex problem and **understand that no single prompt works forever.**

Instead, they build a feedback loop.

And that loop helps your machine learning models **adapt to your outbound ecosystem** as it evolves.

Ultimately, this leads to AI logic that keeps making better, **informed decisions** over time.

### **Step 1: Measure what’s working (and what’s not)**

Start with what you already have:

* **Make logs** track every classification decision:
   → Which lead was tagged as Tier 1, 2, or 3
   → Where it was routed
   → What happened next
* **HeyReach dashboards** show campaign-level performance:
   → Check **reply rates** by campaign or list
   → Spot **bounce spikes** or low engagement (bad signs)
   → Look for **inbox overload** – early signal that unqualified leads are slipping through

### **Step 2: Review + refine weekly**

Set aside 30 minutes each week. Ask:

* Are Tier 1s replying?
* Are Tier 2s worth keeping in play?
* Are Tier 3s sneaking into live campaigns?

Refine prompts based on metrics.

### **Step 3: Improve the input (when you’re ready)**

Once v1 is stable, take it deeper:

* Add **signal enrichment** from tools like **Clay** or CRM datasets
* Feed GPT more context (e.g. recent activity, funding rounds, tech stack)
* Create separate prompts per segment (Marketing vs. Sales vs. Ops). Every small change compounds the **agent’s performance** and classification accuracy.

> **Pro tip:** Track how wording changes affect outputs through prompt comparison table:

## **Not ready for full AI systems? Start with simple rules-based workflows**

You don’t need GPT to get started with smarter outbound. In fact, many teams are building effective routing systems using **basic rules-based logic** – no AI required.

This approach gives you:

* A safe entry point into AI-driven initiatives
* Full control over campaign triggers
* Zero reliance on unpredictable AI outputs

### **Example**

Using **Make filters + HeyReach list logic**, you can route leads like this:

* If job\_title contains “Founder” AND company\_size > 10 → add to Campaign A
* If industry = SaaS AND company\_size > 20 → add to Campaign B
* Else → pause lead or send to fallback

Simple logic. No prompt tuning. No black box decisions.

### **Hybrid mode: Add AI only where it helps**

Once you’ve nailed the rules, you can **layer in generative AI** to handle the edge cases and complex tasks:

* When title doesn’t clearly match (e.g. “Head of Biz Dev” or Supply Chain Manager”) → GPT check
* If company size is missing or unclear → GPT infers based on LinkedIn/about page
* When signals conflict → GPT helps break the tie

Think of it like this: **Rules handle the predictable. AI handles the ambiguous.**

You can even build it like this inside Make:

* Router module → rule-based paths
* Else → GPT module → new router

This gives you **total visibility and control** without going all-in on AI from day one.

### **Real teams are already doing this**

HeyReach has published multiple use cases where teams:

* Used **rules-based routing** to qualify inbound form fills
* Triggered multi-step outbound and handled **routine tasks** without AI
* Built fallback queues and logic entirely with Make + HeyReach

You’ll find examples in these breakdowns:

* [Outbound Sales Automation with Make](https://www.heyreach.io/blog/outbound-sales-automation)
* [Multichannel Outreach Workflows](https://www.heyreach.io/blog/multichannel-outreach)

## **Next steps: Where to go from here**

You’ve got the point. Now it’s time to act.

### **Start simple**

You don’t need GPT to get moving. If you’re not ready for full AI, don’t wait.

Use **Make filters or field-based rules** to start segmenting leads and assigning campaigns. Even the most basic logic – like routing by job title or company size – will outperform a “send everything” blast.

Start here. Start clean.

### **Test AI logic on your next batch**

Ready to dip into goal-based agents? Use the **sample GPT prompt** from earlier and plug it into the **HeyReach x Make scenario**.

Route your next 50 leads using AI-based classification:
 → Tier 1 goes to your top campaign
 → Tier 2 to nurture
 → Tier 3 gets paused or flagged

Then check which campaigns perform best — and refine from there.

### **Monitor. Learn. Iterate.**

Don’t just set it and hope. Build your feedback loop:

* **Make logs** show how leads were classified and routed
* **HeyReach dashboards** reveal reply rates, bounce issues, and list health
* **Refine your prompt or fallback logic** weekly based on what actually works

Even a 30-minute review once a week will sharpen results fast.

Once your first routing flow is live, the next frontier is agentic layering – where you **use AI agents** to dynamically adjust content, timing, and even channels.

But it all starts here: **Routing the right lead to the right flow – safely and scalably.**

* Route your next 100 leads with AI agent logic and bake **problem solving** right into your outbound flow.
* When you pair structured workflows with the reasoning power of **large language models and solid algorithms**, outbound finally starts working for you.

## **Ready to scale smarter? Steal the system, clone the scenario, book the call**

And that’s it! You’ve learned how to:

* Build routing logic that works – even without AI
* Layer in GPT prompts to classify and segment leads
* Use Make and HeyReach to automate outbound without losing control
* Add fallback logic, safety guardrails, and review loops that actually scale (all without sacrificing customer satisfaction).

And if you want to move fast:

* Clone our prebuilt[**Make x HeyReach scenario**](https://drive.google.com/drive/folders/11gNMaOxyAkM5QVrys1AcXEJHYOSVSXgT)we made above
* Refine your campaigns using templates from the [**ICP Vault**](https://www.heyreach.io/blog/outbound-sales-automation)
* Use the [**Multichannel Outreach Playbook**](https://www.heyreach.io/blog/multichannel-outreach) if you’re managing volume across multiple clients that will show you how to run clean sequences across LinkedIn, email, and more.

Want expert eyes on your system? [Schedule a 1:1 strategy call](https://cal.com/nadjakomnenic/discovery) and we’ll help you turn this guide into a live, high-performing outbound engine.
