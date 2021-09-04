from json import loads
from time import sleep


lista_saltos = []
lista_sorteadas = []
lista_medias = []

lista = {}
lista1 = []

"""
Unidade Curricular: Algoritmos e Programação 1	Avaliação - Individual
Professor: Ivonei Marques	Conceito: 
Aluno: Nei Guilherme	Data: 06/20/2021

Competências Avaliadas:
- Saber utilizar os comandos de forma correta.
- Saber criar métodos adequados.
- Saber desenvolver uma solução viável para o problema proposto.
- Saber criar as Classes corretamente.

"""

class Atleta:
    def __init__(self) -> None:
        self.__nome_atleta = ''
        self.__saltos_atleta = [0,0,0,0,0]

    #Getter
    def get_atleta(self) -> str:        
        return self.__nome_atleta
    
    #Setter    
    def set_atleta(self, nome) -> str:                
        self.__nome_atleta = nome    
    
    #Getter    
    def get_saltos_atleta(self):
        return self.__saltos_atleta

    #Setter    
    def set_saltos_atleta(self, saltos):
        self.__saltos_atleta = saltos


    def calcula_medias(self):    
        lista_aquivos = tratamento()
        #print(lista_aquivos)
        for x in lista_aquivos:    
            lista_saltos.append(lista_aquivos[x][0])
        
        for y in lista_saltos:
            a = sorted(y)
            del(a[0])
            del(a[-1])
            lista_sorteadas.append(a)

        for i in lista_sorteadas:
            a = (sum(i)/ len(i))        
            lista_medias.append(a)   


class Clube:
    def __init__(self) -> None:
        self.__nome_clube = ''
        self.__atletas_do_clube = []

    #Getter
    def get_clube(self) -> str:
        return self.__nome_clube
    #Setter
    def set_clube(self, nome) -> str:
        self.__nome_clube = nome   
    

class Cores:
    def cor(element, color):
        if color == 'green':
            return f'\033[32m{element} \033[m'
        elif color == 'red':
            return f'\033[31m{element} \033[m'
        elif color == 'blue':
            return f'\033[34m{element} \033[m'
        elif color == 'yellow':
            return f'\033[33m{element} \033[m'


class Menu:    
    def menu_principal():        
        print(Cores.cor('\n====================================\n               MENU \n====================================', 'green'))
        print("""0 - Finaliza\n1 - Cadastra o Atleta\n2 - Cadastra os Saltos do Atleta\n3 - Relatório de Geral Atleta\n4 - Cadastra Clube do Atleta\n5 - Relatório de Atletas por Clube\n6 - Relatório de Final\n""")
        print(Cores.cor('====================================\n', 'green'))

    def menu_atletas():
        lista_aquivos = tratamento()
        print('='*40)
        print(' '*8, '--ATLETAS CADASTRADOS--')
        print('='*40)

        for x in lista_aquivos.keys():
            print(f'{x.lower().capitalize()}')            
        print('='*40) 

    def menu_relatorio():
        lista_aquivos = tratamento()
        if len(lista_aquivos) > 0:            
            print('\n'+'='*50)
            print('RELATÓRIO:\n\nAtletas:             Saltos:')          
            for x in lista_aquivos:            
                print(f'{x.lower().capitalize():<20}: {lista_aquivos[x][0]}')                
            print('='*50)
        else:
            print(Cores.cor('Nâo há atletas cadastrados ainda...', 'yellow'))

    def menu_atletas_sem_clube():
        lista_aquivos = tratamento()

        print(Cores.cor('='*36, 'green'))
        print(Cores.cor('   ATLETAS CADASTRADOS SEM CLUBE     ', 'green'))
        print(Cores.cor('='*36, 'green'))
        for x in lista_aquivos:
            for y in lista_aquivos[x][1]:
                if y == '':
                    print(x)
                break     
        print(Cores.cor('='*36, 'green'))       

    def menu_medias():
        lista_aquivos = tratamento()
        if len(lista_aquivos) > 1:
            a.calcula_medias()
            print(Cores.cor('='*36, 'green'))
            print(Cores.cor('ATLETAS                  MÉDIAS', 'green'))
            print(Cores.cor('='*36, 'green'))

            for x,y in enumerate(lista_aquivos.keys()):
                w = lista_medias[x]  
                print(f'{y.lower().capitalize():<26} {w:.2f}')            
            print(Cores.cor('='*36, 'green'))
        else:
            print(Cores.cor('Nâo há atletas cadastrados ainda...', 'yellow'))

    def menu_clube_atleta():
        relatorio_clube_atleta()        
        if len(lista) > 0:
            print(Cores.cor('='*36, 'green'))
            print(Cores.cor('   CLUBES     ATLETAS DO CLUBE  ', 'green'))
            print(Cores.cor('='*36, 'green'))
            for x in lista.items():
                if x[0] == '':
                    print(f'{"Sem Clube":<13} {x[1]}')
                else:                
                    print(f'{x[0]:<13} {x[1]}')            
            print(Cores.cor('\n'+'='*36+'\n', 'green'))        

        else:            
            print(Cores.cor('Não há clubes cadastrados ainda!!!', 'yellow'))
    
    def sugestao_clube():
        relatorio_clube_atleta()  
        if len(lista) > 1:
            print(Cores.cor('='*36, 'green'))
            print(Cores.cor('       SUGESTÃO DE CLUBES!!!  ', 'green'))
            print(Cores.cor('='*36, 'green'))
            
            for i in lista.items():
                print(i[0])
            print(Cores.cor('='*36, 'green'))
        else:
            pass


