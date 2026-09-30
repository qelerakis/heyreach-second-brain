# CRM Integrations (HubSpot, Attio, Salesforce, Breakcold, Alysio)

How HeyReach syncs LinkedIn activity with CRMs so outbound stops living "entirely outside your CRM" (source: "HubSpot integration is live: sync outreach activity automatically"). HeyReach has a **native (OAuth) HubSpot integration**, a community-built **Attio** app, and API-key connections to relationship CRMs (Breakcold) and GTM workspaces (Alysio); Salesforce/Pipedrive/Close are reached via orchestrators. This article covers each plus the "CRM as source of truth" hygiene pattern. All sources are HeyReach's own guides/channel (COI); "officially approved" marketplace claims are vendor claims.

## HubSpot (native, OAuth)

HeyReach's deepest CRM integration — an "officially approved" HubSpot app (marketplace listing 24004400), connected via OAuth (source: "How to set up HubSpot Integration in HeyReach"). Setup: HeyReach → Integrations → Connect Account under HubSpot → sign in → choose account. Then:
- **Sync triggers** (choose which fire): "Lead Added to Campaign" and "First Reply Received" (default & recommended = on first reply).
- **Field mapping** — you MUST select which HubSpot property holds the LinkedIn URL; a wrong property means leads fail to import. Auto-find missing LinkedIn URLs from email is ON by default (reverse email lookup); if not found, the lead is marked failed.
- **Activity Mappings** — message replies + LinkedIn engagement sync to the contact's timeline; conversations log as **notes on the contact record, one per sender**, so the full LinkedIn thread sits beside the email thread and "when a rep leaves, the conversation history stays."
- **Logs** — full sync history (date, lead, HubSpot account, activity, status) filterable to spot failures.

On install, HeyReach creates a dedicated **property group with 20 properties** (campaign attribution, first/last touch dates, LinkedIn Sender, **Reply sentiment** positive/neutral/negative used to auto-tag warm leads, engagement metrics) (source: "HubSpot integration is live: sync outreach activity automatically"). You can also **launch campaigns straight from HubSpot lists** — pull any static or dynamic HubSpot contact list into HeyReach as a campaign source. Activities logged natively: connection requests sent & accepted, messages sent & replied, InMails sent & replied, campaign enrolments, list assignments.

## Attio (community-built app, two-way)

A **community-built** Attio app (explicitly "not a native HeyReach product") does a two-way sync via standard Attio lists + webhooks, working on any Attio tier (source: "HeyReach + Attio integration guide"). Inbound (HeyReach→Attio): install the app → connect the HeyReach API key → it **auto-creates up to 12 webhooks** (one per event type) plus a dedicated "HeyReach Events" list (LinkedIn URL, message body, campaign, company, tags — "don't delete… it's the backbone of the sync") → toggle which events to track (defaults: connection request accepted, message replied; many disable "profile viewed"). Outbound (Attio→HeyReach): bulk-add People (More → Add to HeyReach Campaign/List → pick account + campaign) or add an individual from the record's HeyReach section. If a contact doesn't exist, the app auto-creates a person record. **Hard product rule surfaced here:** HeyReach rejects old-style LinkedIn URLs containing `/pub/` — use `linkedin.com/in/username` or the lead fails (source: "HeyReach + Attio integration guide").

## Breakcold (relationship CRM)

Breakcold is "a modern relationship-based CRM tracking multichannel engagement... that tells you WHO to contact and WHEN," summarized as: "Breakcold helps you identify who to contact and when, while HeyReach takes care of how" (source: "How to integrate HeyReach with Breakcold for effortless LinkedIn outreach"). Setup: install the HeyReach app in Breakcold (Settings → App Store) → paste the HeyReach API key → Validate & Save → choose push method: **automatic** (toggle "Automatically push leads to HeyReach," set conditions like "when a lead reaches a CRM stage → assign to a HeyReach list/campaign") or **manual** (three-dot menu → Push to HeyReach). Reply/status sync *back* from HeyReach to Breakcold is not native yet — do it via HeyReach Webhooks + Zapier/Make (a native reply-sync was on the roadmap) (source: "How to integrate HeyReach with Breakcold for effortless LinkedIn outreach").

