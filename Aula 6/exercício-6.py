# JEITO 1

x, y = input("Digite dois números: ").split()

x = int(x)
y = int(y)

menu = input("\nSelecione uma das opções:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n> ")

match menu:
    case "1":
        print(f"\nO resultado é: {x+y}")

    case "2":
        print(f"\nOs resultados são: {x-y} e {y-x}")

    case "3":
        print(f"\nO resultado é: {x*y}")

    case "4":
        print(f"\nOs resultados são: {x/y} e {y/x}")

    case _:
        print("\nComando inválido.")


# JEITO 2
        
x = int(input("Digite um número: "))

y = int(input("Digite um número: "))

menu = input("\nSelecione uma das opções:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n> ")

if menu == "1":
    print(f"\nO resultado é: {x+y}")

elif menu == "2":
    print(f"\nO resultado é: {x-y}")

elif menu == "3":
    print(f"\nO resultado é: {x*y}")

elif menu == "4":
    print(f"\nO resultado é: {x/y}")

else:
    print("\nComando inválido.")
