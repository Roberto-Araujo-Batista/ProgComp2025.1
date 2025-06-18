import random
palavras = ('abacate', 'lima', 'abacaxi')
segredo = palavras[random.randint(0,len(palavras)-1)] #palavra aleatoria dentro da variavel palavras

segredo = segredo.upper() #tópico 4: deixar o segredo em maiúsculo

visivel = '-'*len(segredo)


tentativas = 4
#programa para retornar os resultados
while tentativas > 0: #tópico 1: limitar as tentativas
    print('você tem ', tentativas, 'tentativas')
    print(visivel)
    letra = input('digite uma letra: ').upper()#tópico 4: deixar letras em maiúsculo

    if len(letra) != 1: #tópico 3: não permita digitação de mais de uma letra
        print('/'*10)
        print('você digitou mais de um caracter, isso não é permitido, mas não é considerado como erro!')
        print('/'*10)
    else:
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

if visivel == segredo: #tópico 2: indicar sucesso ou falha
    print('meus parabéns! você acertou')
else: 
    print('uma pena, você errou :(, tente novamente')
