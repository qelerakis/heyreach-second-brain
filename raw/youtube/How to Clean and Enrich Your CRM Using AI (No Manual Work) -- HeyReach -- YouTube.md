# How to Clean and Enrich Your CRM Using AI (No Manual Work)

Source: https://www.youtube.com/watch?v=pxXrhO6AwTE

If your CRM looks like this, then you're potentially losing out on a huge amount of revenue and deals every single week. Now, I see it time and time again. You get your CRM organized, everything looks

good, you try and keep implementing your changes, but then you get CRM fatigue and everything just gets into a mess to the point where you feel like you have to start over again or you'll have to

spend thousands and thousands on paying an expert to do it for you. But in this video, I'm going to show you how you can set up some simple workflows from Hey Reach to NA10 to your CRM so you can

keep everything organized, clean with very minimal effort. And don't worry, there isn't 20 complex integrations and it doesn't break the bank to set up. Now, firstly, let's go through what a

bad CRM looks like. Now on my screen at the moment I am sharing five examples of five elements in a CRM which could go very very wrong very quickly. Now I felt spiritually wrong to create an example

within my own CRM which is why I'm sharing it on slides at the moment with the help of chat GPT to create a few of these examples for me based on my instructions. But I'm sure a lot of you

have at least encountered one of these issues if you've been using CRM for a long time. So firstly here we have overdue leads everywhere. So you add a new lead in it sits in new lead forever.

You don't follow up with it. It never moves forward. We have unassigned leads across the pipeline. So whose lead is it right? Like who was the person that should be dealing with this and then it

gets messy because people don't know who's what and then reporting becomes messy and it yeah just generally a nightmare. Missing all useless notes. Now, if you work in a team of people,

this can be incredibly frustrating, especially if an SDR is filling out details for an account executive to then take a sales call and [music] they don't have good notes from, you know, the

conversations that have happened previously. This is going to put you in a bad position to close that sales call. Leads in wrong or contradictory stages when you have too many stages. Sometimes

people want to monitor the pipeline too granularly and you get fatigue because it's like what is this stage even for and then it sits in the stage you never update it and then it's really difficult

to report or know how effective your sales activity is at that current moment in time and then finally dead pipeline no movement for weeks. So nothing's getting moved across stages. No one

knows when they should be reaching back out to leads and it just becomes a mess. these bad practices if you keep doing them is very hard to fix over time. What you're going to want to do first is

create a workflow within NA10. We're going to have a web hook trigger here. For the purpose of the video, I'm just going to show you quickly how you set this up. So, when you create a trigger,

right? So, I've got a trigger node here and it's going to be web hook. What we want to do is you want to get the test URL. You want to go to hey reach. You want to create a web hook. URL you copy

and paste in here for the test and then you name it. In this instance, I name it hey reach to N8N to ATIO because now I know right which flow is this linked to. So when I refer

back to the web hooks or maybe I need to create a new web hook or make an adjustment to one of my existing web hooks, I know which one to select and what flow it corresponds to. At this

point we want to choose first message reply received. you could do based on when a lead tag is updated. However, you have to manually update the tag. So, it kind of defeats the purpose of the

automation. I don't want to have to go manually into, hey, reach and mark a lead as interested. I just want to be able to do that whole process automatically. I want to measure the

sentiment automatically. I barely want to even have to look at the inbox. I want to just be able to see when a positive reply comes in and then go to Hey Reach and deal with the positive

reply. Then here you want to just leave it on all campaigns unless you're running multiple different campaigns and you need to be careful about which ones you select for this particular flow. And

then you create web hook. So we go back to NA10, we listen for a test event, we go back to hey reach, we test the web hook and you can see now success is working. Now once our web hook is up and

running, we can then move to setting up the CRM agent. Now the reason I'm showing a succeeded run is so I can show you how the data runs through the flow into our CRM at the end. So we have the

AI agent itself with the prompt and the system instructions. We have our output passer which is in JSON. This is so we can pick variables out of the prompt output instead of it just being one big

blob of data. And then we have our model. We're using 03 mini here. So we just need to connect our check GPT or open AAI API key to the model. So we can run this workflow. Now it's very simple

