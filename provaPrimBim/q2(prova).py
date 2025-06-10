n = int(input('entre com o número de n: '))
m = int(input('entre com o número m: '))
fatorial = 1
i = 1
#calcular o fatorial de n:
while i <= n:
    fatorial = fatorial * i
    i = i + 1
if fatorial%m == 0:
    print(m, 'é um Jaime de', n)