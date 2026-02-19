import csv
import os
import pickle
import sys
import pandas as pd
from .getworks import getsearchdata, midpointsave

'''
Sample work search
'''

filepath = sys.argv[1]
url = sys.argv[2]

fieldnames = ['Date Last Updated', 'Warnings', 'Category', 'Ratings', 'Fandom', 'Pairing', 'Character', 'Freeform', 'Word Count', 'Kudos', 'Hits', 'Language', 'Chapter Count']


if not os.path.exists(filepath):
    with open(filepath, "w", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        getsearchdata(page=url, writer=writer)
else:
    with open(filepath, "a", encoding="utf-8") as csvfile:
        with open('/Users/gingermaemiller/Desktop/ao3data/pausedpage.pkl', 'rb') as f:
            page = pickle.load(f)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        getsearchdata(page=page, writer=writer)

df = pd.read_csv(filepath)
df.drop_duplicates(inplace=True)
df.to_csv()
