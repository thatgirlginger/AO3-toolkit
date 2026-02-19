import logging
import pickle
import sys
import requests
import time
from .ao3funcs import WorkAttributes, RequiredTags, TagAttributes, Stats
from .ao3requests import Request, paginate

'''
loops through pages in a selection and retrieves work data from them
'''
def midpointsave(x):
    with open('/Users/gingermaemiller/Desktop/ao3data/pausedpage.pkl', 'wb') as f:
        pickle.dump(x, f)    

def getsearchdata(page, writer):
    #logging.debug(f"log for scraping search {page}")
    n=1
    try:
        while True:
            if page is None:
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
                    fandom = work.fandom()

                    requireds = RequiredTags(i)
                    rating = requireds.rating()
                    warning = requireds.warnings()
                    category = requireds.category()

                    attrs = TagAttributes(i)
                    relationship = attrs.ships()
                    character = attrs.characters()
                    freeform = attrs.freeforms()

                    stats = Stats(i)
                    language = stats.language()
                    wordcount = stats.words()
                    kudos = stats.kudos()
                    hits = stats.hits()
                    chapters = stats.chapters()
                    writer.writerow({'Date Last Updated':datetime, 'Warnings':warning, 'Category':category, 'Ratings':rating, 'Fandom':fandom,  'Pairing':relationship, 'Character':character, 'Freeform':freeform, 'Word Count':wordcount, 'Kudos':kudos, 'Hits':hits, 'Language':language, 'Chapter Count':chapters})
                    p+=1
                    #logging.debug(f"work {p} of the page has been written to your csv")
                n+=1
                logging.info(f"page {n} souped")
            page = paginate(pageitem)
            time.sleep(6)
    except KeyboardInterrupt:
        midpointsave(page)
        #logging.info(f"interrupted by user at {n}, see log for details")
        sys.exit()
    except requests.exceptions.HTTPError as err:
        #logging.error(f"there's been an error getting the page, {err}")
        midpointsave(page)
        sys.exit()
