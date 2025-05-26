#autor: Roberto Araujo Batista, matricula: 20251014050041, redes de computadores
#professor: Galileu

#declaração de variáreis
import random
aleatorio = random.randint(1,100)
print(aleatorio)
limiteMenor = 1
limiteMaior = 100

print('-------------joguinho de advinhação----------------')
print('adivinhe qual o número escolhido pelo computado de 1 à 100')

#como não pode usar repetição, item b do arquivo, o programa será repetido nas 4 vezes, exceto a última
print('///////////////////////////////////')
print('primeira tentativa: ')
numero = int(input("informe um número: "))
if (numero < limiteMenor) or (numero > limiteMaior):
    print('esse numero não está entre ', limiteMenor, ' e ', limiteMaior, ', você perdeu uma tentativa') #caso o usuário tente um número fora do limite
else:
    #conferir se acertou:
    if aleatorio == numero: #a primeira tentativa é caso tenha acertado, assim ele não calcula variável desnecessária
        print('você acertou, meus parabéns!')
    if (aleatorio < numero) and (aleatorio > limiteMenor): #define o novo limite caso o usuario tenha errado para cima
        limiteMaior = numero
        print('o numero está entre ', limiteMenor, ' e ', limiteMaior)
    else:
        if (aleatorio > numero) and (aleatorio < limiteMaior): #define o novo limite caso o usuario tenha errado para baixo
            limiteMenor = numero
            print('o numero está entre ', limiteMenor, 'e', limiteMaior)


print('///////////////////////////////////')
print('segunda tentativa: ')
numero = int(input("informe um número: "))
if (numero < limiteMenor) or (numero > limiteMaior):
    print('esse numero não está entre ', limiteMenor, ' e ', limiteMaior, ', você perdeu uma tentativa')
else:
    if aleatorio == numero: 
        print('você acertou, meus parabéns!')
    if (aleatorio < numero) and (aleatorio > limiteMenor): 
        limiteMaior = numero
        print('o numero está entre ', limiteMenor, ' e ', limiteMaior)
    else:
        if (aleatorio > numero) and (aleatorio < limiteMaior):
            limiteMenor = numero
            print('o numero está entre ', limiteMenor, 'e', limiteMaior)

print('///////////////////////////////////')
print('penúltima tentativa: ')
numero = int(input("informe um número: "))
if (numero < limiteMenor) or (numero > limiteMaior):
    print('esse numero não está entre ', limiteMenor, ' e ', limiteMaior, ', você perdeu uma tentativa')
else:
    if aleatorio == numero: 
        print('você acertou, meus parabéns!')
    if (aleatorio < numero) and (aleatorio > limiteMenor):
        limiteMaior = numero
        print('o numero está entre ', limiteMenor, ' e ', limiteMaior)
    else:
        if (aleatorio > numero) and (aleatorio < limiteMaior):
            limiteMenor = numero
            print('o numero está entre ', limiteMenor, 'e', limiteMaior)

print('///////////////////////////////////')
print('última tentativa: ')
numero = int(input("informe um número: "))
if (numero < limiteMenor) or (numero > limiteMaior):
    print('esse numero não está entre ', limiteMenor, ' e ', limiteMaior, ', você perdeu uma tentativa')
else: #resultado do jogo:
    print('///////////////////////////////////')
    print('que pena! você perdeu, o número era ', aleatorio)
    print('mas não desanime, rode o código de novo e tente até conseguir! :)')