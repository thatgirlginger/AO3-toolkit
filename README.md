# AO3-Scraper-Tools
a python set for scraping and getting AO3 fanfiction data for given parameters compatible with Python3

this particular AO3 scraping repository is made customizable to what you want to do with your project. i've included a couple of sample scripts, just to show how i use these in gathering data on individual search criteria and whatnot

please be mindful of AO3's requests regarding web scraping. set user headers to "bot", implement a generous request timing, and don't scrape on weekends (I can't find a public version of that last one, but I was recommended by an OTW volunteer staffer when I reached out regarding recommendations to ensure that I avoided overloading the site and respected users' wishes for their content)

reference here:
https://www.transformativeworks.org/ai-and-data-scraping-on-the-archive/


the copyright license for this work strictly prohibits the code's use for AI training purposes

## to get started
i'm in the process of turning this into a package, but i want to make it as efficient as possible before i do so. for the time being, much of the functions are set up to be used in many different cases. if you are just using them to get data from a straightforward search, i've included a sample script to get started and see how it all works. 

### python dependencies
this repo uses BeautifulSoup, requests, and pandas. as any good python user would advise, create a venv and install
```
$ python3 -m venv <name-your-env>
$ source <your-env>/bin/activate
$ pip install requests
$ pip install bs4
$ pip install pandas
```
to get the repo itself:
```
$ git clone https://github.com/thatgirlginger/AO3-toolkit
```

### what each bit does

ao3requests.py essentially carries out all of the requests sent to AO3, including pagination (if you are trying to gather data across multiple pages)

ao3funcs.py is for getting work attributes from an individual work listing. As I update this and shape it into a package, I'll implement other ways to get from point A (search page) to point B (navigable work listing)

tagequiv.py holds the functions for retrieving all relatives of a tag, including its parent tags, sibling tags, and subtags. Because of the way AO3 is organized, this can be extremely helpful in organizing data (if, say, you want aggregate freeform tag behaviors for a certain fandom or ship but authors take a lot of liberty with what their tag strings actually say, or you wanted to track variation on a set of freeform tags)

counters.py takes each kind of tag in a given dataset, counts, and returns them. good for finding the most or least popular tag associations in a given set

### i just want to gather tag stats what about that

that's what getworks.py is for! it takes a given set of works (like a work search result or work browsing page) and returns a dataset. I have not modified it to include versions that check and condense for tag equivalencies, but that's next on the list

to use it:

```
$ python3 getworks.py <path-to-your-csv-.csv> <url-to-scrape>
```
as ao3 users know too well, the server likes to just Do Stuff sometimes. if that happens, this code has a catch built-in: it pickles the url of whatever page you were on when the Thing happened. since the code writes to the csv line by line, if there's an exception that side of things will be fine. If you run it again, make sure you use the same filepath. it doesn't matter too much if you use the url or not, because no matter what it'll set the url to scrape as whatever you pickled.

### if there's any issues
please don't hesitate to send in an issue or submit a pull request! I'm still learning a lot of things, so any of this is a teachable moment for me :-)


thank you to alexwlchan(https://github.com/alexwlchan/ao3), radiolorian(https://github.com/radiolarian/AO3Scraper) and toastystats(https://github.com/fandomstats/toastystats) for the work they've done so far in this vein!! i have taken a lot of inspiration from the code that they have written thus far

i'm on tumblr as secretly-historic; i'd love to see any cool things made with this repo!
