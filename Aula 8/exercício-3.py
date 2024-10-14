soma = 0

for i in range(4):
    numero = int(input(f"Digite um número: "))

    if numero % 2 != 0:
        soma += numero

print(f"A soma dos números ímpares é: {soma}")
