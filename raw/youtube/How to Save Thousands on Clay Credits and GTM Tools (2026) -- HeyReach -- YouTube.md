# How to Save Thousands on Clay Credits and GTM Tools (2026)

Source: https://www.youtube.com/watch?v=JmaRNOJnjkY

Clay is by far one of the most powerful sales enablement tools in today's market. You've probably run into this problem though. When you try and scale Clay using Clay credits, it gets super

expensive super fast. So, in this video, I'm going to show you a few workaround methods you can use within Clay for data enrichment, which could save you hundreds if not thousands of dollars

depending on your scale. Now firstly before we get into the video I want to show you an example clay table which really exhibits how expensive using clay credits can be. So looking over here

I've just run one row on myself just to not give away anyone's data. We started with full name, company name and domain. I've then enriched the LinkedIn URL. So I've scraped the data from the LinkedIn

profile which costs one credit. And then we're finding work email using lead magic. That's another credit. And then we're validating email with zero bounce which is another credit. So overall

we're using six credits for this enrichment. If I just go to the column runs, we can see that for LinkedIn profile URL we're using three. For enrich person, we're using one. For find

work, we're using one. And validate email, we are also using one. So altogether this is using six credits for a bare minimum kind of enrichment. Now I just want to allude to a LinkedIn post I

wrote previously. I approximately worked out that it cost 0.0349 0349 per credit on the explorer plan which gets you 10,000 credits. Now if we do a calculation here based on our template

table if we times by 6 we get this number. So it's 0.2 so 20 the cost comes out to $2940. So that's just to row 1,000 rows using this very basic enrichment setup that

I've provided here. So this really shows how extortionate Clay can be for a very basic enrichment setup and it shows the importance of leveraging thirdparty APIs and tools and also some of the

functionality within Clay to reduce your costs. Now I also just want to quickly speak about the pricing for Clay as you're probably thinking hang on Rob we're talking about doing outbound cost

effectively and Clay shouldn't even be in our tech stack for that. Well, that is true if perhaps you want to scrape data from Apollo directly and then just chuck it into a cold email or LinkedIn

campaign. I like to do personalized hyper relevant outbound at scale. So, I'm going to be showing you how you can do that within Clay for a reasonable price without breaking the bank. Now,

just to quickly speak about the packages here, I would recommend one or two for the vast majority of people. So, it's either going to be starter or explorer. The one difference which is worth

mentioning between these two is the email sequencing integrations, the web hooks and the integrate with any HTTP API. Email sequencing is going to allow you to integrate your API directly into

a tool like hey reach or a tool like smart lead. Without this, you're not going to be able to do that. So you're going to have to manually export your leads into a CSV file. Web hooks is

running a clay table based on a trigger action or like notification inside Clay. Now, that has its use case, but you won't always be using that. It isn't a big miss. I use it occasionally. And

then integrate with any HTTP API. So, what this means is you can just integrate with any third-party tool without having a native integration with Clay. The last point that I'm going to

mention in the video, I do use a HTTP API, but that's really mainly for intermediate to advanced Clay users who are really looking to scale their data enrichment and their outbound. I think

for the majority of people you will be okay with this subscription. But just fair warning that one of the methods I'm going to be using is in this subscription, but it's only worth it if

you know you're doing you know hundreds of thousands of kind of enrichments per month. So let's get into the good stuff. We're going to outline three methods that you can use right away to reduce

your cost significantly within Clay for data enrichment and whatever function you're doing within Clay. The first one being is going to be conditional formulas. The second one is integrating

your own API key from chat GPT into Clagent and learning how to do advanced data enrichments using that API. And then finally, we're going to talk about how you can leverage tools like Appify

Marketplace and the Rapid API marketplace to get API keys or scraper APIs connected directly into your clay table that are often 5x cheaper. So firstly, let's run into the conditional

formulas. I've got an example table here which greatly exhibits how effective conditional formulas can be to reduce your cost and get the most out of claim. So what is a conditional formula? First

of all, you're probably asking a formula that permits a certain action if something is true or false. You can have and or mixed in there, but in general that's the general idea of when you use

conditional formulas. So a certain action is going to happen based on a condition that I set. Now, to really simply explain this, at the start of my table here, I've got first name and last

name conditional formula set up. These are both designed to pull data from this full name into the first name and into the last name columns because if I want to run a cold email campaign, I will

