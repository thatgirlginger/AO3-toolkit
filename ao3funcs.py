from bs4 import BeautifulSoup as bs

'''
these classes find and retrieve different work attributes
'''

class WorkAttributes:
    info="functions to get the top-level work attributes"
    def __init__(self, item):
        self.item = item
    def datetime(self):
        dateclass = self.item.find('p', {'class':'datetime'})
        date = dateclass.get_text()
        return date 
    def getfandom(self):
        heading = self.item.find('h5', {'class':'fandoms heading'})
        fandoms = heading.find_all('a', {'class':'tag'})
        fandommultis = []
        for i in fandoms:
            domfan = i.get_text()
            fandommultis.append(domfan)
        if len(fandommultis) > 1:
            fandomslist = '+'.join(fandommultis)
        else:
            fandomslist = fandommultis[0]
        return fandomslist
    def reqtagblock(self):
        req = self.item.find('ul', {'class':'required-tags'})
        return req
    def attrtagblock(self):
        tags = self.item.find('ul', {'class':'tags commas'})
        return tags
    def statsblock(self):
        stats = self.item.find('dl', {'class':'stats'})
        return stats

class RequiredTags(WorkAttributes):
    def getrating(self):
        req = WorkAttributes.reqtagblock(self)
        rat = req.find('li')
        ratin = rat.find('span')
        rated = ratin.get('title')
        return rated
    def getwarnings(self):
        req = WorkAttributes.reqtagblock(self)
        warn = req.find('li')
        warned = warn.find_next_sibling('li')
        warning = warned.find('span').get('title')
        return warning
    def getcategory(self):
        req = WorkAttributes.reqtagblock(self)
        cate = req.find('li')
        categ = cate.find_next_sibling('li')
        categor = categ.find_next_sibling('li')
        category = categor.find('span').get('title')
        return category
    def getcompletionstat(self):
        req = WorkAttributes.reqtagblock(self)
        com = req.find('li')
        comp = com.find_next_sibling('li')
        complet = comp.find_next_sibling('li')
        complete = complet.find_next_sibling('li')
        completed = complete.find('span').get('title')
        return completed

class TagAttributes(WorkAttributes):
    info = "this is the class that gets the tag attributes of a work"
    def getrelationship(self):
        tags = WorkAttributes.attrtagblock(self)
        relation = tags.find_all('li', {'class':'relationships'})
        relations = []
        for it in relation:
            rel = it.find('a', {'class':'tag'})
            rela = rel.get_text()
            relations.append(rela)
        if len(relations) > 1:
            relatlist = '+'.join(relations)
            return relatlist
        elif len(relations) == 0:
            return "none"
        else:
            relatlist = relations[0]
            return relatlist
        
    def getcharacters(self):
        tags = WorkAttributes.attrtagblock(self)
        charac = tags.find_all('li', {'class':'characters'})
        characs = []
        for ite in charac:
            cha = ite.find('a', {'class':'tag'})
            char = cha.get_text()
            characs.append(char)
        if len(characs) > 1:
            characlist = '+'.join(characs)
            return characlist
        elif len(characs) == 0:
            return "none"
        else:
            characlist = characs[0]
            return characlist
        
    def getfreeforms(self):
        tags = WorkAttributes.attrtagblock(self)
        frees = tags.find_all('li', {'class':'freeforms'})
        freebies = []
        for itera in frees:
            free = itera.find('a', {'class':'tag'})
            freef = free.get_text()
            freebies.append(freef)
        if len(freebies) > 1:
            freeflist = '+'.join(freebies)
            return freeflist
        elif len(freebies) == 0:
            return "none"
        else:
            freeflist = freebies[0]
            return freeflist

class Stats(WorkAttributes):
    def getlanguage(self):
        stat = WorkAttributes.statsblock(self)
        language = stat.find('dd', {'class':'language'}).get_text()
        return language
    def getwords(self):
        stat = WorkAttributes.statsblock(self)
        words = stat.find('dd', {'class': 'words'}).get_text()
        return words
    def gethits(self):
        stat = WorkAttributes.statsblock(self)
        hits = stat.find('dd', {'class':'hits'}).text
        return hits
    def getkudos(self):
        stat = WorkAttributes.statsblock(self)
        kudo = stat.find('dd', {'class':'kudos'})
        kudos = kudo.find('a').text
        return kudos
    def getchapters(self):
        stat = WorkAttributes.statsblock(self)
        chap = stat.find('dd', {'class':'chapters'})
        chapter = chap.find('a').text
        return chapter
    def getbookmarks(self):
        stat = WorkAttributes.statsblock(self)
        book = stat.find('dd', {'class':'bookmarks'})
        bookmark = book.find('a').text
        return bookmark
