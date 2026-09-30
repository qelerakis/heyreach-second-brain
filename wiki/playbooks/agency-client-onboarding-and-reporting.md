# Agency Client Onboarding & Reporting

How a lead-gen agency onboards a new client cleanly, runs many client accounts without cross-contamination, and reports results in a way that renews retainers. The organizing idea from HeyReach's agency content: "you can't separate the service you're selling from the system you use to deliver it" — set up isolated per-client structure from day one, standardize the ops, and make reporting a repeatable 45-minute task, not a Sunday-night scramble (source: "How to scale a lead generation agency: From LinkedIn outreach to allbound"; source: "Build a repeatable system for agency client reporting with Claude"). The account-safety/seat-rotation side of delivery is in [[scale-linkedin-outreach-safely]]; the business-building side is in [[start-and-scale-a-lead-gen-agency]].

## Onboard each client onto isolated infrastructure

- **Intake form first.** Use a pre-built Tally/Typeform to collect the essentials before anything is built: ICP, offer, CTA, tone of voice, a LinkedIn headshot, calendar link, and content preferences (source: "LinkedIn client management that doesn’t break when you scale").
- **A workspace per client from day one.** Spin up a dedicated HeyReach Workspace per client so campaigns, lead lists, sender accounts, Unibox and tags never bleed across clients — "never share workspaces/lists/senders across clients," because a single flagged shared account can kill every client's campaign ("5 clients to 0 in 60 days" from one shared account) (source: "LinkedIn automation for outbound agencies: A zero-chaos system"; source: "How to scale a lead generation agency: From LinkedIn outreach to allbound"). HeyReach supports up to 30 workspaces per organization (request more), with adjustable seat limits per workspace (source: "LinkedIn client management that doesn’t break when you scale").
- **Boring naming conventions.** Standardize names like `ClientName_ICP_SaaS_Founders`, `ClientName_Campaign_Intro_v1`, and for reporting `[Client]_[ICP]_[Month]` (e.g. `AcmeCorp_CFOs_July`) — inconsistent naming silently breaks automations and reporting (source: "LinkedIn automation for outbound agencies: A zero-chaos system"; source: "Build a repeatable system for agency client reporting with Claude").
- **Client hub + walkthrough.** Build a per-client hub in Notion/Airtable and record a Loom walkthrough; invite the client with **view-only** access to their own workspace ("give your clients visibility, but not control") (source: "LinkedIn client management that doesn’t break when you scale").
- **Educate the client up front.** A 1-pager or Loom on what you do/don't do, realistic timelines, and *why* you won't send 500 messages/day heads off unrealistic expectations (source: "LinkedIn client management that doesn’t break when you scale").

## Delegate with role-based permissions

Give each person only what they need via granular Workspace roles/permissions (connect accounts? view/manage campaigns? create lists? respond to vs view DMs? access integrations/billing?): a VA gets inbox-only, a strategist manages campaigns, the client can connect their LinkedIn but can't edit lead lists or see billing or other clients (source: "LinkedIn client management that doesn’t break when you scale"; source: "Best LinkedIn Outreach Software in 2026 ❘ HeyReach Review ❘ Full Tutorial"). A key pricing point that shapes staffing: HeyReach charges **per LinkedIn sender, not per seat**, so unlimited teammates/VAs/clients are free — non-sending managers who only work the inbox/reports aren't paid seats (source: "The best LinkedIn management tools for scaling outreach without getting banned"). Manage everything across clients from the **Master View** (all workspaces, campaigns and a master Unibox on one screen) (source: "LinkedIn client management that doesn’t break when you scale").

## Evaluate the setup like a client would

HeyReach's agency-selection checklist doubles as a self-audit for what your own delivery must nail: tool-stack transparency (deliverability, CRM integration, reporting access, data ownership, compliance), process clarity (onboarding → launch), an agreed definition of "success," portfolio/ICP fit, and communication cadence (source: "The only LinkedIn outreach agency checklist you actually need"). Sanity-check benchmarks it offers (guidance, not verified): ~25–35% acceptance = targeting works, 8–15% reply (of accepted) = messaging resonates, 10–20% meeting booking (of positive replies) = qualified buyers.

## Build the reporting system once, run it in ~45 minutes

The reporting playbook: invest 2–4 hours building the system, then execute in 45–60 minutes per client per month (source: "Build a repeatable system for agency client reporting with Claude"):

