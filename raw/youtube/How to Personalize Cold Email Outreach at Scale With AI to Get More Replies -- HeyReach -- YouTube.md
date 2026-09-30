# How to Personalize Cold Email Outreach at Scale With AI to Get More Replies

Source: https://www.youtube.com/watch?v=OMCJMlZhoEE

When you think of AI personalized outreach, you probably think of something along the lines of, "Hey, first name, I saw your profile and I thought our product name would be

relevant for company name." Now, this just doesn't cut it in 2025. People can sniff AI copy from a mile off. But the truth is, there really, really is a way you could use AI personalization in a

scalable way to get amazing results. And I'm going to walk you through my exact methodology in today's video. Using this AI personalization method, I've sent around about 4,000 emails, got 51

positive replies, and booked 15 meetings in the space of a few weeks. So, let's begin with the Clay table. Now, I'm obviously using Clay for this because it has native integrations. It's very

convenient. It obviously has Clay agent as well, which is built into the platform. So, you can easily prompt for web surfing or for prompting. It's just very quick. So we have a range of

decision makers here who are relatively industry agnostic. I did specify a range of industries which would be relevant to the service that we are offering which is SEO services. Now for these leads I

did some brainstorming and I figured that what people mostly care about as like let's say like a positive leading indicator for their website performance is their traffic. So, if I can scrape

all their traffic, but also if I can scrape their traffic from, let's say, 3 months ago, I can work out if they've lost traffic, if their traffic has remained stagnant, if they've got low

traffic or if they've grown traffic. So, there's four buckets there. This is really effective because it shows we've done our due diligence and we've searched about the prospect before we've

sent them an email. So, we're actually reaching out to them with a data point which signifies a painoint rather than just assuming a painoint which often people do in cold email copy. So, I'm

not going to go into extreme detail with this clay table. I'll of course include the template within the description if you want to set up something similar. Starting off with the traffic. So, I'm

using rapid API and it's scraping similar web. And what this does is it gets the traffic from this API key which is publicly available. You pay a monthly subscription. and it's using a HTTP API.

I also have a LinkedIn activity checker here. This is because I will be launching a campaign with hey reach using this same methodology. You can see the type of data points we can get from

the similar web scrape here. So we got traffic 3 months ago, 2 months ago, 1 month ago, their total visit count, their organic visit share. So we can work out what's organic and what's paid.

And then we formulate this into a nicely formatted number. And we also can get their paid search traffic, but that's not applicable. So now we can identify the four buckets that we highlighted

earlier in the video and we can use the prompt for each lead to dynamically create copy based on that variable. So I created this prompt and all it does is it summarizes their business from their

website. So it just goes to their website. It grabs a couple of sentences for me just to give the AI enough context to insert this into the copy. Then we have the cold email copy prompt.

Now, what I'm using for this is I've obviously got my API key set up here. I'm only having to use chat GPT for OM Mini. This is by far the most cost effective and I actually think for most

tasks within Clay, it does a better job than even some of the more expensive models. Now, let's go through the prompt section by section so you can really understand how I've got this to work

dynamically for each of the leads in this clay table. Now, immediately in the first section, I'm always defining the role. So, this is like the introduction. This is you telling the AI what their

job is, what they're an expert at, and giving it some small bit of context as to what you're trying to achieve with the copy. So, that's how I approach this introduction. And then, because there's

a lot of dynamic variables here, I want to make very clear which variables are going to be used within this clay table. If you're not aware, all of these sections here are columns within my

table. And the way you can add a column is just doing a forward slash and then you can select whatever variable as you can see here their LinkedIn ID or their location. I can insert this as a prompt.

So this obviously works the same way as stuff works in N810. So it will dynamically change the prompt depending on that row. So I've initially just told the AI right this is all the data points

that you're going to be using within this prompt to make it super clear. And then this whole section here I'm defining the buckets. So, it's also important to mention here is that your

data variables that you're using, you want to turn them off so Clay doesn't think they're required for the prompt. So, now we go into each of our buckets so we can explain exactly what leads

should go into what buckets. So, this is arguably the most important part of the prompt to really clearly communicate to the AI when it should be dynamically changing the copy. Initially, here we

have traffic stagnation. So I've got a row in this table which is a formula and whenever it notices that their traffic 3 months ago is within 500 it will say their traffic has stagnated. We then

have traffic loss which again is like another formula here. It minuses their current traffic from what their traffic was 3 months ago to work out if they've lost traffic. This is actually the

