import requests
import requests_cache
from bs4 import BeautifulSoup

def htmlFromUrl(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html


def main():
    requests_cache.install_cache('banco')
    pesquisa = input('Digite sua busca: ')
    url ='https://www.google.com.br/search?q='+ "+".join(pesquisa.split())

    html = htmlFromUrl(url)
    print(html.text)


if __name__ == "__main__":
    main()
