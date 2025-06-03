num1 = 91
num2 = 99

resultado = num1 * num2

print(resultado)


#invertendo um número para ver se é polindromico
tmp = resultado
novoNum = tmp %10

while tmp %10 !=0:
    algarismo = tmp%10
    tmp = tmp //10
    novoNum = novoNum*10 + algarismo

print(unidade, dezena, tmp)
