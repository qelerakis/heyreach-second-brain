# How to Automate LinkedIn Outreach in 2026 Using AI and No-Code

Source: https://www.youtube.com/watch?v=Spp9PR_eLDs

In this video, I'm going to show you how you can completely automate your LinkedIn outreach so you can send killer outbound messages to your ideal customer persona every single day. Before you go

and say, "These messages probably aren't that good." Trust me, just wait and see. The messages that we're sending are hyperpersonalized at scale thanks to some of the tools that we are using and

they're indistinguishable from sending a manual message to a prospect. We're actually talking to the pain points and needs of our prospects while automating the whole thing. And there are only a

couple of things that you need here. We're firstly going to be using Clay for lead scraping and data enrichment. Secondly, we're going to be using Hey Reach as our LinkedIn automation tool.

And then finally, we're going to be using NAN as our post positive reply flow. Now, I know this sounds absolutely crazy, but I promise you I'm going to walk you through the process step by

step, and you'll be surprised at how easy it actually can be. So let's start with Clay. Clay is the tool which is going to allow us to scrape our lead and company data, help us qualify that data

to make sure we're reaching out to the right people and then also find new data points about those leads or about those companies which will help us create relevant hyperpersonalized campaigns and

also so we can reach out at the right time. You're currently looking at my workbook for this flow. So this workflow is designed to initially we're finding the people we're qualifying those people

within this table here. So making sure they're actually lead genen agencies and they're qualified for our specification. It then branches off into two funnels. So we have our event job posting with

this is a signal that we're using over here which will run monthly and what this is going to do is it's going to find out if any of our lead genen decision makers are posting for a job in

operations. We've also got a find people which is going to find people based on if they left the company. So, what we're using is a really cool filter that you can use within Clay where you can find

people not just if they're in a current position at that company, but if they've ever worked for that company. And of course, then we can layer on some other enrichments to ensure that they have

left the company within the last few months or so. And then obviously this is a key moment where we can reach out because we can say we can reference that person and say, "Hey, I figured that you

might be having capacity issues at the moment and maybe I can help out." But to begin with with the find people search, you can do this within Clay very easily. It's basically like a sales nav search.

So all I've done here is looked for my ICP company. So I'm looking between 2 to 50 employees, the relevant industries, and the relevant keyword descriptions just to make it a little bit more

targeted. We're then choosing the relevant job titles that are applicable to the decision makers we're looking for. And then I'm choosing the locations. Now I only want

English-speaking countries. So, United Kingdom, United States, and Canada are relevant to me. I can then preview these people and I can find them. And then what that will result in is this table

here. But at this point, obviously, we've got a lot of data in this table. And some of it might not be accurate to lead generation agencies. So, we want to qualify the lead generation agencies

first before we stack on any other data enrichments. So all you need to do and I do this with every single clay flow that I do. I always run a clasian prompt to categorize the ICP that I'm looking for

using their website. So essentially what this is is an AI agent which will go to their website and based on the prompt that I give it, it will produce an output and that output will be either

marking it as my ICP which is lead gen agency or the industry which they actually are. Once that's run, I can then create a view. And the reason we want to split this out in the view

because when we do some of the other enrichments later in some of those other tables, we want to be able to separate these leads away from the unqualified leads. So here, all we've done is lead

genen agency contains lead genen agency. And that will just make sure that they're all lead genen agencies. As you can see here, if we look at the default view, this is a separate view. And all

you have to do is duplicate the view. And then in that view that you duplicate, change the filters and change the name. And then you'll be able to easily reference this when you get to

your next part of the enrichment. Now we've got our qualified lead genen agencies. We want to layer on the signals. So we know which leads to reach out to and what campaigns they should be

funneled into. So we've initially got job posting here. And very similarly, what we're doing here is firstly we have the view. As I mentioned before, we can now choose qualified lead genen agencies

because we created that view in lead genen decision makers 11 to 50. We choose company domain as the identifier. And then we can choose the job titles. Now differently to the decision makers

in the other list. Obviously I was looking for founders. I was looking for you know like CEOs of those companies. Whereas here I'm actually looking for operation type job titles or like

anything to do with that. So like account manager, operation ops, even GTM, client fulfillment, anything to do with fulfillment. It could indicate if they're hiring for one of those

positions that they have a slight capacity issue at the moment, which opens up the door for me to reach out to them. So the posting date, we want to make sure that this is a maximum of 30

