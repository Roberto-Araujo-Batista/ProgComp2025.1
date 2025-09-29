#problem52 projectEuler melhorado


def pos_numero(numero):
    novonumero = numero
    numeropos = 0
    while novonumero !=0:
        algarismo = novonumero %10
        numeropos = numeropos + 10**algarismo
        novonumero = novonumero //10
    return numeropos

numero =2
multiplicador =1

entrada = int(input('multiplicador: '))

while multiplicador != entrada:
    primeironumero = pos_numero(numero)
    novonumero = pos_numero(numero)*multiplicador

    if primeironumero == novonumero:
        multiplicador = multiplicador + 1

    else:
        multiplicador =1
        numero = numero +1
    
print(numero, primeironumero, novonumero)