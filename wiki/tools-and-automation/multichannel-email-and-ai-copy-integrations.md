# Multichannel Email & AI-Copy Integrations

The "message side" of the stack: the cold-email platforms HeyReach hands leads to for multichannel LinkedIn+email (Instantly, Smartlead, EmailBison) and the AI copy layers that write the LinkedIn messages (SmartReach AI, Twain). The pitch across all of them is coordinated multi-touch — "double the touchpoints with half the effort" — instead of LinkedIn and email running as separate silos (source: "HeyReach + Instantly integration guide"). This article covers each integration's mechanics, the shared **Find Email** branching node, and the custom-variable + fallback pattern. All sources are HeyReach's own guides (COI); the "2-3x response rates" style claims are vendor claims, not measured. For the orchestrated LinkedIn+email design, also see [[multichannel-linkedin-email-sequencing]].

## The Find Email node (multichannel branch point)

Native email handoffs hinge on the **"Find Email" action** inside a HeyReach sequence: it branches **Email Found** (route to Instantly/Smartlead/EmailBison or continue LinkedIn) vs **Email Not Found** (LinkedIn-only). It can be added **once per sequence**, triggers once per lead per campaign, and consumes HeyReach credits (source: "HeyReach + Instantly integration guide"). HeyReach distinguishes an **Enriched email** (auto-discovered, not editable) from a **Custom email** (imported/manual); **Custom email always wins** when both exist. In the Campaign API these are the `FIND_EMAIL`, `SEND_LEAD_TO_INSTANTLY`, `SEND_LEAD_TO_SMARTLEAD`, and `SEND_LEAD_TO_BISON` node types — see [[heyreach-campaign-api-and-webhooks]].

## Instantly (bidirectional)

Setup HeyReach→Instantly: Instantly → API Keys → create key with **ALL scopes** (missing scopes cause errors) → HeyReach → Integrations → Instantly → Connect Now → paste → add an **"Add to Instantly"** action in the sequence, choosing **Instantly Campaigns** (leads enter the email sequence immediately; campaign must pre-exist) or **Instantly Lists** (collect first for enrichment/QA) (source: "HeyReach + Instantly integration guide"). Instantly→HeyReach: get a HeyReach API key → build an Instantly Automation with a trigger (interest-status changed / campaign finished / lead added to list / lead replies) → a HeyReach action (Add Lead to Campaign/List). Direction rule: LinkedIn cold + email warm → Instantly→HeyReach; LinkedIn warm + email cold → HeyReach→Instantly. Thresholds shown: no acceptance → wait 10 days → Find Email → Instantly; messages ignored → wait 5 days → Instantly List (leads *without* an email fail when sent to campaigns but are still added to lists).

## Smartlead (native, agency-oriented)

Setup HeyReach→Smartlead: Smartlead → Profile → API Key → HeyReach → Integrations → Smartlead → Connect Now → paste → add "Add to Smartlead" action → pick the (pre-existing) Smartlead campaign (source: "HeyReach + Smartlead integration: Complete setup guide"). Smartlead→HeyReach uses Smartlead **"SmartAgents"** (or the template "Push Replied Lead to a HeyReach Campaign"): connect the HeyReach API key, paste the **Campaign ID from the browser URL**, choose an Agent Trigger level (Account / Client / Campaign), Deploy. Note: **the Smartlead integration is not available for white-label users**. Vendor claim: "Increase response rates by 2-3x through coordinated multi-touch outreach."

## EmailBison (native, auto-push)

HeyReach's "third multichannel integration" after Instantly and Smartlead (source: "HeyReach + EmailBison integration"). Setup HeyReach→EmailBison: EmailBison → Developer API → New Token → HeyReach → Integrations → EmailBison → paste → Update API Token. EmailBison→HeyReach: get a HeyReach API key → EmailBison → Connect Now → paste key + copy the **Destination URL** → configure Workspace Defaults (default campaign; "Refetch Campaigns" if new ones don't show) (source: "How to Connect HeyReach with EmailBison (Full Integration Guide)"). **LinkedIn Profile URL is required** by EmailBison — map a HeyReach custom variable (e.g. `linkedinUrl`) or leads fail. Push manually (Leads/Unibox → Push to EmailBison) or enable **Automatic Push** (campaign → Integration Settings) — any lead whose sequence finishes **without a reply within 3 days of the final step** is auto-pushed. Channel-switch triggers: LinkedIn DM not replying → email; connection pending 5+ days → email; email ignored → LinkedIn. Gotcha: the target EmailBison campaign must be Active (a draft is the most common push failure), and the token is per-workspace.

## SmartReach AI (LinkedIn copy generation)

SmartReach AI writes per-lead LinkedIn copy and pushes it into HeyReach's message steps via special variables **`{connection}`, `{follow_up_1}`, `{follow_up_2}`** (source: "How to connect HeyReach + SmartReach AI for automated and hyper-personalized LinkedIn campaigns"). Setup: SmartReach AI → Settings → paste the HeyReach API key → build the campaign in HeyReach with those variables in the message steps → in SmartReach AI define the "prompt engine" (Description / Pain points / Social proof / Strategic advantages; tip: leave Keywords/Mandatory text empty at first) → select the list via "Upload from HeyReach" → tick HeyReach Campaign, untick Smart Link Campaign → pick the sender + campaign → set the number of follow-ups to generate → optionally enable Tone Optimizer and Auto Upload → launch from HeyReach. (Smart Link Connection Request requires a Sales Navigator license.)

## Twain (AI personalization layer)

Twain writes personalized messages from lead data/web activity and exports them to HeyReach (source: "How to Integrate HeyReach with Twain to automate personalized outreach"). Setup: create a HeyReach campaign with an **empty lead list**, assign a sender not used elsewhere, set a **conditional sequence** (if connected → message; if not → connection request), and **leave all message fields blank** (Twain fills via variables) → in Twain, Export Last Saved → HeyReach → paste the HeyReach API key → choose the lead list → name custom variables (e.g. `{{JobTitle}}`, `{{Company}}`) → Export → then in HeyReach insert the variables and add **fallback text** with the syntax `{{FirstName | there}}` → launch. Twain's deep-research mode outputs 3 emails + 3 LinkedIn messages with cited research and ICP-mismatch warnings, at ~12 Clay credits/row when run inside Clay (source: "Clay + HeyReach Integration Tutorial: Personalized LinkedIn Outreach at Scale (Step-by-Step)").

## The custom-variable + fallback pattern

Every AI-copy integration relies on the same mechanic: the copy tool populates HeyReach **custom variables**, and you set a **fallback message** for when a variable can't populate — a "safe soft opener like 'Quick one' / 'Wanted to reach out directly' — avoid faux-specific" (source: "HeyReach + Bitscale: Turn signals into LinkedIn outreach, automatically"). Variable names must match exactly between the source tool and HeyReach. See [[clay-enrichment-and-data-waterfall]] and [[ai-personalization-at-scale]].

## Related
- [[heyreach-campaign-api-and-webhooks]]
- [[clay-enrichment-and-data-waterfall]]
- [[signal-and-intent-integrations]]
- [[crm-integrations]]
- [[make-automation-workflows]]
- [[n8n-automation-workflows]]
- [[automation-workflow-templates]]
- [[multichannel-linkedin-email-sequencing]]
- [[multichannel-outreach-architecture]]
- [[ai-personalization-at-scale]]
