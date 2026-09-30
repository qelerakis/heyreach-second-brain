# Hiring campaign that generates 100s of replies on autopilot

Source: https://www.heyreach.io/outbound-playbooks/build-hiring-campaign

Summary: Step-by-step guide to building a hiring campaign that monitors job postings, finds 5-6 contacts per company, and automates outreach through HeyReach and email.

Timing is everything in outbound sales. And there's no better signal than when a company actively hires for roles that indicate they need your solution.

Hi, I’m Matthew Coleman, GTM Engineer at [LevelUp Leads.](https://levelupleads.io/)

Today, I'm breaking down our Evergreen Hiring Campaign—a system that connects us with thousands of prospects every month and generates hundreds of replies automatically, without manual intervention once it's configured.

## The Foundation: Setting up job posting signals

The core of this campaign is a job hiring table powered by signals. A signal continuously searches for new job postings each month, automatically feeding fresh data into your table and subsequently into your HeyReach and email campaigns.

Here's how to get started:

### **Step 1: Define your ICP**

Identify companies that match your ideal customer profile. Filter by:

* Industry
* Company size
* Location
* Other relevant firmographic data

### **Step 2: Target relevant job postings**

Search for job titles that signal buying intent for your solution. For us at LevelUp Leads, companies hiring SDRs or BDRs represent perfect timing—they're clearly investing in outbound and likely need the tools and services we provide.

## Cleaning your data for deliverability

Raw job posting data needs refinement before it hits your campaigns. Here are the critical cleaning steps:

### Standardizing job titles

Some job titles come through messy—think "Business Development Representative BDR B2B SaaS Sales Hunter." If that lands in an email, you're headed straight to spam.

**Solution**: Use formulas to standardize:

* If title contains "Sales Development" → SDR
* If title contains "Business Development" → BDR

This keeps your messaging clean and avoids spam triggers.

### Normalizing company names

Company names often pull through with inconsistencies—extra characters, odd formatting, or legal suffixes that look unnatural in outreach.

**Best practice**: Run a normalization formula to clean company names before they populate your email templates.

### Trimming first names

First names frequently include initials, parenthetical notes, or extra characters (e.g., "Abdul Q" or "Sarah (she/her)").

**Formula approach**: Remove anything after the first space. This ensures your personalization tokens stay clean and natural-sounding.

## The multiplier effect: Finding multiple contacts per company

Instead of reaching out to a single VP of Sales, we identify multiple relevant stakeholders at each hiring company.

Using [Clay](https://www.heyreach.io/integration/clay)'s "Find Contacts at Company" feature, we search for:

* **Seniority levels**: Mid to senior-level decision-makers
* **Relevant titles**: Marketing, Sales, Revenue Operations
* **Exclusions**: Engineering, Consultants, and other non-relevant roles

The result? When we identify a company hiring an SDR, we automatically find 5-6 relevant contacts across sales and marketing who might be involved in the hiring decision or related initiatives.

This dramatically increases our chances of getting a foot in the door.

## Personalization at scale

Once our data is clean and contacts are identified, we use Octave to analyze both the job posting and the prospect's LinkedIn profile, generating personalized messaging for each contact.

## Automation workflow

The final step: Everything flows automatically into:

1. **HeyReach** for LinkedIn outreach
2. **Smartlead** for email campaigns

Since the entire system runs on signals, new job postings are discovered, contacts are found, data is cleaned, messaging is generated, and outreach is sent—all in the background, automatically.

## Results

This evergreen hiring campaign allows us to:

* Connect with thousands of prospects monthly
* Generate hundreds of replies automatically
* Engage companies at the perfect moment (when they're actively hiring)
* Scale outreach without increasing manual workload

The key is setting it up once correctly, then letting the automation handle the rest.

‍
