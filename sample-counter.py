import pandas as pd
import sys
import collections
import os
from pathlib import Path
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
from tagcounter import *


selection = "" #pd.read_csv(path-to-your-csv)

frame = getTypes(selection)
freeform = frame.freeforms()
fandom = frame.fandoms()
character = frame.characters()
relationship = frame.relationships()
rating = frame.ratings()

shorthand = "alt-uni-nd"

#turn multiple types into a list to loop through
typelist = [freeform, fandom, character, relationship]
count = 0
for iter in typelist:
    count += 1
    tagcounter = countTags(iter)
    tagcounts = tagcounter.counter()
    #tagcounts.to_csv(path-to-your-csv)

print("your items have been saved to your folder, bye now!")