want to address people by their first name. So, I need this as a separate variable. We can do this very quickly within Clay. So, we insert column to the right. We choose formula. Now, we can

use the AI function within Clay. And this doesn't cost any money. So all I'm going to say is take the first word from full name. And as you will see, it will pull the first name for each of our

list. Very simple. This is probably the simplest conditional formula you can use. And it's a good way of starting out. What we're doing is we're using a conditional formula to manipulate the

data sets that we already have in our data. So we can organize and format it in certain ways which will help aid us in our outbound activity. I had an enrichment in here which is the LinkedIn

activity checker. This is leveraging a HTTP API. I won't go into the specifics until we get to that later. What is required for this HTTP API to work is I need the LinkedIn ID. Unfortunately, I

can't use a person LinkedIn URL. It doesn't work. The LinkedIn ID is everything after this forward slash. So this bit here in the URL slug which takes all the text after that forward

slash and in certain instances there's another forward slash at the end. So I get it to remove that as well. And as you can see we get a clean output for the LinkedIn ID. We press output is

correct. Save formula. And now this will run for each row without me spending a dime. Now our LinkedIn activity checker can run correctly. So this is a slightly more advanced way of thinking about it.

Now we can also use clay to run columns based on a certain condition. Now for certain rows we might not want to run some enrichments because they're either unqualified, maybe we don't have a

validated email. It's not worth us doing further enrichment with that particular lead. So the way you can do this with the conditional formulas is actually within an enrichment. So I'm going to

show you this href scrape. So in this instance within this table, I do not want to scrape their traffic because this is going to be used in a variable in our campaigns unless they have a

final validated email or they have LinkedIn activity in the last 2 months. So if we go to edit column here and we go back down to the run settings, you can set up a formula within each of your

enrichments in the table. And this works for anything in clay. So all I do here is only run if final validated email is not empty or recent LinkedIn activity date is within 2 months. This is a date

column. So that's very important. Obviously, we need it to be a date so the formula can actually assess the data. And then we've obviously got our final validated email as a variable. And

now our traffic column, as you can see, it will only run for the cells where we have a final validated email or we have LinkedIn activity within 2 months. Incredibly crucial when it comes to

building lists within Clay. If you're doing complex enrichments and let's say you're using, you know, 10 HTTP APIs or you're using, you know, five different clay agents, there's often no reason to

run all of those clay agents or all of those enrichments for every single one of your leads in your clay table. Often I might split leads into certain buckets where, you know, I only need to run a

certain enrichment for those leads. I only need to run a certain enrichment for those leads over there. So the conditional formulas allow us to do this without creating a million different

clay tables. I wanted to show some ways which you can actually qualify and add data into certain campaigns depending on the variables within your clay table. So here as you can see I've got multiple

different smart lead enrichments that are running here for different campaigns. I've got multiple hey reach enrichments as well and each of these columns represents a campaign in my

account. We have bespoke copy for these buckets and we want to add them to the campaigns accordingly and we also want to automate it. And the way you do this is obviously using the API key within

smart lead and clay. But the next step is using these conditional formulas in order to do this. Let's show you an example for hey reach, which is actually one of the more complex formulas I've

set up here. So only run if current organic traffic is below 4,000, traffic loss is below 1,000 or is zero, and traffic stagnation is no, and recent LinkedIn activity date is within 45 days

of the present date. This will now only run for those leads where we have decent significant traffic loss and it will only go into that campaign. So now you can see how this conditional formula is

now lead routting leads into the correct different campaign and we're not having to manually split up the CSV files. Are we actually saving money with this? No. But we're saving a hell of a lot of time

because if you're having to manually QA each list and you've got like nine different campaigns where you're segmenting leads, it's going to take you a long time to export the CSVs, set up

the filters, get the CSV, add it to the campaign, make sure the variables are connected correctly. It just doesn't work very well. Moving on to our next way to reduce costs, and that is Clagen.

Clayen is your best friend within Clay, but it will only be your best friend unless you connect your API key via OpenAI or Claude or whatever model you're using. Right. Firstly, I'm just

going to very quickly show you how to set this up within OpenAI. So, you want to navigate to platform.openai.com. You need to unfortunately have a paid account, $20 or so a month, but that

enables you to have access to the API key, which I promise you is worth the investment over the year because you're going to save so much money from those API enrichments. So, the way you want to

