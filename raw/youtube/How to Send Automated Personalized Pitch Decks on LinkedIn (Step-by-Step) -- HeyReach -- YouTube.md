# How to Send Automated Personalized Pitch Decks on LinkedIn (Step-by-Step)

Source: https://www.youtube.com/watch?v=5DGutgxI96o

While 99% of people are just sending normal textbased outreach on LinkedIn, I found a method which allows me to send personalized pitch decks at scale. And the best part is it is completely

automated. Using this system for one of my clients, they improved their reply rate on LinkedIn by 44%. So in this video, I'm going to show you how to set up this whole process from start to

finish. But firstly, let's get into the psychology behind it and why it works really well on LinkedIn. So on my screen at the moment I have an example of one of the automated pitch decks that I've

created using this flow. But just to give you some context here, this is a landing page analysis in the form of a pitch deck and it has a customized image at the top of the product that they're

using within their meta ad which is linked to that landing page. We have a bunch of value which we're providing up front on what's working well on their landing page, areas of improvement,

recommended changes which is all nicely formatted and looks very professional with the theme that we're using. We also have expected results improvements and we even have a CTA block at the bottom

here which has a link to my Google calendar so they can book a call directly with me. Now, of course, this is going to have the wow factor with most prospects. They're going to receive

the value upfront because we're going to be sending this in our first message, whereas one of the pitfalls of email outreach is you can't use links reliably in your first message because of

deliverability reasons. So you often have to ask for permission before you send a document to prevent your emails from going to spam and your email infrastructure going bad. Now on

LinkedIn, we don't have this issue because we can send it within the first message. So we're giving the value up front. This is going to pattern break. Secondly, we're going to hit home

potentially on some pain points here because they're running ads. They're going to want to improve their performance. And if you can improve the conversion rate of your landing page is

one of the easiest lowhanging fruit ways if you can do it effectively to automatically improve the performance of your ad campaigns without changing the creative or copy of the ads. Of course,

textbased approach can still work. We can still have personalization. We can still reach out on a pain point, but there's no way that this compares to a nicely presented pitch deck which shows

that we've researched a prospect. We're highlighting pain points and we aren't asking for time from them upfront. And a vast majority of your total addressable market are going to appreciate that

approach much more than your competitor who is being very spammy and is trying to book a call directly with them. Now let's move on to the workflow. So we're of course using three tools here. We're

using Clay for our prospecting and our data enrichment so we can build these automated pitch decks in the first place. We're using Gamma to facilitate the pitch deck creation and then we're

using Hey Reach to send our automated pitches at scale. This is a dummy campaign that I have created for the purpose of this video. I'm using Ampify to directly scrape from the meta ads

transparency suite using keyword searches. So once we've scraped the data set from Ampify, we need to clean it up a bit because there's lots of irrelevant columns from the scrape. And then we

have a final list of prospects for that particular category or niche. In this particular clay table, at the start of the flow, we'll have their Facebook ad URL, their FP page name, which usually

corresponds to their company name. We'll get their website, we'll get their ad copy, and a few other data points, which are useful. So, there's a few things I'm doing here. So, initially, I run the

meta ads enrichment here, and that's just because the meta ads count that I get from the initial Facebook ad scrape isn't accurate. So, I have to rerun this. This just gives me more

qualification data because I don't want to reach out to anyone that's running too little ads. So between 20 to a,000 is really going to be people that have probably been testing ads for a little

bit and they're actually spending a decent amount of budget on their ads. I then have some other enrichments which I run here which will help us later on with the ad enrichment flow. One of the

good things is from this meta ads page is we get the landing page URL for an example ad. So we can use this landing page URL for the analysis when it comes to our automated presentation decks. So

this gives us one example and then from that we can run this clagion prompt here to find more data about that landing page. So what this prompt is going to do is it's going to go to their website.

It's going to find their value proposition, their product name, their price, the niche here as well that it returns. And we also get a couple of other data points here in terms of their

ad launch date. So I want to see are they launching ads regularly here because this is potentially something we could also include in our pitch deck to make it seem more personalized. We have

their number of ad landing pages here and obviously we just output their number of ads that they are running on meta and then we have their ad text here which is from the initial Facebook ad

