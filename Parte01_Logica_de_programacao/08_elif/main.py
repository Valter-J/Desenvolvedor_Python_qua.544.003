# Declaração de variáveis
def calcularMedia(nota1, nota2, nota3):
    media = sum(nota1, nota2, nota3)/3

    if media >= 7:
        resultado = nome + "Você Está aprovado"
    elif media < 7 and media == 6:
        resultado = nome + "Você Está de recuperação"
    else:
        resultado =  nome + "Você Está reprovado"

    resultadFinal = []
    resultadFinal.append(resultado)
    
    
    return print(resultadFinal)


nome = input("informe o nome do aluno").title()
nota1 = float(input("Digite a nota 1 do aluno").replace("," ,"."))
nota2 = float(input("Digite a nota 2 do aluno").replace("," ,"."))
nota3 = float(input("Digite a nota 3 do aluno").replace("," ,"."))

calcularMedia(nota1, nota2, nota3)


# verifica se a nota é válida

