#fazer um programa que receba um número com no máximo 4 algarismos (9999) e faça a soma dos algarismos

#auto: Roberto Araujo Batista, matricula: 20251014050041, aluno de redes de computadores
#professor: Galileu

#Entrada de dados e criação de variáveis
print('-'*10 + 'somando algarismos' +'-'*10)
numero = int(input("informe um número(0<=inteiro<=9999): "))

#condições para o programar funcionar como pedido:-
if (numero > 9999) or (numero < 0):
    print('esse número não está entre 1 e 9999, tente novamente com um número menor')
else:
    #se o numero é 1945, então significa que é 5*1 + 4*10 + 9*100 + 1 *1000
    #para separar os algarismos então basta dividir por inteiro: 
    milhar = numero //1000
    numero = numero %1000 #numero recebe o resto para poder continuar a conta, agora número passa a ser = 1945-1000= 945

    centena = numero //100
    numero = numero %100
    dezena = numero //10
    numero = numero%10
    unidade = numero

    soma = milhar + centena + dezena + unidade

    print('a soma dos algarismos é: ', soma)

