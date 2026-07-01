x = float(input("Informe o valor de x: ").replace(",","."))
y = float(input("Informe o valor de y: ").replace(",","."))

# menu
print("1 - Somar")
print("2 - Subtrair")
print("3 - multiplicar")
print("4 - Dividir")



opcao = input("Informe a opção desejada: ").strip()

match opcao:
    case "1":
        print(f"A soma é {x+y}.")
    case "2":
        print(f"A subtração é {x-y}.")
    case "3":
        print(f"A Multiplicação é {x*y}.")
    case "4":
        print(f"A divisão é {x/y}.")
    case _:
        print("Opção inválida")


