# How to Automate CRM Hygiene in HubSpot Using n8n [Full Workflow Tutorial]

Source: https://www.youtube.com/watch?v=P6x8EmrfvX8

Today we're going to talk about something that is very important and very crucial, often times neglected. And no, this is not me creating fear of missing out. What I'm talking about when

doing outbound campaigns is keeping the data fresh and clean inside our CRM. CRM should be, in my opinion, the central source of truth because often times this outbound outreach world is super

volatile and our tech stack, the current tech stack, might change at any point in time. For example, if we're doing cold emails and maybe we're currently using Instantly and then switch to SmartLead

or any other platform or vice versa. All of those platforms do have CRM-ish like features. What happens if we decide to migrate to another platform? So, what I think it's much better is to have a CRM

from the very beginning, you name it. It I'll I'm going to show this on HubSpot's example because a lot of my clients are using HubSpot, but you can pick any CRM of your choice. So, the idea is whatever

we do as part of outbound activities to keep it stored in HubSpot. And we don't want to reach out to people before they're in HubSpot. And we can do that in many different ways. By the way, my

name is Nenad Pavlov and I have been running my outbound and GTM agency for the last 8 years. Everything I talk about is from my experience working with dozens and dozens of companies since

2018. Also, just recently I started a community project called Go-to-Market Wiki and I'm sharing knowledge for free on YouTube and LinkedIn. And also there is a paid school community. So, there's

something for everyone. So, let me quickly walk you through what I'm talking about. And one note, everything that I'm showing you here, it is like test HeyReach account, test HubSpot

account, but the flow, the idea, the principles and tools along the way are from real-world examples that I built for my clients and that we are using for future us to future-proof our sales

activities. So, in the future when we take a look at our CRM, well, we will be happy and grateful to ourselves from the past that we did all this work, saved all this information so we can filter

and segment and do all sorts of things. So, first things first, adding leads {slash} to use, to our CRM is up to you. In this case, for some clients they have some integrations.

For example, Sales Navigator has integration built by LinkedIn with most popular CRMs like HubSpot, Salesforce, etc. So, directly going and cherry-picking and going one by one into

HubSpot. That's why I have here a HubSpot trigger. You might take a list from a platform, I'm I'm not going to spend next half an hour just reciting the names of all sales intelligence

platforms we have currently, but you use some platform and then pulled out a CSV, a list of people, imported into HubSpot and then you created maybe a list or filters or whatever or we're just using

search contacts node inside HubSpot and we're pulling this in the this workflow. Regardless, the point is the same. We're adding people to HubSpot then pulling them for further processing. Now, in

this case, I'm going to use HeyReach for LinkedIn outreach. The reasons are multiple. Sometimes we cannot find email addresses and phone numbers. Sometimes if we're reaching out to corporate

accounts {slash} companies because of security email gateways, we cannot our emails cannot reach to those people or whatever is the reason. And the beautiful thing about LinkedIn is

whichever database we're using, LinkedIn URL is so easy to get. It's not like with email addresses or phone numbers and verifications and this and that. It's super easy to get LinkedIn

URLs. And what we're doing, I divide into two segments, pre-campaign and post-campaign. So, going things going into our CRM, then in our outbound campaign and then from outbound campaign

coming to our CRM. And we can again visualize this, pre-campaign and post-campaign or during campaign. Things that we need to do to prep. One thing that has proven to be

really, really useful is due to the nature of LinkedIn and the limitation of 150-ish connection requests per week per account, we have this hard limit. And

maybe we're running a business that our total addressable market is huge and maybe we don't have many uh sales people or general colleagues in our company and even if we employ their LinkedIn

profiles, it's not enough. There are some ways that we could potentially scale this, but that's a different discussion. If we keep everything with this within this bandwidth, it would be

a shame if we were to contact people they're not active on LinkedIn. How would do we know if they're not active on LinkedIn? Well, we can take a look at their profile and we can take a look and

say, "Okay, cool. Do they have profile photo? Do they have cover photo, about section longer than some arbitrary number of characters? Do

they post? Do they interact with other people? Do they have this experience section filled out, etc." So, this is one way to go about this. And of course, manually it would be super painful. And

we have multiple ways to go about this. We can use We can sit down and think about what would be the criteria for determining whether or not someone's eligible for contacting because we don't

want to spend this bandwidth that is limited to contact people that have basically abandoned profiles like no headline, no photos, three connections. You know what I mean.

So, we can sit down and determine, "Okay, for us an eligible profile would have X, Y, and Z." And maybe sit down and code manually a scraper or ask CloudCoder or any other LLM system to

build a scraper for us or maybe use something that already exists such as an Apify actor. And one actor that I'm using is really, really doing a fantastic job in this case. And the

