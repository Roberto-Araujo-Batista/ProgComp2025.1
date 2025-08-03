#ALUNO: Roberto Araujo Batista, Matricula: 20251014050041
#PROFESSOR: Galileu Batista, CURSO: redes de computadores 2025.1, IFRN

'''
primeira parte:
1) (4 pontos) Faça um programa que permita o cadastramento de MAC adresses
vinculados a um CPF. O seu programa suportar as seguintes operações: a) cadastrar
CPF; b) adicionar MAC address a um CPF; c) remover um MAC address de um
CPF; d) remover o CPF (só permitir se não existirem MAC addresses vinculados);
e) listar os CPF cadastrados; f) listar os MAC adresses vinculados a um CPF; 


segunda parte:
g) salvar o “banco de dados” em um arquivo (perguntar o nome do arquivo); h) ler o
“banco de dados” de um arquivo (perguntar o nome do arquivo). 
Em todas as operações que requerem entrada de CPF e MAC adresses, valide-os
'''

'''
"banco de dados" será =
{
    cpf : [mac adress1, mac adress2, mac adress3]
    08333839495 : ['00:1A:2B:3C:4D:5E', '0-1A-2B-3C-4D-5E']
}
'''


def cadastrar_cpf():
    print('programa para cadastrar cpf ainda não foi criado')

def remover_cpf():
    #remover cpf apenas se a lista estiver vazia
    print('programa para remover o cpf ainda não foi criado')

def listar_cpf():
    print('programa para listar cpf ainda não foi criado')

def adicionar_mac():
    print('programa para adicionar mac a um cpf ainda não foi criado')

def remover_mac():
    print('remover mac de um cpf ainda não foi criado')

def listar_mac():
    print('programa para listar mac de um cpf ainda não foi criado')


'''
EXEMPLO DE CÓDIGO
dados = dict()
cpf = '083338384895'
dados[cpf] = ['00:1A:2B:3C:4D:5E']
dados[cpf] = dados[cpf] + ['0-1A-2B-3C-4D-5E']

print(dados)
'''



while True: 
    try: 
        #criar primeiro um menu para saber para onde o usuário irá e por onde começar a programar

        #castras cpf, remover cpf, listar cpf, adicionar mac, remover mac, listar mac
        print('''
        MENU
        1.Cadastrar CPF
        2.Remover CPF
        3.Lista de CPF cadastrados
        4.Adicionar um Mac
        5.remover um Mac
        6.Listar Mac por CPF
        0.Sair
        ''')
        menu = int(input('digite uma opção: '))

        if menu == 0:
            break
        if menu == 1:
            cadastrar_cpf()
        elif menu == 2:
            remover_cpf()
        elif menu == 3:
            listar_cpf()
        elif menu == 4:
            adicionar_mac()
        elif menu == 5:
            remover_mac()
        elif menu == 6:
            listar_mac()
        else:
            print('essa opção não existe')



    except:
        print('comando inválido')



