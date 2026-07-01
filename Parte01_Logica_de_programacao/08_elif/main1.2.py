
nome = input("informe o nome do aluno").title()
nota = float(input("Digite a nota  do aluno").replace("," ,"."))



# verifica se a nota é válida

if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} está aprovado.")
    elif nota >= 5:
        print(f"{nome} está de recuperaçãor")
    else:
        print(f"{nome} está reprovado.")
else:
    print(f"Nota de {nome} inválida")