person behind this actor made clear about the all criteria they're using for determining the score from zero to 10. So, you can read through this. This is the name of the actor. It's super

cost-efficient and you can maybe think how you would do and go about this or maybe just use this one. So, and the only thing this actor requires is, no surprise, only LinkedIn profile. And if

we run it here, we will be getting this kind of information. So, detailed analysis, different fields and analysis. It's It's working great. So, that's what we're doing here. And so, we are simply

getting these results and updating HubSpot. Why? I want to save this score in HubSpot because I want to be able later on to filter out all the people, all the leads or contacts if we want to

use HubSpot's terminology, and say, "I don't know. I want to see all the people that have activity level beyond something that replied, didn't reply, something happened to them." And create

new segments and think about different approaches to get in contact with these people. Simple if node where we say if this person in question has two score from zero to 10, two or more, push it to

a HeyReach campaign. So, we're using HeyReach in this scenario and simply this is a test account, but we are going to have a simple campaign. We are going to send connection requests, blank

connection requests, and if they accept after a certain number of days, we're just going to send them a message. So, this is the point where this lead is getting into

the campaign. Now, we are going to move to this second part which is during or post-campaign. Things that I'm interested in saving is are the fact that we sent a connection

request to this person, a timestamp or date because I want to see who we contacted in certain period of time. And it's also useful because in example of one of my clients, they have several

sales people and sales director wants to have this information easily accessible to him and he doesn't want to go into any kind of outreach platforms and get dashboards. He just wants to have

everything inside HubSpot. So, it's easy if we have a timestamp, just give me the activity for this sales rep in this period of time, how many contacts, connection requests we've sent for this

person, etc. You get the point. So, timestamp of the connection request when we sent it. When someone accepts the connection request, this is also something that in this case will be a

textual message because in the in the example of this client, they have every sales representative has his or her her own accounts, aka companies, and sometimes

they switch around territories and all the usual stuff. So, if we just have a checkbox, for example, and say, "Okay, this person accepted connection request." But then

we don't know which sales rep this person connected with, we are going to save that as connected with first name and last name of the sales rep on and then date. And then

whenever a sales rep sends a message directly to this lead, we are saving the text of this message so they can analyze later on maybe on their sales calls and you know, update calls and whatever it's

called in you know, inside the company. And lastly, something that might be also interesting is whenever we have a reply from a lead to analyze the sentiment, to save, to preserve the whole thread in

the HubSpot and to analyze the sentiment of the whole conversation. And this is something that is going to be triggered every time we get a reply. So, maybe we're going back and forth with someone

chatting and simply communicating and the sentiment might change. For example, we might connect with someone and send them the first message, offer something. And that

person, they can say, "Cool, that sounds interesting. Please share your booking URL." We do that outside LinkedIn, they book a call, they don't show up. We follow up on LinkedIn

and we ask, "Hey, just to check if everything is fine. You didn't show up. Well, are you still interested?" And for example, what happens? They say, "Yeah, sorry, we're just too busy with

other things. We will postpone this or no, we're not interested anymore. Actually, we're not interested." So, the sentiment of the first part of the conversation with the when they said,

"Oh, this is so cool." was positive, right? So, later on, it turned into neutral or negative. That's why whenever we get a reply, we are going to just flatten this JSON. This is a little bit

of handwritten JavaScript. Yes, handwritten. Yes, I'm bragging about it. And have this thread and then just give to the AI agent node and a model of your choice to say, "Okay, just analyze the

sentiment." I already talked about that in one of my videos on this channel. You can search for it, but also I can explain more separately. And finally, we are updating HubSpot to

custom properties. One is sentiment, the other one is the LinkedIn LinkedIn reply thread. If we take a look, this is the just my alter ego go to market Wiki project.

So, instead of my agency, we have the LinkedIn response sentiment positive, the date when we send the connection request, and then the whole thread. This is dummy

data, but you can understand. And I also made this JavaScript code. Just make a note if there is like attachment or voice, so we know in the future when we're analyzing and LinkedIn connection

requests. So, the name of the sales representative and date and activity LinkedIn activity score. So, basically, in this fashion, we have everything that flows into HubSpot as like initially

leads and contacts, qualifying them for LinkedIn outreach, doing the outreach, and then whenever something happens in HereEach, we are handling the most important events. So, regardless what

happens, we will have that all in HubSpot. We can create dashboards we can analyze. They have their own MCP servers, so we can do additional analysis directly by

chatting and prompting. So, and basically, have everything cleaned up and up-to-date. That's it. Hopefully, this has some value to you. And if you have any additional questions about this

workflow or some ideas or want to share how you're doing things, please do in the comments. I'll be waiting for your responses. Have a good one. Bye.
