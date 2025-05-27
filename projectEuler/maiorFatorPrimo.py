#fazer um comando que encontre o maior fatorial primo de 600851475143
meta = 600851475143
aux = meta

#encontrar números primos
primos = 2

while meta > 1:
    if meta % primos == 0:
        meta = meta / primos
    else:
        primos = primos +1


print(primos)
