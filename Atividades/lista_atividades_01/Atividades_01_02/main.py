'''
Crie um programa que receba uma vez o nome e a idade do usuário, e em seguida mostre os filmes em cartaz em 5 salas de cinema:

- A volta dos Que não Foram (Livre)
- a roda Quadrada (12 Anos)
- As tranças do Rei Careca (14 Anos)
- Poeira em Alto Mar (16 anos)
- A vingança do Frango Assado (18 Anos)
O usuário irá escolher a sala onde o filme desajado está passando.
Caso o usuário não tenha idade, o programa impede sua entrada e 
re-exibe a lista para que o mesmo possa escolher outro filme, 
caso o usuário tenha a idade mínima, o programa grava em arquivo
 o bilhete do filme e encerra o programa
'''

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("\n=========================================\n")
    print("Bem vindo ao Cinema da Bagunça")
    print("Por favor escolha uma das opções abaixo: ")
    print("0 - A volta dos que não foram. CLASS: livre ")
    print("1 - A roda Quadrada. CLASS 12 Anos")
    print("2 - As tranças do Rei Careca. CLASS: 14 Anos")
    print("3 - Poeira em Alto Mar. CLASS: 16 Anos")
    print("4 - A vingança do Frango Assado. CLASS: 18 anos")

    filmes = [["A volta dos que não foram. ", 0],
             ["A roda Quadrada. ", 12],
             ["As tranças do Rei Careca.", 14],
             ["Poeira em Alto Mar.", 16],
             ["A Vingaça do Frango Assado",18]]


    indice = filmes[int(input(""))][1]
    
    return indice

    
def pegarFilme():

    indice = menu()

    filmes = [["A volta dos que não foram. ", 0],
                 ["A roda Quadrada. ", 12],
                 ["As tranças do Rei Careca.", 14],
                 ["Poeira em Alto Mar.", 16],
                 ["A Vingaça do Frango Assado",18]]

    for i in filmes:
        i
        if(indice == i[1]):
            valor = i[0]
            break

    return valor


def gerarBilhete(nome, idade):

    valorFilme= pegarFilme()

    with open(f"Atividades_01_02/arquivos/{nome}.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(
            f"\n=======================================\n"
            f"\n======BEM VINDO AO CINEMINHA ==========\n"
            f"\n=============={nome}===================="
            f"\n=============={idade}==================="
            f"\n======{valorFilme}======"
            "======================================"
        )
    
def abrirbilhete(nome):

    with open(f"Atividades_01_02/arquivos/{nome}.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        print(conteudo)


def verificacaoIdade(idade):
    valorMenu = menu()
    if (idade >=valorMenu):
        return True
    else:
        return False

    
try:

    nome =input("Por favor digite seu Nome:").strip()
    idade = int(input("Por favor digite sua idade"))
    
    while True:

        processo = True
        menu()
        pegarFilme()
        limpar()
        if verificacaoIdade(idade) == True:
            gerarBilhete(nome, idade)
            abrirbilhete(nome)
            processo = False
            break
        else:
            print("Opção inválida, Por favor digite um número do MENU. ")
            continue    
    
except Exception as e:
    print(f"Opção inválida {e}") 