days. You could slightly make that bigger, that number, but really we only want to reach out to people that have recently posted jobs because it's hyper relevant to that moment in time. That's

everything for the filters here. And once we run this, this is going to run monthly, but we can set the frequency to a different type of frequency. So, we can do a bi-weekly, but bear in mind

this is going to use more clay credits. So, just to show you what happens here, this is managed to find four leads that have been posted in the last month. Four of these jobs are from the same company.

So, really in reality, it's two people that I can reach out to. But remember, we had quite a small sample size. There was only like 300 agencies in that list. Here we have all the company data which

is pulled through and then we can pull the company record from our other table. So we can pull the decision maker's full name, their job title and their more importantly their LinkedIn URL because

we're going to need that for the campaign. And now we have two people that we know are hiring for roles that we could actually help with from a white labeling perspective. Now let's move

over to the other signal which is find people. Now, this is slightly more complex, but the find people source, what I've done here is the past experiences. Clicking this on means I

can find people even if they're not currently working at that place. They just have to have an experience at that company on their LinkedIn profile. That's going to pull the table and we

got like 242 rows of people that have worked at these companies. Now, the problem with this is some of these companies might have left ages ago. So, we don't want to just outreach these

people because one of these guys could have left two years ago and I reach out to them saying, "Oh, this guy left." The guy's going to be like, "Hang on a second." Like, this was ages ago and it

wouldn't make any sense. To get around this issue, what you want to do is you want to use LinkedIn enrichment filter. Now, I've just used the clay integration, which costs one credit per

row, but feel free to use something from rapid API. You could easily do this with a cheaper API tool, but just for ease of use because it's all native integration, I've created the Clay integration. And

this is just going to pull all this data. So, I can take their latest experience. And then, obviously, I can cross-check that with their current experience because the other issue with

this is if someone had changed job roles, but they're at the same company, they would still be pulled. And also people are still pulled if they're presently working at the company. So you

have to be really careful because there could be false positives so to speak and you could add people to the campaign which are haven't actually left the company. So the way we get around that

because we have all their data now we can put this into a prompt. It's basically taking this enrich person column and analyzing it and then coming back to me with an answer of if they're

still working for that company. The expected output is a date. So the date of when they left that role or if not it will output present which will tell me that they're still working at that

current company. And what this enables us to do is one ables to qualify the list. So now we know who's actually left the company. And then secondly we get a date. So we're able to again qualify

based on when they left the company. And then I can create this view called left lead genen agency less than four months ago. And we can see here we've only got five rows but again it's a small sample

data set. We found five people which are qualified for our campaign. So now we've done these clay enrichments. What we can do is we can add them to our LinkedIn campaigns. Just because I'm in clay at

the moment, I'm going to show you how you do that. But what you want to do first is you actually want to create the copy of the LinkedIn campaign before you do this because you need to know roughly

what personalized variables or what column headers you're going to pull into the campaign. We can connect our API key. So, all you need to do is add an account, fill out your API key here,

name it, and then what we can do is choose the campaign ID. There's usually a drop down here, but when you've added it, it doesn't add the drop down. So, you can just choose the campaign name.

You choose their first name, last name, you just map all the fields. In our case, the personalized variable that we want is their employee field. So, we want to pull their first name of the

employee so we can reference them in the messaging. And then we're making sure only run if decision m first name has a value just to make sure there's no like people that get pulled which don't have

a first name and then they'll end up being added to a campaign when they shouldn't be. That's just a protection measure that I've inputed there. Then for job posting very very similar

exactly the same process but apart from our customiz variable is going to be the job title instead of the person's name. So we're going to be referencing the job title in our outreach message. So now

the clay table's done. Once this workbook is built, you can go in and as long as it's on auto, you can add people to this lead genen decision makers from other sources or do another people

search up here and connect it here and the whole flow will be completely automated. Everything will run through and everything will get added to your Hey Reach campaigns without you even

having to lift a finger. Now, moving over to Hey Reach, here we have our job post. We have send a connection request and then wait 2 days and then our message, hey, first name, good to

connect. I saw we're both in Legion and I had an idea that might be relevant. People like yourself often get bogged down with ops and fulfillment as automated GTM is tricky skill set to

hire for. I white label myself etc etc etc. Notice that you had a job post up for job title name. So it could be like an ops manager. How's capacity looking for the time being? It's a personalized

message. Then we have a fallback message just in case these variables don't pull through for whatever reason. So it's just a safety mechanism. And then we just have one follow-up after 7 days. I

