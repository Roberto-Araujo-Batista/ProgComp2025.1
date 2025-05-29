somaQuadrado = 0
quadradoSoma = 0 

for i in range(101):
    somaQuadrado = somaQuadrado + i**2
    quadradoSoma = quadradoSoma + i
quadradoSoma = quadradoSoma**2

resultado = quadradoSoma - somaQuadrado
print(resultado)
