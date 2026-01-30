import requests
from bs4 import BeautifulSoup as bs


#pagination: while span class is enabled
#'ol' class 'pagination actions pagy' 

class Request:
    def __init__(self, url):
        self.url = url
    def objectify(self):
        try:
            response = requests.get(self.url, {'user-agent':'bot'})
        except requests.exceptions.HttpError as err:
            print(f"error code f{err}")
        html = response.content
        soup = bs(html, 'html.parser')
        return soup


