# Introducing HeyReach Campaign API

Source: https://www.heyreach.io/blog/campaign-api

Summary: HeyReach Campaign API gives AI agents full programmatic control over LinkedIn outreach. Manage campaigns, leads, inbox, and analytics via API — no browser required. Build from Claude, Slack, or any tool.

**LinkedIn outreach, everywhere you work. Build and launch campaigns from Claude, OpenClaw, Slack — all through one powerful API. Give your AI agents full control over campaigns, leads, inbox, and analytics. No tabs. No logins. Just results.**

For almost three years, HeyReach has been the LinkedIn automation tool agencies and GTM teams trust. That trust was earned by building together: multi-sender rotation, unified inbox, agency-friendly pricing, powerful integrations, HeyReach MCP, and many other features.

Trust is a responsibility we take seriously. Which is why today's release matters: **HeyReach Campaign API** is the most-requested feature recently, and it fundamentally changes how LinkedIn automation works.

**What changes:** LinkedIn outreach is no longer locked in a browser. Campaign API gives you full programmatic access to LinkedIn automation. Every feature — campaigns, inbox management, lead routing, analytics — is now accessible via our API. Give your AI agents complete control: campaigns, leads, inbox, analytics.

Just natural language commanding your entire LinkedIn outreach infrastructure. Use cases:

* Build a campaign for CMOs at $10M+ ARR SaaS companies
* Import all closed-lost accounts from HubSpot and launch a 3-step sequence starting with “If Connected” filter and then segment existing and new connections into two separate flows
* Launch a connect-only LinkedIn outreach campaign for all new users this month

## **How-to videos for Campaign API**

‍

‍

> ⚠️ HeyReach Campaign API is live in beta for all users. We're shipping fast and iterating based on your feedback, so expect additional updates in the coming days.
>
> ‍**Important:** Campaign API is powerful. Improper usage could affect other areas of the tool. Please read the documentation below carefully before building. Questions? Email [support@heyreach.io](mailto:support@heyreach.io) or reach out in your dedicated Slack channel.

### **Full documentation**

Below is the complete technical reference for building and launching HeyReach campaigns from anywhere. All endpoints require API key authentication (available in Settings → API).

## 1. `POST /api/public/campaign/Create`

**Purpose**: Creates a fully configured campaign in **DRAFT** status in a single call. You must call `StartCampaign` separately to activate it.

### Request body — `CreateCampaignApiInputDto`

| Field | Type | Required | Constraints | Description |
| --- | --- | --- | --- | --- |
| name | string | Yes | 1–50 chars | The campaign name |
| linkedInUserListId | long | Yes | Must exist, must be type USER\_LIST | The lead list to run the campaign against |
| linkedInAccountIds | int[] | Yes | 1–100 items | LinkedIn sender account IDs; must exist and have valid auth |
| excludeContactedFromOtherCampaigns | bool | No | default false | Skip leads already in any other campaign |
| excludeHasOtherAccConversations | bool | No | default false | Skip leads with existing conversations from other accounts |
| excludeContactedFromSenderInOtherCampaign | bool | No | default false | Skip leads the sender accounts have touched in other campaigns |
| excludeListId | long? | No | Must not equal linkedInUserListId | A separate list of leads to always exclude |
| schedule | CampaignScheduleApiDto | No | See Schedule object | If omitted, defaults to Mon–Fri 09:00–17:00 UTC |
| sequence | PublicSequenceNodeDto | No | See Sequence notes | The automation tree. The START node is implicit — do not include it. If omitted, must be added via UpdateSequence before starting |

### Response — `200 OK`

`{ "campaignId": 12345 }`

### Errors

| HTTP | Cause | How to avoid |
| --- | --- | --- |
| 400 | Lead list not found | Verify linkedInUserListId exists |
| 400 | Lead list is wrong type | The list must be of type USER\_LIST, not a tag/filter list |
| 400 | Include and exclude list are the same | Use a different list for excludeListId |
| 400 | A LinkedIn account ID was not found | Verify every ID in linkedInAccountIds exists in the workspace |
| 400 | A LinkedIn account has invalid auth | The account session has expired; reconnect it first |
| 400 | Schedule is invalid (bad time window) | Ensure dailyStartTime < dailyEndTime, both ≤ 24:00:00 |
| 400 | End date is not after start date | endDate must be strictly after startDate |
| 400 | No schedule days enabled | At least one enabled\* day must be true |
| 400 | Invalid timezone | Use a valid IANA timezone identifier |
| 400 | Sequence structural errors | See sequence validation rules below |
| 403 | No active subscription | Workspace has no active subscription |

## 2. POST `/api/public/campaign/UpdateSettings`