highest priority I have here because I think it's the strongest signal. So I make that clear to the AI as well. We also have the total visits count here. And this will be able to highlight. Now,

if they have low traffic, now I'm defining anything below 3,000 as low traffic. This is probably the weakest signal here because for certain different niches, low traffic is going

to mean something different, right? So, for a very specific B2B SAS business, which has like 2,400 traffic, that could actually be really high traffic for that niche. So, it isn't perfect, but it

still works relatively well, and it helps us maximize our total lead list. We then also have traffic loss again, but this is because if there's a negative value, we know that they've

grown traffic. I'm saying here that this is the fallback copy because a lot of companies will have grown traffic, but I can still reach out to them and we can still use that as a variable because it

shows that we've done research on the business. And I'll show you the copy and how I've spun this later down in this prompt here. We are just basically taking that company description which we

have got the AI to do based on the website and we are asking it to summarize that particular business. So manufacturing firm, IT service provider, marketing agency, etc., etc., etc. It's

going to quickly summarize what that type of business is. I'm also explaining here to use the summary only once or twice. If you just ask it to always include the personalization of the

industry, it literally might include it at every single point it can within the copy. We obviously only want to dynamically bring this in at relevant points and we also don't want to bring

it in just for the sake of it, right? It's got to be positioned correctly so it looks like we've reached out manually to this person. Again, just giving it some context on the tone here and how I

want it to write. And now this again is a very important part. So this is actually arguably where most people go wrong. They'll do a really detailed prompt like we've done above, but

they'll expect the AI to just write a really good email and to be able to keep consistency for each specific lead. The truth is AI is too far away from that. So, we still need to use a patternbased

approach in order for the AI to achieve consistency. So what I've done here is I have written out the buckets again and I've written personally an example template piece of copy for the AI to

adapt from based on the current situation and based on the variables it sees. So as you can see here, we're not going to go through each of the copies here, but notice your site has lost

around about this traffic. We've correlated this with a similar trend we've been seeing with other short business summaries. So that's when it's going to bring in that context about the

business. This particular audience seems to be moving from Google to LLMs for online searching, right? Can I send a short video showing how we've helped a similar business increase organic

visitors by improving visibility on chat GPT? We've got the observation here, the icebreaker, why we're reaching out. We've got the pain point, why this could be happening, and then we've also got

the CTA here, but with value prop. And then the copies follow similar structure, but depending obviously on the data point, we need to adjust the copy slightly so it makes sense. And

obviously we've got our fallback copy at the bottom here. Notice your site's organic traffic has grown over the last 6 months. Nice work. So we're actually pointing out, right, we've done some

research on your business. We've seen that your traffic has grown. However, for these types of businesses, we're seeing more users turn to AI tools over Google. Future proofing your content for

LLMs can help you keep that traffic growth compounding. Can I send a quick video? And then finally, at the bottom of the copy here, we have the output instructions. So I'm telling them to

keep it under 30 words. No explanations, no metadata. Keeping it professional, confident language, vary phrasing slightly between outputs to sound natural and human. Always include light

personalization by summarizing what the business does, but only where it fits smoothly. And then I'm saying make sure you format like a normal email and use paragraphs between sentences because we

obviously want this email to be inserted straight into our cold email or LinkedIn automation tool. So we don't have to do the formatting ourselves manually, right? Because obviously that would kind

of defeat the point of using AI for this. So now I can show you some of the outputs. Here we have our email copy here. So hey guy noticed your site's organic traffic is around 844 which is

quite low for most consulting and technology service for SMBs. This does correlate with more users going to chat GPT to search online. It's becoming increasingly difficult to grow traffic

through Google search. We're helping similar businesses grow by improving visibility in AIdriven search platforms like ChatGpt. Can I share a short video on how we've done this? Let's just go to

another random one. So this is lost traffic this time. Notice your site has lost around 2,800 visits over the last 6 months. We've correlated this with a trend where many software companies for

manufacturers are seeing a shift in user behavior moving from search Google to LLMs for search. Can I send a short video? So we know now and I've gone through these individually right before

I sent this campaign because it's very important to quality assure. So just to give you context of when you're doing these AI prompts, you should be iterating consistently. It took me a few

hours to write that prompt because I was noticing mistakes. So, you initially write your base prompt. You run it for a few rows. You see the output. You improve the output. And you need to do

this at least three or four times to really nail the prompt. And then you want to run it on at least, let's say, like 500 rows and meticulously check through these rows because you don't

