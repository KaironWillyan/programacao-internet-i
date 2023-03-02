import requests;
import requests_cache;
from bs4 import BeautifulSoup;
import re
from page import Page
import os
from view import printHeader, printContextOccurrences,showUrlRanking, showUrlsMostAccesseds



def attRanking(accessedUrls, url, rankingPoints):
    accessedUrls[url] += rankingPoints



def addUrlToDictionary(dictionary, url):
    if url in dictionary.keys():
        dictionary[url] += 1
    else:
        dictionary[url] = 1



def isUrlAlreadyAccessed(url, accessedUrls):
    return url in accessedUrls.keys()



def getUrlsFromPages(accessedUrls, page, depth):
    if(depth == 0):
        return
    
    for i in range(len(page.insideUrls)):
        if not page.insideUrls[i] in accessedUrls:
            print(i, " ", page.insideUrls[i])
            addUrlToDictionary(accessedUrls, page.insideUrls[i])
            getUrlsFromPages(accessedUrls, Page(page.insideUrls[i]), depth - 1)
        else:
            addUrlToDictionary(accessedUrls, page.insideUrls[i])


            
def sortDictionary(dictionary):
    ordered = {chave: valor for chave, valor in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
    return ordered

    

def getOcurrencesSearchTerms(searchTerms, url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectTimeout:
        return []
    html = BeautifulSoup(response.text, 'html.parser')
    return html.find_all(string=lambda text: searchTerms in text)



def rankUrls(accessedUrls, searchTerms):
    accessedUrlsArray = list(accessedUrls.keys())
    for i in range(len(accessedUrlsArray)):
        occurrences = getOcurrencesSearchTerms(searchTerms, accessedUrlsArray[i])  

        if len(occurrences) > 0 and len(occurrences[0]) != 0: #critério de exclusão
            attRanking(accessedUrls, accessedUrlsArray[i], len(occurrences) * 10) #critério positivo de ranqueamento
        else:
            accessedUrls.pop(accessedUrlsArray[i])



def showContentFromUrl(url, searchTerms):
    occurrences = getOcurrencesSearchTerms(searchTerms, url)
    printContextOccurrences(occurrences)



def menu(option, urlsRankingArray, urlsAccessOrderedDictionary, searchTerms):
    if(len(urlsRankingArray) != 0):
        if option == '1':
            os.system('cls')
            showUrlRanking(urlsRankingArray)
            input('\npress <enter> to continue')

        elif option == '2':
            os.system('cls')
            showUrlRanking(urlsRankingArray)
            index = int(input('\nSelect a URL by id (0 if empty list) '))
            os.system('cls')    
            printHeader(urlsRankingArray[index - 1])
            showContentFromUrl(urlsRankingArray[index - 1], searchTerms)
            input('press <enter> to continue')
        elif option == '3':
            os.system('cls')
            showUrlsMostAccesseds(urlsAccessOrderedDictionary)
            input('press <enter> to continue')

    elif option == '1' or option == '2':
        print('The searcher does not return anything')
        input('press <enter> to continue')



def search(searchTerms, url, depth):
    requests_cache.install_cache('banco')
    accessedUrlsDictionary = {} 


    addUrlToDictionary(accessedUrlsDictionary, url)
    getUrlsFromPages(accessedUrlsDictionary, Page(url), depth)


    accessedUrlsOrdered = sortDictionary(accessedUrlsDictionary)
    accessedUrlsOrderedCopy = accessedUrlsOrdered.copy()


    rankUrls(accessedUrlsOrderedCopy, searchTerms)


    urlsRanking = sortDictionary(accessedUrlsOrderedCopy)
    urlsRankingArray = list(urlsRanking.keys())
    
    return urlsRankingArray, accessedUrlsOrdered