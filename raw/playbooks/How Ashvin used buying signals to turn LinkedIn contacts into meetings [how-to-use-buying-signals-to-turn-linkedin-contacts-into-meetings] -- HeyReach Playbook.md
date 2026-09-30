# How Ashvin used buying signals to turn LinkedIn contacts into meetings

Source: https://www.heyreach.io/outbound-playbooks/how-to-use-buying-signals-to-turn-linkedin-contacts-into-meetings

Summary: Signado founder Ashvin Jankee ran signal-triggered LinkedIn outreach via HeyReach API and hit 47.8% acceptance and 36.4% replies from 23 contacts.

Signado's founder built a signal-triggered outreach loop on top of HeyReach to test whether the personalization playbook that works in cold email could hold up on LinkedIn — and the numbers say yes.

## Key numbers

**47.8%** connection acceptance rate

**36.4%** reply rate (among accepted connections)

**2 meetings** booked from 23 signal-triggered leads

## Useful links and tools

* [HeyReach](https://heyreach.io/blog/heyreach-review) — LinkedIn outreach automation
* [Signado](https://signado.io) — signal detection, ICP scoring, and AI message generation
* [Sales Navigator](https://heyreach.io/integrations) — LinkedIn prospecting for batch 2 list building

## In their own words

"HeyReach's longevity in the LinkedIn outreach space, its proxy infrastructure, and its proven track record made it the obvious choice for our send layer. The API made the integration straightforward: we push the leads to an existing campaign with the personalized items, HeyReach handles the send cleanly."

— Ashvin Jankee, Founder @ Signado

## How it works

Ashvin Jankee built Signado to solve a specific problem: most personalization is cosmetic. A first name, a job title, maybe a company name thrown in somewhere. Real personalization references something that actually happened — a post someone wrote, a role they're hiring for, a round they just closed. Signado detects those events, scores them for ICP fit, and writes a message around them. HeyReach handles the send.

Here's the exact campaign he ran.

### Step 1: Define the ICP

For batch 1, Ashvin targeted US-based B2B SaaS companies at the Series A or B stage, 50–500 employees. Titles: VP Sales, Head of Sales, SDR Manager. The logic: companies at this stage are actively building GTM motions and feel the pain of unscalable outreach more acutely than enterprise orgs.

For batch 2, he narrowed the employee range to 201–500 and kept the same titles, sourcing from a Sales Navigator search pasted directly into HeyReach, exported as a CSV, and imported into Signado for signal monitoring.

### Step 2: Let Signado detect the signals

Once contacts hit Signado, monitoring across 7 signal types kicks off automatically:

* Funding rounds
* Hiring surges
* Leadership changes
* LinkedIn posts (including reposts and comments)
* Product launches
* Partnerships
* Press coverage

One thing that makes the timing work in practice: Signado backfills the past 6–12 months of signal data as soon as monitoring starts. No waiting around for a new event to fire — contacts with existing signals go into the queue immediately.

For batch 1, 23 contacts had active signals across the signal types above. All 23 were pushed to HeyReach with AI-generated messages.

### Step 3: Signado writes the message

Every message Signado generates follows the same structure: first name, a specific icebreaker referencing the actual signal, and a soft open-ended question. No generic praise, no "congrats on the growth." The icebreaker names a real thing that happened.

Two examples from batch 1 (anonymized):

**Signal: LinkedIn post about AI agents**

*"Hey D., saw Lev's post on AI agents silently choosing dependencies. That's a huge blindspot. What are the current approaches of your company to change this?"*

**Reply:** *"Hey Ashvin, love that you picked up on that. We see silent dependency selection as one of the biggest operational and security risks with agents..."*

**Signal: LinkedIn repost about BDR evolution**

*"Hey T., saw Justin's take on BDRs becoming 'AI operators'. That post is spot on. How are you equipping your team for that future?"*

**Reply:** Prospect compared Signado to their current tool, then booked a meeting.

### Step 4: Push leads to HeyReach

Connecting Signado to HeyReach takes one step: grab the HeyReach API key, paste it into Signado's integration settings, and save. From there, any lead with a generated message can be pushed to an existing HeyReach campaign in a few clicks — select the campaign, map the variables, push.

Signado passes the personalized icebreaker and other custom variables directly into the campaign. HeyReach runs the sequence from there.

### Step 5: Run the sequence

**Batch 1 sequence:**

1. Like post
2. Wait 1 day
3. View profile
4. Wait 1 day
5. Send blank connection request
6. If accepted: wait 3 hours → send personalized DM
7. If not accepted after 4 days: view profile → wait 2 days → end
8. If no reply after 3 days: view profile → wait 1 day → end

The 3-hour post-acceptance delay in batch 1 turned out to be the weak point. The message landed too fast and felt automated. Ashvin dug into HeyReach's own sequence timing data and rebuilt the flow for batch 2.

**Batch 2 sequence (updated):**

1. Check if connected
2. View profile
3. Wait 1 day
4. Like post
5. Wait 2 days
6. Send blank connection request
7. If accepted: wait 3 days → send personalized DM
8. If not accepted after 10 days: end

Two key changes: the warm-up steps were reordered (view before like, not like before view), and the post-acceptance delay went from 3 hours to 3 days. The goal was a sequence that looks like a real person happened to notice something, not a tool that fired the moment someone clicked accept.

Batch 2 scaled to 353 contacts. Results are pending as data comes in.

## Why it worked

* Signal-based personalization isn't a nice-to-have — in batch 1, parallel generic connect-only campaigns on the same account ran 17–21% acceptance and 0% replies. Signal-triggered outreach hit 47.8% acceptance and 36.4% reply rate. The message content did the work.
* Referencing something verifiable creates a different kind of first impression. The icebreakers in these messages named a specific post, a specific observation, a specific question — not a category of observation. That specificity is what earned replies.
* Sequence timing is part of the personalization. A message arriving 3 hours after acceptance signals automation to the reader, regardless of how good the copy is. Spacing that out to 3 days is as important as what the message says.
* Connecting your signal source to your send layer eliminates the manual step that kills most outreach workflows. When the path from signal detection to sent DM is automated and the only human input is approving the message, you can run this at scale without adding headcount
