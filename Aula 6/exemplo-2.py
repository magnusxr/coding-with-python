import time

print("Inciando contagem regressiva.")

contador = 5

while contador > 0:
    print(contador)
    time.sleep(1)  #  sleep = delay de x segundos
    contador -= 1

print("Fim da contagem regressiva!")
