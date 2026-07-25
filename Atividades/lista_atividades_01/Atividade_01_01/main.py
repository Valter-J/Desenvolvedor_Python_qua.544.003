# TODO: Atividade 01

"""Crie um programa que receba o nome, peso e altura do usuário 
e informe na tela o seu IMC o seu diagnóstico com base no valor IMC"""

print("\n===================================\n")
print("Olá bem vindo ao Calculo do seu IMC")
print("\n===================================\n")


nome = input("Por favor, digite seu nome: ").strip()
altura = float(input("Por favor digite sua altura: ").replace(",","."))
peso = float(input("Por favor, digite seu peso em kG: "))


Calculo = peso /(altura**2)

if (Calculo < 18.5):
    print(f"{nome}, você está abaixo do Peso, tem que comer mais.")

elif (Calculo < 25.5):
    print(f"{nome}, você está no peso ideial. Continue assim. ")

elif (Calculo < 29.9):
    print(f"{nome}, você está com excesso de peso, parar de comer. ")
    
elif (Calculo < 34.9):
    print(f"{nome}, você com obesidade classe I, esse caminho é tendencioso")
    
elif (Calculo < 39.9):
    print(f"{nome}, você com obesidade classe II, meu Deus, consegue andar ? ")

else:
    print(f"{nome}, meu amigo, pode deixar pra proxima vida, que essa não dá mais tempo")

