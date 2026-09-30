# The AI Agent Every LinkedIn Outreach Campaign Needs

Source: https://www.youtube.com/watch?v=uNjuWkvK3IU

In this video, I'm going to show you how to set up an amazing N8N automation that captures every LinkedIn reply from our outreach campaigns, analyzes the sentiment of conversations using AI, and

finally saves everything to our CRM. Today we are talking about super important topic and that is how we should handle replies from hey campaigns programmatically. This is important

because we have web hook support in hay reach and up until very recently the only event that we had at our disposal regarding messages was only for first message reply received. Good news is

that we have a new event that says every message/inmail reply received. Whenever a reply comes in we will be notified through a web hook. So I'm going to save this and turn

to my N8N account. So this is the setup. First, we want to be notified whenever we have a reply in one of our campaigns. When we start a conversation through Hey Reach, we can choose if we want to

handle those conversations through LinkedIn or hey reach inbox. Regardless, hey reach will take notice of those conversations will show them inside her reach inbox and notify us through a web

hooks. We want to save the complete conversation with our leads in our CRM. In this case, I'm using Hopspot. It's easy to use. You can use whichever serum you prefer. So to show you this is an

example of data format. I want to have the time stamp who sent the message, the message itself. This is a real message with one of my colleagues and this is a custom field that I've created inside

HubSpot. And the second thing is the sentiment of this conversation. Is it positive, negative, neutral? And for that we are going to have a helping hand, an AI agent that will help us

determine the sentiment. I picked this task on purpose because determining sentiment is kind of tricky to squeeze every single conversation into these three boxes. And sentiment is not set in

stone. It can change with every single message. What I mean by that is, for example, we send a connection request message and someone accepts the request and replies back and we're saying

something along the lines, hey, curious, how are you handling X, Y, and Zed when it comes to sales metrics? because we are solving A, B and C. Would you like to hear more? And they say, "Yeah,

sure." So the sentiment of this conversation is positive. Then for whatever reason, they ghost us. We fall back and then they say, "Oh, sorry. We are busy. We're in the middle of

something. Let's push this to next quarter." And now it's like a neutral, negative, not now kind of sentiment. So because of it, we have to analyze the whole thread of messages every time we

get a new message. Let me just quickly run this workflow and then we are going to explain node by node. Before we break down each node in detail, you can grab this exact NA10 workflow template from

the description below 100% for free. It includes all API calls, the AI sentiment analysis prompt, HubSpot integration, and evaluation setup that we're covering today. All you have to do is download

it, import into your N810 account, and adjust it for your use case. So here first of all I'm simulating a reply coming in. I've pinned some of the information so I can use those for

developing the whole workflow. So what happened? We received a data about this event. First things first we have the information about the message. So this is the message that we received from the

lead. The timestamp the text of the message that this property is it reply. Then conversation ID super important. Then information about campaign, about the sender, information about the lead,

then the information about the list they're in, the time stamp, event type. Now the second note is to set variables that are going to be used across the workflow. In this case, maybe this can

be skipped because here I have only API key for hey reach. So let's imagine we had multiple API calls. It's much easier to have one variable or some variable that is for something else. So what I'm

doing here, I'm using an API call to hey reach and saying hey look the information gave me through a web hook fantastic super useful but I'm lacking some information in order for me to do

what I want to do in my use case. So I've made these sticky notes with a lot of additional information explanations and here we have a link direct link to the API endpoint that I'm going to

trigger and it's called get chat room. So this is the URL. We need account ID. That's a ID of the LinkedIn account that is used for starting conversation and conversation ID. Luckily, we have

everything that we need from web hook data. So if I open this node, we'll see these two dynamic fields that are filled from web hook. So sender, this is the ID that was assigned inside a reach and

conversation ID. Those are things that we need. we got from the API information they're describing this whole conversation and the most important thing is messages now we have all the

messages that we need to assess the sentiment of the conversation and everything along those ways so the next node the whole idea what I want to do is from JSON format that I have all these

