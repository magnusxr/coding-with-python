pretinho = 5

escolha = input("Bem-vindo ao lava-jato! Escolha o tipo de lavagem desejada:\n1 - Lavagem Completa por R$50\n2 - Lavagem Básica por R$35\n> ")

if escolha == "1":
    lavagem = "lavagem completa"
    valor = 50

    adicional = input(f"\nVocê escolheu a {lavagem}, no valor de R${valor}. Deseja adicionar o pretinho por mais R$5?\n1 - Sim\n2 - Não\n> ")

    if adicional == "1":
        valor_total = 55
        total = print(f"\nVocê escolheu a {lavagem} e o pretinho, no total de R${valor_total}.")

    elif adicional == "2":
        print(f"\nVocê escolheu somente a {lavagem}, no valor de R${valor}.")

    else:
        print("Escolha inválida.")

elif escolha == "2":
    lavagem = "lavagem básica"
    valor = 35

    adicional = input(f"\nVocê escolheu a {lavagem}, no valor de R${valor}. Deseja adicionar o pretinho por mais R$5?\n1 - Sim\n2 - Não\n> ")

    if adicional == "1":
        valor_total = 40
        total = print(f"\nVocê escolheu a {lavagem} e o pretinho, no total de R${valor_total}.")

    elif adicional == "2":
        print(f"\nVocê escolheu somente a {lavagem}, no valor de R${valor}.")

    else:
        print("Escolha inválida.")

else:
    print("Escolha inválida.")

adicional = input(f"\nVocê escolheu a {lavagem}, no valor de R${valor}. Deseja adicionar o pretinho por mais R$5?\n1 - Sim\n2 - Não\n> ")

if adicional == "1":
    valor =+ 5
    print(f"\nVocê escolheu a {lavagem} e o pretinho, no total de R${valor_total}.")