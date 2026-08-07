usuario = [
    {'nome': "Fulano",
     'idade':18,
     'email': "fulano@gmail.com"},
    
    {
        'nome':"cicrano",
        'idade': 21,
        'email': "cicrano@gmail.com"
    },
    {
        'nome':"cicrano",
        'idade': 21,
        'email': "cicrano@gmail.com"
    }
    
]


# percore a lista de dicionários

for usuario in usuario:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")