don't really want to annoy people too much on LinkedIn. That's not my style. And then that follow-up is just like, as I haven't heard from you, I assume capacity isn't an issue right now. When

you make an assumption, people will often quickly correct you if you're wrong. So, it's a good little sales tactic there. Also, I want to network with some of these people. So, I'm

offering to network. And then you can go and launch the campaign. All you need to do is make sure all your leads have pulled through. And as we can see, all the correct leads are pulled through

from our clay tables. So, we're good to go. and then we can launch the campaign. Now, of course, on top of this, you could create a generic campaign. We could just get rid of the personalized

variables, and this would be a decent message to just send to people automated. It won't be as effective because they don't have a signal. If you're struggling to keep up with the

cadence of the campaigns, you could create a generic campaign on top of the campaigns that you've created here with the signals just so you get enough outbound out there, but for the purpose

of the examples, I haven't done that yet. Our campaigns already, the clay tables are ready. We know everything's pulling through to the correct campaigns. We can tick these campaigns

on, right? So, we can we can turn these and we can launch them and we can be confident everything's going to work correctly. What I also want to do is create a post-ositive reply automation

flow so that when leads positive reply to me, they get put into my CRM. They get qualified for positive sentiment. So, we know if they're a positive reply and then I want AI to automatically do a

response to that person and any follow-up messages that they send within that conversation. And the way I've done that is using NA10. And I'm going to show you that now. So, this is an

execution that I've run in NA10 which has worked all the way through. So, I know that this is running well. Initially, to set this up, we need a trigger. That's just an event which is

going to trigger the workflow. And for us, it's a web hook with hey reach. You're just going to go to editor here. You're going to type in web hook. And then you're going to be able to click on

web hook. And then you're going to be able to create a node like this at the bottom here. So it'll be separated like that. And then if we go in here, you're going to have a test URL. This is really

important because you need this mock data to build the flow cuz otherwise you won't be able to use these dynamic variables within the automation. What I mean by dynamic variable is these are

going to change depending on the lead which gives us a positive reply. So if we put one of these into a prompt for instance that variable is going to change. So if I got like the sender's

first name and I put that in and one sender was called John and one sender was called Rob is going to dynamically change that in the prompt. So we can do some really really clever things so it's

personalized for each person. the test URL. What you're going to want to do is just click here to copy and paste the test URL. You go back to Hey Reach. You go to integrations. You go to web hook

here. You create a web hook. You copy and paste your web hook URL. You give it a name. So, positive replies. And then we're going to choose in my instance what I've chosen is every message. So,

every message that comes into hey reach is going to automatically ping to my N8N flow. and then it will just go through the whole workflow. So I can reply using the AI tools that I will show you later

on to any of the messages in the conversation. But what you could do is you could just have it on first message, the first positive reply and it will only run for that. You then create the

web hook. Then once you have the web hook, you want to test it. So you'll be able to click back on it and you'll see this button appear. You go back to your flow, you listen to test event, you go

back to hey reach, you press test event and then this data will pull through and you'll know the web hook is working correctly. Just note as well you need to change this to post not get. Now let's

go back to the executions and walk you through the flow. So what the CRM agent is going to do initially this is going to firstly qualify the sentiment. So it's going to look at the message and

categorize whether it's positive, negative or neutral. If it's positive, it will create a record in our CRM and it will also create a JSON output. And what that means is it will just create

those dynamic variables that I'm talking about before because otherwise it will be a big blob of data if we don't use this. So it will create those dynamic variables for us so we can pull them

through in some of the other nodes at the end here and we're not just pulling one big bit of data. So it's split out nicely for us. It will only do this if it's positive. If it's negative, it

won't it will just stop. But what I'm going to just quickly show you is how this all works. I'm not going to go through the prompt in detail. What you want to do is you want to create a

system message. So that's just a drop-down here. If we go back to our canvas, I can quickly show you. We go to editor in this AI agent. You'll click add option system message. This is very

very important. This is basically the backend information that your AI agent will always abide by. If you make this really detailed and accurate, every single prompt you give it, this will act

almost like their training data and what they abide to, right? So, you want to make sure your system message is very nicely organized and very clearcut for the AI agent to easily interpret. The

way I like to do it is have their role, have their primary tasks if it's split into multiple tasks, and then I have rules, and then I have the chosen output at the bottom. prompt is really where

you're going to put all your dynamic variables. So all the information relevant to that particular execution is going to be housed here. My CRM agent is relatively simple. Basically all I've

