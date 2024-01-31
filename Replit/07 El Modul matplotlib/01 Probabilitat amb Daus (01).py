import random
comptador_dobles = 0

num_repeticions = int(input("Selecciona el nombre de repeticiones: "))

for i in range(num_repeticions):
    dau1 = random.randint(1, 6)
    dau2 = random.randint(1, 6)

    if dau1 == dau2:
        comptador_dobles += 1

print(f"Nombre de dobles en {num_repeticions} tirades: {comptador_dobles}" )