#fazer um programa para ver a maior corrente de collatz sequence, abaixo de um milhão


i =2
limite = 10**6
maior = 0

while i < 10:
    number = i
    contador = 1 
    while number > 1:
        if number % 2 ==0:
            number = number //2
        else:
            number = 3*number+1
        contador = contador +1
    #para receber o maior numero de sequencia
    if maior < contador:
        maior = contador
    i = i+1


print(number, maior)

