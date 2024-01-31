import time
import math
import os
from random import randint

print("EXERCISI 1\n")
print("tens 30 segons per fer les multiplicacions\n")
temps1 = time.time()
temps2 = time.time()
encert = 0
errades = 0

while temps2 - temps1 < 30:
  num1 = randint(1, 10)
  num2 = randint(1, 10)
  resultat = num1 * num2
  print(num1, "*", num2, "=")
  resposta = int(input("Introdueix la resposta\n"))

  if resposta == resultat:
    print("Correcte")
    encert = encert + 1
  else:
    print("Incorrecte")
    errades = errades + 1
  temps2 = time.time()

print(f"Has fet {encert} encerts i {errades} errades.\n")

#####

print("EXERCISI 2")
print("Tens 30 segundos per a calcular logaritmes en base 2.\n")
temps1 = time.time()
temps2 = time.time()
encert = 0
errades = 0

while temps2 - temps1 < 30:
    num = randint(2, 100)  # Genera un número aleatorio entre 2 y 100 para asegurar logaritmos enteros en base 2
    resultat = int(math.log2(num))  # Calcula el logaritmo en base 2 del número aleatorio y lo convierte a entero
    print(f"log2({num}) = ?")
    resposta = int(input("Introdueix la resposta: "))

    if resposta == resultat:
        print("Correcte")
        encert += 1
    else:
        print("Incorrecte")
        errades += 1
    temps2 = time.time()

print(f"Has fet {encert} encerts i {errades} errades.\n")
