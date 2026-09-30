# Make Automation Workflows

Make (formerly Integromat) is the other primary orchestration layer HeyReach supports — via a **native integration** (no HTTP modules needed) and a library of cloneable "Make scenarios." HeyReach frames Make as "your no-code automation glue" and "the logic layer," where "agent decisions happen (GPT logic, lead scoring, API triggers, fallbacks/safety checks)" while HeyReach executes (source: "How to integrate HeyReach with Make (in under 5 minutes)"; source: "Smarter outbound sales with AI agents: HeyReach + Make workflow"). The GTM-agents roundup lists Make at 3,000+ integrations, from $9/mo, now part of Celonis (source: "The Best AI Agents for GTM Engineering (Your 2026 Stack Guide)"). This article covers setup, the native modules, and Make's signature routing/AI patterns; full recipes are in [[automation-workflow-templates]]. HeyReach authors this (COI).

## Setup: native modules

Under five minutes: (1) in Make create a scenario → "+" → search HeyReach → select a module (e.g. **"Add lead to campaign"**) → Create a webhook → Add API connection; (2) generate the key in HeyReach → Integrations → find Make → **"Integrate with Make" → generate API key** (Make-specific, safe for this workflow only) → copy; (3) paste into the Make popup → Save. Then choose a campaign from the dropdown and map data (name / email / LinkedIn URL) into HeyReach (source: "How to integrate HeyReach with Make (in under 5 minutes)"). HeyReach's **"Watch" trigger modules** fire on new replies, connection requests accepted, and messages sent; the **"Add Lead"** module pushes leads into a campaign from anywhere (source: "Outbound sales automation with Make: From manual grind to scalable growth").

## Signature pattern 1 — AI lead-scoring & routing before send

Make's headline HeyReach pattern is **"GPT → routes → HeyReach sends – only when qualified"** — score and tier leads *before* any message goes out (source: "Smarter outbound sales with AI agents: HeyReach + Make workflow"). Core build (under 30 min): (1) lead intake (form/webhook/CRM → Make); (2) a **GPT module** classifies Tier 1 (ideal) / Tier 2 (okay) / Tier 3 (unfit) — a strict-JSON prompt like `{"tier":"Tier 1"}`; (3) a **Make Router** sends Tier 1 → HeyReach Campaign A, Tier 2 → Campaign B or a self-serve queue, Tier 3 → hold (pause / discard / Slack alert); (4) log classifications to Google Sheets to refine the prompt over time. Its philosophy line: "Automation ≠ autopilot... One burns your sender limits. The other builds a pipeline – safely." A **rules-based / hybrid** variant uses Make filters for predictable cases and routes ambiguous ones (unclear titles, missing data) to a GPT module: "Rules handle the predictable. AI handles the ambiguous" (source: "Smarter outbound sales with AI agents: HeyReach + Make workflow").

## Signature pattern 2 — LinkedIn + email orchestration ("the Pull and the Push")

Make is the logic layer that fuses HeyReach (LinkedIn = "the Pull") and Smartlead (email = "the Push") into one system to avoid "brand schizophrenia" (a polished email 9:00 AM + a disconnected LinkedIn message 9:05 AM) (source: "Outbound sales automation with Make: From manual grind to scalable growth"). Its building blocks:
- **Enrichment waterfall in Make** — pull LinkedIn URL from a signal → Clay/Apollo find email → Router tags "multi-channel ready ✅" vs "LinkedIn Only" (saves Smartlead credits).
- **Omnipresence sequence** — Day 1 HeyReach Profile View → Day 2 connection request (blank for execs) → Day 4 if accepted, wait 48h then a Smartlead email → Day 7 if no reply, a value-add LinkedIn message.
- **Smart Pause** — trigger "New LinkedIn Reply in HeyReach" → find the lead in Smartlead → set Paused/Unsubscribed (stop the bot when a human replies).
- **Reply triage** — an OpenAI/Anthropic module classifies replies (Interested / Not / OOO → pause 14 days / Referral = "Golden Nugget").
- **Batcher & Bounce Watcher** — a Data Store releases 50 leads/day/account instead of dumping 5,000; a Smartlead bounce immediately stops LinkedIn outreach for that lead.
- **Agency multi-client** — one master scenario + a Google-Sheet look-up table mapping Client ID → each client's Smartlead + HeyReach API keys.

Its self-reported figures (unattributed vendor claims): blank/no-note connection requests "often have 10-15% higher acceptance rates" for execs; AI reply classification "~95% accuracy" (source: "Outbound sales automation with Make: From manual grind to scalable growth").

## Signature pattern 3 — lead routing (rotation, sync, enrich)

HeyReach's lead-routing post ships three cloneable Make scenarios (source: "Lead routing that scales: 3 playbooks to automate assignment, sync, and enrichment"):
1. **Account Rotation** — lead enters → check who was used last → round-robin → assign to next sender → add to that owner's HeyReach campaign → update the sender log. A persona column + Make Router routes by role.
2. **CRM-to-Outreach Sync** — form submit or CRM stage change → map fields → add to a specific HeyReach campaign → optional Slack alert (uses a Pipedrive→HeyReach scenario; swap for HubSpot triggers).
3. **Enrich Before You Outreach** — lead enters → Make calls Clay/Clearbit/Dropcontact → Router checks ICP fit → yes → the right SDR's campaign, no → fallback/"Needs Review" queue.

All require the HeyReach API key + campaign IDs and `sender_account_id`s per seat; every playbook needs a no-data fallback path (ALL leads must have a LinkedIn URL). Templates live at heyreach.io/make-scenarios.

## Signature pattern 4 — personalized lead magnets at scale

Clay → Make → Google Docs to send a *personalized document* (not a meeting) at the top of the funnel: on a positive reply, tag it in the Unibox → HeyReach webhook "lead tag updated" fires to Clay → Claygents build variables (best case-study URL, a YouTube-style title, an outline) → Clay POSTs JSON to a Make custom webhook → Make's **Google Docs "create a document from a template"** module maps variables → share link pasted into the HeyReach reply (source: "How to Generate Unlimited Leads Using LinkedIn and Make.com (2026)"; method credited to Michael Suja, external). A parallel AE workflow triggers **Cargo/Make** on a Unibox reply or CRM status to categorize intent and route to the AE (source: "Best AI sales prompts and role-specific workflows that SDRs and AEs can run today").

## Make vs. n8n vs. Zapier

HeyReach supports all three; Make and [[n8n-automation-workflows]] both have native modules/nodes, while [[zapier-albato-and-other-orchestrators]] Zapier is webhook/API-only (no native app). The failure-mode guidance applies to Make too: **deduplicate at the orchestration layer** (Make/n8n), not inside HeyReach, because HeyReach only "sees within a campaign" (source: "Autonomous AI agents in B2B sales: What works and what quietly breaks").

## Related
- [[n8n-automation-workflows]]
- [[zapier-albato-and-other-orchestrators]]
- [[heyreach-campaign-api-and-webhooks]]
- [[clay-enrichment-and-data-waterfall]]
- [[multichannel-email-and-ai-copy-integrations]]
- [[automation-workflow-templates]]
- [[crm-integrations]]
- [[ai-outreach-agent-architecture]]
- [[multichannel-linkedin-email-sequencing]]
- [[qualify-and-prioritize-leads]]
