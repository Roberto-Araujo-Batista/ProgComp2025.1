#programa que mostra a nota baseado nos critéios do IFRN
#autor/aluno: Roberto Araujo Batista, matrícula: 20251014050041, Redes de Computadores 2025.1
#professor: Galileu

#as formulas e informações usadas em comentários foram retiradas da página 59 do ppc do IFRN, enquanto conferir o código, consulte o arquivo.


#entrada de dados e declaração de variáveis:
print('Calculadora de nota IFRN')
print('/////////////////////')
notaPrimeiro = float(input('informe sua nota no primeiro bimestre: '))
notaSegundo = float(input('informe sua nota no segundo bimestre: '))
media = (2*notaPrimeiro + 3*notaSegundo)/5  #md = (2n1 + 3n2)/5
media = round(media,2)

mediaIdeal = 60
provaFinal = 0
opcao1 = 0 # opções para a media final
opcao2 = 0
opcao3 = 0
mediafinal = 0


print('/////////////////////')
if media >= mediaIdeal: #caso tenha passado
    print('meus parabéns, sua media foi ', media,' você foi aprovado!')
else:
    if media >=20: #media menor que 60 maior igual a 20, vai para prova final
        print('/////////////////////')
        print('essa não! você foi para a prova final, sua media foi ', media)
        provafinal = float(input('Qual foi sua nota na prova final? '))
        opcao1 = (media + provafinal)/2 #mfd = (md + naf)/2
        opcao2 = (2*provafinal + 3*notaSegundo)/5 #mfd = (2naf + 3n2)/5
        opcao3 = (2*notaPrimeiro + 3*provafinal)/5 #mfd = (2n1 + 3naf)/5
        #mfd = media final, naf = nota prova final 
        if (opcao1 > opcao2) and (opcao1 > opcao3): #verificar se a opcao1 é a maior nota
            mediafinal = round(opcao1, 2)
        else: 
            if(opcao2 > opcao1) and (opcao2 > opcao3): #senão for a primeira verifica se é a segunda
                mediafinal = round(opcao2,2)
            else: #senão é nenhuma das duas só pode ser a opcao3
                mediafinal = round(opcao3, 2)
            #aprovação ou reprovação com média final
            if mediafinal >= 60:
                print('meus parabéns, sua média foi ', mediafinal, 'você foi aprovado!')
            else:
                if mediafinal <60:
                    print('infelizmente, você foi reprovado, sua nota média final foi: ', mediafinal)
