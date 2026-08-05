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


cidade = input("Informe o país a ser pesquisado: ").strip().strip()


qtd = cidades.count(cidade)

print(f"{cidade} foi encontrado {qtd} vezes na lista.")