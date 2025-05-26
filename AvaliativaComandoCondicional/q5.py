#programa que calcula o acumulo de tarifas em relação as horas
#os minutos contam como uma hora completa, então o programa precisa arredondar o número para cima sem o uso de ferramentas, exemplo: 20min =1h


tempo = float(input("quanto tempo você ficou no estacionamento?(em minutos)"))
tempo = tempo /60
if tempo - int(tempo) != 0: #código para arredondar o número para cima
    tempo = int(tempo) +1

somaTarifa =0
tarifa = 0
tempoLocal = 0

if tempo > 12: #excessão para calculo de tarifa
    tarifa = 30
    somaTarifa = tarifa
    tempo = 12

if tempo > 4: #"horas seguintes"
    tempoLocal = tempo - 4 #tempo de estadia nessa categoria
    tarifa = 3 * tempoLocal
    somaTarifa = somaTarifa + tarifa
    tempo = 4 #tempo de estadia nas outras categorias menos nessa que já foi calculada
if tempo > 2:
    tempoLocal = tempo -2
    tarifa = 5*tempoLocal 
    somaTarifa = somaTarifa +tarifa
    tempo = 2
if tempo != 0:
    tarifa = 8*tempo 
    somaTarifa = somaTarifa +tarifa    

print("a tarifa que você terá que pagar é de ", somaTarifa, "reais")

    
