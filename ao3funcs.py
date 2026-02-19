from bs4 import BeautifulSoup as bs
'''
classes and methods for work information listed on ao3
'''

class WorkAttributes:
    '''
    get the attributes for each work, all accessible from the same parent element
    '''
    def __init__(self, item):
        self.item = item
    def datetime(self):
        dateclass = self.item.find('p', {'class':'datetime'})
        date = dateclass.get_text()
        return date
    def fandom(self):
        heading = self.item.find('h5', {'class':'fandoms heading'})
        fandoms = heading.find_all('a', {'class':'tag'})
        fandommultis = []
        for i in fandoms:
            domfan = i.get_text()
            fandommultis.append(domfan)
        if len(fandommultis) > 1:
            fandoms = '+'.join(fandommultis)
        else:
            fandoms = fandommultis[0]
        return fandoms
    def requiredtags(self):
        req = self.item.find('ul', {'class':'required-tags'})
        return req
    def attributes(self):
        tags = self.item.find('ul', {'class':'tags commas'})
        return tags
    def stats(self):
        stats = self.item.find('dl', {'class':'stats'})
        return stats

class RequiredTags(WorkAttributes):
    def rating(self):
        req = WorkAttributes.requiredtags(self)
        rat = req.find('li')
        ratin = rat.find('span')
        rating = ratin.get('title')
        return rating
    def warnings(self):
        req = WorkAttributes.requiredtags(self)
        warn = req.find('li')
        warned = warn.find_next_sibling('li')
        warning = warned.find('span').get('title')
        return warning
    def category(self):
        req = WorkAttributes.requiredtags(self)
        cate = req.find('li')
        categ = cate.find_next_sibling('li')
        categor = categ.find_next_sibling('li')
        category = categor.find('span').get('title')
        return category
    def completion(self):
        req = WorkAttributes.requiredtags(self)
        com = req.find('li')
        comp = com.find_next_sibling('li')
        complet = comp.find_next_sibling('li')
        complete = complet.find_next_sibling('li')
        completed = complete.find('span').get('title')
        return completed

class TagAttributes(WorkAttributes):
    info = "this is the class that gets the tag attributes of a work"
    def ships(self):
        tags = WorkAttributes.attributes(self)
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
        
    def characters(self):
        tags = WorkAttributes.attributes(self)
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
        
    def freeforms(self):
        tags = WorkAttributes.attributes(self)
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
    def language(self):
        stat = WorkAttributes.stats(self)
        language = stat.find('dd', {'class':'language'}).get_text()
        return language
    def words(self):
        stat = WorkAttributes.stats(self)
        words = stat.find('dd', {'class': 'words'}).get_text()
        return words
    def hits(self):
        stat = WorkAttributes.stats(self)
        hit = stat.find('dd', {'class':'hits'})
        if hit is None:
            hits = "None"
        else:
            hits = hit.text
        return hits
    def kudos(self):
        stat = WorkAttributes.stats(self)
        kudo = stat.find('dd', {'class':'kudos'})
        if kudo is None:
            kudos = "None"
        else:
            kudos = kudo.find('a').text
        return kudos
    def chapters(self):
        stat = WorkAttributes.stats(self)
        chap = stat.find('dd', {'class':'chapters'})
        if chap is None:
            chapter = "None"
        elif chap.find('a') is None:
            chapter = chap.text
        else:
            chapter = chap.find('a').text
        return chapter
    def bookmarks(self):
        stat = WorkAttributes.stats(self)
        book = stat.find('dd', {'class':'bookmarks'})
        if book is None:
            bookmark = "None"
        else:
            bookmark = book.find('a').text
        return bookmark
