# HeyReach CLI

The HeyReach CLI is a command-line tool that makes everything in the dashboard scriptable — "Run LinkedIn outreach from the terminal / from Claude without a browser": launch/pause/edit campaigns, write and send data-drafted (non-template) messages, and pull pipeline (replies, sentiment, meetings, ROI) in plain English (source: "HeyReach CLI is here 🎉"). Critically, the CLI **wraps all 47 HeyReach API endpoints and registers them as MCP tools**, installs via a single npm command, and works as both a CLI and an MCP server — compatible with Claude Desktop, Claude Code, Cursor, n8n, Make, and OpenClaw (source: "The Best AI Agents for GTM Engineering (Your 2026 Stack Guide)"). It was built by the **Top of Funnel team** (Brandon Charleson) and is open-source. This article is HeyReach/partner documentation (COI).

## Install and authenticate

One command, ~60 seconds: `npm install -g heyreach-cli` (global), then authenticate with your HeyReach API key from account settings (source: "OpenClaw LinkedIn 0utreach: How to build your HeyReach AI agent"). Inside Claude Code, add it with `claude mcp add` (key + URL) and verify with `/mcp` or `claude mcp list` (source: "How I Get Unlimited Leads Using Claude Code + LinkedIn"; source: "Claude + LinkedIn = Unlimited Leads on Autopilot"). Download at /cli, with setup videos for Mac and Windows (source: "HeyReach CLI is here 🎉"). For agent installs, the pattern is to paste the public GitHub repo to the agent — "please install HeyReach CLI for me and help me authenticate" — and supply the API key, which the agent stores securely (source: "How I Get Unlimited Leads With Hermes Agent + LinkedIn").

**Security note (raised by the tool's author):** don't paste your API key into a chat interface — authenticate in the terminal backend (source: "OpenClaw LinkedIn 0utreach: How to build your HeyReach AI agent"; source: "Copy this OpenClaw system:  it'll BLOW your LinkedIn game overnight").

## Command groups exposed

The CLI is "a remote control wrapping HeyReach's API endpoints," with these command groups (source: "How Openclaw Runs My Entire LinkedIn Outreach System"):

| Group | What it does |
|---|---|
| campaigns | list / get / create DRAFT (a human must launch) / start / pause / resume |
| inbox (Unibox) | read conversations and reply |
| accounts | manage connected LinkedIn sender accounts |
| lists | create / manage lead lists |
| leads | add / get leads |
| lead tags | tag leads |
| stats | campaign analytics (acceptance rates, performance) |
| webhooks | manage webhook events |
| workspace | workspace-level operations |

The OpenClaw blog summarizes the surface as Campaigns (launch/monitor/pause/manage), Unified inbox (read & reply), Lead lists (create/manage), and Campaign analytics — with the design fact that **"every command doubles as an MCP tool"** so an agent calls any HeyReach function natively, "no logins, no browser tabs" (source: "OpenClaw LinkedIn 0utreach: How to build your HeyReach AI agent").

## Claude Skills

The launch shipped two reusable Claude Skills for GTM operators (source: "HeyReach CLI is here 🎉"):
- **"Launch campaigns"** — push qualified leads + signals; the agent builds the campaign and writes messages.
- **"Measure pipeline"** — Claude pulls replies, sentiment, meetings, and ROI and reports what's working.

The stated intent: "It stops being a set of commands and starts making real decisions" / "turn commands into decisions" (source: "HeyReach CLI is here 🎉").

## Open source

The CLI is open source — inspectable, extensible, and accepts pull requests on NPM/GitHub; it lives in Top of Funnel's resources (topoffunnel.com/resources) (source: "OpenClaw LinkedIn 0utreach: How to build your HeyReach AI agent"; source: "How Openclaw Runs My Entire LinkedIn Outreach System"). Because it is a community/partner-built tool wrapping the API, treat it as distinct from HeyReach's first-party MCP server, though the two overlap by design.

## CLI vs. MCP

Some practitioners prefer the CLI. The Hermes-agent build calls the CLI "the better option" over the MCP for agent use (source: "How I Get Unlimited Leads With Hermes Agent + LinkedIn"), and the OpenClaw build argues a vetted CLI "beats writing custom scripts every time" because it "wraps API calls with predictable behavior" (source: "OpenClaw LinkedIn 0utreach: How to build your HeyReach AI agent"). HeyReach itself presents CLI + MCP together as the two ways to "run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw" (source: "Run LinkedIn outreach without leaving Claude, Chat GPT or OpenClaw"). See [[heyreach-mcp-server]] and [[heyreach-campaign-api-and-webhooks]].

## Related
- [[heyreach-mcp-server]]
- [[heyreach-campaign-api-and-webhooks]]
- [[ai-agent-builds-claude-openclaw-hermes]]
- [[ai-outreach-agent-architecture]]
- [[automation-workflow-templates]]
- [[manage-replies-and-inbox-at-scale]]
