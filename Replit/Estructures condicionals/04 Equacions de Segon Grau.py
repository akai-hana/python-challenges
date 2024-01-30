import math # necesito esto para poder calcular raices sin volverme loco

# pedir coeficientes al user
a = float(input("Introdueix el coeficient A: "))
b = float(input("Introdueix el coeficient B: "))
c = float(input("Introdueix el coeficient C: "))

# calcular el discriminante
discriminant = b**2 - 4*a*c

# comprobar si el discriminante tiene solucion o no
if discriminant < 0:
    print("L'equació no té solució real.")
elif discriminant == 0:
    # calcular la solucion si es una sola
    x = -b / (2*a)
    print(f"L'equació té una única solució real: x = {x}")
else:
    # calcular las dos soluciones si discriminant =/= 0
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"L'equació té dues solucions reals: x1 = {x1} i x2 = {x2}")