want to be losing out on some of that sending volume. Basically, sending trash AI emails to people and them noticing that it's written by AI. So, I would say these emails do a very good job of

sounding human, but they're also dynamically changing based on the specific business and the specific bucket which I've put them in, but they're not veering too far away where

the copy is changing too much each time. We're having too much inconsistency. When you're sending thousands of emails to people, you need to have consistency. Now, if you want to use this AI prompt,

I'm going to include the link to the clay table within the description of this video. It will include all the enrichment rows. You'll be able to get all the prompts that I've used and apply

that to your own business. Just please note that you will have to adapt these prompts to your specific use case, and you may need to purchase certain tools that I'm using in order for the clay

table to be functional. Now, you're probably interested about what type of results this can achieve and how do I now set this up in my email sending tool and in my LinkedIn automation tool. So,

initially I just want to show you some of the results we've achieved on Smart Lead. As we can see, we've contacted around 4,000 people. We've got a really decent reply rate, but this is including

OOS's just to mention here. So, it's not always people not interested or positive replies, but we got 51 positive replies there. This is really good for like cold email standards today. It's dynamically

working for each lead now. So, I can literally just put leads into this campaign and the copy will be written for me straight away. All of those enrichments will run and then they'll

automatically be added to the campaign through an API connection. So, moving on to how you set this up. Now, I can actually show you from an import perspective if you're going to do this

through a CSV. If we go here and we just go save here, the beauty of this method is we don't even need any of these variables because it's the the copyy's already been written. We actually only

need this email copy variant and we need the final validated email. So, we're just going to put that as email. So, we would just press save next here and then run this. Right, these aren't going to

import because this is already a list that I've already imported into the campaign. But, just to show you how simple it is once the AI copy has been written and it's ready to go. Now, if we

go to the sequences here, I've just got the subject line, traffic, and email copy. That's literally it. And this is obviously going to be dynamic for each of our decision makers. Now, if I go to

this tab where I've got a few examples of this. So, I just added the examples that I just previously showed you in the clay table. As you can see, the copy is bespoke each time, and the sentence

structure is even different. Sometimes it uses multiple sentences, but it is still using the context of our template emails that we gave. so it's not veering too far away. Another reason why this is

really good for email is you don't really have to worry about spin tags. Your emails are going to be unique each time depending on the lead and it's going to actually have unique structure

as well. You're going to have very normal human sending behavior patterns with this as long as you're not sending loads and loads of emails in a short period of time. Now, finally, I haven't

actually set this up in Hey Reach yet. I'm going to do this now live just to show you how you would do it within Hey Reach, right? So firstly, we need to obviously start with our lead list. So

let's add the leads. We're going to import from CSV. We're going to continue. We're going to upload a spreadsheet. And we're going to choose that table that we've just exported from

our clay table. You can see here it's already mapped the column. So we got person LinkedIn URL, first name, last name, location, company description, and company name. All we need to do here is

add a custom variable. And we just need to find our cold email copy. So email copy here. And then we're just going to name this email copy. so it appears as a personalized variable when we come to

create our sequence. So we're going to select the list we're going to port that to which is obviously SEO leads and we're going to import those leads into the campaign. So now that's done. We

have all our leads into the campaign. We're going to go back to our campaign over here and we're going to find our new campaign. So the SEO video analysis here and then we're going to select SEO

leads. So now our leads are imported into this campaign. We're going to choose the senders. I'm going to just choose myself for this. And then we're going to go to sequence. We're going to

continue. Send connection requests. I like to do blank connection requests. You get a better acceptance rate. So I leave all of this blank. So I just save that. Then I always wait one day at

least, sometimes even two to make it look like normal human behavior. And then we're going to add as send message in our tree. And then what we're going to do is just put email copy. And our

fallback message. I would just say something along the lines of like thanks for connecting. And then what that means is if they're like a really good lead and they've connected with me, I can

manually send a message and it obviously doesn't ruin my reputation with that particular person. So we can save that now. So it works exactly the same way as we showed you on Smart Lead. And then

you can add as many follow-ups as you like. I usually only do one follow-up on LinkedIn just cuz it's a bit annoying if someone's constantly following you up in your DMs. And then obviously you just

review and launch after this. We're just going to end these actions here just so I can show you. Continue. And then we can launch the campaign. Now, that was just the personalization part. You're

probably now wanting to see our full end-to-end lead generation system. Click the video to the right of me and we'll go through our exact step-by-step lead generation system so you can book

thousands of meetings for your business. See you over there.
