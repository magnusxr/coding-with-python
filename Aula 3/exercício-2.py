print("Calculadora de IMC")

peso = float(input("Qual o seu peso em KG? "))
altura = float(input("Qual a sua altura em metros? "))

imc = peso / altura**2

print(f"Seu IMC é igual a: {imc:.1f}")
