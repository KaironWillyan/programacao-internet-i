import requests
from bs4 import BeautifulSoup


def main():
    cep = input('Digite o cep: ')
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)

    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    main()
