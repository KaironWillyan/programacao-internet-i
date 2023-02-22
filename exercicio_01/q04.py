import requests
import requests_cache

def downloadImageFromUrl(url, name):
    f = open(name,'wb')
    response = requests.get(url, stream=True)
    f.write(response.content)
    f.close()
    print("download concluído")

def main():
    requests_cache.install_cache('banco')
    url = input('Digite a url da imagem: ')
    name = input('Digite o nome da imagem com o formato: ')
    downloadImageFromUrl(url, name)


if __name__ == "__main__":
    main()

