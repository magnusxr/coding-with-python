pontos = 0
perguntas = 3


while True:
    p1 = input("\n[] é o símbolo para lista? V ou F\n> ").lower()
    if p1 == "v":
        print("\nVocê acertou!")
        pontos += 1
    else:
        print("\nVocê errou. O símbolo para lista é [].")


    p2 = input("\n<> é o símbolo para dicionário. V ou F\n> ").lower()
    if p2 == "f":
        print("\nVocê acertou!")
        pontos += 1

    else:
        print("\nVocê errou. O símbolo para dicionário é {}.")

    p3 = input("\nO símbolo '=' significa 'igual a'. V ou F\n> ").lower()
    if p3 == "f":
        print("\nVocê acertou!")
        pontos += 1

    else:
        print("\nVocê errou. O símbolo que significa 'igual a' é ==.")

    if pontos > perguntas/2:
        print(f"\nParabéns! Você ganhou com {pontos} pontos!")

    else:
        print(f"\nNão foi dessa vez! Você perdeu com {pontos} pontos!")

    jogar = input("\nJogar novamente? S/N\n> ").lower()
    if jogar == "s":
        continue

    else:
        print("Obrigado por jogar!")
        break