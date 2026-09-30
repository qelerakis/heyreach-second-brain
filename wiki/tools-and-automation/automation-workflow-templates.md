# Automation Workflow Templates

A catalog of the concrete, end-to-end plays HeyReach and its practitioners publish — organized *by workflow* (the tool-by-tool mechanics live in [[n8n-automation-workflows]], [[make-automation-workflows]], [[clay-enrichment-and-data-waterfall]], and the integration articles). Each recipe below names the stack, the trigger, and the outcome, with the source and any self-reported result. Most ship a free importable template. All are HeyReach's own blog/channel (COI); result numbers are self-reported.

## 1. Sentiment-triage inbox (does NOT auto-send)

**Stack:** HeyReach + n8n + GPT-4o Mini + Slack + a documented playbook (PDF). **Flow:** a reply lands in HeyReach → webhook sends the **full thread** to n8n → AI classifies intent → if INTERESTED, AI summarizes + drafts a reply from your playbook → pushes a structured alert to Slack → the SDR reviews/edits and **sends manually inside the Unibox** → the workflow auto-tags the lead (source: "Automate your LinkedIn inbox with this sentiment analysis workflow"). The Unibox stays the execution/manual-send layer: contra auto-reply tools, "Automation supports judgment — it doesn't replace it." Auto-tag mapping: Interested → Warm Lead; Objection → Objection; Not interested → Closed. See [[manage-replies-and-inbox-at-scale]].

## 2. Reply-sentiment → CRM (HubSpot or Attio)

**Stack:** HeyReach + n8n + an LLM (GPT-4.1 / O3 Mini) + HubSpot or Attio + Slack. **Flow:** the new **"every message/inmail reply received"** webhook → HTTP "get chat room" pulls the whole thread → code node flattens it → AI outputs one of positive/negative/neutral/unsure → write to CRM custom properties; sentiment is re-analyzed on every reply because it flips over a conversation (source: "The AI Agent Every LinkedIn Outreach Campaign Needs"). The Attio variant creates Person + Company + Deal (stage "Lead Interested") and schedules Slack reminders at 3/7/14 days, with a "Gone Cold" move at 14 days no reply (source: "How to automate your CRM with HeyReach, n8n, and AI sentiment analysis"). See [[crm-integrations]].

## 3. Automated Monday reports

**Stack:** HeyReach native n8n nodes + Gmail + Google Sheets. **Flow:** a cron trigger fires every Monday 00:00 → "Get overall stats" + a 7-day window → generate a Gmail draft from a template (weekly + lifetime stats) → append a row to a master Google Sheet. **Version 2** adds a fresh weekly tab of everyone who replied (filter `messageStatus == "MESSAGE_REPLY"`) — "Most agencies end up using Version 2" and "The workflow does 95% of the reporting work" (source: "Automate your LinkedIn outreach campaign reports"). The Claude-driven agency reporting system is the sibling — build once (2–4 hrs), then 45–60 min/client/month, using HeyReach MCP to tag leads by tier and summarize by ICP (source: "Build a repeatable system for agency client reporting with Claude"). See [[agency-client-onboarding-and-reporting]].

## 4. YouTube comments → LinkedIn

**Stack:** n8n (or Make) + Apify (two actors) + Google Sheets + HeyReach. **Flow:** a schedule trigger → read video URLs from a Sheet → Apify YouTube **comments** scraper (use "Run an Actor and Get Dataset" so it waits) → filter out your own comments → Apify YouTube **profile** scraper → code node normalizes social links → upsert to Sheets (unique key = YouTube profile ID) → filter to profiles with a LinkedIn URL → HeyReach campaign with a short contextual connection message ("Hey! Thanks for commenting on my YouTube video. Would love to connect!") (source: "YouTube lead generation: How to turn comments into high-intent LinkedIn leads"; source: "How to Turn YouTube Comments Into High-Intent Leads"). YouTube comments are "a goldmine" because the commenter discovered, consumed, and engaged publicly. One demo run: 77 comments → 46 after filtering → 3 usable people with LinkedIn.

## 5. Signal → enrich → outreach (post-engagement)

**Stack:** Trigify + Clay + HeyReach + Slack (+ n8n). **Flow:** Trigify monitors post engagement → webhook to n8n → AI drafts a 2-sentence opener ending in a question → **Add Lead to Campaign** → HeyReach fires the sequence (multi-seat rotation on) → optional Slack approve/decline with a regenerate loop (source: "Ultimate HeyReach + n8n LinkedIn automation ready-to-use playbook"). The single-post-engagement variant: Trigify fires on an "engagement" event → n8n filter (only engagers) → AI agent crafts the line → HTTP POST to the HeyReach API, using **"add to campaign" not "add to list"** so a finished campaign re-triggers (source: "I Built an AI Agent in n8n That Books Sales Calls For You"). See [[signal-and-intent-integrations]] and [[clay-enrichment-and-data-waterfall]].

