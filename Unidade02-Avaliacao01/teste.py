arquivo = open('icf.txt', 'r', encoding = 'utf-8')
lista_formatada  = open('lista formatada.txt', 'w')


for linha in arquivo:
    final_palavra = linha.find(',')
    if final_palavra == 5:
        palavra = linha[:final_palavra]
        lista_formatada.write(palavra + '\n')

    




