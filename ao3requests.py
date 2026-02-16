import requests
from bs4 import BeautifulSoup as bs

'''
this might be redundant to have but it helps clean up code for me, this just makes and sends requests, along with a function to paginate if you go from my sample
'''
class Request:
    def __init__(self, url):
        self.url = url
    def objectify(self):
        try:
            response = requests.get(self.url, {'user-agent':'bot'})
        except requests.exceptions.HTTPError as err:
            print(f"error code f{err}")
        html = response.content
        soup = bs(html, 'html.parser')
        return soup

def paginate(object):
    pagy = object.find('ol', class_='pagination actions pagy')
    nextpage = pagy.find('li', class_='next').find('a')
    if nextpage is not None:
        nextlink = nextpage.get('href')
        full = f"https://archiveofourown.org{nextlink}"
        return full
    else:
        return None
