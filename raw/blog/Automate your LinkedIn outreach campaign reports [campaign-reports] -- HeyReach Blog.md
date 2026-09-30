# Automate your LinkedIn outreach campaign reports

Source: https://www.heyreach.io/blog/campaign-reports

Summary: Stop spending Mondays on manual reporting. Automate LinkedIn outreach campaign reports with HeyReach and n8n, send weekly performance summaries effortlessly, and track every reply in one place.

Weekly reporting shouldn’t eat up the first hour of your Monday. But for most teams running LinkedIn outreach, it does.

Opening spreadsheets, exporting stats, checking individual campaigns, trying to remember last week’s numbers, and then writing the same client email again and again.

You can automate all of that.

With [HeyReach’s native nodes in n8n,](https://www.heyreach.io/blog/linkedin-automation-n8n) you can build a workflow that automatically collects campaign performance, organizes it in Google Sheets, and prepares a ready-to-send email draft every week. And if you want something even smarter, you can extend that workflow to include every person who replied to your outreach in the last 7 days.

**The result?** Your reporting runs quietly in the background while you sleep, and the only thing you do on Monday morning is: open Gmail → review → send.

I’ll walk you through both versions of the workflow – starting simple, then leveling up. You can follow it on video, read the article and [grab the template.](https://www.heyreach.io/n8n-templates/automate-heyreach-reports-n8n)

## **Why does automating LinkedIn outreach reporting work so well?**

Teams and agencies that run outbound usually have three types of stakeholders:

* someone above them who wants regular summaries,
* teammates who rely on numbers for planning, and
* clients who expect weekly updates “sent by Monday morning.”

The workflow below solves this neatly. It:

* runs automatically every Monday at midnight,
* pulls all campaign performance without manual exports,
* creates a fresh spreadsheet row with weekly stats,
* drafts a complete email with pre-filled recipients,
* and (in the advanced version) adds a list of all leads who replied that week.

It’s the same output as doing everything manually – only it happens at 00:00 while you’re asleep.

## **Two versions you can build**

To keep things structured, let’s go through these two workflows separately.

### **Version 1 — Weekly performance summary**

A simple, reliable report that includes:

* Lifetime campaign stats
* Last 7 days of results
* A prepared email draft
* A weekly row added to your reporting sheet

### **Version 2 — Weekly summary + leads who replied**

Everything from Version 1, plus:

* A separate sheet created every week with replied leads
* All their data stored in one place
* Their details inserted directly into the email draft

Most agencies end up using Version 2 because it provides “numbers + conversations,” which makes client communication frictionless.

The core workflow first. 👇

## **Version 1: Weekly outreach report (core workflow)**

## **1. Trigger the workflow automatically every Monday at midnight.**

Set up a schedule that fires once per week – the cleanest rhythm for outbound reporting. [The n8n schedule node](https://www.heyreach.io/integration/n8n) lets you configure this using a cron expression.

* **Trigger:** Every Monday at 00:00

**💡 Why Monday?**

You always start the week with the previous week fully closed.

## **2. Pull total campaign stats from HeyReach.**

The first part of every weekly report is context: performance from the beginning of time.

Using HeyReach’s official n8n nodes, you can retrieve:

* total invites sent
* overall acceptance rate
* cumulative replies
* total messages sent
* any channel-specific metrics you use

No HTTP requests, no JSON bodies – just choose the “Get overall stats” operation and connect your account.

## **3. Define the time window for weekly stats.**

To calculate weekly performance, you need two dates:

* **end date = right now**
* **start date = 7 days ago**

These values are easier to reuse if you store them as variables. n8n’s built-in date library allows subtracting days directly, so if you ever want a 14-day or 2-day reporting window, you just change the number.

## **4. Pull last week’s stats.**

Use the same [HeyReach](https://www.heyreach.io/blog/heyreach-review) node again – this time referencing the start and end dates you just defined.

This gives you your weekly results:

* invites in the last 7 days
* accepted connections
* sent messages
* replies
* reply rate
* LinkedIn interactions for each campaign

This snapshot becomes the main body of your Monday report.

## **5. Generate the weekly email draft automatically.**

This is where the workflow becomes genuinely useful.

Using Gmail’s draft creation node, you:

* build a subject line based on the reporting date,
* insert weekly and total stats into a prewritten template,
* add client emails to CC or To fields,
* and create a polished draft that’s waiting inside Gmail before you’ve even had coffee.

**There’s also a neat formatting trick:** ISO timestamps include a “T” between date and time. Splitting by "T" removes the time portion and keeps only the date, giving you a cleaner subject line.

## **6. Append weekly stats into your spreadsheet.**

Finally, the workflow records everything in a dedicated Google Sheet.

Each Monday:

* a new row is added
* start and end dates are logged
* weekly metrics are stored
* lifetime metrics are optionally included

Over time, this becomes the master file for trend tracking, forecasting, and client transparency.

That’s it – your base workflow is complete.

## **Version 2: Weekly report + list of leads who replied**

The second version builds on the first, but adds one powerful feature: the ability to track exactly who replied during the last 7 days and store their details in a dedicated tab.

This is extremely useful for:

* agencies reporting to clients
* sales teams reviewing weekly engagement
* internal dashboards
* tracking follow-ups
* validating outreach quality

Let’s break down how it works.

## **1. Prepare additional variables.**

To make the workflow predictable, you create variables for:

* spreadsheet ID
* main sheet name
* newly generated sheet name for this week’s replies
* date formats with and without timestamps

This prevents issues with dynamic names failing in downstream nodes.

## **2. Create a new sheet for this week’s replied leads**

Every weekly cycle generates a fresh tab inside your spreadsheet.

**Name example:** Leads — 2025-11-13

If the sheet already exists (because you’re re-running tests, or activated the workflow twice), n8n simply returns an empty output and moves on without throwing an error.

To avoid breaking the workflow, be sure to enable “Always output data.”

## **3. Add header columns (only if the sheet is new).**

Because sheet creation doesn’t populate headers, the workflow needs to insert column names manually.

A simple IF/Else logic checks:

* If a sheet was created → append header row
* If it wasn’t → skip to the next step

Columns often include:

* first name
* last name
* job title
* company
* LinkedIn profile
* email
* message status
* timestamp

This gives every weekly tab a clean structure.

## **4. Retrieve weekly and total stats again.**

These nodes appear again because the workflow branches and merges – stats need to be available to the final email node.

## **5. Fetch all campaigns.**

The workflow retrieves a collection of all your active campaigns.

Depending on how many campaigns you run, this list might have:

* 3 campaigns
* 10 campaigns
* 40 campaigns

Each campaign is processed individually next.

## **6. Split campaigns and retrieve leads campaign-by-campaign.**

n8n treats each campaign as a separate item and fetches all leads associated with it.

For each lead, the workflow pulls:

* profile metadata
* message history
* messageStatus
* timestamps
* and any other stored attributes

The key field here is **messageStatus**.

## **7. Filter only leads who replied in the last 7 days.**

This is the heart of Version 2.

When messageStatus equals **"MESSAGE\_REPLY"**, the workflow knows that the lead responded within your reporting period.

Only these leads pass through the filter.

It’s normal for this to represent a small subset of total leads — especially in test environments.

## **8. Add replied leads to the weekly sheet.**

Each lead is saved into the newly created sheet for that week.

This is useful for clients because they get a transparent look at:

* who responded
* what their role is
* where they work
* how they can be contacted
* when the reply happened

It’s also incredibly useful for sales teams reviewing follow-ups.

## **9. Format a clean, human-readable lead list.**

To insert lead details cleanly into your email draft, the workflow uses a code step that transforms raw JSON into formatted text.

The output looks something like:

*- Jane Smith (Head of Growth, OrbitLabs)*

*LinkedIn: https://linkedin.com/in/...*

*Email: jane@orbitlabs.io*

This list can sometimes be long, but that’s exactly what clients want to see.

## **10. Generate the enhanced email draft.**

This draft now includes:

* weekly stats
* total stats
* AND a fully formatted list of replied leads

You can send it directly, or customize it slightly and forward it to clients or internal teams.

The workflow does 95% of the reporting work for you.

## **Common mistakes to avoid when building this workflow**

Even though this automation looks straightforward, there are a few small details that can break the workflow if you miss them.

Here are the most common pitfalls and how to avoid them:

### **1. Forgetting to enable “Always output data” when creating the weekly leads sheet**

If the sheet already exists, n8n returns an empty output instead of throwing an error. Without this option enabled, the workflow won’t know how to continue and will stop mid-run

Turning it on ensures the workflow keeps flowing even when nothing new is created.

### **2. Using dynamic sheet names directly inside nodes**

Dynamic names like “Leads – 2025-11-13” can sometimes resolve, and sometimes fail silently.

**The safer approach:** generate the name once, store it in a variable, and reference that variable everywhere else.

### **3. API rate limit errors from pulling multiple campaigns at once**

HeyReach’s API is fast, but if you loop through many campaigns in the same second, you may hit a “too many requests” block.

Enable retry-on-fail with a short delay (e.g., 2 seconds) to make the workflow more resilient.

### **4. Missing fields in the Gmail draft due to incorrect mapping**

If a field is missing in the email, the cause is almost always the same: **the Gmail node is using a field from the wrong branch or the wrong item index.**

Testing each node and checking the output JSON once before activating solves this entirely.

### **5. Seeing empty weekly reply tabs and thinking something is broken**

If no one replied during the last 7 days, your weekly sheet will be created but remain empty.

This is expected behavior – **not an error.** The workflow is still working exactly as designed.

## **Where can you take this next?**

Once this workflow runs automatically, teams usually start enhancing their reporting stack with:

* monitoring systems for delivery drops
* [Slack](https://www.heyreach.io/integration/slack) alerts for sudden changes
* Workspace-level consolidated reports
* CRM syncing
* deeper segmentation (e.g., replies by campaign type)
* enrichment steps before adding leads to sheets

But the automation above is the foundation. Once this is in place, **your weekly reporting practically runs itself.**