**Purpose**: Updates the general settings of a campaign — its name, lead list, and exclusion options. Cannot be called on ACTIVE or COMPLETED campaigns.

**Side effect**: If the campaign was in **SCHEDULED** status, it reverts to **DRAFT**.

### Request body — `UpdateCampaignSettingsApiDto`

| Field | Type | Required | Constraints | Description |
| --- | --- | --- | --- | --- |
| campaignId | long | Yes | Campaign must exist | The campaign to update |
| name | string | Yes | 1–50 chars | New campaign name |
| linkedInUserListId | long | Yes | Must exist, must be type USER\_LIST | Replacement lead list. Cannot be changed after the campaign has started at least once |
| excludeContactedFromOtherCampaigns | bool | No | default false |  |
| excludeContactedFromOtherCampaigns | bool | No | default false |  |
| excludeHasOtherAccConversations | bool | No | default false |  |
| excludeContactedFromSenderInOtherCampaign | bool | No | default false |  |
| excludeListId | long? | No | Must not equal linkedInUserListId |  |

### Response — `200 OK`

Empty body.

### Errors

| HTTP | Cause | How to avoid |
| --- | --- | --- |
| 404 | Campaign not found | Verify the campaign ID belongs to your workspace |
| 400 | Campaign is in ACTIVE or COMPLETED status | Only DRAFT, SCHEDULED, and PAUSED campaigns can be updated |
| 400 | Lead list not found | Verify linkedInUserListId exists |
| 400 | Lead list is wrong type | Must be a USER\_LIST |
| 400 | Include and exclude list are the same | Use a different excludeListId |
| 400 | List changed after campaign has started | Once a campaign has been started at least once, linkedInUserListId is locked |
| 403 | No active subscription |  |

## 3. `POST /api/public/campaign/UpdateSequence`

**Purpose**: Creates or fully replaces the sequence (automation workflow) of a campaign. For **PAUSED** campaigns, a safe update is performed — existing lead states are preserved and leads are remapped to compatible positions in the new sequence. For **SCHEDULED** campaigns, the campaign reverts to **DRAFT**.

### Request body — `UpdateCampaignSequenceApiDto`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| campaignId | long | Yes | The campaign to update |
| sequence | PublicSequenceNodeDto | Yes | The root of the sequence tree. The START node is implicit — do not include it; start with your first action node |

### The `PublicSequenceNodeDto` object

| Field | Type | Required | Constraints | Description |
| --- | --- | --- | --- | --- |
| nodeType | PublicSequenceNodeType (enum) | Yes | See node types | The action or condition this node performs |
| unconditionalNode | PublicSequenceNodeDto | Depends | Required unless this is an END node | The next node to follow unconditionally (or when a condition is false) |
| conditionalNode | PublicSequenceNodeDto | Yes, for branching node types such as CONNECTION\_REQUEST, CONNECTION\_REQUEST, CHECK\_IS\_OPEN\_PROFILE | ROnly for CONNECTION\_REQUEST, CONNECTION\_REQUEST, CHECK\_IS\_OPEN\_PROFILE | The next node to follow when the condition is true |
| actionDelay | int | No | 0–100, default 0 | How long to wait before executing this node |
| actionDelayUnit | ActionDelayUnit (enum) | No | HOUR or DAY | The unit for actionDelay |
| payload | PublicSequenceNodePayload | Depends | Required for certain node types | Node-specific configuration (see per-node payload below) |
| externalReference | string? | No | Max 100 chars | Your own tracking ID for this step for reference via API and webhooks. |

### Node types (`PublicSequenceNodeType`)

| Value | Description | Payload required? | Branches (conditional/unconditional)? |
| --- | --- | --- | --- |
| CONNECTION\_REQUEST | Send a LinkedIn connection request | Yes — PublicConnectionRequestPayload | Both (conditional = true path, unconditional = false path) |
| MESSAGE | Send a direct LinkedIn message | Yes — PublicMessagePayload | Unconditional only, conditional (when there is a reply must be an END node) |
| INMAIL | Send a LinkedIn InMail | Yes — PublicInMailPayload | Unconditional only, conditional (when there is a reply must be an END node)o |
| VIEW\_PROFILE | View the lead's profile | No | Unconditional only |
| FOLLOW | Follow the lead | No | Unconditional only |
| LIKE\_POST | Like/react to the lead's recent post | Yes — PublicPostLikePayload | Unconditional only |
| FIND\_EMAIL | Attempt to find the lead's email | No | Both (conditional = email found, unconditional = email not found) |
| CHECK\_IS\_CONNECTION | Branch on whether the lead is a 1st-degree connection | No | Both (conditional = true path, unconditional = false path) |
| CHECK\_IS\_OPEN\_PROFILE | Branch on whether the lead has an open profile | No | Both |
| SEND\_LEAD\_TO\_INSTANTLY | Send the lead to an Instantly list/campaign | Yes — PublicSendLeadToInstantlyPayload | Unconditional only |
| SEND\_LEAD\_TO\_SMARTLEAD | Send the lead to a SmartLead campaign | Yes — PublicSendLeadToSmartLeadPayload | Unconditional only |
| SEND\_LEAD\_TO\_BISONt | Send the lead to a EmailBizon campaign | Yes — PublicSendLeadToBisonPayload | Yes — PublicSendLeadToBisonPayloadtd> |
| Tempor incididunt | Ut labore | Et dolore | Magna aliqua |
| END | Terminates the path for this lead | No | None — must be a leaf node (final node in all branches of the sequence) |

