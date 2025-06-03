#encontrar os divisores de um número e somá-los
limite = 1000
resultado1 = 0
resultado2 = 0
soma = 0

for n in range(1, limite):
    for div in range(1, n):
        if n %div == 0:
            print(div)
            resultado1 += div

    for div in range(1,resultado1):
        if resultado1%div ==0:
            resultado2 += div

    amigos = resultado2 == n
    if amigos:
        soma += n

print(resultado1, resultado2, amigos, soma)