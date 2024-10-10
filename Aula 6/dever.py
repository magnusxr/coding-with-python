# INFORMAR A COR DA LIXEIRA CORRETA

print("Bem-vindo ao programa de reciclagem!")

material = input("Informe o material que você deseja reciclar:\n1 - Papel\n2 - Plástico\n3 - Vidro\n4 - Metal\n5 - Orgânico\n6 - Resíduos Não-Recicláveis\n> ")

match material:
    case "1":
        print(f"\nLixeira Azul")

    case "2":
        print(f"\nLixeira Vermelha")

    case "3":
        print(f"\nLixeira Verde")

    case "4":
        print(f"\nLixeira Amarela")

    case "5":
        print(f"\nLixeira Marrom")

    case "6:":
        print(f"\nLixeira Cinza")

    case _:
        print("\nErro: Comando Inválido. Tente novamente.")

