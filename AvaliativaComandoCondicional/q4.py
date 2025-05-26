#programa que conte quantos dias tem entre duas datas
#autor/aluno: ROBERTO ARAUJO BATISTA, matricula: 20251014050041, Redes de Computadores
#professor: Galileu
print('//////////////////////////////////')
print('programa que conta os dias')

#entrada de dados
print('//////////////////////////////////')
print('DATA INICIAL')
diaInicial = int(input('informe o dia: '))
mesInicial = int(input('informe o mês: '))

print('//////////////////////////////////')
print('DATA FINAL')
diaFinal = int(input('informe o dia: '))
mesFinal = int(input('informe o mês: '))

#eliminado datas inválidas, considerando que não é um ano bissexto
if ((mesInicial == 1) or (mesFinal ==1)) and (((diaInicial < 1) or (diaInicial>31)) or ((diaFinal <1) or (diaFinal >31))): #janeiro
    print('essa data não é váldia')
if ((mesInicial == 2) or (mesFinal ==2)) and (((diaInicial < 1) or (diaInicial>28)) or ((diaFinal <1) or (diaFinal >28))): #fevereiro
    print('essa data não é váldia')
if ((mesInicial == 3) or (mesFinal ==3)) and (((diaInicial < 1) or (diaInicial>31)) or ((diaFinal <1) or (diaFinal >31))): #março
    print('essa data não é váldia')
if ((mesInicial == 4) or (mesFinal ==4)) and (((diaInicial < 1) or (diaInicial>30)) or ((diaFinal <1) or (diaFinal >30))): #abril
    print('essa data não é váldia')
if ((mesInicial == 5) or (mesFinal ==5)) and (((diaInicial < 1) or (diaInicial>31)) or ((diaFinal <1) or (diaFinal >31))): #maio
    print('essa data não é váldia')
if ((mesInicial == 6) or (mesFinal ==6)) and (((diaInicial < 1) or (diaInicial>30)) or ((diaFinal <1) or (diaFinal >30))): #junho
    print('essa data não é váldia')
if ((mesInicial == 7) or (mesFinal ==7)) and (((diaInicial < 1) or (diaInicial>31)) or ((diaFinal <1) or (diaFinal >31))): #julho
    print('essa data não é váldia')
if ((mesInicial == 8) or (mesFinal ==8)) and (((diaInicial < 1) or (diaInicial>31)) or ((diaFinal <1) or (diaFinal >31))): #agosto
    print('essa data não é váldia')
if ((mesInicial == 9) or (mesFinal ==9)) and (((diaInicial < 1) or (diaInicial>30)) or ((diaFinal <1) or (diaFinal >30))): #setembro
    print('essa data não é váldia')
if ((mesInicial == 10) or (mesFinal ==10)) and (((diaInicial < 1) or (diaInicial>31)) or ((diaFinal <1) or (diaFinal >31))): #outubro
    print('essa data não é váldia')
if ((mesInicial == 11) or (mesFinal ==11)) and (((diaInicial < 1) or (diaInicial>30)) or ((diaFinal <1) or (diaFinal >30))): #novembro
    print('essa data não é váldia')
if ((mesInicial == 12) or (mesFinal ==12)) and (((diaInicial < 1) or (diaInicial>31)) or ((diaFinal <1) or (diaFinal >31))): #dezembro
    print('essa data não é váldia')

#fazendo o calculo dos dias usando o calendario juliano
#o mes de janeiro terá o mesmo valor dos dias, depois cada dia terá a soma dos dias do mês anterior
#terá que calcular para cada mês
if mesInicial == 2:
    diaInicial = diaInicial+31
if mesInicial == 3:
    diaInicial = diaInicial+59
if mesInicial == 4:
    diaInicial = diaInicial+90
if mesInicial == 5:
    diaInicial = diaInicial+120
if mesInicial == 6:
    diaInicial = diaInicial+151
if mesInicial == 7:
    diaInicial = diaInicial+181
if mesInicial == 8:
    diaInicial = diaInicial+212
if mesInicial == 9:
    diaInicial = diaInicial+243
if mesInicial == 10:
    diaInicial = diaInicial+273
if mesInicial == 11:
    diaInicial = diaInicial+304
if mesInicial == 12:
    diaInicial = diaInicial+334

#para o mês final agora:
if mesFinal == 2:
    diaFinal = diaFinal+31
if mesFinal == 3:
    diaFinal = diaFinal+59
if mesFinal == 4:
    diaFinal = diaFinal+90
if mesFinal == 5:
    diaFinal = diaFinal+120
if mesFinal == 6:
    diaFinal = diaFinal+151
if mesFinal == 7:
    diaFinal = diaFinal+181
if mesFinal == 8:
    diaFinal = diaFinal+212
if mesFinal == 9:
    diaFinal = diaFinal+243
if mesFinal == 10:
    diaFinal = diaFinal+273
if mesFinal == 11:
    diaFinal = diaFinal+304
if mesFinal == 12:
    diaFinal = diaFinal+334

resultado = diaFinal - diaInicial

if resultado < 0:
    print('a data final é maior que a data inicial, o resultado deu negativo por conta disso: ', resultado)
    print('reinicie o código e faça novamente com uma data melhor, caso queira')
else:
    print('a diferença entre as datas é:', resultado, ' dias')