set this up is you go to your API keys. You create a new secret key. It will come up with a screen here. You want to copy and paste that and keep it in a safe place because once you've generated

your key, you will never be able to find it again. You can't recover the key. And then you want to go to billing. And this is actually like quite an important step because if some of you are starting out

to use an open AI key, you might not be aware of this. So, it's important to mention you need to be in usage 2 in order for it to be functional within Clay. You need to add $50 worth of

credit in order to land into usage tier 2. So, you go to your billing here, maybe just do $5010 just to make sure you're over the amount. And then you'll go back to your limits, scroll down, and

you should have automatically moved to current usage 2. Once you've got this, you can go back to Clay. So, we go back to our table here and we go edit column. Choose your model. I always use chat

GPT4 mini. It's the cheapest and for the vast majority of the tasks we're going to be doing, it's more than accurate enough. Then, what you're going to see here, it's going to be on Clay managed

Open AI account. You want to go down to add account. You want to input the name of your connection. And then you want to copy and paste your API key into this section here. And then save. And then

you're good to go. You've connected your API key. I wanted to show this particular clay table. This is something I've been working on recently with one of my clients. It really shows off the

capability of what clay agent can do in terms of advanced data extraction and scraping and hopefully it will change your mind and your perspective about how you see other data enrichment tools and

how you can actually reduce the bloat in your tech stack. This particular lead, their target is head teachers. Now they offer an automation tool which helps teachers mark faster. Right? There's a

score within the UK for schools called Offstead. It's a governing body which will score the schools on the basic criteria across four different categories. Now, one of these categories

was very interesting to me when I was doing my research and ideation for this campaign and it was a leadership and management because within this category, one of the points is teacher

satisfaction. What's linked to teacher satisfaction? Workload. So if we can highlight accurately for each of our schools what grade they have, we can make our messaging much more relevant

and we can reach out to people at the right time. So if I see that they have a requires improvement score, I know that this is going to be a red-hot prospect for me to reach out to because they're

going to be very interested about how they can improve their teacher satisfaction at their particular score. So I saw that this was publicly available data and that there was a

pattern in that every school will always have a table and they'll always have you know scrapable data which we can port back into our clay table using clay. So then we prompt this using our API key

and we can extract the four inspection outcomes with these detailed instructions. So I can include the clunion prompt. This very accurately was pulling this data for me and it was only

costing me 0.001 per row. So, this is incredibly cheap considering that this is actually quite a complex scraping task. It's got to scrape four different rows. It's got to

validate the information is correct. It's got to validate if the school name is correct based on my instructions. Now, for other scraping tasks, it will be much much cheaper. But this is a

slightly more complex one which uses more tokens. But still, you could pay thousands and thousands and thousands of dollars on a ready-made data list which has this information. But I'm doing it

from 0.001 001 cents per row. Now the second one I want to show you here which is a little bit more simple linked to the teacher satisfaction because this is like the main pain point which we want

to hammer home. This one's on teacher vacancies. So if we can see a high volume of teacher vacancies open at a school within a school term that suggests that there's a problem with

teacher retention which then suggests that teacher satisfaction might be low at that particular school and our tool might help improve the satisfaction by reducing their workload. So that's my

hypothesis here. What I noticed was most schools have a job portal on their website. You can scrape and bypass other third-party tools which offer this as a paid service. Now, there's plenty of

scraping tools where this is one of their unique selling points. But I've bypassed that and I don't need to pay for something in my text stack, which is useless to me. So, Claggent is your

number one method for reducing text stack because you can very easily scrape data. This prompt is then going to go to the school. It's going to navigate to their job portal. It's going to go

through the vacancies and make sure they've got these particular titles. It's going to count them up and return this as a number for me. It's even going to give me the titles that they're

hiring for in case that's applicable. I could be like, "Hey, you're hiring for the role of teacher of mathematics or something along those lines within my copy." It's not personalization for

personalization's sake. We are actually pointing out a painoint here. The opportunity here is endless. is essentially any data which is publicly available on the internet. Now, Clay

will sometimes have limitations with scraping big enterprise companies. So, for instance, it struggles to scrape LinkedIn. So, you're not going to be able to scrape LinkedIn. You'll need to

use other tools and bypass that. But, it can still scrape the metadata within a Google search for LinkedIn profiles. So, I can still scrape LinkedIn URLs using Clagent. Now, finally, I want to move on

