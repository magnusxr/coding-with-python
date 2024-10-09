soma = 0
contador = 0

# SOLICITAR AO USUÁRIO QUE INSIRA 5 NÚMEROS
while contador < 5:
    numero = float(input("Insira um número: "))
    soma += numero
    contador += 1

# EXIBIR A SOMA TOTAL
print(f"A toma total é: {soma}.")