scrape. Now we have the base of our data. We have more than enough to work here. So we're able to now craft a prompt to analyze that landing page with a high degree of accuracy without us

even having to lift a finger. So this is where the magic starts to happen here in this flow. We have our ad image feedback prompt. Now, we initially run this to get the data which is going to make up

the bulk of the content of our presentation. So, what we're doing here is we're using Meta's recommendations for running ads on their platform. The reason I use this is because it helps

keep it very consistent between the different companies and the different products because we've got all different types of niches here. What we're using here is their landing page. So, we're

asking AI to go directly to the landing page and then provide feedback for us based on that landing page. and it's going to be looking for all of these points here that we've noted. If it

notices that the advertiser is not abiding by some of these best practices, we're then going to get the data for our content that we can add to the presentation. So, lower down in the

prompt here, we go in a bit more detail, right, about certain things. For context, I usually write a base prompt myself and then I send that base prompt to AI to then add on to my prompt. But

it's just so I can get things like this. Like this was something I hadn't even considered but it was like the font size. So like the readability that was something I would have never thought of

myself. Then we have the output format here. So I wanted four or five sections here. Firstly want a summary of the creative on the landing page. We want what's working well. In the majority of

occasions, right, people have been optimizing their landing pages. They're going to be doing some things well. So we want to make it seem realistic. We don't want to just be like, "Right, your

landing page is trash." Because it's not going to go down well with the prospect. We want to have a balanced analysis here. We then have what could be improved and then we have recommended

changes for better performance. And as I said here, we have the meta compliance risks here, but as they running meta ads, I decided not include this in the final output. And then what it's going

to do is it's going to output all of this data into a JSON object for me. So I had this which I again created with AI. Once I knew the format that I wanted to be created, I could then create it to

my specification, what was going to be easier for me. So each of those bullet points I asked it to output is going to do those into separate values and then I can pull those separate values into my

presentation prompt when we get to that stage. Also just for a bit of context on the model I'm using I am going a bit more expensive for this because it's important and I found that for this type

of task GPT 4.1 is going to be better. It's going to have a better output for the analysis because it's going to take longer to think and reason. The next part off of a flow is the fun part. So

this is when we're actually creating the HTTP API request for Gamma. Gamma is a AI tool which allows you to create websites or presentations with AI and we're using Gamma. So we're connecting

the API from Gamma and we're connecting that with Clay. We're using all the data that we've enriched within Clay and we can apply that to the prompt. So each presentation is hyperpersonalized to

each prospect. What we start with is this HTTP API request. We're initially starting with a post because we're sending data to Gamma and then we're using that endpoint URL here. Just to

note here, there is a website here. I'll probably include this in the description of the video. It seems really complicated, but as long as you follow each of these sections here, so each of

the sections which are available in the JSON body, right? So kind of the input text for the presentation, the text mode, the format, the AI image generation, the access options, and if

you follow each of these sections one by one, you won't have a problem building this yourself, even if you don't have any knowledge prior to that. So we have our method here. We're obviously posting

the data. So we're sending the data to Gamma. We have the endpoint which we've taken from the Gamma API instructions at the top here. So we can see we can just copy and paste this URL. And it's

similar with the headers, right? So we want to mimic the exact settings here. And as you can see, I've done that within the clay table. So we have all the settings here as well as you can see

the API key. We have application and JSON here. Then it goes about building our body. Now my recommendation here is to copy and paste this exact body because this is going to help you

immediately build out your text and then you can just edit the bits to your specification. And once you've copied and pasted here, you then can follow the instructions that Gamma provides you. So

you can think of the input text as the content which is going to be on each slide. I've split out the title page which is at the top here. Then we have summary of creative as you can see

what's working well, what could be improved, recommend changes for better performance and then our CTA block. So it's going to implement each of these slides with these page line breaks. I'm

saying to Gamma I want this content on different slides. And the way you can do that is again you follow the instructions which it sets out here which is in this section here. But

essentially all we're doing here is using this to split out cards. So we're using this little bit of code here between the different sections. And that's why you see when you go back to

mine, what clay actually does is it actually formats it how it's going to be seen on the other side. And as you can see with the summary of the creative here, you can see all the bullet points

of content which we have here across all of the bullet points for each of the sections here. Obviously on our last slide here, we don't really care about that. We just need a CTA block. So I