for how this works. You have your system message here which is the instructions that the AI agent is going to run on for each individual workflow. So here we obviously have if I open this up, we

have the role here. We have the determine the sentiment of the reply. So we're we're giving it instructions on what output it should be giving essentially. We're then giving some very

clear examples and then we're showing the example of the output in the prompt because our system instructions is doing the majority of the work here. We can keep this very simple. So the full

conversation we have me and the prospect. I'm just want to give it enough context to the conversation so we can understand if it's positive or if it's negative. So you can see here this

is all the data that we've received from the web hook. All we need to choose is my message which would be this one here because this is message zero which is essentially message one. So I can see

that this is me and then I can see that this is the reply from the lead. I've essentially pulled this variable into this section and I've pulled this variable into this section and labeled

them me and prospect. Now it's going to change for each lead which enters my workflow. Now, I won't go into the exact details of how you set up an API key, but all you need to know is you need to

set up credentials and then connect your API key to the model for this workflow to run. And then we have our JSON output here. Now, you can easily just create this from doing a prompt in chat GPT.

Just ask it to do a JSON object based on the sentiment and the reasoning and it will output this for you. And this will mean that when it goes to our next stage of the workflow, we can actually pull

out each of the variables as a dynamic variable like I showed you within the CRM agent. At this point, we want to remove all the negative responses. So, if we go back to a successful run here

and I show you how this is running. So, obviously now we have our sentiment nicely split out because of our JSON object and we have our reasoning. So, we want to pull out sentiment and then

contains positive. So anytime this sentiment is positive, it will filter it out and it will remove any of the negative responses simultaneously. Finally, we are connecting ATIO through

HTTP API. If you use something like Air Table or if you use HubSpot, you're going to have native integrations within NAT for the vast majority of CRM. It's only Atio, which is quite a new product

on the market. I had to create a HTTP request. But essentially all you have to do is find the URL. So like the end point that ATIO receives. So you copy and paste that URL. Always specify the

headers for application JSON. So we have one header here for the content type. And then here all we're doing is we're pulling all of the data points. So we're pulling name, first name, last name,

LinkedIn URL, company name, etc., etc. All of the data that we have from Hey Reach, we are now sending to our CRM so we can run the automation within Atio. Now, moving on to Atio. I'll quickly

show you where you go in order to set up these workflows, right? So, you're going to want to go to automations and workflows. Each CRM will have a builder like this. I know HubSpot does. I know

Pipe Drive has a builder like this. I know Air Table has a builder like this. So, initially we need a web hook. N. Now you remember I showed you the end point within NAN for the HTTP API request.

That is this web hook URL. So we want to copy and paste this and bring that back to our NATM workflow. And that would go into our HTTP request in this URL box here. And now what that's going to do is

whenever a lead runs through the NATM workflow, Attoio is going to be listening for it when it comes out the other end essentially. So once we've connected our web hook, we then need to

pass the JSON. The reason for that is because when we get the data sent from NAN, it will be in one big JSON object and the fields won't be split out into dynamic variables. So what this node

allows us to do is pull out those variables and values such as full name, first name, last name, etc., etc. Otherwise, it would just be one long line of data with all of these variables

next to each other. The way you do that is whatever is sent from NA10. So if that variable is called full name, just copy and paste the exact wording of what it's called within NA10 and then it will

match the string and then you can just name the Elias so you can refer it to it within the workflow. If you don't name it, it will just come up as field one and it will be really difficult to

differentiate between the different variables within the workflow that you're building. So at this point, we've now got all of our dynamic variables. So we can create our records. Here I'm

firstly creating a person record and we're just getting the main data points that we can pull from our LinkedIn campaign. So what we're going to have available is full name. We're going to

have email available for some of our leads. We're going to have company name, job title, and we're going to have LinkedIn URL. After this, very similar. We're now creating a company record. So

we have name here, create record here for team. This is just so we can associate the person we just created with the team at this particular company. And that's really about it. We

have the website as well at the top there. So once we've created a person and a company record, we can now associate them with a deal. But we need to create that deal first. So our next