to the third party tools that we integrate. Now, sometimes, unfortunately, our clay agent lets us down and it's unable to get some data points that are often behind pay walls.

A couple of tools are my go-tos. One being a next one being rapid API. So, I'm going to walk through those two alternatives. Again, it's quite limitless. Any tool that has API

functionality, you can integrate into Clay. So, just bear that in mind. Now, of course, you will have to be on that Explorer subscription, which is of course a bit more expensive. But

firstly, I'm just going to show you run ampy actor which you don't need a HTTP API because it has a native integration within clay which makes it very attractive for running certain scrapes.

This was a profile LinkedIn enrichment we were using. I needed to find the about us section, their current job duration and their LinkedIn followers for a particular client that I was

building a data list for. Now you probably saw earlier that I used the same enrichment within the expensive table and that was correct. that costs one credit per row. This is going to

cost us $5 per a thousand rows and we're going to get all of this data. You're going to get their full experience, even their interest, you know, even their profile pick URL, their experiences.

There's a huge amount of data. There's a huge amount of qualification you can do from this. And it's only cost us $5 for a,000 rows. So now I'm going to show you how you integrate this. So let me just

first quickly explain what Appify is. Appify the best way to describe it is a scraper marketplace. So developers build scrapers. They're available for sale in terms of usage or subscription. You

choose what you want. So here you can see we have a Google map scraper. We have a website content crawler. We have a Tik Tok scraper. In our instance, what we care about is a LinkedIn profile

scraper. So what you want to do, sign up to Appy. You get $5 free. So we're going to want to type in LinkedIn profiles. And I've chosen this particular scraper here. You can look at the information,

the kind of detail that you're going to get before you start investing in the tool. It all looks very complicated at this point, but it's actually really, really simple when you get to running

it. So, to run it in clay, what you're going to want to do, you want to save this as a new task. You save as a new task. Continue. I've already got a task for this, but I'm just showing you for

the purpose of completeness. You're then going to go to your save tasks and it will be saved in here. So, I've got one here. Then, when we go back to Clay, so I'm just going to show you by creating a

column. So, you choose run ampify actor. So, what this is going to enable you to do is run that particular actor within Clay. You choose your API, then you'll be able to find the scraper that you

just saved as a task. So, in our case, it's a LinkedIn profile scraper. And now we just need to input our input data. And by the way, this works for all actors. So, once you learn it once,

you'll never have to learn it again. You go to the JSON object here. What we actually want to do is we want to put like an example in here so we can see where we'll need to put the data when we

export we copy and paste the JSON object back into Clay. So I'm just going to put Roblo here. And then when I swap to JSON now we have a username column. So I can just copy and paste this over. We go

back to ampify actor. We put it in the input data. And then what we want to do is remove the username. So we can find LinkedIn profile. And now we're good to go. We can save this. And this is now

going to run like it has done here for each of them rows. And we can export any of these data points as a column. So whenever I need to find data which I know is going to be behind some awkward

payw wall or maybe I need to get a big chunk of data. So for instance with this ampify actor, the reason why I use the actor is cuz I can't use clay on a LinkedIn profile. So my next best

alternative is to use this scraper. Now moving on to rapid API. This is a similar process but with rapid API we will need to integrate the HTTP API. is interesting to learn how to use this

because the power of the HTTP API in clay. When you get up to enriching 50,000 leads per month and above, this is going to save you a huge amount of money. Rapid API is a API marketplace

for developers. So essentially, people resell subscriptions to API access to certain tools or they build API access or they build a scraper, they build a tool and they sell the API for a

subscription per month. So the really really cool thing about rapid API is you can get access to tools like hrefs, semrush or tools like this without actually having to have access to the

tool or pay a monthly subscription. You can pay for the API specifically for the data points that you want and then you go from there. So how do you use rapid API? Relatively simple again but it's a

bit more complex to set up than what we were doing with ampy. So in this case I'm going to show you one I do with similar web which is like an intelligence tool. a competitor

intelligence tool. The one I am using at the moment is this one here by Pinto Studio and I am using this get analytics v1. So the thing we care about here from an HTTP API perspective. So integrating

this inter clay is this body here. So what we're going to want to do is we're firstly going to want to subscribe to the tool. So you go to the API so you can test it for free and then you can go