### Payload objects

**`PublicConnectionRequestPayload`** (for `CONNECTION_REQUEST`):

| Field | Type | Constraints | Description |
| --- | --- | --- | --- |
| messages | string[]? | Max 300 chars each | Message templates for the note. A random one is picked per lead. May be empty for a blank request. Supports {{firstName}} etc. |
| fallbackMessage | string? | Max 300 chars | Used when a personalization variable can't be resolved. Required if any message uses variables |
| toBeWithdrawnAfterDays | int? | ≥ 14 | Auto-withdraw the pending request after N days if not accepted. null = never withdraw |

#### **PublicMessagePayload**

(for MESSAGE):

| Field | Type | Constraints | Description |
| --- | --- | --- | --- |
| messages | string[] | Required, ≥1 item, max 8000 chars each | Message templates. Supports personalization variables |
| fallbackMessage | string? | Max 8000 chars | Fallback when variables can't be resolved |

##### **PublicInMailPayload** (for INMAIL):

| Field | Type | Constraints | Description |
| --- | --- | --- | --- |
| messages | PublicInMailMessage[] | Required, ≥1 item | InMail templates |
| fallbackMessage | PublicInMailMessage? |  | Fallback when variables can't be resolved |

##### PublicInMailMessage:

| Field | Constraints/th> |
| --- | --- |
| subject | Required, max 200 chars, supports personalization variables |
| message | Required, max 1900 chars, supports personalization variables |

##### **PublicPostLikePayload** (for LIKE\_POST):

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| reactionType | PublicReactionType enum | LIKE | LIKE, CELEBRATE, SUPPORT, FUNNY, LOVE, INSIGHTFUL, CURIOUS |
| randomReaction | bool | false | If true, picks a random reaction type, ignoring reactionType |
| reactBefore | PublicReactBefore enum | MONTH1 | Only react to posts published within this window: DAY1, DAY3, WEEK1, WEEK2, MONTH1, MONTH3 |
| skipDelayIfCannotLike | bool | false | Skip actionDelay if there are no eligible posts to react to |

##### **PublicSendLeadToInstantlyPayload** (for SEND\_LEAD\_TO\_INSTANTLY):

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| instantlyResourceId | string (UUID) | Yes | Instantly list or campaign GUID |
| resourceType | PublicInstantlyResourceType enum | No | LIST (0) or CAMPAIGN (1) |

##### **PublicSendLeadToSmartLeadPayload** (for SEND\_LEAD\_TO\_SMARTLEAD):

| Field | Type | Required | Constraints |
| --- | --- | --- | --- |
| smartLeadCampaignId | long | Yes | ≥ 1 |

### Sequence validation rules

* Every path through the tree must terminate with an `END` node.
* `CONNECTION_REQUEST`,`CHECK_IS_CONNECTION` and `CHECK_IS_OPEN_PROFILE` nodes must have **both** `conditionalNode` and `unconditionalNode` set.
* All other non-END nodes must have `unconditionalNode` set and must **not** have `conditionalNode` set.
* `actionDelay` must be 0–100.
* Node payloads must be valid per the constraints listed above.
* The sequence tree must not contain paths that are structurally impossible to complete.

### Response — `200 OK`

Empty body.

### Errors

| HTTP | Cause | How to avoid |
| --- | --- | --- |
| 404 | Campaign not found | Verify the campaign ID |
| 400 | Campaign is ACTIVE or COMPLETED | Only DRAFT, SCHEDULED, PAUSED allowed |
| 400. | Sequence has no valid start | Ensure the root node is a valid action/check node |
| 400 | Sequence has an unterminated path | All branches must end with an END node. |
| 400 | Delay is out of range | actionDelay must be 0–100 |
| 400 | Invalid node children/parent relationship | Check conditional/unconditional rules per node type |
| 400 | Invalid node type | Use only the defined PublicSequenceNodeType values |
| 400 | Inconsistent sequences for update. | On a PAUSED campaign, the new sequence must be structurally compatible with existing lead states |
| 403 | subscription |  |

