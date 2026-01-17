import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import sys
from getsearchdata import *

firsturl = "" #replace this with your starting url

def requestfunc(url, num):
                url = f"{link}&page={num}"
                try:
                    response = requests.get(url, headers = {'user-agent': 'bot'})
                    html = response.content
                    soup = bs(html, 'html.parser')
                    work_container = soup.find("ol", class_="work index group")
                    workitems = work_container.find_all('li', {'role':'article'})
                except AttributeError:
                    pass
                return workitems
def makepagelist(startpage, endpage):
            pagelist = []
            for i in range (int(startpage), int(endpage) + 1):
                        pagelist.append(i)
            return pagelist
def datafunc(num):
            try:
                workitems = requestfunc(url_orig, num)
            except requests.exceptions.HTTPError as err:
                if err.response.status_code == 404:
                    print(f"404 Error at page {num}")
                elif err.response.status_code == 429:
                    print(f"too many requests error, take a minute and restart with page {num}") #if you get this, please be a good person and add a few seconds to your timing
                break
            print(f"page {num} has been souped")
            for i in workitems:
                try:
                    work = workAttributes(i)
                    datetime = work.getDateTime()
                    fandom = work.getFandom()

                    req = work.reqTagBlock()
                    reqblock = requiredTags(req)

                    rating = reqblock.getRating()
                    warning = reqblock.getWarnings()

                    tag = work.tagBlock()
                    tagblock = tagAttributes(tag)

                    relationship = tagblock.getRelationship()
                    character = tagblock.getCharacters()
                    freeform = tagblock.getFreeforms()

                    stat = work.statsBlock()
                    statblock = stats(stat)

                    language = statblock.getLanguage()
                    wordcount = statblock.getWords()
                    kudos = statblock.getKudos()
                    hits = statblock.getHits()
                except AttributeError:
                    pass
                writer.writerow({'Date Last Updated':datetime, 'Warnings':warning, 'Ratings':rating, 'Fandom':fandom, 'Pairing':relationship, 'Character':character, 'Freeform':freeform, 'Word Count':wordcount, 'Kudos':kudos, 'Hits':hits, 'Language':language})
            time.sleep(6)
            print(f"page {num} has been added to your csv")

def datafuncloop(url_orig, pagelist):
    global pages_to_retry
    pages_to_retry = []
    for num in pagelist:
        try:
            datafunc(num)
        except KeyboardInterrupt:
            print(f"keyboard interrrupt at page {num}")
            break
        except Exception as e:
            print(f"there's been another kind of exception: {e}\nadding {num} to list of pages to retry")
            pages_to_retry.append(num)

startpage = "" #set an integer for a startpage
endpage = "" #same here
pagelist = makepagelist(startpage, endpage)

filepath = "" #filepath here
fieldnames = ['Date Last Updated', 'Warnings', 'Ratings', 'Fandom', 'Pairing', 'Character', 'Freeform', 'Word Count', 'Kudos', 'Hits', 'Language']

if os.path.exists(filepath):
            with open(filepath, 'a') as file:
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        datafuncloop(firsturl, pagelist)

else:
            with open(filepath, 'w') as file:
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        writer.writeheader()
                        datafuncloop(firsturl, pagelist)

#this next part will automatically go through and retry if there are error pages, i have not built it in yet to retry if they return an error again but i'm working on it

count = len(pages_to_retry)
if count > 0:
            with open(filepath, 'a') as file:
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        datafuncloop(firsturl, pages_to_retry)
else:
            print("finished! selling you to One Direction now")
