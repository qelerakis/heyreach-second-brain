# Zapier, Albato, Pabbly, Cargo & Slack

Beyond n8n and Make, HeyReach connects to a range of no-code automation platforms — Zapier, Albato, Pabbly Connect, and Cargo — plus Slack for notifications. Most of these bridge to HeyReach through **webhooks + the API** rather than deep native modules, so the shared setup pattern is: generate a HeyReach API key, create a webhook bound to specific campaigns + event types, and match those events on both ends. This article covers each. All sources are HeyReach's own integration guides (COI); they are procedural how-tos with no result metrics. See [[heyreach-campaign-api-and-webhooks]] for the underlying webhook catalog.

## Zapier (webhook/API only — no native app)

Notable product fact: **HeyReach has no native Zapier app**, so you connect using Webhooks (source: "How to connect HeyReach with Zapier"). Two directions:
- **HeyReach → Zapier:** Zapier → Create Zap → trigger "Webhooks by Zapier" → "Catch Hook" → copy the URL; in HeyReach → Integrations → Webhooks → Add New Webhook → paste URL → select events ("Reply received", "Connection request accepted"); then an action (Slack/Teams notify, update HubSpot/Salesforce/Pipedrive, add a Google Sheets row).
- **Zapier → HeyReach:** a trigger app (Calendly, Typeform, Google Sheets) → action "Webhooks by Zapier" → POST to the HeyReach API endpoint (from Settings → API) → add header `Authorization: Bearer YOUR_API_KEY` → map fields (firstName, lastName, LinkedInProfileUrl, email).

Example use case: "Calendly → HeyReach: Every new meeting adds the contact into a LinkedIn outreach sequence" (source: "How to connect HeyReach with Zapier").

## Albato (600+ apps, two-way)

Albato is a no-code "command center" with two-way sync across 600+ apps (source: "How to connect HeyReach with Albato (and automate outreach like a pro)"). Setup: Albato → Automation → Create new → Add a trigger → HeyReach → pick an event ("New reply", "Message sent", "Connection request accepted") → Add a connection (paste HeyReach API key from Integrations → Get API Key) → Albato generates a Webhook URL; then HeyReach → Integrations → View/Create Webhooks → Create Webhook → paste Albato's URL and select **campaigns + event types that MATCH what you chose in Albato** (the key gotcha — mismatched events won't fire). Then build the rest in Albato (update CRM on reply, Slack notify, add to Google Sheet/Notion). Note a documented native limitation: pausing campaigns / assigning Unibox senders were not native in Albato as of Aug 2025 (source: "How to connect HeyReach with Albato (and automate outreach like a pro)").

## Pabbly Connect (webhook fan-out)

Pabbly Connect pushes HeyReach campaign events into other tools via webhooks (source: "How to Integrate HeyReach with Pabbly"). Setup: Pabbly → Create Workflow → choose HeyReach as the Trigger App → select a Trigger Event ("New Reply Received," "Connection Accepted"); in HeyReach → Integrations → View/Create Webhooks → Create Webhook (name, Pabbly URL, campaign, event type); then pick an Action App (Slack / HubSpot / Google Sheets / Gmail) and map the incoming HeyReach fields (name, LinkedIn profile, message). Example flows: HeyReach → Slack (notify on reply), → HubSpot (push leads/replies), → Google Sheets (log connections), → Gmail (follow-up on accept).

## Cargo (visual "Plays")

Cargo is a B2B workflow-automation platform that bridges data sources (HubSpot, CRMs, datasets) to tools like HeyReach via visual "Plays" (trigger → connector → action) (source: "How to Integrate HeyReach with Cargo"). Setup: Cargo → New Play → Create from Blank → choose a trigger source (Datasets or Integrations like HubSpot/Salesforce) → drag a connector → choose HeyReach → paste the API key (HeyReach → Integrations → Get API Key) → configure Actions (Object type, Action = add to campaign / add to list, Campaign) → hit Play. "Cargo acts as the bridge, pushing leads straight into HeyReach so your outreach engine runs the moment new data appears." Cargo also appears as the trigger layer in an AE reply-routing workflow (source: "Best AI sales prompts and role-specific workflows that SDRs and AEs can run today").

## Slack (notifications via Incoming Webhook)

Slack is the near-universal alert/approval endpoint across HeyReach automations. The native notification setup: HeyReach → Integrations → **Connect with Slack** → name it → in Slack's Admin panel, Configure Apps → Custom Integrations → Incoming WebHooks → pick a channel → copy the URL → paste into HeyReach → Create Connection → Test Connection (source: "How to connect HeyReach with Slack"). Notification events: **connection request accepted, message or email reply received, campaign completed**; supports multiple channel notifications. (In n8n/Make builds, Slack additionally serves as the human approve/decline gate — see [[n8n-automation-workflows]].)

## Choosing an orchestrator

| Platform | Native depth | Best for |
|---|---|---|
| n8n | Native nodes + community npm node | Complex, self-hosted, code-friendly builds |
| Make | Native modules + scenario library | Visual multi-branch routing, AI scoring |
| Albato | Trigger/action connectors, 600+ apps | Two-way sync across many SaaS apps |
| Pabbly | Webhook trigger → action | Simple event fan-out to Slack/CRM/Sheets |
| Cargo | Visual "Plays" connector | CRM/dataset → HeyReach data pipelines |
| Zapier | Webhooks only (no native app) | Quick form/calendar → HeyReach zaps |
| Slack | Incoming webhook | Notifications + human approval gates |

The lead-routing playbooks note Airtable "Watch Records" or Typeform/Tally webhooks can swap in as intake for any of these (source: "Lead routing that scales: 3 playbooks to automate assignment, sync, and enrichment").

## Related
- [[n8n-automation-workflows]]
- [[make-automation-workflows]]
- [[heyreach-campaign-api-and-webhooks]]
- [[crm-integrations]]
- [[automation-workflow-templates]]
- [[ai-outreach-agent-architecture]]
- [[agency-client-onboarding-and-reporting]]
