#saber o produto entre abc, que são um terno pitagorico e a soma é igual a 1000

for a in range(1, 1000+1):
    for b in range(1, 1000+1):
        c = 1000 -a -b
        pitagoras = (c**2) == (a**2)+(b**2)
        if (a+b+c == 1000) and pitagoras and c>b>a:
            print('deu certo', a*b*c)