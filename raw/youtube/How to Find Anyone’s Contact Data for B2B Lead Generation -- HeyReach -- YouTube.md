# How to Find Anyone’s Contact Data for B2B Lead Generation

Source: https://www.youtube.com/watch?v=VSJRNAbuKf0

If you've ever scraped local or service-based businesses using a tool like Apollo or even Sales Navigator, I can guarantee you're missing the majority of your total addressable

market. So, in this video, I'll show you hands down the best method for scraping these hard to find leads so you can just copy it and do it for yourself. So, I'm on a tool called Apollo.io. You've

probably used it before. It's like the largest B2B database. Now, the issue with that when it comes to professional service or local service type businesses is that sometimes these companies don't

even need a LinkedIn company page or don't even bother with it. And even if there is a LinkedIn company page, the employees don't have listed that they work there. This is obviously an issue

and it is a massive blind spot where you'll miss a massive part of your TAM. And I'm going to exhibit that now by showing you a search function that correlates to the campaigns that I'm

about to show you today. So, if I go here and what we're going to do is we're going to choose industry first because we need to narrow down the search to a niche and this is the most applicable

niche. We then need to narrow this down further because if I scrape this list now, there's going to be a vast sum of companies here which aren't relevant to our target audience. So, what I'm going

to do is just type in clinic here. And then we're going to just make sure the account location is United Kingdom. And what we can see immediately here is there's only 1,300 results, which is

suspicious, especially considering that a lot of these companies might not even be relevant. It might be a clinic management software, for instance, that is in this list, which is list under

this criteria and has a relevant keyword. So, let's also show you from another source how this can be missed, right? So, if I remove these filters now, so the filters aren't getting in

the way of anything. If I then go here, this is actually a town near me and it's a clinic. I'm going to search this in the company search and see if we can find them. And what do you know, we

can't find them on Apollo. Paying for a tool like Apollo is quite expensive. And the method that I'm going to show using Google Maps is much cheaper. So before we get into the weeds of the automations

and the scraping, let me just show you the results of these campaigns across Hey Reach. So that's my LinkedIn automation platform and also instantly because I'm running both email and

LinkedIn campaigns using this method. So, what we can see on Hey Reach, we have this campaign which is running at the moment. It has a 32% connection acceptance rate across two accounts and

we're hitting a 24% reply rate which is really high. Then, if I go to our lead analytics and let me just show you the positive responses cuz obviously not all of those responses are positive. We can

see that we've roughly got around 31 positive responses. Now, not all of them closed, but that's a very good ratio considering we roughly reached out to around a,000 people. and it isn't the

most customized copy in the world because we have limited data on some of these people. So, we have to keep it relatively generic for some of the messaging. If I move over to instantly,

this is a very similar campaign and we can see that we had overall here 35 positive replies from this campaign from 1,500. So, very similar results on our email campaigns, which is to be

expected. So, we're seeing very similar levels of engagement from both of our campaigns. Now, if I didn't have this method, I wouldn't even be able to reach out to any of these people. So, you'll

see down here that there's actually a lot of personal emails, which is an indication of actually how hard this data is to find because a lot of the time I can't even find work emails for

these people and they might not even have work emails. They're just not online as much and they don't require to have the same infrastructure as a normal business. So, how do we actually run

this campaign? Initially, obviously, we've got to start with the scraper. Now, I use Google Map Scraper on Appify. It's relatively cost effective. There's probably other methods out there where

you could do it for a bit cheaper, but just for the convenience and the fact it has like integrations into some of the tools. It's the tool I use, but feel free to use other methods if you please.

So, the way the scraper works is you plug in your location here. You can put your search term in here if you please. The way I've preferred to do it is I do category. So, I literally chose every

single category which was relevant to clinics. And I was very meticulous about this so I could scrape every possible option. There's some in here which will be unqualified, but further along the

line, I use categorization to prevent me from having unqualified people in the list. And then we can literally press save and start. Now, the issue with this is that it's better to do city and

country rather than country as a whole. So, obviously, I want to maximize as many private clinics as possible, but I don't want to have to run this one by one for each location. And as you can

see, there's no bulkedit option here. So, I've got a bit of a workaround here which I'm going to quickly walk through for you. To be honest, it's not really needed. It only would take you probably

like an hour or so to do all of these runs manually by just copy and pasting the locations in. But I've created this method because I often run these scrapers. So, it's going to be in the

link in the description. You can take it for yourself and you don't have to do any of the work. So, we first start in clay for this method. And what we need to do is we need to find cities and the

country and then formulate this. So into a search term like this so it fits the specification for the scraper. I just go to chat GPT and just tell me can you list all the major cities in the UK and

