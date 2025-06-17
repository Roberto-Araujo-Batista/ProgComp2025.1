import random
palavras = ('abacate', 'lima', 'abacaxi')
segredo = palavras[random.randint(0,2)]
visivel = '-'*len(segredo)

#programa para retornar os resultados
while visivel != segredo:
    print(visivel)
    letra = input('digite uma letra: ')
    indice = 0
    novavisivel = ''

    while indice < len(segredo):
        if segredo[indice] == letra:
            novavisivel = novavisivel + segredo[indice]
        else:
            novavisivel = novavisivel + visivel[indice]
        indice = indice + 1
    visivel = novavisivel
print(visivel)
print('você conseguiu acertar a palavra, meus parabéns!!!')
    
