from ao3funcs import *
from ao3requests import *
import csv
import os
import pandas as pd
import pickle
import sys

'''
Sample use of the work attribute classes. Works with any work search results/work browsing page. Does not work with bookmarked pages at this point
'''
def midpointsave(x): #super helpful if you want to pause and restart or if ao3 is having a bad day
    with open('pausedpage.pkl', 'wb') as f:
            pickle.dump(x, f)   


def getsearchdata(page, writer):
    n=1
    try:
        while True:
            if page == None:
                break
            else:
                response = Request(page)
                pageitem = response.objectify()
                items = pageitem.find('ol', {'class':'work index group'})
                listings = items.find_all('li', {'role':'article'})
                p=0
                for i in listings:
                    work = WorkAttributes(i)
                    datetime = work.datetime()
                    fandom = work.getfandom()

                    requireds = RequiredTags(i)
                    rating = requireds.getrating()
                    warning = requireds.getwarnings()
                    category = requireds.getcategory()
                    
                    attrs = TagAttributes(i)
                    relationship = attrs.getrelationship()
                    character = attrs.getcharacters()
                    freeform = attrs.getfreeforms()

                    stats = Stats(i)
                    language = stats.getlanguage()
                    wordcount = stats.getwords()
                    kudos = stats.getkudos()
                    hits = stats.gethits()
                    chapters = stats.getchapters()
                    writer.writerow({'Date Last Updated':datetime, 'Warnings':warning, 'Category':category, 'Ratings':rating, 'Fandom':fandom, 'Pairing':relationship, 'Character':character, 'Freeform':freeform, 'Word Count':wordcount, 'Kudos':kudos, 'Hits':hits, 'Language':language, 'Chapter Count':chapters})
                    p+=1
                    #logging.debug(f"work {p} of the page has been written to your csv")
                n+=1
                logging.info(f"page {n} souped")
            page = paginate(pageitem)
    except KeyboardInterrupt:
        midpointsave(page)
        #logging.info(f"interrupted by user at {n}, see log for details")
        sys.exit()
    except requests.exceptions.HTTPError as err:
        #logging.error(f"there's been an error getting the page: {err}")
        midpointsave(page)
        sys.exit()
    except Exception as e:
        #logging.error(f"there's been an error at page {n}: {e}")
        print("there's been an error, see log for details")
        midpointsave(page)
        sys.exit()


url = sys.argv[1]

filepath = sys.argv[2]
fieldnames = ['Date Last Updated', 'Warnings', 'Category', 'Ratings', 'Fandom', 'Pairing', 'Character', 'Freeform', 'Word Count', 'Kudos', 'Hits', 'Language', 'Chapter Count']

if not os.path.exists(filepath):
    with open(filepath, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        getsearchdata(page=url, writer=writer)
else:
    with open(filepath, 'a') as csvfile:
        with open('pausedpage.pkl', 'rb') as f:
            page = pickle.load(f)
        getsearchdata(page=page, writer=writer)

df = pd.read_csv(filepath)
df.drop_duplicates(inplace=True)
df.to_csv(filepath)
