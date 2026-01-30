import ao3funcs
from ao3requests import *
import counters

class EquivGetter:
    info="returns tag equivalency list for a given tag"
    def __init__(self, tagname):
        self.tagname = tagname
    def split_to_url(self):
        tagtolist = self.tagname.split(' ')
        urladd = '%20'.join(tagtolist)
        baseurl = "https://archiveofourown.org/tags"
        concaturl = f"{baseurl}/{urladd}"
        return concaturl
    
class TagListing(EquivGetter):
    def tagpage(self):
        url = EquivGetter.split_to_url(self)
        request = Request(url)
        item = request.objectify()
        return item
    
class FamilyTree(TagListing):
    def parenttags(self):
        parenttags = []
        item = TagListing.tagpage(self)
        select = item.find('div', class_='parent listbox group')
        listing = select.find_all('a', class_='tag')
        for tag in listing:
            tagname = tag.text
            parenttags.append(tagname)
        return parenttags
    def siblingtags(self):
        synonyms = []
        item = TagListing.tagpage(self)
        selection = item.find('div', class_='synonym listbox group')
        listing = selection.find_all('a', class_='tag')
        for tag in listing:
            tagname = tag.text
            synonyms.append(tagname)
        return synonyms
    def childtags(self):  #note: this does not distinguish between child and grandchild tags
        children = []
        item = TagListing.tagpage(self)
        selection = item.find('div', class_='sub listbox group')
        listing = selection.find_all('a', class_='tag')
        for tag in listing:
            tagname = tag.text
            children.append(tagname)
        return children
