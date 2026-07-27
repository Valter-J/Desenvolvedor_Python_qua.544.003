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

try:
    nome =input("Por favor digite seu Nome:").strip()
    idade = int(input("Por favor digite sua idade"))
    
    while True:
        
        print("\n=========================================\n")
        print("Bem vindo ao Cinema da Bagunça")
        print("Por favor escolha uma das opções abaixo: ")
        print("1 - A volta dos que não foram. CLASS: livre ")
        print("2 - A roda Quadrada. CLASS 12 Anos")
        print("3 - As tranças do Rei Careca. CLASS: 14 Anos")
        print("4 - Poeira em Alto Mar. CLASS: 16 Anos")
        print("5 - A vingança do Frango Assado. CLASS: 18 anos")
        opcao = int(input())
        
        os.system("cls" if os.name == "nt" else "clear")
        
        match opcao:
            
            case 1:
                if (idade > 0):
                    print("Bem vindo a sala 1, Bom filme. ")
                    break
                    
            case 2: 
                if (idade > 12):
                    print("Bem vindo a sala 2, Bom filme. ")
                    break
                else:
                    print("Opss, você não tem idade Suficiente. Por favor retorne ao MENU. ")
                    continue
            case 3:
                if (idade > 14):
                    print("Bem vindo a sala 3, Bom filme. ")
                    break
                else:
                    print("Opss, você não tem idade Suficiente. Por favor retorne ao MENU. ")
                    continue
            case 4:
                if (idade > 14):
                    print("Bem vindo a sala 4, Bom filme. ")
                    break
                else:
                    print("Opss, você não tem idade Suficiente. Por favor retorne ao MENU. ")
                    continue
            case 5:
                if (idade > 14):
                    print("Bem vindo a sala 5, Bom filme. ")
                    break
                else:
                    print("Opss, você não tem idade Suficiente. Por favor retorne ao MENU. ")
                    continue
            case _:
                print("Opção inválida, Por favor digite um número do MENU. ")
                continue
    
    
except Exception as e:
    print(f"Opção inválida {e}") 