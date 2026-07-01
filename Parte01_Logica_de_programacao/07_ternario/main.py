# Declaração de variaveis

nome = input("Informe seu nome: ").title()

idade = int(input("informe sua idade: "))


print(f"{nome} é maior de idade." if idade >= 18 else f"{nome} é menor de idade")