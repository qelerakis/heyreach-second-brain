# HeyReach MCP, CLI, and Campaign API (as Product)

HeyReach treats its programmatic surfaces — the **MCP server**, the **CLI**, and the **Campaign API** — as first-class product, not just developer plumbing. The positioning: "LinkedIn outreach should live in your stack, not a browser tab," so operators can run campaigns from Claude, ChatGPT, Cursor, the terminal, or any tool (source: "HeyReach MCP: Build and launch campaigns end to end"; source: "HeyReach CLI is here 🎉"; source: "Introducing HeyReach Campaign API"). This article covers what these surfaces *are* and how HeyReach positions them; for wiring them into Clay/n8n/Make and building AI-agent architectures, see the tools-and-automation category. All claims here are HeyReach's own.

## HeyReach MCP (Model Context Protocol server)

The MCP page's pitch: "You describe the play, Claude runs it for you" — tell an LLM who to target, what to say, and when to follow up, and it writes messages, segments leads, and launches campaigns "without touching settings" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). Product facts:

- **Free.** "How much does HeyReach MCP cost? Nothing, you can use it straightaway"; setup "in minutes" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").
- **Built-in authentication** on MCP endpoints; "call and merge APIs without any extra setup or dev work." Each **workspace generates its own unique MCP key + endpoint** (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"; source: "The new baseline for LinkedIn outbound").
- **Connects to** Claude, ChatGPT/OpenAI, Cursor, Clay, n8n, Slack, "or any other popular MCP" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").
- **8 campaign-building MCP tools** shipped: CreateCampaign, CreateCampaignFromTemplate, UpdateCampaignSequence, UpdateCampaignSettings, UpdateCampaignSchedule, UpdateCampaignAccounts, GetCampaignSequence, and StartCampaign — enough to "run a full campaign without touching the app," and they went live automatically for existing MCP users (source: "HeyReach MCP: Build and launch campaigns end to end"). Single-prompt example: "Clone my best-performing campaign, swap in this lead list, assign my three warmest senders, set it to send 9-5 CET on weekdays, and launch it."
- **Positioning claim:** HeyReach's self-review calls it the "first outreach automation tool" to connect AI agents — a vendor claim (source: "HeyReach Review: The scalable LinkedIn outreach tool for agencies & sales teams"). Its stated framing: "For the first time, you don't have to be a tech genius to do advanced tech things" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").

Common MCP use-cases HeyReach markets: list hygiene (it demoed cleaning a **23k-lead list in minutes**), AI icebreakers, campaign auditing, reply classification in the Unibox, and seat rotation/rescheduling (source: "The new baseline for LinkedIn outbound"). See [[ai-personalization-at-scale]] and the tools-and-automation category.

## HeyReach CLI

The CLI extends the same "outreach belongs where you work" thesis to the terminal: "everything in the dashboard is now scriptable" — launch/pause/edit campaigns, send data-drafted (non-template) messages, and pull pipeline (replies, sentiment, meetings, ROI) in plain English (source: "HeyReach CLI is here 🎉"). Product facts:

- **Downloadable at /cli**, with Mac and Windows setup videos (source: "HeyReach CLI is here 🎉").
- Ships **two reusable Claude Skills**: (1) "Launch campaigns" (push qualified leads + signals; the agent builds the campaign and writes messages) and (2) "Measure pipeline" (Claude pulls replies, sentiment, meetings, ROI and reports what's working) (source: "HeyReach CLI is here 🎉").
- Positioning: "Connect it, point it at a campaign, and let it rip"; "It stops being a set of commands and starts making real decisions" (source: "HeyReach CLI is here 🎉").

## HeyReach Campaign API

The Campaign API is HeyReach's REST surface for controlling campaigns, leads, inbox, analytics, and lead routing programmatically — "no browser required" (source: "Introducing HeyReach Campaign API"). Positioning and product facts:

- Described as "the most-requested feature recently," and framed as fundamentally changing "how LinkedIn automation works"; **live in beta for all users** and complementary to the MCP (source: "Introducing HeyReach Campaign API").
- Buildable from Claude, OpenClaw, Slack, "or any tool"; requires an **API key from Settings → API** (source: "Introducing HeyReach Campaign API").
- **Campaign lifecycle:** Create makes a DRAFT; StartCampaign activates it separately; statuses are DRAFT → SCHEDULED → ACTIVE → PAUSED → COMPLETED, with most edits blocked once ACTIVE/COMPLETED (source: "Introducing HeyReach Campaign API").
- **Sequence node types** exposed include CONNECTION_REQUEST, MESSAGE, INMAIL, VIEW_PROFILE, FOLLOW, LIKE_POST, FIND_EMAIL, CHECK_IS_CONNECTION, CHECK_IS_OPEN_PROFILE, END, plus native email-handoff nodes **SEND_LEAD_TO_INSTANTLY / SEND_LEAD_TO_SMARTLEAD / SEND_LEAD_TO_BISON** (EmailBison) for multichannel (source: "Introducing HeyReach Campaign API").
- Age marker: "For almost three years, HeyReach has been the LinkedIn automation tool agencies and GTM teams trust" (source: "Introducing HeyReach Campaign API").
- Caution HeyReach itself flags: "Campaign API is powerful. Improper usage could affect other areas of the tool" (source: "Introducing HeyReach Campaign API").

The full endpoint/DTO reference (payload limits, schedule DTO, validation rules) is developer-integration material — see the tools-and-automation category. Note the source doc contained OCR/markup artifacts (a lorem-ipsum row, "SEND_LEAD_TO_BISONt", duplicated node names); the clean node names are as listed above.

## The product narrative these support

Together, MCP + CLI + API are how HeyReach makes its "new baseline for LinkedIn outbound" argument: outbound outcomes "now depend on how well your stack connects and executes," and MCP works in real time so "the model isn't just guessing—it pulls fresh data from your stack before taking action" (source: "The new baseline for LinkedIn outbound"). HeyReach also markets these to non-technical operators — "You choose your interface" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). A naming quirk to note: HeyReach pages inconsistently write "OpenClaw" vs "OpenClay" (likely a typo) (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw").

## Related
- [[heyreach-product-overview]]
- [[heyreach-features]]
- [[heyreach-vs-competitors]]
- [[ai-personalization-at-scale]]
- [[scale-linkedin-outreach-safely]]