done here is because we're adding fields to the CRM. I've just added all the relevant data points that I want the AI to add into my CRM. To summarize here, the system instructions is what is

directing your AI on a general basis. The prompt is the information it needs to execute the system instructions. That's the best way to describe it. If we go back and just show you the CRM, we

want to create a row in easy pitch sales pipeline from our view which is leads. And if I go over to my CRM here, you'll see that my test examples have pulled through. So, this was completely

automated. I didn't do any of this. The AI agent actually did these two rows here. It just pulled the data in automated and I know that it's the easy pitch sales line and it's leads. I'm

just matching the dots here and then I'm mapping the data. If you were like really lazy and you really couldn't be asked to even map the data points, you could get the AI to let the model define

this field. I prefer to avoid that when there's multiple fields and it becomes a little bit more complex. We then remove negative responses. All we're doing here is we're taking our sentiment, which was

nicely put into a JSON output by our tool here. We're then splitting out the sentiment and reasoning. If I didn't use that JSON output, this would all be one big blob of data. So, it would all be

combined together. And obviously, if I put the whole thing together, it might not get the right output. I only want the word positive here because then I can filter out any of the positive

replies. And then if the filter notices it's a positive sentiment, it will move on to the next part of the flow which is another AI agent that we have working for us. AI agent is going to create a

LinkedIn message based on our campaigns. So I've given it the context in the system instructions. I've told it I'm a GTM engineer. My target is lead gen agencies. So I'm trying to give it

enough information to kind of write on behalf of me. I've given it the rules so how to approach each reply. I've then given it examples and then I've given it strict rules at the bottom. And the way

I do this, I'll try and make it as optimized from the beginning and I'll run it. I'll read the message and then I'll iterate. So the point I'm making here is you need to iterate on the

prompt. The AI agent is only going to be as good as the input you provide. If your system message is very short here, I promise you it will not be a good output. As you see with the prompt here,

again, super simple. All I've done here is pulled the conversation. If we go here, we can find the conversation. So, recent messages, I just pulled this whole field. And if we scroll over it,

you can see sounds interesting. Are you free at 400 p.m. tomorrow for a chat? So, in this instance, there was only one message. So, it only pulled that one message. But it shows you that if there

was like multiple messages in the conversation, it would have pulled the whole message. And that's important because I want them to reply to the latest message. Once we've prompted all

of this and we're happy with the output, I've then added my calendar because what I noticed is some of the leads are going to reply and actually want to chat. And there could be the odd edge case where

they're asking, "Hey, Rob, I actually want to chat tomorrow at 4 p.m." In which case, I need the AI agent to send the correct message. I need them to check my calendar. Because what they

might end up doing, the AI agent, is just booking a random time or accepting a random time when I'm not available. So, I've said to the AI within the prompt, make sure you check my calendar

if a time is mentioned. And then it's going to use this as a tool. If you were going to complete that task, think about what tools you would need. So, if I'm going to be a sales SDR and I need to

log data into a CRM, I'm obviously going to need the CRM to log the data. Similarly, here I'm going to need my Google calendar because I need to check my schedule to know if I can book that

particular time and then I will reply in accordance with that schedule. So, what we're doing here is you just connect your Google calendar account. Really easy this one. You literally just sign

into your Google account through N8N. We're then choosing the operation availability. Again, very important because we don't want them to book anything. We just want them to check our

availability. And then we're just choosing the time frame to choose between. And then what the AI agent will do, this will run only if it specifies a time. What you'll notice if you actually

watch the execution run, it will get to LinkedIn agent. If no time is specified, it will just run here and then will move straight to Slack. But if a time is specified, it will check the calendar

and then it will go to Slack. I don't want the AI to run off and send messages for me. But I do want it to draft messages for me because it saves a lot of time on my part. I don't have to keep

checking the account. I could set up a follow-up flow from my CRM in a separate workflow. So, it saves me a hell of a lot of time. But, I don't want it to message on behalf of me without me

checking. Personally, I would say in this flow, six out of seven messages, a good out of 10. But, there's going to be times that you need to add your own nuance to the message. Especially if

it's an open-ended question asking a bit more information about yourself. You can give it all the information in the world, but it's not you. It's not your mindset. So, you do need to step in at

this point. And what this is is a send message and wait for a response node. I created an app within Slack which was a bot, but you can literally just use your own profile. And that's really easy. You

