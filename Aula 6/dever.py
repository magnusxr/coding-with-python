print("Bem-vindo ao programa de reciclagem!")

contagem = {"Papel": 0, "Plástico": 0, "Vidro": 0, "Metal": 0, "Orgânico": 0, "Resíduos Não Recicláveis": 0}

def reciclar(material):
    match material:
        case "1":
            print(f"\nLixeira Azul.")
            contagem["Papel"] += 1

        case "2":
            print(f"\nLixeira Vermelha.")
            contagem["Plástico"] += 1

        case "3":
            print(f"\nLixeira Verde.")
            contagem["Vidro"] += 1

        case "4":
            print(f"\nLixeira Amarela.")
            contagem["Metal"] += 1

        case "5":
            print(f"\nLixeira Marrom.")
            contagem["Orgânico"] += 1

        case "6":
            print(f"\nLixeira Cinza.")
            contagem["Resíduos Não Recicláveis"] += 1

        case _:
            print("\nErro: Comando Inválido. Tente novamente.")

while True:
    
    material = input("\nInforme o material que você deseja reciclar:\n1 - Papel\n2 - Plástico\n3 - Vidro\n4 - Metal\n5 - Orgânico\n6 - Resíduos Não-Recicláveis\n> ")

    reciclar(material)
    
    continuar = input("\nDeseja continuar reciclando? S/N\n> ").lower()
    
    if continuar == "s":
        reciclar(material)

    elif continuar == "n":
        print("\nObrigado por contribuir com a reciclagem!")

        print("\nResumo:")

        for material, quantidade in contagem.items():
            print(f"{material}: {quantidade}")
        
        break

    else:
        print("\nErro: Comando Inválido. Tente novamente.")
