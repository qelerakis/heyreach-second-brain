# I Built an AI Agent in n8n That Books Sales Calls For You

Source: https://www.youtube.com/watch?v=EI5VmqNsjzg

I used NA10 to build an AI agent that helps me book dozens of highquality conversations that turn into booked meetings without me even having to lift a finger. The beauty of this system is

that you can sit back and relax and know that not only the agent take care of this for you, but it does an amazing job. So by the time this video is done, you're not only going to understand how

to use this AI agent step by step, but I'll be also giving you the template that you can copy paste and implement so you can start using it as soon as today instead of having to spend hours reverse

engineering the system. Let's say we post something, we will have people react and engage with this content. That's all fine, but we will have some strangers, people that are not connected

to us. We never talked to these people and it would be a shame not to start a conversation. In the past, what were the options? Well, we can post something, leave it for a few days and come back

and then click here and see who engaged with our content and go one by one, open their profiles and send them connection requests, wait for them to accept and that would be a really really tiresome.

So, this is the first level that we can do. A level above that could be potentially create a campaign or actually to build a list of people reactors that engage with our content.

This is cool, but I will suggest something even more robust than that. And that is to combine multiple platforms that can observe all of our posts over time and even in the future

whenever someone engages to notify us and to have a workflow in place 100% automated that can handle that. So craft customized message and add these people to a hatri campaign in which we will

have following steps. So if we're not connected send connection request a blank one then when they accept send a proper message that will have personalized message and then we can

have a fallback message and that can be on an autopilot. You'll be able to download this workflow and to import it into your NA10 account and use it as I'm using it. So we are simulating some data

coming from trigify and then we are setting some variables filtering out and then we have AI agent that is crafting the message and if the message has been created we are sending everything to hey

reach as this part of the message is going to be personalized for example we can see in the output one of the examples that AI agent generated hey Mike I saw your like my post about web

coding tool ideas and then asking a question about the post starting a conversation But this is the idea to replace any manual work in order to do this. If you're not familiar with

Triggery, it's a really powerful platform that can do a lot of things. One of the most powerful things is to monitor certain keywords to find people that are posting on LinkedIn about

certain topics or simply we can follow our posts and engagements. These are all posts from Vauashin. So if I open one, this is the one about Vibe coding. We can see all the people that liked,

commented, but we need a way to do it programmatically to get to this information. Luckily, Trigify has integrations and web hook support. So, we can just create a web hook. This is

from NA10. And then to do some testing and we can choose an event and in this particular case, we can pick only one event and that is when engagement happens. So someone reacts or comments

on one of our posts and then we will get some information a JSON structure about the event who did it time stamp on which exact post the company this person is coming from. So we can test our

workflow. So in this case I can say execute workflow like this send an example and we're receiving some data. This is a way while I'm building a workflow how I can make sure that I have

ability to start a workflow from a web hook and also to use data that I want to use. For example, if we open up this set variables note, we will see that when we're getting from web hook, this is

something that triggery provides because it says, hey, I can provide you with the structure of JSON, but I cannot give you some really realworld text from a post. This is just dummy content. But I want

to test generating these messages that AI agent is doing by providing it proper text of a proper post. So if I start this workflow manually, it will use these real life data. If I'm starting

from triggery, this is when I want to test the connection between triggery and this workflow and later on when I push it to production mode to have this connection ready. How I'm doing this is

by using a pinch of JavaScript. So I'm using this operator and asking hey LJ JSON is an object and body is a property. If this doesn't exist then use this hard-coded value. So if we're not

getting information from triggery or any API then use this hard-coded value and so it will be always Mike. If we're using will be John this is first name. So if this exists then use actual proper

data and I just cherrypicked things that I know I need later on for AI agent hey reach. So, first name, last name, LinkedIn URL, post text, event type, and here reach campaign ID because we need

to set this in order to send the information to a proper campaign. Now, this event type is something that I'm going to filter. Why? Well, because I want to only have engagers. And this is

by taking this variable and saying is not equal to comment. I added one T because otherwise it'll just stop if it's coming from Trigify because in triggery test data, it's always comment.

And additional thing when we think about it, no one is posting 100% of time only about promoting their offer. Sometimes people post about day-to-day things. So this is an example. In this post,

Vauashin posted about looking to hire someone. Do we really want to engage with people that reacted and asked them something about hiring people? So it would be cool if we had a mechanism to

filter out those posts that are not actual promotional post. One thing that we can do is to just measure if like out of 10 posts nine are promotional, one is not. Whenever we're posting this one not

promotional post, we can add somewhere in the text some word or phrase or a hashtag that will fit in naturally but actually give us a chance to filter out like this special tag. The post is not

processed. The event is not processed. So, people that engage with this post are not going to be added to a campaign and engaged in this way. And I know what you're thinking probably. Oh, wait.

You're really going to let an LLM and a AI agent generate some text that could potentially be cringey and interact with people? And I understand. And if you stay a little bit longer with me later

on, I'm going to address some really huge elephants in the room and also show you variation of this workflow, but with just human in the loop. So, we have our system message where we set the tone,

the rules in general, how we want this agent to act. Setting the roles like you're an expert business assistant. Do not use m dash symbol. This is really basic and you can be more creative or

