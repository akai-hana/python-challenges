# Cojer los 4 numeros enteros
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))
c = int(input("Ingrese el tercer número entero: "))
d = int(input("Ingrese el cuarto número entero: "))

# vale, pues no se puede usar la funcion max...
max = a
if b > max:
  max = b
if c > max:
  max = c
if d > max:
  max = d

print("El número más grande es:", max)
