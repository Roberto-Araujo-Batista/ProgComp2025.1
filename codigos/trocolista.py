#fazer um programa que retorne o troco de uma compra especificando cada nota devo dar de troco

notas = [200, 100, 50, 20, 10, 5, 1]

contNotas = []

valor = int(input('qual foi o valor da compra? '))
pagamento = int(input('quanto foi o pagamento? '))

troco = pagamento - valor
print(f'o troco é {troco} e será em: ')

pos = 0
while pos < len(notas):
	if troco // notas[pos]:
		contNotas = contNotas + [troco //notas[pos]]
		troco = troco % notas[pos]
	else:
		contNotas = contNotas + [0]
	pos = pos +1

pos = 0
while pos <len(contNotas):
	print(contNotas[pos], 'de ', notas[pos], 'reais')
	pos = pos + 1