then after that point I can go a bit more granular if I feel like it's missed some results. But that's going to give me pretty good coverage straight away. I then have this HTTP API where it's

essentially going to start the run with all my settings from the appy scraper. Now this looks really complex but I didn't actually do any of this. So, if I go back to my Google map scraper, I can

just plug in the settings that I want, go to JSON at the top, and just copy and paste this. This will automatically write our JSON object for us without us having to do it. And then, if we go back

to the clay table, all we need to do is change the location and then this is going to dynamically change for each row. So, once we've done that, you'll see there's a few errors here. The

reason that is is because on my plan, I can only run so many at a time. So, you're going to have to do this in batches. So when it starts to run in ampify, we'll then get this data and

we'll be able to find the data set ID. So this is really crucial. We don't need to create a new column, but then we can create another HTTP API. And this is going to get our data sent over to NA10.

And what I've done here is I've just created a little JSON object. It's very simple, but it's just going to type in the location data, and it's going to give me the specific data set ID for

that particular run in Apify. And that's going to be very crucial so we can then consolidate this data into one file. So if I go over to NAN, it's an extremely simple workflow. I'm not going to go

into the really nitty-gritty here, but essentially there's a web hook here and all this is doing is when I press play and clay, it's then going to automatically get pulled through to NAN

and then it's going to get the run data from that data set ID which is here. And you can change this with the link and then it's going to dynamically change for each of our runs. If you want to

find what that looks like in Appify, you can just go over to API, go to API endpoints and you'll be able to find everything you need within here if you want to set something up yourself. So

once we get the run data, we then send this back to Clay. Now you're probably thinking, why didn't I just use NAN for this whole flow? Now the reason for that is because when you run a run within

ampify it will do it in one big piece of data so that when I take one of these dynamic variables such as the data set ID it will only do it for one of the runs. The beauty of clay is it's already

formatted in a way where is rowby row. So when one of these runs it will then send it to NA10 in one and then it will run through the workflow. What will happen in NA10 is it runs everything in

one go which creates issues. Before we get any further, I just wanted to quickly mention that you can grab this whole workflow for completely free in the link in the description. All you

have to do is download it, import it into your NA10 and Clay account, and then customize it to your specific use case. So now we've ran all our Google Maps scrapes simultaneously, and we've

consolidated all that data automatically with the help of Clay and NA10. We now have our final list of clinics, which we can enrich further. So here are all my London clinics. So, I've managed to find

19,220. If we compare that to the Apollo method, how many could we find? We only had 1,300, which really shows the difference in the two methods. At this point, we've

already got some really good data, right? We've got their name, their phone number. Now, we've got the company data. We need to now find the decision makers, but I also need to do some

qualification. Now, I'm not going to go into the weeds of this. I'm just going to show you roughly what I did. We're only interested in private clinics. So, I've set up this prompt to search on

their website. It's very obvious if they're NHS. If you're watching from the US or somewhere else, it's basically National Health Service. We're not interested in these leads because

they're linked to the government. They don't work privately. They have their own systems. They have less budget. They're not relevant to the particular service offering. So, this will come

back with a very accurate answer. And I can completely exclude all the NHS leads for now. I like to find their generic email address because sometimes it can actually be helpful to reach out to some

of these people. Some of these clinics are quite small. So they might only have one email address which is the point of contact. So it just lengthens our ability to reach out to certain people.

We have a booking page URL. I'm not going to get into the weeds of that. We're just interested in if they're using certain booking software. And we also have a couple of other rows here

which are essentially pulling. So for example in their booking page URL they'll have Clino which is a clinic management software and I can take extract this from the URL. This is

relevant to our campaign. So it's very useful for us because I can do different copy to this particular person because the particular offering that we have is linked to this software and it's elicits

a positive signal for what we are actually offering. We also have a similar one for e-rescriber here. All of this I'm just mentioning to you because it just shows you my thought process and

making sure when you get a list in your first four should be right qualification. We need to make the list more tight because it's going to make a dramatic difference to our results. The

main interesting prompt which you will need to apply to your scrape is this one here. So what this does is it will go to their website. It will track their about us page, their team page, and it will

return a list of people that work at that clinic and their job title. I've made this specific to doctors because they were relevant to us. But it actually does scrape kind of clinic

managers as well. And what it's going to return is going to return their full name, their job title, and if it can find a contact email, it will do that because sometimes a contact email is

available. And what this will do is we will then get a list of all the doctors that work at the clinic. These people might not have been linked to the clinic on platforms like LinkedIn or Apollo. So

we would completely miss this data, but the website often has bits of data and I actually run these prompts sometimes even for very online businesses because some people just aren't on LinkedIn or

some people just aren't on Apollo. So it's a very good method for finding more of those people, more relevant decision makers at those clinics. And you can see here how successful this is. So for this

