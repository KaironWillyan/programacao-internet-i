import requests
import requests_cache
from bs4 import BeautifulSoup
from pprint import pprint
import re

def htmlFromUrl(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html


def FindTermOccurrences(html, termo):
    ocorrências = html.find_all(string=re.compile(termo))
    return ocorrências

def printContextOccurrences(termo, ocorrências):
    for ocorrência in ocorrências:
        texto = ocorrência.get_text()
        indice = texto.find(termo)
        
        limite_inferior = indice - 20
        limite_superior = indice + len(termo) + 20

        if(limite_inferior < 0):
            limite_inferior = 0
        
        if(limite_superior > len(texto)):
            limite_superior = len(texto)

        print(texto[limite_inferior:limite_superior])


def main():
    requests_cache.install_cache('banco')
    url = input('Digite uma url: ')
    termo = input('Digite um termo a ser buscado: ')
    
    html = htmlFromUrl(url)
    occurrences = FindTermOccurrences(html, termo)
    printContextOccurrences(termo, occurrences)


if __name__ == "__main__":
    main()
