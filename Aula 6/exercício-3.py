soma = 0

while True:
    numero = float(input("Insira um número positivo: "))
    parar = input("Aperte ENTER para continuar ou digite 'parar' para receber a soma: ").lower()

    if parar == "parar":
        print(f"A soma total é: {soma}.")

    else:
        soma += numero