can connect it through this in a couple of clicks. So, this is the message which is always going to be outputed to Slack. So, a new reply has been received on LinkedIn. Here is the conversation. I'm

pulling the conversation dynamically for each lead. Your AI agent has crafted the reply to this response below. So, I pull the reply from the LinkedIn AI agent and then please approve or disapprove this

message. If disapproved, reply to the lead manually just to make sure I'm reminded to do that. What you're going to want to do is click approval here and then you want to click approve and

disapprove in the drop down here. And then you can just leave it. That will create two buttons. So, you have an approve and disapprove. It will look like this. So, you can see this

messaging here. I can see the conversation. I can approve this. And then what will happen is in my flow, this will then permit the AI to send a message directly from hey reach. This is

the final part of the flow and it's replying to the lead. This is going to take the LinkedIn message that the AI crafted and send it directly to the lead. So we don't even have to send it.

As soon as we click approve, it will send the message. Just go to Postmaster, go to send message, and just copy everything here. We know that there's a query and we know we need to get the

LinkedIn ID for the LinkedIn sender for this to work. So we create a query. We type in the same name and then we pull the LinkedIn ID. This is a sender ID. So we pull this here, pull it over here as

an expression and then it will dynamically change for the API key. You find that from hey reach. If you go to your integrations and you go to hey reach API get API key, you can then copy

and paste that over. You've got your content type, your name, which you just copy over, and then your JSON. For the JSON, obviously here on Postmaster, you've got the message, subject,

conversation ID, LinkedIn account ID, which corresponds to this. You just need to change the variables within these quotation marks that it dynamically changes for each lead. So, it replies to

the right person. Once you've done that, what you're going to want to do initially is you're actually going to want to find a conversation ID and a LinkedIn ID because this won't work on

test data. So, it won't work on your mock data because they're just making up random bits of data. So, you need to actually find out what your LinkedIn ID is. And then you need to get a dummy

conversation. What I actually did is I created a dummy LinkedIn account in my name just to test this. I then created a test campaign here. And what you can do is just instead of connecting because

obviously you can already be connected. Just send message and it will send a message within like 15 minutes and obviously you don't want to just launch it without testing it on a dummy account

before you let the flow just run off and do its thing. You can fill out these manually. So what I mean by that, don't pull this over. Just literally write out your ID, write out the conversation ID

or copy and paste the ID. You can run it once and then you can ensure that it's running correctly. Then you'll know when you change it back to those dynamic variables, it's going to work correctly

for all of the leads. You're going to see something like this in your uni box, like with this conversation here. I did this execution, and that's the execution that I was just showing you, and it

says, "Yes, I'm 3:00 at 4 p.m. AI is sending the correct message to the correct person, and it's understanding the context. It's checked my calendar, so I know all the flows are working

well. I also know that it's pulling the data into my Air Table. So, I know that's working well. And now the flow is complete. The final thing we want to do to get this flow working completely, you

go back here, you go to your LinkedIn positive reply web hook, you go to production URL and you swap the production URL for your test URL. So, you go back to your integrations, you go

to your web hook, I change it, and then I remove this one with the production URL. I go back to my N810 workflow and I make sure this is active. And now this will all run autonomously without you

having to lift a finger, but you also don't have to worry about the AI just messaging people randomly because you'll get a Slack message which will notify you that you've had a positive reply for

one. So that's really helpful, but also you're going to be able to approve the message that it drafts for you just by clicking approve. What we've been able to do is generate data in clay, create

an autonomous digital data enrichment flow which automatically enriches it based on the data points we need. It's automatically putting them into the corresponding campaign. So if they

posting for a job, it's going to go into our job posting campaign. If someone left the company recently in an ops position, it's going to go through the left company campaign. Once that

campaign is running and we're getting positive replies, everything is going to go into this NHM flow. We're going to log it in the CRM. We're going to then craft a message. We're going to approve

that message and then we're going to reply to the lead. So, the whole flow is pretty much completely automated. Thank you for listening, guys. I really do hope you found some value. And hopefully

now you're in a position where you can plug in this LinkedIn automation system directly into your outbound stack seamlessly. If you're wondering what you'd learn after using this system to

send over 5 million LinkedIn DMs and you want to skip that boring trial and error part, please do click the video to the side of me where we go over everything and all of the learnings so you can put

more calls, generate more pipeline, generate more revenue, and grow your overall business. If you're serious about using LinkedIn to the best of your ability, we will see you over
