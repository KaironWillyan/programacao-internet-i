import requests
import requests_cache
from bs4 import BeautifulSoup
from pprint import pprint


def printContentOfTag(tag):
    response = requests.get('https://www.bbc.com/portuguese')
    html = BeautifulSoup(response.text, 'html.parser')
    cabecalhos = html.find_all(tag)

    for cabecalho in cabecalhos:
        texto = cabecalho.get_text()
        print(texto)


    
def main():
    requests_cache.install_cache('banco')
    tag = input('Digite uma tag: ')
    printContentOfTag(tag)


if __name__ == "__main__":
    main()