just provide my calendar link. And what it's going to do is actually going to input that into a CTA button within the deck. For these settings here, we're choosing preserve. Preserve just means

it's going to use the text that we've provided and it's going to make slight adjustments based on that. I know that there's roughly going to be seven cards based on, you know, having a CTA slide

and the five cards in the middle and then a title slide. And then we're splitting this by auto. I have additional instructions here. And this is mainly based on the imagery from the

presentation. In my experience, gamma AI imagery is almost non impossible to get right across the whole deck. But when you use it for one specific image, usually where this is best placed is in

the title. It's much much better with the shapes and the graphics, the text boxes, the CTA buttons. These are easier for the AI to process. When it comes to like photo realistic images, it will

often hallucinate. The images will look weird occasionally. So, what I prefer to do is keep it really simple and prompt it here. For non-title slides, you may include simple icons, vector symbols,

abstract shapes, colored boxes, callout elements, right? And then at the top here, I basically have the dynamic variable for the Facebook page and their product name. And what it's going to

then do is it's going to search on the web for that image. And the reason why it does that is because I've chosen the source here to be web all images. This is the key here is web all images

because it's actually just going to search for images on the web. and it's going to apply that one image to your title slide and in this case it's going to be personalized to that particular

brand. So if we have you know the product name is going to search for that exact product. If I go back to the example deck I'm showing earlier it's now showing the t-shirt that was being

sold by this particular brand. Now here we have a bunch of optional settings. So I haven't included this here but you can actually include your logo. You just need like um image web URL. You can

actually be really really clever here, but it's a bit sporadic and I took it out because you can't find it for every lead. But I was actually getting AI to scrape the logo image address from

websites. Then it would actually include the logo in the footer or the header of the slide for each slide like a normal presentation. You can also add card numbers to the bottom here. And then you

just have your access settings at the bottom. Now once this is all built out, now what we want to do is run this for each row. And all that's going to do is create the presentations within gamma.

Then from that, there's one more step that we need to do because we're still in clay and we haven't found people yet. So, we want to get the generation ID and then we want to get the presentation

URL. So, if I click on all of these, we have each presentation and they're all customized to the particular brand. We have a customized analysis for each brand. We have the PDF, we have a CTA.

So, as you can see here, this goes to my Google calendar where you can book a meeting. And this is applied to every single lead. So, I know everything's working now. And now we're ready to find

people. Now, the reason I don't find people yet is because I'm finding multiple people at these companies, and I don't want to run the presentation deck for each person. I'd rather run it

per company, and then I can link that presentation deck for each person at the company. So, now we're on the find people search here. I've just done a basic company search here for decision

makers, but obviously we're finding emails here. We've got their LinkedIn URLs and we're running a few other enrichments here which I just wanted to run as relevancy so I could split them

out into you know different segments. The key thing here is we just want to get the presentation URL so we can link it to each person. This is doing a company table data enrichment. So it's

basically finding all the company enrichment from our previous table and linking it to each of the people that we found from our people search. We're now ready to add them into our campaign. So

I have the API connected to Hey Reach. We're going to just show you the what we're including here. So I have my campaign. We have first name, last name, LinkedIn profile, all the data points we

need. And then of course we have a custom field at the bottom here for our presentation URL. So we can dynamically add this for each lead that we add into Hey Reach. So if I move over to Hey

Reach here, we have this draft campaign. It's a dummy campaign that we've created, but just so I can show you that the copy that I was using. And if we go into the campaign, what I tend to do

with this is that I want the presentation to do all the talking for my campaign. So we send a blank connection note. And then I just say first name, run a performance analysis

on one of your meta ad landing pages. Cheers. First name. The reason I do this is because it pattern breaks massively here. This is 100% going to be different to what anyone else is doing. Firstly,

we're actually sending them a customized presentation deck, which is already a bit of a wow factor. But secondly, usually people don't provide value upfront in the first place, which is a

bit of a pattern break. And the fact that we don't even have a CTA here is also another pattern break. It almost gives the air that we're not interested in the call. We're just sending you this

deck just to show you what you could improve. If you're interested, you're interested. If you're not, it's fine. Here we have obviously the fallback message, which is just great to connect

