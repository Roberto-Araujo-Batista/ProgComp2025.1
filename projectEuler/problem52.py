
numero = int(input('digite um numero: '))
multiplicador = int(input('digite um multiplicador: '))
lstnumero = []


while (len(lstnumero) != multiplicador):
    #variaveis para calculo
    aux = numero
    algnumero = list()
    lstnumero = [numero]

    #separar os algarismos dos números
    while aux > 0:
        algarismo = aux % 10
        aux = aux //10
        algnumero = algnumero + [algarismo]
    algnumero.sort() #algarismo do numero prontos para comparação

    #separar algarismos do numero multiplicado
    contador = 1
    igual = True
    while (contador < multiplicador) and igual:
        aux = numero
        aux = aux + numero
        algmulti = []
        while aux >0:
            algarismo = aux %10
            aux = aux //10
            algmulti = algmulti + [algarismo]
        algmulti.sort() # algarimso do numero multiplicado pronto para comparação
        print(algmulti, algnumero,lstnumero)
    #comparar algarismos do numero multiplicado com algarismos do primeiro numero 
        if algnumero == algmulti:
            lstnumero = lstnumero + [numero]
            print('eles são iguais', lstnumero)
        else:#preparando para compara o próximo número
            print('eles não são iguais', numero)
            numero = numero +1
            igual = False 
        contador = contador + 1