## 6. Full autopilot: companies → people → email/LinkedIn split

**Stack:** n8n + Clay + HeyReach + Smartlead + HubSpot + Slack. **Flow:** qualify companies (Sales Nav/Clay) → find people inside them → waterfall for valid emails → **WITH email → Smartlead (email), WITHOUT email → HeyReach (LinkedIn)**; bounces and no-reply email-completers get routed to HeyReach so no lead is left behind; a switch node branches on HeyReach event names; ChatGPT handles reply sentiment + OOO detection (source: "How to Get Unlimited Leads on LinkedIn Using N8N + Clay.com + HeyReach"). See [[make-automation-workflows]] for the Make version ("the Pull and the Push").

## 7. Personalized assets at scale (lead magnets & pitch decks)

**Stack:** Clay + Make/Gamma/Google Docs + HeyReach. **Lead-magnet play:** on a positive reply, tag it → HeyReach "lead tag updated" webhook → Clay Claygents build variables → Clay POSTs to a Make custom webhook → Google Docs "create from template" → share link pasted into the HeyReach reply; the personalized asset moves to the *start* of the funnel (source: "How to Generate Unlimited Leads Using LinkedIn and Make.com (2026)"; method credited to Michael Suja). **Pitch-deck play:** Clay + **Gamma** (deck via API) + HeyReach — Apify scrapes Meta ads, Claygent analyzes the landing page, an HTTP POST to Gamma builds a ~7-card deck, and the presentation URL is passed to HeyReach as a custom field; a blank connection note + a no-CTA first message "does all the talking" (one client: +44% reply rate, self-reported) (source: "How to Send Automated Personalized Pitch Decks on LinkedIn (Step-by-Step)"). See [[ai-personalization-at-scale]].

## 8. CRM hygiene (CRM as source of truth)

**Stack:** n8n + HubSpot + HeyReach + Apify (activity score). **Flow:** get leads into HubSpot first ("We don't want to reach out to people before they're in HubSpot") → score profile *eligibility* via an Apify 0–10 activity score → if ≥2, push to a HeyReach campaign → write every HeyReach event back to HubSpot (connection sent + timestamp, "connected with [rep]," message text, full reply thread + sentiment) (source: "How to Automate CRM Hygiene in HubSpot Using n8n [Full Workflow Tutorial]", practitioner Nenad Pavlov — COI). See [[crm-integrations]].

## 9. Lead routing (rotation, sync, enrich)

**Stack:** HeyReach + Make (+ Sheets/Airtable/CRM). **Three cloneable scenarios:** Account Rotation (round-robin senders + persona routing), CRM-to-Outreach Sync (stage change → campaign), and Enrich-Before-Outreach (enrich → ICP router → SDR campaign or "Needs Review" queue) — "most ops teams use all three" (source: "Lead routing that scales: 3 playbooks to automate assignment, sync, and enrichment"). The lifecycle version routes on real-time stage using the `add-lead` / `pause-lead` / `assign-lead` endpoints (source: "Your lifecycle strategy is leaking revenue — Here’s how to patch it"). See [[make-automation-workflows]] and [[heyreach-campaign-api-and-webhooks]].

## 10. Website visitors → LinkedIn

**Stack:** RB2B + n8n/Zapier + HeyReach (+ Instantly + FullEnrich). Covered in full in [[website-visitor-identification]] — de-anonymize → tag-route by hot-lead/hot-page → follow + like pre-touches → connection request → message.

## Cross-cutting template rules

- **Human approval before send** — Slack "send and wait" with a ~10-min timeout is the standard gate.
- **Test before you schedule** — pin a real webhook payload / use a JS fallback; run n8n evaluations against a ground-truth Sheet.
- **Fallbacks everywhere** — a fallback message for every variable; a "Needs Review" queue for missing data.
- **Dedup upstream** — in the orchestrator, not HeyReach.
- **Grab the free template** — most of these ship an importable n8n/Make template or a Notion/Google Drive asset.

## Related
- [[n8n-automation-workflows]]
- [[make-automation-workflows]]
- [[zapier-albato-and-other-orchestrators]]
- [[clay-enrichment-and-data-waterfall]]
- [[signal-and-intent-integrations]]
- [[website-visitor-identification]]
- [[crm-integrations]]
- [[multichannel-email-and-ai-copy-integrations]]
- [[heyreach-campaign-api-and-webhooks]]
- [[ai-agent-builds-claude-openclaw-hermes]]
- [[manage-replies-and-inbox-at-scale]]
- [[agency-client-onboarding-and-reporting]]
- [[ai-personalization-at-scale]]
