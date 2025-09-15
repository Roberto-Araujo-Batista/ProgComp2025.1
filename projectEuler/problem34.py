def fatorial(numero):
    contador = 1
    fat =1

    while contador <= numero:
        fat = fat * contador
        contador = contador +1
    return fat

def separando_algarismo(numero):
    aux = numero 
    soma = 0
    while aux > 0:
        algarismo = aux %10
        soma = soma + fatorial(algarismo)
        aux = aux //10
    if soma == numero:
        print(soma)

numero = 10


while numero <= 9999999:
    separando_algarismo(numero)
    numero = numero + 1