## 4. `POST /api/public/campaign/UpdateAccounts`

**Purpose**: Replaces the entire list of LinkedIn sender accounts assigned to a campaign. For **PAUSED** campaigns, removing an account will stop any leads currently being processed by that account. For **SCHEDULED** campaigns, the campaign reverts to **DRAFT**.

### Request body — `UpdateCampaignAccountsApiDto`

| Field | Type | Required | Constraints | Description |
| --- | --- | --- | --- | --- |
| campaignId | long | Yes | Campaign must exist | The campaign to update |
| linkedInAccountIds | int[] | Yes | 1–100 items | Full replacement list of sender account IDs. All must exist and have valid auth |

> **⚠️ This is a full replacement**, not a merge. Any account not in the new list will be removed. On a PAUSED campaign, leads assigned to a removed account will be stopped and cannot be resumed.

### Response — `200 OK`

Empty body.

### Errors

| HTTP | Cause | How to avoid |
| --- | --- | --- |
| 404 | Campaign not found | Verify the campaign ID |
| 400 | Campaign is ACTIVE or COMPLETED | Only DRAFT, SCHEDULED, PAUSED allowed |
| 400 | A LinkedIn account ID was not found | Every ID must exist in the workspace |
| 400 | A LinkedIn account has invalid auth | Reconnect the account before using it in a campaign |
| 403 | No active subscription |  |

## 5. `POST /api/public/campaign/UpdateSchedule`

**Purpose**: Replaces the schedule of a campaign. Defines when the campaign runs each day, which days it is active, the timezone, and optional start/end dates. For **SCHEDULED** campaigns, the campaign reverts to **DRAFT**.

**Restriction**: Once a campaign has been started at least once, the `startDate` cannot be changed.

### Request body — `UpdateCampaignScheduleApiDto`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| campaignId | long | Yes | The campaign to update |
| schedule | CampaignScheduleApiDto | Yes | The new schedule configuration |

### The CampaignScheduleApiDto object

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| dailyStartTime | TimeSpan (e.g. "09:00:00") | Yes | — | Start of the daily active window. Must be before dailyEndTime. Max "24:00:00" |
| dailyEndTime | TimeSpan (e.g. "17:00:00") | Yes | — | End of the daily active window. Must be after dailyStartTime. Max "24:00:00" |
| timeZoneId | string | Yes | "Etc/GMT" | IANA timezone identifier (e.g. "America/New\_York", "Europe/London"). All times are interpreted in this zone |
| enabledMonday | bool | No | true |  |
| enabledTuesday | bool | No | true |  |
| enabledWednesday | bool | No | true |  |
| enabledThursday | bool | No | true |  |
| enabledFriday | bool | No | true |  |
| enabledSaturday | bool | No | false | Row3 E |
| enabledSunday | bool | No | false |  |
| startDate | DateOnly? (e.g. "2025-06-01") | No | null | Future start date. If null or in the past, the campaign starts immediately when activated. Cannot be modified after the campaign has started once |
| endDate | DateOnly? | No | null | The campaign stops automatically on this date. Must be after startDate if both are set |

### Response — `200 OK`

Empty body.

### Errors

| HTTP | Cause | How to avoid |
| --- | --- | --- |
| 404 | Campaign not found. | Verify the campaign ID |
| 400 | Campaign is ACTIVE or COMPLETED | Only DRAFT, SCHEDULED, PAUSED allowed |
| 400 | Invalid schedule | dailyStartTime must be before dailyEndTime; both must be ≤ 24:00:00. |
| 400 | End date not after start date | endDate must be strictly after startDate. |
| 400 | No days enabled. | At least one enabled\* day must be true |
| 400 | Cannot modify start date after campaign has started | Remove startDate or leave it unchanged once the campaign has been activated |
| 400 | Invalid timezone ID | Use a valid IANA timezone string |
| 400 | No active subscription |  |

## 6. `GET /api/public/campaign/GetCampaignSequence`

**Purpose**: Retrieves the current sequence (workflow) of a campaign as a `PublicSequenceNodeDto`. The returned object is directly compatible with the `Create` and `UpdateSequence` endpoints — you can use it as the `sequence` field in either request body without modification.

### Query parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| campaignId | long | Yes | The campaign whose sequence to retrieve |

### Response — `200 OK`

Returns a `PublicSequenceNodeDto` (the root of the sequence tree, without the implicit START wrapper). Returns an empty `200` response if the campaign has no sequence.

### Errors

| HTTP | Cause | How to avoid |
| --- | --- | --- |
| 404 | Campaign not found | Verify the campaign ID belongs to your workspace |
