#fazer um código que liste os números primos e mostre o 10001 número primo

#listar número primos


#descobrir se um número é primo

primos = []
limite = 10000 #já que o primeiro número é 0 então o 10001 está na pos 10000

numero = 2
while len(primos) <= limite:
    divisor = 2
    ehprimo = True

    while divisor <= numero**(1/2) and ehprimo:
        if numero %divisor == 0:
            ehprimo = False
        else:
            divisor = divisor +1
    
    if ehprimo:
        primos = primos +[numero]
    
    numero = numero +1

print(primos[limite])
