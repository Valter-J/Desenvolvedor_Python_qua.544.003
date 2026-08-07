usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'Cpf': "123.456.789-12"
}

# usuário informa a chave que deseja alterar

chave = input("informe o nome da chave: ").strip().lower()


if chave in usuario:
    
    # usuário informa o novo valor para a chave
    usuario[chave] = input(f"Informe o novo valor para a {chave}").strip()
    
    # Exibe o dicionário com novo valor da chave escolhida
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    
else:
    print("Chave não encontrada")

