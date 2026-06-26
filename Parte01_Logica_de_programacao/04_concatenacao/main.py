# declaracção de variáveis

nome = input("Informe seu nome: ")
telefone = input("Informe seu telefone: ")

# Saída de dados

# Exibe uma mensagem usando vários argumentos separados por vírgula.
# O print adiciona espaços automaticamente entre os argumentos.
print("Olá", nome,", e meu telefone é ", telefone, "." )

# Exibe a mesma mensagem concatenando (juntando) as strings com o operador +.
# Todas as partes precisam ser do tipo string.
print("Olá" + nome + ", e meu telefone é " + telefone + ".")

# Exibe a mensagem usando o método format().
# As chaves {} são substituídas pelos valores passados ao format().
print("Olá {}, e meu nome telefone é {}.".format(nome, telefone))


# Exibe a mensagem usando uma f-string.
# É a forma mais moderna, simples e recomendada no Python.
print(f'olá, {nome}, e meu telefone é {telefone}')