messages in I want to create this to convert JSON format data into just plain text or string type of data so I can process it later in different ways. So this code is doing exactly that. This

code is actually just iterating or aka going through the collection of messages and is just creating the sender. I want to have who sent the message and this operator is just saying the value of

this property sender is me. Then take my name and last name to just connect those values with an empty space. So I'm getting Nana Pablo versus if it's not this value or it's correspondent or

anything else just take these values of the correspondent first name and last name. That's it. That's the whole magic. And here is just formatting. So I want to have timestamp. I want to have who is

the sender and the message body an empty row and that's it. Now we have our AI agent. The system message is you're just an expert business assistant helping to determine the sentiment of LinkedIn

communication. Super simple. So explaining what we want to do and we're feeding it this text version of the whole thread and telling it to just output one of four possible values and

explaining what positive means, what negative means, neutral, unsure, etc. And then ultimately we are saving that to our HubSpot found our custom properties and said okay LinkedIn reply

save these messages in this textual form or a LinkedIn sentiment response and that's it. When it comes to this AI part, your imagination is the limit. In your case, maybe you want to make this

AI agent or multiple agents suggest a reply based on the whole thread or which lead magnet we should send to a person if the sentiment is neutral. Maybe they say, "Okay, not now. Let's connect in a

month or so." And then we can say, "Okay, cool. But here, farewell gift." Something that might be useful. We can analyze their company size, their role in the company and based on that to

determine which kind of material we should send them or to put human in the loop with Slack messages that we can approve or decline the suggestion of AI etc etc. If you want to see me build

those kind of scenarios just let me know in the comments and I will upgrade this workflow with additional things. Now, I want to talk about evaluations. Why they're super powerful and important.

Evaluations serve the purpose of testing our AI prompts and agents. We need some kind of way to test our prompts and the model that we've picked. And if we hover here, we'll see like production

checklist setup error notifications that refers to in our settings stating which workflow is error handler. And it's here. just create a workflow set error trigger as the beginning and maybe Slack

or whichever channel you want to be notified to and that's it. So the second item is test relability of AI steps referring to evaluations. So in order for us to use evaluations in our

workflow first step is to add this trigger note of evaluations. Here we need to connect with our Google Sheets account or Google account because N10 is expecting Google Sheets test data in a

Google sheet. And let me show you how it looks like. So here it is. And the idea behind this is that every row is one test. The structure of this document is not set in stone. There is no

standardization when it comes to number of columns, the names of columns or anything that regard. We can create it as we see fit. In this case, I have some number of fake conversations that I've

created to simulate the different sentiments. So this is what one person the second person etc etc and I call this column messages. Then I have the second column where I just wanted to

call it expected sentiment and say okay I expect this sentiment to be categorized as neutral. So here in this node we can choose the method whether stating the ID of the spreadsheet or the

name or just picking the spreadsheet and at the end we need to have at least this evaluation set outputs note where also state in which sheet the evaluation should push the output values in and the

name of the column and the value. So let me demonstrate instead of starting the whole workflow from here from this node I'm going to start from here. So from this evaluation trigger note and I'm

going to start and if we take a look at the log we'll see that the evaluation will take row by row this data feed it into AI agent. A agent will apply our prompt and finally this node will push

into our spreadsheet some values and we can check and see for example in this case these values match our expected values. If we had a mismatch that would just mean that for this test data AI

agent model is interpreting these messages differently when it comes to sentiment. So we know for sure then we should improve our prompts. We can improve and until we get desired

results. If you take a look at NA10 evaluation documentation, you'll see there is light evaluations, metricbased evaluations. This type is light evaluations. It's recommended to use

when building workflow. So for general adjustments but when we start having production data then we can do metric based and go into nitty-gritty details etc etc. I'm not going to cover that in

this video. What I just showed you is great if you already have conversations going. But what if you need new leads in your CRM to reach out to? If that's you check out the next video where we show

you how to generate potentially unlimited leads with a workflow that includes NA10 hey reach and clay like I just showed you in this video. See over there.
