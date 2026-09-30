# How to Get Unlimited Leads on LinkedIn Using N8N + Clay.com + HeyReach

Source: https://www.youtube.com/watch?v=dDTOSfTQGiw

In this video, I'm going to share with you a step-by-step process of building an automated system that can run 247 and can generate potentially an unlimited number of highly qualified LinkedIn and

email leads without almost no human intervention. Because after sending many millions of LinkedIn DMs and emails in the last 7 years, I came up with this system that helps me on a daily basis.

So, first I'm going to explain the whole system and what we're building and then I'm going to explain all pieces and walk you through it so you can replicate it on your end. First of all, I'm going to

explain the whole system, how all the parts connect with each other, how data is flowing. So you'll have clear understanding how everything is working and you'll be able to replicate this

system for yourself and create a lean mean lead generation machine that can generate unlimited number of leads because it can run on autopilot 24/7. First things first, we need an input. We

are going to follow the principle of starting with companies. So we're going to qualify some companies and in a moment I'm going to explain an example that we're going to use for this

exercise. We can use sales navigator to find companies and qualify them or maybe we can use clay and it's company search and find suitable companies. Once we do that we are going to find inside clay

people from those qualified companies and also enrich their information and use waterfall for trying to find their valid business email addresses. Inevitably, we will end up with two

groups of people with and without valid business email addresses. And we are going to utilize two channels for outreach, email and LinkedIn. Those people with valid email addresses will

go to smart lead. You can use any other platform of your choice for cold email automation. Everyone else are going directly from Clay to Hey Reach. And then we need a central place to act as a

glue in between all of these platforms that don't have necessarily native integrations in between themselves. We are going to use N8 for that. You'll be able to download this workflow and

import into your N8 account and replicate everything yourself. Then we don't want to leave any leads behind. That's why we're going to push those people into Hayreach. And hey is a great

platform that allows us to connect a lot of senders and scale LinkedIn outreach. So we can cover and overcome this usual bandwidth issue with LinkedIn. So bounced people will go to hreach. Also

people that receive all of the steps in our sequences, email sequences, but they didn't respond to us. Then they are going to hreach as well. And also it would be a shame not to save all the

relevant information about these people in a ser of our choice. In this case, we're going to use Hopspot. And then to be able to act quickly when we receive a reply from either channel, we're going

to use Slack as to just get notifications. Let's start with the idea and the practical example. I'm going to use an amalgamation of different scenarios that we're using for different

clients. The common denominator between them is that they're doing something regarding digital marketing. One qualification step for us is to see if a certain company is running ads. If we go

here and let's say I took mental health care businesses and mindfulness businesses just a small fraction or a small tiny batch of companies and I've added websites of those companies in

clay. Then we want to enrich information about these companies. We can use clay's builtin enrich company option to get company name, LinkedIn, Facebook, all social platforms urls of those

companies. Now, what is the easiest way to find out if a company is actually running ads? We have three major publishers. We have Meta, LinkedIn, and we have Google. We will cover Meta here.

If you're interested, just drop a comment and I can cover all other relevant publishers. So, for Facebook, if we take a look at the company website, every page, company page on

LinkedIn has this about section. And inside this about section, we have page transparency. And we can see this sentence here that says this page is currently running ads. This is really

helpful. We can use this to determine automatically if this is qualified business for us. So we need to get this Facebook business profile page to get this information and then this is just a

formula that says just add this string at the end of the URL. And then we are using Zenro scraper to get this body text from this page. And we have a formula here that says does this body

text includes this page is currently running ads sentence. If it does then it's true. So they're running ads false if this sentence is not contained. And also what we can do in case of meta is

pull this information this page ID unique page ID for this business. So what we can do then is to use meta ads library. The good thing about this meta ads library that in parameters of URL we

can set page ID. So unique ID and instead of just searching for this name of the company page if we put this unique URL that we extracted from their page we have all information about all

of their ads. In theory, everything that we see here, all the information including visuals, we can pull with certain actors and then we can push some information in different tables and

maybe we can use agent or chat GPT to prompt to summarize this information to find patterns. So, we can use that in our copy and mention, hey, I've noticed that you're running the same ad for this

long or whatever based on our offer. Basically, we do that. We qualify those companies and we find people. We can use filtering just to first see all companies running ads and then find

people from those companies using Clay's in native people search and set titles and everything that we're interested in and we get something like this. Then we are running a waterfall. Some people

will have email addresses, some people will not. Those with email addresses we're going to push to smart lead in this case. Everyone else are going to hay reach. If our offer is applicable to

people not running ads, then we can do the same thing. Just filter out companies, find people and repeat the whole process. If you go back to our workflow, we did this part. Now inside

hey reach and smart lead, we need to set up our web hooks and we are getting to our N8N scenario. Inside hey reach, I can have multiple running campaigns for different types of businesses. Here we

have a web hook that is listening for events and based on event we have a this switch module that is just branching depending on type of event that is happening. For example, if we say

message reply received let's say connection request sent. We need to save this before testing the web hook. Important we need to click this test workflow otherwise we'll get an error

