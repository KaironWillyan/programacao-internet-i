import requests
import requests_cache
from bs4 import BeautifulSoup
from pprint import pprint


def findAllAnchorTag(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    anchor = html.find_all("a")
    return anchor

def printAllHref(anchors):
    for anchor in anchors:
        href = anchor.get('href')
        print(href)

def main():
    requests_cache.install_cache('banco')
    anchors = findAllAnchorTag('https://www.reddit.com/r/investimentos/')
    printAllHref(anchors)
    

if __name__ == "__main__":
    main()
