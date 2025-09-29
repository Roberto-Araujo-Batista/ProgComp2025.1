#programa para converter ips em decimal para lista

def convertInt(ipstring : str) -> int:
    octetos = ipstring.split('.')
    ipbinario = []

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
        
        ipbinario += [binario]
    return ipbinario




#com o formato de listas da para separar e saber quais são cada octeto
print(convertInt("19.128.10.41"))