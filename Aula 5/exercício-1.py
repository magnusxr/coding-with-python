item1 = input("Olá! Selecione o(s) item(s) desejado(s):\n1 - Hambúrguer por R$10,00\n2 - Refrigerante por R$10,00\n3 - Batata-frita por R$10,00\n> ")

valor = 10
valor_combo = 22

if item1 == "1":   # HAMBÚRGUER
    item1 = "hambúrguer"
    item2 = "refrigerante"
    item3 = "batata-frita"

    adicional = input(f"\nVocê escolheu {item1}, no valor de R${valor}. Deseja adicionar mais algum item?\n1 - Refrigerante por R$10,00\n2 - Batata-frita por R$10,00\n> ")

    if adicional == "1":
        valor = 20

        combo = input(f"\nVocê selecionou {item1} e {item2}, no valor de R${valor}. Deseja completar o combo por mais R$2?\n1 - Sim\n2 - Não\n> ")

        if combo == "1":
            print(f"\nVocê selecionou o combo de hambúrguer, refrigerante e batata-frita! O valor total é de R${valor_combo}.")

        elif combo == "2":
            print(f"\nSeu total é de R${valor}, com {item1} e {item2}.")

        else:
            print("Escolha inválida.")

    elif adicional == "2":
        valor = 20

        combo = input(f"\nVocê selecionou {item1} e {item3}, no valor de R${valor}. Deseja completar o combo por mais R$2?\n1 - Sim\n2 - Não\n> ")

        if combo == "1":
            print(f"\nVocê selecionou o combo de hambúrguer, refrigerante e batata-frita! O valor total é de R${valor_combo}.")

        elif combo == "2":
            print(f"\nSeu total é de R${valor}, com {item1} e {item3}.")

        else:
            print("Escolha inválida.")

    else:
        print("Escolha inválida.")
        

elif item1 == "2":  # REFRIGERANTE
    item1 = "refrigerante"
    item2 = "hambúrguer"
    item3 = "batata-frita"

    adicional = input(f"\nVocê escolheu {item1}, no valor de R${valor}. Deseja adicionar mais algum item?\n1 - Hambúrguer por R$10,00\n2 - Batata-frita por R$10,00\n> ")

    if adicional == "1":
        valor = 20

        combo = input(f"\nVocê selecionou {item1} e {item2}, no valor de R${valor}. Deseja completar o combo por mais R$2?\n1 - Sim\n2 - Não\n> ")

        if combo == "1":
            print(f"\nVocê selecionou o combo de hambúrguer, refrigerante e batata-frita! O valor total é de R${valor_combo}.")

        elif combo == "2":
            print(f"\nSeu total é de R${valor}, com {item1} e {item2}.")

    elif adicional == "2":
        valor = 20

        combo = input(f"\nVocê selecionou {item1} e {item3}, no valor de R${valor}. Deseja completar o combo por mais R$2?\n1 - Sim\n2 - Não\n> ")

        if combo == "1":
            print(f"\nVocê selecionou o combo de hambúrguer, refrigerante e batata-frita! O valor total é de R${valor_combo}.")

        elif combo == "2":
            print(f"\nSeu total é de R${valor}, com {item1} e {item3}.")

        else:
            print("Escolha inválida.")

    else:
        print("Escolha inválida.")


elif item1 == "3":  # BATATA-FRITA
    item1 = "batata-frita"
    item2 = "hambúrguer"
    item3 = "refrigerante"    

    adicional = input(f"\nVocê escolheu {item1}, no valor de R${valor}. Deseja adicionar mais algum item?\n1 - Hambúrguer por R$10,00\n2 - Refrigerante por R$10,00\n> ")

    if adicional == "1":
        valor = 20

        combo = input(f"\nVocê selecionou {item1} e {item2}, no valor de R${valor}. Deseja completar o combo por mais R$2?\n1 - Sim\n2 - Não\n> ")

        if combo == "1":
            print(f"\nVocê selecionou o combo de hambúrguer, refrigerante e batata-frita! O valor total é de R${valor_combo}.")

        elif combo == "2":
            print(f"\nSeu total é de R${valor}, com {item1} e {item2}.")

    elif adicional == "2":
        valor = 20

        combo = input(f"\nVocê selecionou {item1} e {item3}, no valor de R${valor}. Deseja completar o combo por mais R$2?\n1 - Sim\n2 - Não\n> ")

        if combo == "1":
            print(f"\nVocê selecionou o combo de hambúrguer, refrigerante e batata-frita! O valor total é de R${valor_combo}.")

        elif combo == "2":
            print(f"\nSeu total é de R${valor}, com {item1} e {item3}.")

        else:
            print("Escolha inválida.")

    else:
        print("Escolha inválida.")

else:
    print("Escolha inválida.")
