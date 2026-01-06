class workAttributes:
    info="this class retrieves work attributes that are not grouped with others within certain elements, as well as the elements in which some tags are grouped"
    def __init__(self, item):
        self.item = item
        #where object is the individual listing of a given ao3 fic
    def getDateTime(self):
        dateclass = self.item.find('p', {'class':'datetime'})
        date = dateclass.get_text()
        return date 
    def getFandom(self):
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
    def reqTagBlock(self):
        req = self.item.find('ul', {'class':'required-tags'})
        return req
    def tagBlock(self):
        tags = self.item.find('ul', {'class':'tags commas'})
        return tags
    def statsBlock(self):
        stats = self.item.find('dl', {'class':'stats'})
        return stats

class requiredTags:
  info = "this class gets the tags that are grouped within the required tags element"
    def __init__(self, req):
        self.req = req
    def getRating(self):
        rat = self.req.find('li')
        ratin = rat.find('span')
        rated = ratin.get('title')
        return rated
    def getWarnings(self):
        warn = self.req.find('li')
        warned = warn.find_next_sibling('li')
        warning = warned.find('span').get('title')
        return warning
    def getCategory(self):
        cate = self.req.find('li')
        categ = cate.find_next_sibling('li')
        categor = categ.find_next_sibling('li')
        category = categor.find('span').get('title')
        return category
    def getCompletionStat(self):
        com = self.req.find('li')
        comp = com.find_next_sibling('li')
        complet = comp.find_next_sibling('li')
        complete = complet.find_next_sibling('li')
        completed = complete.find('span').get('title')
        return completed


class tagAttributes:
    info = "this class gets tags that are within the main tag element"
    def __init__(self,tags):
        self.tags = tags
    
    def getRelationship(self):
        relation = self.tags.find_all('li', {'class':'relationships'})
        relations = []
        for it in relation:
            rel = it.find('a', {'class':'tag'})
            rela = rel.get_text()
            relations.append(rela)
        if len(relations) > 1:
            relatlist = '+'.join(relations)
            return relations
        elif len(relations) == 0:
            return "none"
        else:
            relatlist = relations[0]
            return relatlist
        
    def getCharacters(self):
        charac = self.tags.find_all('li', {'class':'characters'})
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
        
    def getFreeforms(self):
        frees = self.tags.find_all('li', {'class':'freeforms'})
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

class stats:
  info = "this class gets statistical elements of a given work"
    def __init__(self, stat):
        self.stat = stat
    def getLanguage(self):
        language = self.stat.find('dd', {'class':'language'}).get_text()
        return language
    def getWords(self):
        words = self.stat.find('dd', {'class': 'words'}).get_text()
        return words
    def getHits(self):
        hits = self.stat.find('dd', {'class':'hits'}).text
        return hits
    def getKudos(self):
        kudo = self.stat.find('dd', {'class':'kudos'})
        kudos = kudo.find('a').text
        return kudos
    
