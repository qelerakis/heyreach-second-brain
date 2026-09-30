# Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook

Source: https://www.heyreach.io/blog/linkedin-automation-n8n

Summary: Your n8n + HeyReach LinkedIn automation guide with 3 playbooks to streamline lead gen, personalize outreach, and scale booked calls.

LinkedIn outreach breaks fast. One minute you’re cruising, the next you’re drowning in manual work, broken campaigns and tools that don’t speak the same language. The fix? A smarter **LinkedIn automation** setup.

I’m giving you three copy-ready playbooks to grow your LinkedIn network, scale outbound, and turn positive replies into booked calls, combining **n8n** (orchestration), **HeyReach** (LinkedIn automation), **Clay** (ICP + signals), **Trigify** (engagement capture), and **Slack** (human-in-the-loop).

You’ll get exact step-by-step process, prompts, powerful workflows and JSON mapping ideas you can plug into your stack today.

## **Why this setup for Linkedin automation?**

If you already use n8n and want signal-led LinkedIn automation, this stack pays off fast. What I get from it every time:

* **More qualified conversations** (Clay + signals → HeyReach campaigns).
* **Less manual work** ([n8n automation](https://www.heyreach.io/blog/n8n-integration) handles webhooks, approvals, retries, and error handling).
* **Safer AI automation** ([Slack](https://www.heyreach.io/integration/slack) approvals, fallbacks, campaign rescheduling, and HeyReach Unibox for context).

The best part? The flows are simple enough for **beginners** but super scalable for advanced teams.

## **Part I: Growing the network (post engagers → warm conversations)**

**Searchable prompt:** *How do I auto-DM LinkedIn post engagers using n8n + HeyReach?*

**A little gist before we wire anything:** I let [Trigify](https://www.heyreach.io/integration/trigify) watch my posts, send a webhook to n8n, have an AI bot draft a tight, personal opener – and then I drop the lead straight into a HeyReach campaign.

If I want a human in the loop, I add a Slack approve step.

### **Why this matters?**

It lets the system catch every engagement.

* **Manual pain:** Checking likes, opening profiles, sending requests—total time sink.
* **Automation win:** Capture → copy → campaign is handled end-to-end, with Slack approvals when needed.

### **Architecture**

Keep the topology simple so it’s easy to debug:

* **Source:** Trigify monitors social media posts/keywords → sends engagement events (like/comment) to an n8n webhook.**‍**
* **n8n workflow:** Variables → filters → AI drafts message → HTTP request node pushes to HeyReach.**‍**
* **HeyReach:** Campaign sends connection request → personalized message → fallback → follow-up.**‍**
* **Optional:** Slack approval before sending.

### **Steps**

I set it up in this order so each step has the data it needs:

* **Webhook setup:** Create test + prod URLs → add to Trigify engagement event → test JSON.**‍**
* **Set variables + filters:** Map fields, filter out comments, tag posts #no-engage.**‍**
* **AI agent prompt:** Two-sentence opener that ends with a genuine question; route to Slack if it returns null.**‍**
* **Send to HeyReach:** Use **Add Lead to Campaign** (re-activation safe).**‍**
* **HeyReach campaign setup:** Connection request → opener → fallback/follow-up. Turn on multi-seat auto-rotation.**‍**
* **Human-in-the-loop:** Slack approve/decline with regenerate loop.**‍**
* **Error handling:** Define a global error workflow. Send Slack alerts for confusing posts.

### **💡 Notes**

A few tiny choices save hours later:

* Use **POST**, not GET, for webhooks.
* Trigify test data is dummy → add a **null-coalescing** fallback.
* Use the Slack tool whenever the AI is uncertain.
* Run **n8n Evaluations** with test cases before going live.

### **Trigify filters you’ll want**

I always add two light filters to streamline the engagement flow and keep the stream clean:

* **Keyword monitors (optional):** Track topic mentions beyond your own posts – same webhook flow.
* **Skip-tag:** Add **#no-engage** to non-promo posts; n8n drops those events.

## **Part II: Scaling outreach (signal-led ICP campaigns)**

**Searchable prompt:** *How do I build a Clay → HeyReach pipeline that targets ICPs at the right moment?*

I **import** leads into [Clay,](https://www.heyreach.io/integration/clay) enrich them, layer signals, then push qualified records into the right HeyReach campaigns with safe personalization.

### **Architecture**

A layout that keeps Clay tidy and mapping predictable:

* **Clay workbook → ICP classifier.**
* **Split views:** qualified ICP vs. non-ICP.
* **Signals:** ops job postings (≤30 days), employee exits (≤4 months).
* **Push to HeyReach:** personalized variables with fallbacks.
  **Steps**

Left-to-right so enrichments don’t step on each other:

* **ICP search:** Filters (size 2–50, industry, keywords, ENG countries). **Roles:** founders, CEOs, growth leads.
* **ICP classifier:** AI-powered agent categorizes websites. Output JSON {icp: true|false, reason, alt\_industry} → **Qualified ICP** view.
* **Signal A:** Ops job postings (≤30 days). Titles: Ops, Fulfillment, GTM, Account Manager.
* **Signal B:** Employee exits (≤4 months). Enrichment checks past/current roles → AI outputs leave date.
* **Push to HeyReach campaigns:**
  + Campaign 1: Job-post signal → reference job title.
  + Campaign 2: Employee-left signal → reference the ex-employee.
  + Safeguard with fallbacks + **only run if FirstName exists**.
* **Run cadence:** Clay monthly/bi-weekly; HeyReach with Unibox + rescheduling.

### **Clay guardrails**

I keep these on for quality control, budget protection, and optimization of lead generation consistency:

* **Classifier output:** { "icp": true|false, "reason": "...", "alt\_industry": "..." } → log the **reason** to a CRM note.
* **Signal freshness:** Job posts **≤30 days**; exits **≤120 days**.
* **Name safety:** Don’t send if the first name is missing.
* **Credit control:** Job-post monthly; exits bi-weekly only if budget allows.

### **💡Notes**

Two small details prevent most mapping bugs:

* Make the classifier **output alt industry** – it clarifies odd fits.
* Refresh job-posting signals monthly (or bi-weekly if you can afford it).
* Always keep fallbacks for personalization fields.

## **Part III: Nailing booked calls (positive replies → Slack approval)**

**Searchable prompt:** *How do I auto-triage positive replies without losing control?*

**The reply flow is lean on purpose:** HeyReach webhooks into n8n, I gate by sentiment, log to CRM, draft a reply, check calendar if time is mentioned, ask Slack to approve, then send through HeyReach.

### **Architecture**

Minimal steps from reply → booked call:

* **Trigger:** HeyReach webhook (every message or first positive).
* **n8n flow:** Sentiment agent → CRM log → AI reply → Google Calendar check → Slack approval → HeyReach send.

### **Steps**

A sequence that keeps approvals quick and reliable:

* **Webhook setup:** Start on test URL → swap to production.
* **Sentiment filter:** JSON {sentiment, reasoning}. Only **positive** moves on.
* **CRM logging:** Map name, company, LinkedIn URL, message, sentiment, campaign.
* **AI reply bot:** System = GTM engineer—friendly, concise, single CTA; include the conversation.
* **Calendar availability:** Read-only check. Suggest slots only if a time is mentioned.
* **Slack approval:** Send convo + draft. Approve/decline with a timeout.
* **Send via HeyReach:** Map conversationId, accountId, senderId, message. Test on a dummy account first.

### **CRM logging (minimum fields)**

I only log what helps with handoffs and compliance:

* Lead name, company, LinkedIn URL, **source** (Engager / JobPost / Exit), campaign ID, **sentiment + reasoning**, last message, owner, **opt-out (Y/N)**, next step.
* Auto-assign owner from campaign; if unassigned, escalate in Slack.

### **Example Postmaster JSON (reply send)**

Use this when you hit the HeyReach API endpoint from n8n\_io:

*{*

*"message": "{{ $json.linkedInMessage }}",*

*"subject": "",*

*"conversationId": "{{ $json.conversationId }}",*

*"linkedInAccountId": "{{ $json.accountId }}",*

*"senderId": "{{ $json.senderId }}"*

*}*

> **💡 Testing tip:** On the first live pass, hard-code conversationId, linkedInAccountId, senderId. Once it’s green, swap to expressions. Keep Content-Type: application/json and pass the HeyReach API key in headers.

## **Safety & limits (LinkedIn + system health)**

Never scale campaigns without these guardrails on:

* **Daily pacing & randomness:** Respect action limits; randomize delays; stagger seat start times.
* **Quiet hours:** Don’t send outside the prospect’s work hours.
* **Seat warm-up:** New accounts should post/connect for 1–2 weeks before campaigns.
* **Auto-throttle on errors:** If ≥3 errors in 10 minutes, pause the flow and ping Slack.
* **Blocklists:** Keep company/person blocklists (competitors, partners, prior no-go’s).
* **GDPR (EU):** Log lawful interest + opt-out in CRM; suppress any “stop/unsubscribe.”

> **⚠️ Please note:** For **self-hosting** teams, always double-check server limits and logging so LinkedIn pacing stays within healthy thresholds.

## **Metrics to watch (weekly snapshot)**

A quick weekly read keeps the system honest:

* **Connection accept rate** (engagers vs. cold).
* **Positive reply rate** by signal (job posts usually win).
* **Median time-to-first-reply** and **time-to-booked-call**.
* **Fallback hit rate** (if >10%, fix variables/mapping).
* **Slack approval turnaround** (aim <10 min).
* **Errors per 100 webhooks** (goal <1).
* **Optional:** add UTMs to tie message clicks → site sessions → demo requests.

No need to push any of these into Google Sheets – HeyReach + CRM already cover reporting.

## **n8n node patterns you’ll reuse**

These are the patterns I clone into every new flow:

* **Slack “Send message and wait for response”:** Buttons **Approve / Decline**, timeout 10 min → on Approve send via Postmaster; on Decline regenerate or route to manual.
* **If nodes:**
  + event\_type !== "comment"
  + sentiment === "positive"
  + message\_contains\_time === true → run Calendar tool
* **Global error workflow:** On error → Slack #ops-outbound with node name, error, payload preview, and “Pause campaigns?” buttons.

## **Workflow templates & prompts (copy-paste)**

**AI opener (post engager)**

*“Hey <first\_name>, I saw you liked my post about <post\_summary>. Curious—what’s your take on it?”*

**AI reply (positive)**

*“Hi <first\_name>, thanks for your message. Based on what you shared <conversation\_summary>, here’s what I suggest…”*

**Clay classifier**

*“Visit this website. Is it a lead gen agency? Output: {icp: true|false, reason, alt\_industry}.”*

**AI system messages (ready to paste)**

* **Opener agent (engagers)**
  + ***Role:*** “You are a concise, friendly GTM assistant.”
  + ***Rules:*** 2 sentences max, **no m-dashes**, avoid buzzwords, ask a genuine question about the post.
  + ***Output:*** { "message": "<text>" } or { "message": null } to route to Slack.
* **Positive-reply agent**
  + ***Role:*** “You are a GTM engineer closing next steps on LinkedIn.”
  + ***Rules:*** Acknowledge context, propose **one** clear CTA, offer **2–3 time windows** only if time is mentioned and Calendar is free; otherwise ask for preferences.
  + ***Output:*** { "message": "...", "cta": "call|info|handoff" }.

**➕Extra copy snippets (fallbacks you’ll actually use)**

* **Fallback opener (missing variables):** *“Hey <first\_name>, great to connect. Saw your engagement on a recent post. Curious—what’s top of mind for you around LinkedIn outbound this quarter?”*
* **Calendar ask (no time mentioned):** *“Happy to chat. I can do* ***Tue 10:00–12:00*** *or*
  + Test with a dummy **LinkedIn account** (to ensure the LinkedIn integration fires correctly).
  + Swap **test → production** webhooks.
  + Add **fallback** messages for missing variables.
  + Add **error workflows** with Slack alerts.
  + Keep **Slack approvals** on for replies.
  + Run **n8n Evaluations** with spreadsheet test cases.
  + Balance volume with **campaign rescheduling + multi-seat rotation**. *CET — do either work?”*
* **Polite opt-out handling:** *“Got it! I’ll close the loop on my side. If priorities change, ping me anytime. Have a great week!”*

## **Testing & guardrails**

I don’t flip webhooks to production until this checklist is green:

## **Troubleshooting (fast fixes)**

When something feels off, these are my fastest levers:

* **Nothing sends?** Verify Trigify → n8n **POST** body and production URL swap.
* **Wrong campaign?** Use **Add Lead to Campaign** (not List).
* **Weird AI outputs?** Tighten the system message; add 2–3 good/bad examples; re-run Evaluations.
* **Calendar mismatches?** Use **availability** check only; don’t create events in this flow.
* **High fallback rate?** A Clay column is empty/renamed; re-map and republish.

P.S. I wholeheartedly recommend you to watch our complete tutorial on how to stitch together this full **workflow automation tool** stack:

## **Where HeyReach MCP fits?**

When you’re ready to scale, centralize prompts, personalization, and Clay + Claude enrichment with [HeyReach MCP](https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools). Same flows, stronger governance.

With MCP (Model Context Protocol), you don’t need to build custom [integrations](https://www.heyreach.io/integrations) for every tool.

MCP gives HeyReach a **shared language** to connect directly with other MCP-ready tools like Claude, n8n, Clay, Make, or even your IDE (VS Code).

**Why this matters:**

* One connection per workspace → each HeyReach Workspace gets its own MCP Connection URL and Key.
* Plug-and-play → paste the URL into any MCP-ready tool and you’re connected.
* Safer governance → easier to manage prompts, enrichment, and campaign personalization in one place.
* Future-proof → as more tools adopt MCP, they’ll work out of the box with HeyReach.

**MCP vs API (quick read):**

* API = every integration is custom, and complexity grows as you add tools.
* MCP = one shared standard; any MCP tool can connect to any other instantly.

## **Your next step**

* **Quick win:** Run Part I to auto-convert post engagers.
* **Deeper flow:** Wire Part II + III for signals + booked calls.
* Or [**book a 30-min call with me**](https://cal.com/umer-ishaq-fwwew7/30min) to tailor your GTM flow.

With this no-code workflow automation, reusable **n8n templates,** and tested use cases you’ll have engager capture, ICP signals, and post-reply flows working in sync.

Safe, personal, and fully scalable all within **LinkedIn API** boundaries..