def relatorio_clube_atleta():
    lista_arquivo = tratamento()    
    for x in lista_arquivo.values():  
        if x[1][0] in lista:
            pass
        else:
            lista[x[1][0]] = []  

    for x in lista:
        lista_copia = []
        for y in lista_arquivo.items():
            if x == y[1][1][0]:
                lista_copia.append(y[0])           
        lista1.append(lista_copia)

    for i,y in enumerate(lista):
        lista[y] = lista1[i]


def tratamento_dois():
        lista_aquivos = tratamento()        

        q = False
        for x in lista_aquivos:
            for y in lista_aquivos[x][1]:
                if y == '':                    
                    q = True
                    break
                else:
                    pass
        return q   


def tratamento():
    with open('arquivo.txt', 'r') as arquivo:
        arq = arquivo.read()
        try:
            c = arq.replace("'", '"')
            b = loads(c)
            return b
        except:
            return {}


def cadastra_atleta():        
    lista_atleta = tratamento()
    global new_atleta

    try:
        x = 0
        while x != '999':
            new_atleta = str(input('Novo Atleta [999 para sair]: ')).strip().upper()
            if new_atleta != '999':
                if new_atleta in lista_atleta:
                    print(Cores.cor('Atleta já cadastrado(a)...', 'yellow'))
                    continue
                if new_atleta == '':
                    print(Cores.cor('Escreva o atleta desejado!', 'yellow'))
                    continue
                if len(new_atleta) <= 2:
                    print(Cores.cor('Digite pelo menos 3 caracteres.', 'yellow'))
                    continue
                else:                                   
                    a.set_atleta(new_atleta)                    
                    lista_atleta[a.get_atleta()] = [[0,0,0,0,0],['']]
                    print(Cores.cor('Atleta cadastrado(a) com sucesso!', 'blue'))
                    break
            x = '999'
    except:
        print(Cores.cor('Aconteceu algo... tente novamente!', 'red'))

    b = str(lista_atleta)
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write(b)


def cadastra_salto():
    lista_arquivo = tratamento()
    lista_saltos = []

    if len(lista_arquivo) > 0:
        Menu.menu_atletas()
        w = True
        while w:
            try:
                nome_atleta = input('Qual o atleta que desejas cadastras saltos? [999 para sair]: ').strip().upper()
                if nome_atleta in lista_arquivo:
                    while True:
                        try:                                                                                 
                            while len(lista_saltos) < 5:                                                         
                                saltos = float(input(f'Qual a distância do salto? : '))
                                if type(saltos) == float:
                                    lista_saltos.append(saltos)                                   

                                else:
                                    print(Cores.cor('Digite somente numeros!!!', 'red'))                                                           

                            a.set_saltos_atleta(lista_saltos)
                            lista_arquivo[nome_atleta][0] = a.get_saltos_atleta()                                                       
                            break                            
                        except:
                            print(Cores.cor('Aconteu algum erro, tente novamente!!!', 'red'))

                    w = False
                elif nome_atleta == '999':
                    w = False
                else:
                    print(Cores.cor('Atleta não cadastrado(a)...', 'yellow'))
            except:
                print(Cores.corr('Aconteu algum erro, tente novamente!!!', 'red'))
                pass
    else:
        print(Cores.cor('Nâo há atletas cadastrados ainda...', 'yellow'))
    
    b = str(lista_arquivo)
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write(b)
 

def cadastro_club():
    lista_clube = tratamento()
    global new_clube

    try:
        x = 0
        while x != '999':
            if len(lista_clube) < 1:
                print(Cores.cor('Ainda não há atletas cadastrados!... ', 'yellow'))
                x = '999'
            else:
                Menu.sugestao_clube()
                new_clube = str(input('Novo clube [999 para sair]: ')).strip().upper()
                if new_clube != '999':               
                    if new_clube == '':
                        print(Cores.cor('Escreva o clube desejado!', 'yellow'))
                        continue

                    elif len(new_clube) <= 2:
                        print(Cores.cor('Digite pelo menos 3 caracteres.', 'yellow'))
                        continue                

                    else:
                        if tratamento_dois() == True:
                            c.set_clube(new_clube)                 
                            print(Cores.cor('Clube ok! Agora vincule ao seu atleta!', 'blue'))

                            Menu.menu_atletas_sem_clube()
                            while True:                        
                                escolha = str(input('Qual o atleta citado a cima você gostaria de vincular ao clube?: ')).upper().strip()
                                if escolha in lista_clube:
                                    lista_clube[escolha][1] = [c.get_clube()]                                               
                                    print(Cores.cor('Clube cadastrado com sucesso!', 'blue'))
                                    break
                                else:
                                    print(Cores.cor('Por favor digite corretamente o nome do atleta!...', 'red'))
                        else:
                            print(Cores.cor('Todos atletas possuem clube... cadastre um novo atleta!. ', 'yellow'))
                            break
                x = '999'

    except:
        print(Cores.cor('Aconteceu algo... tente novamente!', 'red'))

    b = str(lista_clube)
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write(b)
    pass


def programa():
    with open('arquivo.txt', 'at+'):
        print(Cores.cor('Arquivo acessado!...', 'blue'))
    
    escolha = ''
    while escolha != '0':        
        Menu.menu_principal()
        escolha = str(input("Escolha: "))

        if escolha == '1':        
            cadastra_atleta(), sleep(1)
        elif escolha == '2':        
            cadastra_salto(), sleep(1)
        elif escolha == '3':        
            Menu.menu_relatorio(), sleep(1)
        elif escolha == '4':
            cadastro_club(), sleep(1)
        elif escolha == '5':            
            Menu.menu_clube_atleta(), sleep(1)                       
        elif escolha == '6':            
            Menu.menu_medias(), sleep(1)    


# ******************      MAiN     ******************
a = Atleta()
c = Clube()
programa()            
