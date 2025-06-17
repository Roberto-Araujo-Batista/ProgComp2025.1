import random
palavras = ('abacate', 'lima', 'abacaxi')
segredo = palavras[random.randint(0,len(palavras)-1)] #palavra aleatoria dentro da variavel palavras
visivel = '-'*len(segredo)


tentativas = 4
#programa para retornar os resultados
while tentativas > 0:
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
    tentativas = tentativas -1


if visivel == segredo:
    print('meus parabéns! você acertou')
else: 
    print('uma pena, você errou :(, tente novamente')
    
