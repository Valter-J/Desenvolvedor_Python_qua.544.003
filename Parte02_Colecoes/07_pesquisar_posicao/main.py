cidades = ["São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Curitiba",
    "Porto Alegre",
    "Salvador",
    "Recife",
    "Fortaleza",
    "Goiânia",
    "Campinas",
    "Florianópolis",
    "Vitória",
    "Manaus",
    "Belém",
    "Brasília" ]


cidade = input("informe a cidade a ser pesquisada: ").strip().lower()

# mostrar a posição do item na lita
if cidade in cidades:
    indice = cidades.index(cidade)
    print(f"Indice de {cidade} na lista é {indice}.")

else:
    print("Cidade não encontrada")