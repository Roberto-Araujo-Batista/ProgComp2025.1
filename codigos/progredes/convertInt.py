def convertInt(ipstring : str) -> int:
    octetos = ipstring.split('.')
    ipbinario = 0

    for octeto in octetos:
        novonumero = int(octeto)
        expoente = 7
        binario = 0
        while expoente >= 0:
            divisao = novonumero // 2**expoente
            if divisao:
                novonumero = novonumero - 2**expoente
            expoente = expoente -1
            binario = binario *10 + divisao
        
        ipbinario = (ipbinario *10**8) #para "andar" oito casas para o lado
        ipbinario = ipbinario + binario
    return ipbinario




#não da para saber quais são os octetos em binário já que com int ele não aceita os 0 na frente
print(convertInt("192.128.10.41"))
