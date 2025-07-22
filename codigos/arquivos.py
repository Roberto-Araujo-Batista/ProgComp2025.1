'''1) Quantos pedidos houve em cada data/hora/minuto?

2) Qual o dia/hora com mais pedidos? 

3) Houve respostas diferentes do código 200? 
   Quais e quantos? Faca um gráfico de barra
   com essa informação.
   
4) Gere um arquivo com nome "resposta_data.txt" em
   que cada linha contem a data e o número de pedidos
   naquela data. Exiba, também, esta informação em 
   um gráfico de linhas.
   
5) Qual o IP fez mais pedidos em cada um dos dias do log?

6) Salve um arquivo com a lista de IPs (um por linha) que 
   fizeram pedidos ao servidor. O nome desse arquivo deve 
   ser "ips.txt"'''


#1 quantos pedidos houveram na mesma hora e minuto
arquivo = open('apache.logs', 'r') #abrindo arquivo para leitura
contagemdata = dict()

for linha in arquivo:
    data = linha.split()[3][1:18]

    if not data in contagemdata:
        contagemdata[data] = 1
    if data in contagemdata:
        contagemdata[data] = contagemdata[data] + 1
arquivo.close()

print(contagemdata)

#2 qual horário com mais acesso?
maior = 0
for chave in contagemdata.keys():
    if contagemdata[chave] > maior:
        maiorchave = chave
        maior = contagemdata[chave]
print('-'* 20)

print(f'o horário com maior acesso foi: {maiorchave} \ncom: {contagemdata[maiorchave]}')



#3 houve código diferente do 200? quais e quantos foram? gere um gráfico de barras
arquivo = open('apache.logs', 'r')

for linha in arquivo:
    print(linha.split()[8])