at this point. The reason being is because the whole message is around that personalized variable. So, if the presentation URL doesn't pull in, the message will not make sense at all. So,

I have to have a completely different fallback message at this point. Another pattern break thing I'm doing is I'm not even following up within the first few weeks. I'm just being very hands-off.

I've then got a follow-up for 3 weeks time and we're just saying managed to take a look. So, I'm only doing one follow-up. It's a very loweffort kind of follow-up here, but again, the

presentation is doing a lot of the talking for here. We do not want to distract from the presentation URL. We want them to click on the presentation URL. That's the main thing, but we've

done the work. We've spent quite a lot of money on each of these presentation decks. This is definitely reserved for like your golden prospects. You don't want to be doing this willy-nilly for

like your whole, let's say, like 10,000 people. But the whole aim of this is to get them to click on that presentation deck. Then for my fallback message here, I've just got a fallback message saying,

I've noticed some observations here. This is just in case something goes wrong, and then we're at least having some relevant outreach. Then I could go to Gamma, find the deck, and then send

them the URL manually. So, it's not lost the opportunity. We're still able to send them some kind of message. 99 times out of 100, you're not going to have this problem. It's just a safety

measure. And that's it. At this point, you just launch the campaign. Now, this is going to run autonomously for me. One of the things what you might want to do in Clay. Before you add to campaign, you

might want to turn off auto update off. And you might want to just quickly go through the decks to make sure there isn't any grave errors. Remember, we're relying on AI quite a lot here. And I'm

not going to try and lie to you that on the odd occasion there's not going to be an error. Usually they're quite minor though and you don't have to worry in the way that I've structured this

because we're giving the AI enough data to work from. And we're structuring the data in a way that is easy for the AI to consume. If we just chucked in a bunch of random data and it was not structured

and we didn't tell the AI which slide it should be inputting content and analysis, it would not work very well. Now, I just want to make a point on the cost here. For gamma, I'm spending, you

know, £20 a month for this. This gives me roughly 4,000 credits. That's going to be enough for roughly 500 to 600 decks. Then I'm obviously using chat GPT4.1

which is a little bit more costly. And because it's a heavy token resource prompt, it does cost like maybe 2 p per row as you can see here. And I would even recommend as you're running this

prompt for your first like 200 prospects, you should probably be checking the decks to make sure there's no errors. And then when you're confident there's a very low error

margin, you can then start scaling this without actually having to look at it. Now, as you're probably wondering to see some of the consistency here, you've seen this one that I showed you earlier

just to like show you that some of the analysis is actually correct here. If we look at their landing page, we can see some of the things that it's pulled out. So, the first one being CTA overload. As

you see here, there is a lot of CTAs. There's a lot of CTA buttons here. So, it's correct in what it's saying. People could argue it's a subjective thing, but it is correct in its output. As you can

see some of the recommend changes here, we go to simplify CTA hierarchy. It's saying only include add to bag above the fold. So it's very clear what the customer should be doing. It's a

worthwhile point. Move, unlock, reward, and subscribe below the first scroll. So when people scroll down, they're taking interest. They're then doing that. Add benefit tagline so we can spot another

thing here. We can't see above the fold here any USPS about the t-shirt. Why is it good for fitness? What is good about this particular t-shirt which sets it apart? So again, it's very valid

feedback here. And there should be some, you know, USP block or value proposition block which explains to customers why they're using this. So this is a bit different. This is a software product

which has been given here. An image from their website looks really really optimized. All the formatting is correct. We have nice blocks here with different icons, step-by-step

improvements that they can make. And then again we have a CTA block here. But the output is incredibly consistent, which honestly surprised me. I was very skeptical of how good a tool Gamma is.

If you give it a structured prompt, you're very explicit in what you want it to do, you can achieve consistency. But it all stems from our clay enrichment. If we didn't have clay interlin with

gamma, we wouldn't be able to achieve this. And of course, if we didn't have hay reach, we wouldn't be able to scale this on LinkedIn. Now, if you like this video, you're really going to like the

one on the screen right now because we go over the full automated system for building lead lists, enriching that data, sending hyperpersonalized DMs, and then converting them into new business.

It's a mustwatch if you're looking to grow and scale your business through LinkedIn. See you over there.