1. **Export the metrics.** Switch to the client's Workspace → filter date range → select campaign/sender → Export CSV (source: "Build a repeatable system for agency client reporting with Claude").
2. **Score with a 3-tier threshold matrix** to standardize the narrative tone: Tier 1 Green (above benchmark), Tier 2 Yellow (stable), Tier 3 Red (corrective action) — tag each client/campaign and drop the matching pre-written paragraph into the report (source: "Build a repeatable system for agency client reporting with Claude").
3. **Translate metrics into client language.** Clients care, in order: "Is this working?" → "Should we keep investing?" (ROI) → "What do we do next?" — say "We booked 40% more calls," not "conversion rates improved 8%." Keep a "metrics translation dictionary" so phrasing is consistent (inconsistent phrasing "erodes trust") (source: "Build a repeatable system for agency client reporting with Claude").
4. **Report the metrics that matter:** connection acceptance rate, reply rate, positive replies/interested leads, and meetings booked — plus, powerfully, 2–3 representative real message exchanges per category, which "builds client trust... faster than withholding this information" (source: "Inbox management for agencies: cut the clutter, close more deals"; source: "3 LinkedIn KPIs that tell you exactly if your outreach drives pipeline"). Note HeyReach does **not** track booked meetings natively — pull them from tagged Unibox replies or a CRM sync (source: "Stop guessing which outreach campaigns work: Audit campaign performance and decide what to scale in 15 minutes").

## Automate the reports

Two automation modes:

- **Semi-automated:** Make/Zapier export post-refresh, auto-populate a Slides/Notion template, and fire a "ready for review" Slack message (source: "Build a repeatable system for agency client reporting with Claude").
- **Scheduled "while you sleep":** an n8n workflow on a Monday-midnight cron pulls total + weekly HeyReach stats via the official HeyReach n8n nodes, drafts a Gmail email with the client's addresses pre-filled (so Monday you just review and send), and appends the week's numbers to a Google Sheet for week-over-week history; turn on retry-on-fail for API rate limits — "your reports will be generated automatically while you sleep" (source: "How to Build LinkedIn Outreach Campaign Reports Using HeyReach"; source: "Automate your LinkedIn outreach campaign reports"). White-label reporting is available on agency tiers. Wiring detail is in [[n8n-automation-workflows]].

## Prove LinkedIn's contribution (CRM attribution)

The reason clients wrongly think LinkedIn "doesn't work" is often an attribution gap: LinkedIn is the last channel connected to the CRM, reps use private profiles, and history walks out when a rep leaves. Fix it by connecting HeyReach to the client's CRM so every LinkedIn activity (connection sent/accepted, message, reply + sentiment) auto-logs to the contact timeline and can be attributed against paid/inbound — "your best meetings are not attributed to an unknown source" (source: "Is LinkedIn Outreach Worth It in 2026?"; source: "HubSpot integration is live: sync outreach activity automatically"). On install, HeyReach's HubSpot integration auto-creates a property group (~20 properties: campaign attribution, first/last touch dates, LinkedIn sender, reply sentiment) and conversations persist as notes even after a rep leaves. Make the CRM the single source of truth from day one, because outreach tools are volatile — "we don't want to reach out to people before they're in HubSpot" (source: "How to Automate CRM Hygiene in HubSpot Using n8n [Full Workflow Tutorial]"). CRM-hygiene and lifecycle sync mechanics are in [[qualify-and-prioritize-leads]] and [[partner-integrations-directory]].

## Run weekly ops to catch problems early

Managing many client accounts is a weekly ritual: a 30-minute Monday review of the Master View/health scorecard catches restriction and delivery issues 3–5 days early, with clear ownership (Ops Lead handles rotations, Account Manager owns client comms, Campaign Manager owns sequences) (source: "LinkedIn automation for outbound agencies: A zero-chaos system"; source: "How to manage multiple LinkedIn accounts without getting flagged"). Named agency operators reinforce the theme: chaos hits around 50 clients when shared seats break, and "the solution isn't more headcount. It's a schema" (Victor André Enselmann/Modeva, Jason Hennessey/Hennessey Digital, others) (source: "How to grow a digital marketing agency: From 20 to 200 clients without breaking ops"). Delivery SLAs, seat rotation and the monitoring dashboard sit in [[scale-linkedin-outreach-safely]] and [[audit-and-optimize-linkedin-campaigns]].

## Related
- [[start-and-scale-a-lead-gen-agency]]
- [[scale-linkedin-outreach-safely]]
- [[manage-replies-and-inbox-at-scale]]
- [[audit-and-optimize-linkedin-campaigns]]
- [[qualify-and-prioritize-leads]]
- [[get-clients-on-linkedin]]
- [[heyreach-features]]
- [[n8n-automation-workflows]]
