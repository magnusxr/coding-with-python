print("Calculadora de IMC")

peso = float(input("Qual o seu peso em KG? "))
altura = float(input("Qual a sua altura em metros? "))

imc = peso / altura**2

classif =  f"Seu IMC é igual a {imc:.1f}. "

if imc < 18.5:
    print(classif + "Classificação: MAGREZA. Grau: 0.")
elif 18.5 <= imc < 25:
    print(classif + "Classificação: NORMAL. Grau: 0.")
elif 25 <= imc < 30:
    print(classif + "Classificação: SOBREPESO. Grau: 1.")
elif 30 <= imc < 40:
    print(classif + "Classificação: OBESIDADE. Grau: 2.")
elif 40 <= imc:
    print(classif + "Classificação: OBESIDADE GRAVE. Grau: 3.")
else:
    print("Classificação não encontrada.")
