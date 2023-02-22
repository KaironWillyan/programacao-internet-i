import requests
from bs4 import BeautifulSoup


def main():
    page = 'https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/'
    response = requests.get(page)
    html = BeautifulSoup(response.text, 'html.parser')
    list_item = html.find('table', attrs={'class':"classificacao_campeonato campeonato_brasileiro"})
    table = list_item.text.strip()
    print(table)


if __name__ == "__main__":
    main()
