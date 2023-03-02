
def printHeader(url):
    width = 100
    spaces = " " * ((width - len(url)) // 2)
    mensagem = "{}{}{}".format(spaces, url, spaces)
    if len(mensagem) < width:
        mensagem += " " * (width - len(mensagem))

    print('=' * width)
    print(mensagem)
    print('=' * width)


def printContextOccurrences(occurrences):
    for occurrence in occurrences:
        texto = occurrence.get_text()
        if len(texto) != 0 and len(texto) >= 20:
            print("-> ", texto, "\n")

    
def showUrlRanking(urlsRankingArray):
    print("\nRanking (Url - Relevância)")
    print("==========================================================================")
    count = 1

    for url in urlsRankingArray:
        print(count, ")", url)
        count +=1


def showUrlsMostAccesseds(UrlsAccessOrderedDictionary):
    print("\nRanking (Url - Acessos)")
    print("==========================================================================")
    for chave, valor in UrlsAccessOrderedDictionary.items():
        print(chave, " : ",valor)
