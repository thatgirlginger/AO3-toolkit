import pandas as pd
import sys
import collections
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore") #this is inherited from an earlier tag-data counter i did using the 2021 data dump, not entirely sure why i implemented it in the first place but i remember it being a headache so i'm just gonna keep this in


class getTypes:
    info = "here are all of the tag types you can get from your selection, just make sure you use the same scraping package"
    #with these, you'll just want to make sure the selection name matches up with what you have named the columns in your dataframe
    def __init__(self, selection):
        self.selection = selection
        if not isinstance(selection, pd.core.frame.DataFrame):
            raise TypeError("your selection object must already be in dataframe format")
    def freeforms(self):
        freelist = self.selection['Freeform'].astype(str)
        freeform = pd.Series(freelist)
        return freeform
    def fandoms(self):
        fanlist = self.selection['Fandom'].astype(str)
        fandom = pd.Series(fanlist)
        return fandom
    def characters(self):
        characlist = self.selection['Characters'].astype(str)
        character = pd.Series(characlist)
        return character
    def relationships(self):
        relationlist = self.selection['Pairing'].astype(str)
        relationship = pd.Series(relationlist)
        return relationship
    def ratings(self):
        ratinglist = self.selection['Rating'].astype(str)
        rating = pd.Series(ratinglist)
        return rating

class countTags:
    info = "this is the class in which you can count the instances of each tag type in what you have narrowed down, with your dataframe as the output"
    def __init__(self, type):
        self.type = type
    def counter(self): 
        taglist = []
        for index, value in self.type.items():
            items = value.split("+")
            taglist.append(items)
        taglist2 = []
        for i in taglist:
            for item in i:
                taglist2.append(item)
        count = collections.Counter(taglist2)
        countdict = dict(count)
        data = pd.DataFrame.from_dict(countdict, orient= "index")
        df = data.reset_index()
        df = df.rename(columns={"index":"tag", 0:"count"})
        return df
