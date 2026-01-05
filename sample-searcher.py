import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import sys
from ao3funcs import *

url_orig = input("copy and paste the search url you are using")

q = input("have you filtered your search? y or n") #if you just click on a tag without adding additional filters, there's a different url parameter

date_update = []
category = []
warning = []
completion = []
rating = []
fandom = []
relationship = []
character = []
freeform = []
words = []
kudos = []
hits = []
language = []
            

start_page = int(input("what is your first page to grab?"))
end_page = int(input("what is the last page to grab?"))


for num in range(start_page, end_page + 1):
    match q:
        case "y":
            url = url_orig + "&page=" + str(num)
        case "n":
            url = url_orig + "?page=" + str(num)
    try:
        response = requests.get(url, headers = {'user-agent': 'bot'})
        html = response.content
        soup = bs(html, 'html.parser')
        work_container = soup.find("ol", class_="work index group")
        try:
            workitems = work_container.find_all('li', {'role':'article'})
        except AttributeError:
            print(f"attribute error at page {num}, should not be an issue") #when i do this i get random attribute errors, but it never actually causes an issue, and i haven't figured out why yet
        print(f"page {num} has been souped, getting data now")

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print(f"404 Error at page {num}, see {url} for details")
        elif err.response.status_code == 429:
            print(f"too many requests error, take a minute and restart with page {num}") #if you get this, please be a good person and add a few seconds to your timing
        a = input("do you want to continue making a csv with what has been scanned?")
        match a:
            case "y":
                break
            case "n":
                sys.exit()

    for i in workitems:
        try:
            work = workAttributes(i)

            datetimetag = work.getDateTime()
            date_update.append(datetimetag)

            fandomtag = work.getFandom()
            fandom.append(fandomtag)


            req = work.reqTagBlock()
            reqblock = requiredTags(req)#you might be able to loop this bit, but i couldn't figure out the best way to

            ratingtag = reqblock.getRating()
            rating.append(ratingtag)

            warningtag = reqblock.getWarnings()
            warning.append(warningtag)

            categorytag = reqblock.getCategory()
            category.append(categorytag)

            completiontag = reqblock.getCompletionStat()
            completion.append(completiontag)


            tag = work.tagBlock()
            tagblock = tagAttributes(tag)

            relationshiptag = tagblock.getRelationship()
            relationship.append(relationshiptag)

            charactertag = tagblock.getCharacters()
            character.append(charactertag)

            freeformtag = tagblock.getFreeforms()
            freeform.append(freeformtag)

            stat = work.statsBlock()
            statblock = stats(stat)

            lang = statblock.getLanguage()
            language.append(lang)

            wordcount = statblock.getWords()
            words.append(wordcount)

            kuds = statblock.getKudos()
            kudos.append(kuds)

            hit = statblock.getHits()
            hits.append(hit)
        except AttributeError:
            pass

    time.sleep(6)
    print(f"page {num} has been added to your csv")

data = {
    "Date_Updated": pd.Series(date_update),
    "Fandom": pd.Series(fandom),
    "Category": pd.Series(category),
    "Warnings" : pd.Series(warning),
    "Completion Status": pd.Series(completion),
    "Rating": pd.Series(rating),
    "Pairing": pd.Series(relationship),
    "Characters": pd.Series(character),
    "Freeform": pd.Series(freeform),
    "Word Count": pd.Series(words),
    "Language": pd.Series(language),
    "Kudos": pd.Series(kudos),
    "Hits": pd.Series(hits)
    }

df = pd.DataFrame(data)
print(f"a dataframe with {len(df)} rows has been created")

#df.to_csv(path/to/your/new/csv)
#print("go to your folder to see your new csv! bye now, i've sold you to one direction")
