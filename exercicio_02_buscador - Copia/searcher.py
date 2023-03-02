import requests_cache;
from page import Page;
from utils import search, menu;
import os

def main():
    requests_cache.install_cache('banco')

    while True:
        os.system('cls')
        print("you are accessing the search engine...\n")
        input("press <enter> to continue")
        os.system('cls')

        searchTerms = input('enter search terms: ')
        url = input('enter URL: ') #"https://www.bbc.com/portuguese"
        depth = int(input('enter Depth: '))
        os.system('cls')
        print('.\n.\n.\n.\n.\n.\n.\n.')
        print('> buscando...')

        urlsRankArray, urlsAccessOrderedDictionary = search(searchTerms, url, depth)

        os.system('cls')
        input('the search is finished, press <enter> to see the results...')

        while True:
            os.system('cls')
            option = input("Select the option:\n\t1. Show URL Ranking Relevance\n\t2. Show Content from URL\n\t3. Show URL Hits\n\t4. New Search\n\t0. Finish program\n\n")

            menu(option, urlsRankArray, urlsAccessOrderedDictionary, searchTerms)

            if option == '0' or option == '4':
                break
        
        if option == '0':
            print("search engine, shutdown...")
            input()
            break
    


if __name__ == "__main__":
    main()