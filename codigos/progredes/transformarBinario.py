#programa para transformar número em binario
def transformarBinario(numero):
    novonumero = numero
    expoente = 7
    binario = 0
    while expoente >= 0:
        divisao = novonumero // 2**expoente
        if divisao:
            novonumero = novonumero - 2**expoente
        expoente = expoente -1
        binario = binario *10 + divisao
    return binario


print(transformarBinario(255))