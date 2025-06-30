import random

lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

#gerando notas dos alunas de forma aleatória
contador = 0
lstNotas = list()
while contador < len(lstNomes):
    lstNotas = lstNotas + [[random.randint(0,100), random.randint(0,100)]]
    media = (2* lstNotas[contador][0] + 3 *lstNotas[contador][1])/5

    aluno = lstNomes[contador]
    nota = lstNotas[contador]
    
    if media < 60: #alunos que irão para prova final
        print(f'o {aluno} foi para prova final com media {media}')
        lstNotas[contador] = lstNotas[contador] + [random.randint(0,100)]
    else:
        print(f'o {aluno} foi aprovado com media {media}')
    contador = contador + 1
    
