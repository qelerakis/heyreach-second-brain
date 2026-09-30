# How to Turn Website Visitors Into Leads (Step‑by‑Step Tutorial)

Source: https://www.youtube.com/watch?v=ciDTangwkKk

Today, I'll be showing you how to build an incredible outreach system that takes your website visitors and sends them 100% personalized messages automatically. So, by the end of this,

you'll be able to not only understand how this system works, but to recreate it for your business, turning anonymous website traffic into qualified conversations without lifting a finger.

We're using a platform called RB2B. If you're not familiar, it belongs to a category of software platforms that we put a script on our website and the platform tries to identify visitors of

our website. Inside this platform, we can have a list of visitors that have been identified by RB2B. And then the natural question arises now that we have all of this information about the people

that visited our website, what to do with them? One of the options, pretty obvious one, is to reach out to them. We can do whatever we think it's a good approach. But what we're going to focus

now how to push these leads from RB2B in LinkedIn campaigns and email campaigns. That's why we are going to have a scenario one where we have only LinkedIn outreach as an option. And the second

one which seems a little bit more complicated and complex but it's not that complicated and complex when we have multi- channelannel emails and LinkedIn. First things first, if we go

inside RB2B in the integration section of the platform, we can see we already have a native direct integration with Hey Reach. You might ask a pretty logical question. Why should we even

consider NA10? It seems like overengineering things when we have a direct integration. And that would be a pretty valid question. And if we go to hay reach and go to integration section

and find RB2B and say okay let's see what we have here. So it seems like we can push all the leads in only one campaign which is okay but if we just look at RB2B what we can see is that we

have a section inside the platform that says hot leads about tagging. So we defined criteria and if a visitor fulfills this criteria it will receive a tag hot lead. Then we have another

section which says hot pages. So those are pages that we define from on our website that are super important to us. And finally when we take a look at the list of leads, we can see that some

leads can be hot lead only, hot page only or both hot lead and hot page depending on their activities and where they're working at and the title and the size of the company etc. depending on

how we define criteria for hot lead. That's why we are building a simple workflow for this. We have a web hook that is listening to events from RB2B. Whenever someone visits our website,

we'll be notified and we will receive information about this visitor. Then we have a switch node which just serves a purpose of routing leads depending on the tags. So this is the information

about the person about the visitor and then we have hot page hot lead or just hot page or just hot lead and based on that we have three different campaigns created inside hey reach so we can do

this granular approach now for the sake of clarity I didn't want to make it more complex but things that come to my mind what we could do additionally is to add an AI agent to help us with personalized

messages for every single visitor and or to scrape their company website and to tell us okay this company is from this industry and we can then do more filtering and say okay we want a

specific messaging for hot page hot lead visitors that are coming from specific industry etc etc so that's totally up to you but this is how we start also we have this branch here which is for

manual run I've pinned information that we got from our web hook so we don't have to rerun. We can listen for new events and we can go to this RB2B integration and get this test

information. And because the nature of RB2B, it's not the most efficient way to just listen for events and just wait for someone to visit our website. It can take a long time. That's why we're using

this test payload. Or we can trigger the workflow manually and pretty much do the same thing with one important difference and that is this. I just copied and pasted all the information that we're

getting from RB2B. And here I can play with different values for tags, for email address, for whatever I want to test out. And then I can build my workflow in a really efficient way. So

this is LinkedIn only. Let's switch to multi- channelannel. So here at the beginning, we have a web hook listening to RB2B events and I have a different branch and I have a schedule trigger.

Not because I want to have it scheduled and run this workflow at every day, every midnight. I'm just going to use this because scheduled trigger has one property that we can use it as a manual

trigger. We can execute it and at the same time N8N is allowing us to have only one manual trigger per workflow. So this is just a helper node to start the testing of our workflow. Then we have

also the payload that we can adjust and tweak and just have it whatever we want. And for this case, I've put here in a note what we're actually building. We can go about this in many many many

different ways. And this is just only one of them. And that is if we go back and analyze our leads, we'll see that a lot of them have their business email addresses here. If we view details,

we'll see that it says RB2B verified. So RB2B is verifying email addresses. And we can decide whether or not to trust it with this verification. Let's say we are. But there are people that have

Gmail addresses or they don't have email addresses at all. So again, we have multiple scenarios and we can handle them in different ways. Let's say if RB2B gives us valid business email