node is create deal. In our case, I select the person's name for the deal name. So I've selected for deal stage here, lead interested. That means they're automatically going to be added

into that stage of the pipeline. I'm selecting myself as the deal owner and then I'm associating the people record we just created and the company record we just created here and you can find

all of these variables when you click use variable. Now at the bottom here I'm selecting cold LinkedIn because this came from a cold LinkedIn campaign from our hey reach and then we're selecting

email. So finally what we want to do at the end of this flow is create a list. The reason I like to do this, as you can see in the lefth hand column here, I have LinkedIn attribution. And if for

instance, you know, a client wants to quickly see what's going on with their LinkedIn campaigns and how many leads have come in or they just want to have a look at the list, they can click here

and they can see all of the leads which have come from LinkedIn within here. And the way you do that, very simple. In this case, we're just choosing creative record that we just created. And all of

those data points are now going to be imported into this list. But you need to create the list first in order to be able to select it in the input variable at the top there. So [snorts] now we've

created our records, we can now build out some automation for follow-up reminders for us within Slack. Now I have three different workflows for this. So if we go into the LinkedIn follow-up

reminders 3 days, and I'll show you what it looks like on Slack on the other end as well. We want a recurring schedule. The reason we want a recurring schedule is because we don't want to manually

have to trigger the flow. We have this set up for daily at 9:00 a.m. Then at this point, it's going to try and find list entries. So, we have this node here. If we didn't have these conditions

set up here, we would literally be sending reminders in Slack, and that would get incredibly crowded within that Slack channel. So, the way we prevent that from happening is we set these

conditions. So only if a lead is lead interested, if the attribution is cold linked and if a created at is before 4 days and after 2 days. This is the cleanest way I believe to get the date

correct because these are relative, right? So it's relative to that date which it happens. So we can be sure that we'll get a follow-up reminder at 9:00 a.m. on the third day of a record being

created from a cold LinkedIn campaign. Our next node here is we want to do a loop. In some CRM or building or automation builders, you don't have to do this. So I know for a fact in air

table you don't have to do this. This is a feature of ATIO where I need to do this loop. The reason for that is so we can run it individually for each row. If a bulk piece of data comes in in one go,

it will try and run everything in one go and it will just mess up. So all we need to do here is choose the variable which is matching list entries and then we want to create a node within the loop

which is post message to channel. We can simply connect this through our slack channel cuz there's a native integration with Atio. All we do here is we choose our corresponding channel within Slack

which is hey reach positive replies and then we write the message here and we can even choose the dynamic variables. So it would read like lead Rob Sloan has been in lead interested for 3 days.

Please follow up on hey reach and then I provide the LinkedIn URL just in case someone wants to quickly click on that from Slack to view the lead. Then what this is going to do so if I go over to

my Slack and I bring this into screen and we go to hey reach positive replies channel here. But as you can see it pulls through through the Atio app and it's going to trigger on 3 days, 2 weeks

or 7 days. So now just to show you, we have a bunch of leads in here which are from our LinkedIn campaigns. We could now create a report based on this list. So this is just like a dummy one that

I've set up. But as you can see here, you could set up like bar charts between channels based on the lists that you create. So we can nicely segment the data and visually see the data in

different ways. And then of course in our deals pipeline, the top funnel, so everything from our outbound campaigns is going to be automated. So, we don't have to really worry about the top

funnel. Once a lead books into a demo, all we need to do is move that lead into the demo section. And as you can see from one of the tests I've done is moved into gone cold because this was set up

for 14 days without a reply. Now, just a note as well, we don't just have to do this for our LinkedIn funnel. We can do this for all of our marketing and sales funnels. We could have a Google Ads one.

You can see in my screen recording we have conference attribution set up from a type form. This will automate all of your topfunnel CRM enrichment so you never have to do it again. But this goes

a long way to streamlining your workflows so your team doesn't have to keep updating the CRM and they can focus actually on closing the deals. If you need to fill up your CRM in the first

place, watch this video to the side of me where we go through how to send thousands of LinkedIn messages through Hey Reach so you can generate hundreds of positive replies, close lots of

deals, and keep your pipeline nice and healthy.
