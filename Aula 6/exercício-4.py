# JEITO 1
pares = []

for i in range(20, 41):
    
    if i % 2 == 0:

        pares.append(i)

print(pares)

# JEITO 2
for i in range(20, 41, 2):
    print(i)

# JEITO 3

x = 20

while 20 <= x <= 40:

    print(x)
    x += 2