address, we're pushing it directly into an email campaign. If we have a Gmail address, I wouldn't use that address for the outreach. Why? Well, because this person didn't opt in with their private

email address. They didn't opt in at all. So reaching out to someone's personal email address about our offer can be also awkward. Here what we're building is first of all the information

is coming from a web hook. Then we're just checking does this email address that we got from rb2b contains gmail.com or is it empty? If not so we have a business email address. Go to switch

node. Similarly what we had for Hey Reach above. In this case we're using instantly for email campaigns. The main reason is instantly and hey reach have now two-way integration so we can

combine and have multi- channelannel outreach in both of those platforms. But what if we have a Gmail address or we don't have email address at all. We could push all of these people directly

into hey campaigns or we can try to enrich them. And for the enrichment I'm using full enrich and that's a platform that I've been using in inside my agency for our clients for over a year. How

does that look like? It can work. This is just for a single person. So we can either use LinkedIn URL which is cool or first name last name company domain. And when it comes to API we can use it and

we will programmatically through NA10 start enrichment task. This node is actually all about that. And of all of our fields, we can use only LinkedIn URL. That's enough for full enrich. And

this because we need to come up with unique name that will be shown here for every single enrichment task. We can do whatever. In this case, I just said test plus a random number from 1 to 10,000.

By the way, before we go any further, if you want to take this workflow and import it into your Nitain account and start running the system as soon as possible, there is a link in the

description where you can find it. Whenever we're using a platform that is asynchronous meaning we say hey platform here's a task for you and the platform says okay cool but I will need some time

to finish the task. So it's not instant result. We should be able to retrieve this information. We don't know when in the future the task will be finished. And some platforms say okay but yeah you

just need to pull that. This is just pulling the name of the mechanism when we're asking the platform hey are you done? Are you done until we get a positive answer or in the case of phone

they've built a mechanism that makes it even easier for us and phone rich says okay thanks for the task. I will take some time and don't worry I will let you know when I'm finished. And that's why

we're using this second trigger which says fullenrich trigger which is just a web hook note wrapped in a nice fullenrich paper. It has web hook URL that we copy and put in this note here.

Start a task and whenever you're ready and finished with the task send this information to this URL and we have this note listening for this information. And now when we receive this information,

this is information from fullenrich. And as we can see, they found email address that is deliverable. And here we are just testing to see, okay, is it deliverable? Cool, it is. And then we're

merging back those two branches into the switch node because now we have a business email address. We can just continue where we left off. If false then we have basically the same switch

as before as above for hey reach campaigns. That way we have a robust system which can handle a lot of different situations. Now let me just explain these two notes. In this

situation when we are basically deciding where to route leads based on tags. Is it hot page or hot lead or both? And that's cool. But when we give a task enrichment task to full enrich and it

returns back all the information we lost this information about tags because we just gave it blinked URL it did its job but we don't have tasks anymore so we are losing this information and one of

the solutions is to have a data persistency to have a place where data will not be lost we can use an external database we can use a spreadsheet or we can use a built-in nitn table feature

which serves the purpose of permanent storage which is fantastic for this kind of situations. So what I'm doing my train of thought was when I receive the information about the lead let's store

it right away in a table which we can go just to data tables create new one and I've created these columns by adding columns and then what I'm doing I'm just mapping incoming information to table

columns and I'm using upsert as an operation which means if this row exists just update it if it doesn't insert a new row and we need unique identifier in order for this note to be able to just

see what is the unique identifier and say I found the row in the table with this specific value in this specific column. So thus this row exists and I'm going to update only or I didn't find

and when I was thinking about which one to use which information I decided to be LinkedIn URL because that is going to be a unique value for every single person. So this is basically a key value that

we're going to use for checking if this person already exists in our table. Then when we finish with full enrich enrichment and what we have we have linked URL. So we can match and say okay

get rows and use LinkedIn URL to search the table and if you find a row just return back the information about this person and here we have tags. we retrieved the information about the

person from our NA10 table and that's why we can merge these branches and in either case have this value to be compared with these values. Naturally, this works really well if you have

traffic going to your website. So, if you want to see a video where I explain how you can generate qualified leads from completely cold traffic, click on a video in the overlay and I'll explain

exactly how you can book appointments with qualified leads, cold leads without lifting a finger.
