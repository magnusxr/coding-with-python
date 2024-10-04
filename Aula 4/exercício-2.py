rodas = int(input("Quantas rodas seu veículo tem? "))

if rodas % 2 != 0 and rodas != 1:
    print("Nenhum veículo correspondente encontrado.")

else:
    if rodas == 1:
        print("Seu veículo é um monociclo.")

    elif rodas == 2:
        print("Seu veículo é uma moto.")

    elif rodas == 4:
        print("Seu veículo é um carro ou van.")

    elif rodas == 6:
        print("Seu veículo é um ônibus.")

    elif 8 <= rodas <= 20:
        print("Seu veículo é um caminhão.")