for the paid subscription. So firstly you just want to test the endpoint. So I've just tested it. Now, this will show us, you know, the data that we're going to get. So, as you can see, we get a

description, we get the country, where the traffic's coming from, we get their split between social, paid, referrals, mail, referral, search, direct. Now, of course, take this with a slight pinch of

salt. It's not going to be 100% accurate, but it gives you a rough indication. We're getting a huge amount of data here. So, how do you use this? So, once you've paid for it, there's

nothing you really have to do. This only costs $10 for 10,000 rows. Now, I tell you that Semrush API, it costs 1,000 per month just to access their traffic analytics API. So, this puts it into

perspective how cheap you're getting this. The first thing we're concerned about is the URL, right? So, we want to copy and paste this. You want to go back to your table, and here is the example,

but I'm going to redo an example just to show you. So, we're going to go here, and then you're going to type in HTTP API. We're going to go to configure, and then we want to go method is get. So

whenever you're retrieving data from somewhere, it's usually get. It sometimes can be post though, so be a little bit careful. You can always find that detail here. So it will tell you

what the request needs to be. And our end point is going to be that URL. There's one important thing to note here though. We obviously don't want it to run for Amazon for each row. So we need

to replace this with a clean domain. So we've already nicely got our website enriched in this particular clay table. So we're just going to go website. Now, this is going to run dynamically much

like I showed you for Appify, much like I showed you for Clagium, right? It's going to run dynamically for each row. We then want to go back to Similar Web and we want to input these headers. I'm

not going to show you this exact process, but literally what you need to do is just copy and paste each section. I'll show you it for one. So, we want to go to headers, key value pairs. We want

to name that and then go back to Rapid API. This is going to be the host. So, we copy and paste this back. And we want to do the same for the API key. So, we add a new header here. There's a bunch

of other settings that you can do here. So for instance, you can actually choose the values you want to return. This is sometimes useful when clay has like a certain data memory limit on a cell. So

sometimes you can actually enrich too much data. What you can do here is you can add tags so you only pull certain data. We won't go into the nitty-gritty, but it's just to highlight actually how

much is available within these settings and how customized the HTTP API can be. And just to go back to our finished integration, just so you can see the finished work here. You can see here

that all we had to do was integrate our API key, our host, and that URL with the variable and the get request. And now this will run across all of our rows, right? So finally, what do we do with

this data? We now need to put it into a campaign. So I'm going to show you how you can seamlessly add these leads once you've data enriched them for a very cheap price and add them into a tool

like hey reach. So what we want to do is we want to go to column add enrichment. We want to choose hey reach. Fortunately hey reach has a native integration so we don't have to be messing around with the

HTTP API. So we can add lead to campaign. At this point we want to choose a campaign that we add it to. I'm just going to choose a random campaign just to show you. We can now map first

name, last name, person LinkedIn URL. We can add any other data points we want. As you can see these are already nicely inputed for us automatically by Clay. If we want to add custom fields, we can

here. So if for instance I wanted to add traffic, we go like that. I can get current monthly traffic. Bang. We've got traffic as a variable which is within our clay table which be imported into

hey reach. At this point we want to press save and we can run it on a row. So just to show you that it's working. Let's press save and don't run. And then I'll just choose one particular row to

run this on. And this will now be added to the campaign as you can see without us doing anything. is now going to be integrated moving forward. So when we add new data into these tables, it's

automatically going to run and put those leads into our Hey Reach campaign. For just a bit of context of where you find this API key, if you go to your settings here, you want to go to your Hey Reach

API within your integrations and get an API key. You then copy and paste your API key, take it back to Clay and away you go. So let me show you the example I showed you earlier with the vacancies

enrichment for one of my clients. We've got an 18% message reply rate for this campaign. 30% connection request rate. So, it's been really successful for us. And this whole process is automated

thanks to using Clay and Hey Reach together in tandem. So, we can create obviously this personalized copy. I saw that you had open vacancies at the moment and then our CTA is a short video

that works. Now, we can obviously reference the open vacancies because we've done that client prompt. So, this really opens up also your ability to write hyperpersonalized campaigns at

scale and you haven't had to break the bank to do it. So, now you've learned how to save a ton of money using Clay. Click the video to the right of me where we walk through how to set up an

end-to-end system using Clay Natn and of course Hey Reach to scale your outbound without lifting a finger.
