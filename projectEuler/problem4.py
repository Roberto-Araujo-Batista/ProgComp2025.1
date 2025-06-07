#mostra o maior número polindromo formado pelo produto de dois números de 3 algarismos
#autor: roberto araujo batista

maior = 0
imaior =0
jmaior =0
for i in range(100, 1000):
    for j in range(100, 1000):

        numero = i*j
        aux = numero #variavel que receberá o numero para poder fazer a conta sem perdê-lo
        inverso = 0


        while aux /10!=0:
            algarismo = aux %10
            aux = aux //10
            inverso = inverso *10 + algarismo

        if inverso == numero:
            if maior < numero:
                maior = numero
                imaior = i
                jmaior = j

print('o maior número polidromo é: ', maior, 'gerado por: ', imaior,'e ', jmaior)

