usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'Cpf': "123.456.789-12"
}

# exibe os dados do dicionário
print("FORMA 1\n")
print(f"Nome: {usuario['nome']}")
print(f"idade: {usuario['idade']}")
print(f"E-mail: {usuario['email']}")
print(f"Cpf: {usuario['Cpf']}")

print("FORMA 2\n")
print(f"Nome: {usuario.get('nome')}")
print(f"idade: {usuario.get('idade')}")
print(f"E-mail: {usuario.get('email')}")
print(f"Cpf: {usuario.get('Cpf')}")

print("FORMA 3\n")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")