add more information. And in the prompt, user message is actually the task, the job that we want it to do. So, take this JSON post text. This is the variable that is populated either by our

hard-coded actual post text or coming from triggery. And if it's coming from triggery, it will have this value and return null is a string and use slack tool. Otherwise, take this generate

message on the template below. So, hey, first name, I saw like my post about summary and post question with some additional instructions how to do it and some additional things. If you cannot do

it because you don't understand something, etc., then just use slack tool and let me know. And this if else is if it doesn't contain null then push it to hey reach where we have an HTTP

node where we are using an API of hey reach to push this lead with additional information this personalized message to this campaign. So we're using variables ID, profile URL, first name, last name,

personalized message, custom field, and this one note about this. We can do this in two different ways because the way hey rich works, every campaign has an associated list of leads. So we can

choose whether to push this lead to a list or directly to campaign. In my view, we should use add leads to campaign. So this paragraph explains it nicely. For example, we have a campaign

that's finished. If we add a lead to a list that is associated with this campaign, nothing will happen because that's the way how people behind Hey Reach envisioned it. But if we're adding

to the campaign, then the campaign will start again for newly added leads, which is in my personal view much better behavior for this case. So I would always use this and then follow the

instructions in the documentation how to craft this JSON and to send it to Kreach campaign. So when it comes to using chat model, I'm using chat GPT 4.1 mini. It's working well for me. Some other models

that I've tested really were behaving in a weird way. So this one is working well for now. And we have one tool, Slack tool, that is being used to send information if something goes wrong. So

this is like a guard railing and also making sure that we're notified if the agent gets confused or something is off or something is wrong. So if we open up Slack, we can see that these are all

messages that agent sent and said AI agent cannot generate the message post URL. So we can debug and see what's the with this post that's confusing our AI and this is something that I'm going to

show in a moment. So basically this is how this works and let me just execute one more time. Everything's fine and that's cool. So elephant in the room, should we let AI agent and any LLM, any

model just generate messages and send it to people? Maybe yes, maybe no. With our prompting and debugging and everything else, it could be okay. But if you don't trust it enough, I'm going to use this

same manual trigger because NN allows us to have only one trigger per workflow that is manual and switch it here. So I have variation of this workflow that is actually human in the loop. The

beginning is the same. So we can start it with trigify or manual. We're setting variables in the same exact fashion and then we're filtering out in the same exact fashion. This is just comment with

double t just in order for it to pass. The message is the same. The prompts are the same. The tool is the same. Everything is the same. So let's see what is happening here. Instead of just

pushing to hey reach, we are going to utilize Slack and be human in the loop. We can do it ourselves. Maybe we can assign a virtual assistant or someone from our team and let's see how this

works. So first of all we are giving AI agent to generate the message. Now we see this is waiting. This is a special node from Slack saying send message and wait for response. If I open my Slack we

will see this message. So this is a message that agent generated. And we have two options approve or decline. If I say approve everything goes well and it's pushed to hey reach. So if we want

to see how this is working when we decline the proposed message we'll start this workflow again and then we are going to decline what is happening is going in the loop and generating new

message and then we can see this is a different message and we decline again and it will do it again and we will be notified again and let's say okay this is fair enough we can use this so we

just close these and it will just pass everything to hey reach so this note mode we can say approve or disapprove based on that we will have these buttons just one button that is if we pick

approve only and options time to after time interval limit type if like after 10 minutes we don't act the workflow will continue so that's the difference and also I've adjusted this prompt so it

doesn't use slack as we used for triggery dummy data etc you will have this workflow so you can download and see how everything is working together. Some things that we should pay attention

to if we're launching and building. First of all, swap the test web hook URL for the production in triggery. Meaning this web hook, we have production URL and we should set this production URL in

this way here. Then hey, reach campaign ID in the variable. So this is the ID that we need to set in the variable if we haven't. So this is a good practice for any workflow, not just this one to

set here and say settings and error workflow error handler. So we can see how it looks like. So it's additional workflow that will be triggered if there's an error in our workflow. So

error workflow can be as simple as this. So we are notified when something happens. Make sure that we include the special tag in our post that we don't want to be processed. And one of the new

features in NAN is evaluations. And this is a little bit of a scope of this video because it would be too long. But it's something that I strongly believe we should all use. And it's a way to test

our workflows or AI agents. Similarly, we can test other things. Especially in software development, we have different types of tests. And because AI agent and LLMs are a little bit like a blackbox,

we can provide a spreadsheet with test cases and see how well it's generating content and whatever is doing what we want it to do. So, this is something that is super important. And again, we

have to conclude two different things. 100% automated and human in the loop. if we don't trust LLMs enough. So, we can approve or decline messages that are being sent either by us, our virtual

assistants, our marketing team, sales team, you name it. So, once again, head down to the description of this video to grab the template if you haven't already. This is because you can

implement it in an afternoon and have it start highquality conversations right away because it's that easy. But if you're still struggling a little bit what to say in your cold DMs and you

want to get really good at crafting DMs in general or for these automated systems, in this video we're going to take a look at Alex Hermos's best advice for sending cold DMs. If you're not

familiar with him, he basically grew his company to a $46.2 million evaluation and he exited it. And a massive part of that was going through cold DMs. So if there is anyone you want to listen to,

that's probably Alex. to see over there.