here. Test workflow workflow is listening for events. Test web hook connection request sent. The same thing we can do when someone accepts our connection request. This is important

for usually to have an ability to easily filter out people in a CRM, who are we contacted in the past, who to push to LinkedIn in the future, etc., etc. So, we have this connection request

accepted. Again, important information. So, we know in easy way to filter out people in a serum who accepted our connection request. So again, we have a little bit more here happening because

we're parsing replies and notifying ourselves on Slack. So when it comes to smart lead, this is an example that can be applied to hey reach as well. This is just for the idea is web hooks. We're

listening to certain events like emails sent, replied, bounced and end of campaign. For replies, this is pretty similar when sent is like connection request sent on LinkedIn. But when it

comes to replies, we can utilize CHGPT to determine sentiment of the reply, positive, negative or neutral to recognize is it out of the office reply or not. So what we built for our clients

is if it's out of the office, parse the contents of the email and then based on dates, use API of smart lead and just pause this lead until this date. For bounced and no replies, we are pushing

them to hey reach for example. Let me just really quickly run this example. We will say email bounced. We'll say test workflow send test web hook. So this is just a brief demonstration how

everything is working, how it's connected. All good, no errors. When we receive an event, we are using this built-in switch module. And basically this is something that we are getting

from hey reach based on their API specification the names of events. So connection request sent, accepted, received, etc. That's how we build this branching. When it comes to HubSpot,

it's pretty straightforward. I don't want to bore you with all the programming stuff. You can just take it and run with it. The similar thing is here where we have connect LinkedIn

custom property inside HubSpot. We're just searching LinkedIn by email address from the person that responded. When it comes to getting existing replies, this is something a little bit of magic and

data manipulation. Why? Because let me just go back here. Test this out. Message reply received. Let's run this test web hook. Okay, let's return here. Because we tested this, we have test

data coming from Hey Reach. Hey Reach sends us an array of messages because on LinkedIn we have a thread. We sent a message, someone replied back, then we replied back and then they replied back.

And so this is an array, a bundle of messages. So every message has creation time, it has text value, the the exact message and is it a reply or not? If it's false, that means we send the

message. If they replied back, it's true. What we're first doing, we're just searching HubSpot based on email address and getting these fields back. And so this is something that we can check. And

we have this test person here. This is some existing value inside the hubs field that I've created as custom field. Here we're just getting LinkedIn reply existing one. Then we are going to parse

replies because this is coming as existing replies and to return from hey reach web hook to go through these replies. So we're actually just iterating through this array and just

pulling this thing here if this value is true. So we're only interested in replies that we're getting and we will exclude everything that we sent. So this piece of JavaScript code does exactly

that. So when we're saving reply, we have JSON replies. This is this field. So everything new and this is all existing replies. So it will just concatenate and add to each other. That

way we are not losing anything from before, but we're just adding to the conversation. So we see more of the same message because this is the only test message we have. But this is a test that

we're working. So as we're going back and forth with this person, we'll just have more and more messages that they've sent to us. Again, we'll be notified on Slack. Some notes to be taken here. Here

we have this time date thing to pay attention to. And when it comes to smart lead, we can just again analyze this and just give some instructions how to parse the sentiment of the message. Then based

on that we can set in a similar fashion we're getting existing email replies from before and just adding new ones to the top and pushing all that into this property. Also setting up the response

sentiment before pushing to hey reach because people can bounce in a campaign for companies running ads as well as someone can bounce in a campaign for companies that are not running ads. So

this is just a piece of JavaScript code that just determines whether or not this company is running ads or not based on campaign IDs. So the same thing for no replies. I've split these branches

because most people they never received anything from us. So we might be okay with pushing them to a regular hey rich campaign because they never heard from us. But people that received all the

emails but didn't reply, maybe we'll ended in their spam. Maybe they read some of our emails. So, we might want to change the copy a little bit. Maybe not. And again, this is determining whether

or not they're running ads than pushing them to a separate campaign. In theory, we can use switch module here. I'm just ex software developer that likes to write JavaScript code. So, I just use

that. But if you don't want to use this option, you can use switch and just say, hey, is this ID equals to ID of the campaign? And then have a little bit more branching. And the thing that I

mentioned in the beginning that this can be running on autopilot is if we keep running this as a scheduled table. So Clay can keep watching for new people and pushing them further and then

everything is happening automatically without human intervention or with minimum of human intervention. And also one note when we want to trigger the end of the campaign we can just add a manual

step and that will trigger further a web hook with this event. And then we are doing everything that we done so far. So again, you'll be able to have this workflow for yourself. Just connect your

own accounts and run with it. Now you have a complete system for generating a potentially unlimited number of highly qualified leads using N8N, Clay, Hay Reach, etc. But that's just one piece of

the puzzle. The next question is, what kind of messaging should you send to these people? And that's exactly why I've created a video that you'll see on your screen where we broke down

everything we learned from sending over 5 million LinkedIn DMs. If you're looking to turn these new leads into qualified sales calls and clients, click on the video. See you in the next one.
