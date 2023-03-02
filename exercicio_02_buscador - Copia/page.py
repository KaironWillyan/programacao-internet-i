import requests;
from bs4 import BeautifulSoup;
import requests.exceptions
from bank import savePage, isPageAlredySaved, getHtml

class Page:
    def __init__(self, url):
        self.url = url
        if url is not None:
            self.insideUrls = self.getUrlsFromUrl(url)
        else:
            self.insideUrls = []

    def getUrlsFromUrl(self, url):
        urls = []
        try: 
            response = requests.get(url)

            if isPageAlredySaved(url):
                htmlString = getHtml(url)
                html = BeautifulSoup(htmlString, 'html.parser')
            else:
                html = BeautifulSoup(response.text, 'html.parser')
                savePage(url, str(html))


            anchorTags = html.find_all('a')
            for anchor in anchorTags:
                url = anchor.get('href')
                if not url == None:
                    if url and url[0] == '/':
                        urls.append('https://g1.globo.com'+url)
            return urls
        
        except requests.exceptions.MissingSchema:
            return []
        except requests.exceptions.InvalidSchema:
            return []
    
    def instantiateInsideUrls(self, accessedUrls):
        for i in range(len(self.insideUrls)):
            accessedUrls.append(Page(self.insideUrls[i]))