particular clinic, we were able to find over 41 doctors for this just one clinic. Each of these people is a wein for us selling this offering. If I was going to go on Apollo, we might have

found two. So you can take this prompt. It will be in the clay table template. You'll have to adjust it to make it relevant for your particular target market. But for the most part, you'll be

able to plug and play. So now we've got our people data. Now obviously we need to cleanse that people data. And we also need to enrich it with contact details. I'm going to go over to the second table

which has all of our people in here. So this has a full list which is pulled from this other table. Now the way you do this, this is actually very critical is you need to write to other table. So

you create a new table. You can just keep it blank. You go to edit column. So what we can do here is we choose the table to write to. So that's the one we've just created. And then you want to

select from a list, right? So if I just get rid of this and I go like this, we can go to that doctor list. And you can see the list of items here. So that's all the doctors that we pulled from the

websites for that particular lead. You want to click here because that's going to list all of the people on a separate row. So now this will pull all of the doctors that are relevant to that

particular clinic and we'll have all the other data points as well because we can map these and create columns. So when you go here, you're going to search like for let's say like full name in this

instance. What you're going to do is you can then just create a new column and it will just copy the name of that column and then we can pull all the relevant bits of data that we want. So we need to

do this for the doctor's list and then we also need to do it for other data points that are not within that JSON object. Now that's very important because I've made that mistake before

where I assumed that just pulling this will then I'll have all the other relevant data points. But no, you actually need to map the other data points that you want. And then this will

just pull all the data for all the particular doctors in rows into the other table. So like you can see if I go to doctor's London clinics. Now you can see that we have now multiple people at

this clinic listed on separate rows which is obviously important for our enrichments. So a couple of little important formatting problems that we have when we do this method is that it

will just scrape the full name. Now you could actually adjust the prompt if you want to split out first name or second name. It will use a little bit more resource from the API key. So I tend to

simplify it. There's more things that can go wrong. I rather do a second prompt after the fact. So at this stage we obviously need to extract the first name because we will just have full name

and it'll be like Dr. Rita second name, right? So we need to extract that first name which I have with this particular prompt here which you can see. So, it's basically going to look at the full name

and it's going to pull the first name. Sometimes there isn't a first name, in which case it's then going to do doctor at the start of it instead if it only has like an initial because sometimes

that happens like you see here. It's going to do Dr. Sloan instead of, you know, Dr. Rob Sloan because that would look weird when we come to our email or LinkedIn copy. So, that cleans that up.

So we have a clean list of names, but we also want to just qualify that they're 100% doctors or people that we want to reach out to, right? So I have this role category which also runs a prompt where

it's going to look at job title, full name and title and category name. So I fed it a bunch of data which is existing within the table and I'm asking it to give me a right answer. Now it might not

be 100% accurate but if it can make it you know 95% accurate is much better than nothing. So, I always recommend making sure you always think about cleansing your list as much as possible

because it's going to have a dramatic effect on your ability to get results efficiently. But make sure you do it with an API key, right? You definitely need an API key for this because

otherwise it will get ridiculously expensive using Clay. And then the rest is relatively simple here. So, when I know they're doctors and when I know I've got the relevant first name, right,

we can then find their personal email. We can find their work email. I have a prompt in here to find their LinkedIn URL. So, I will essentially use their first name and job title to find their

LinkedIn URL. So, it will just go to Google, do a search, find the relevant person, pull the LinkedIn URL if it can find it, and then it will output it here for me with no other text. I can then

use that to try and find personal email because you usually need a professional social network in order to find personal emails linked to an account. I have two different tools I'm using for that. And

then I'm also using Lead Magic to find their work email. You can actually see here that we're unable to find quite a lot of work emails. And that's purely because of how niche and small some of

these clinics are and how the lack of information or data on them online, which is why I stack on these personal email enrichments. And then we obviously have our generic contact emails as well,

which we can use as our fallback option if we want to. So now we have a clean list. We have all our personalized variables. We're able to now add these to campaigns. And guess what? We've got

an absolutely ginormous amount of data. There is no way you would have found 30,000 people by using a method like Apollo or even sales navigator for this type of list. And if you are finding

that amount, that tells me that a lot of your list is going to be unqualified. So these go into our campaigns. And of course, that's where you need to theorize what your copy is going to be,

what your offer is, so you can get really good results from the data that you've just scraped. You just saw how you can actually acquire difficult to find data and reach out to those leads

personally using platforms like Hey Reach. But if you really really want to dial in your outbound, please click the video to the side of me where we go over the lessons we've learned from sending

over 5 million LinkedIn DMs so you can skip the learning phase, gain some insights, and generate a ton of pipeline for you and your business. See you over there.