## Alysio (GTM AI workspace)

Alysio is a "GTM AI workspace" connecting CRMs, data providers, and conversation intelligence into one natural-language interface; it writes to HeyReach via **OAuth** (respecting HeyReach permissions) (source: "HeyReach + Alysio integration guide"). Flow: connect via OAuth → connect data providers (ZoomInfo, Apollo, Salesforce, HubSpot, Salesloft, Outreach, Gong) → prospect in plain English ("Find me 50 VP of Sales at Series B SaaS... not in our CRM") → push to a HeyReach campaign/list (map fields; requires a valid LinkedIn URL) → manage campaigns from Alysio (pause/resume, lead status, metrics). Use cases include mid-campaign refueling and pipeline-informed outreach (check Gong/CRM before pushing so LinkedIn doesn't undercut an active deal).

## HotHawk (shared team inbox)

HotHawk consolidates LinkedIn + email replies into one shared team inbox (with a built-in CRM) (source: "HeyReach + HotHawk integration guide"). Setup: HeyReach → Settings → Integrations → Public API → Generate API Key (from the correct workspace — each HotHawk inbox maps to one HeyReach workspace) → in HotHawk, Connect → paste key (HotHawk auto-registers webhooks for LinkedIn replies, sent messages, and tag updates). The agency angle: give clients "a clean, branded inbox that shows only their conversations" via a scoped client user account, instead of full HeyReach access "where they'd see everything." Tag sync requires an exact name match (including capitalization).

## Auto-populating a CRM from replies (Attio via n8n)

Beyond native connectors, HeyReach shows building CRM sync yourself: HeyReach reply webhook → n8n → OpenAI (O3 Mini) sentiment agent → only "positive" through → HTTP request creates an Attio Person + Company + Deal (stage auto = "Lead Interested," source tag "Cold LinkedIn") → Slack reminders at 3/7/14 days; a "Gone Cold" automation moves a deal after 14 days no reply (source: "How to automate your CRM with HeyReach, n8n, and AI sentiment analysis"). Trigger on the *event* ("first message reply received"), not on a manual tag. See [[n8n-automation-workflows]].

## CRM as source of truth (hygiene)

Because the outreach stack is volatile (swapping Instantly ↔ Smartlead loses their data), practitioner **Nenad Pavlov** (GTM agency — COI) argues the CRM must be the single source of truth: "We don't want to reach out to people before they're in HubSpot" (source: "How to Automate CRM Hygiene in HubSpot Using n8n [Full Workflow Tutorial]"). His n8n build splits **pre-campaign** (get leads into HubSpot → score profile *eligibility* on signals like photo/About length/posting via an Apify 0–10 activity score → if score ≥2, push to a HeyReach campaign — don't burn the ~150/week connection bandwidth on abandoned profiles) and **post/during-campaign** (write every HeyReach event back to HubSpot: connection sent + timestamp, "connected with [rep] + date," message text, and the full reply thread with sentiment). HubSpot's own MCP then allows chat-based analysis. HeyReach's related guidance on keeping CRM data clean during campaigns and lifecycle routing (add-lead / pause-lead / assign-lead) is in [[heyreach-campaign-api-and-webhooks]] and [[automation-workflow-templates]].

## Salesforce, Pipedrive, Close

No native HeyReach app is documented for these; they connect through orchestrators (Zapier/Make/n8n/Albato/Pabbly/Cargo) or via Alysio (source: "How to connect HeyReach with Zapier"; source: "HeyReach + Alysio integration guide"). Salesforce sync was referenced as "soon" in the RB2B webinar (source: "Send personalized LinkedIn messages to your website visitors [HeyReach - RB2B Webinar]").

## Related
- [[heyreach-campaign-api-and-webhooks]]
- [[n8n-automation-workflows]]
- [[make-automation-workflows]]
- [[zapier-albato-and-other-orchestrators]]
- [[data-enrichment-tools-and-providers]]
- [[automation-workflow-templates]]
- [[website-visitor-identification]]
- [[agency-client-onboarding-and-reporting]]
- [[manage-replies-and-inbox-at-scale]]
