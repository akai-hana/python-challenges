#Exemple 1 Programa que genera una llista aleatòria de 20 números entre 1 i 200
from random import randint

llista_1 = []
for i in range(20):
  a = randint(1, 200)
  llista_1.append(a)
print("llista aleatòria= ", llista_1)
print(40 * "=")

#Exemple 2 Programa que crea una llista ordenada de petita a gran amb el contingut de la llista_1
print("EXEMPLE 2")
llista_2 = llista_1.copy()
llista_ordenada = []
petit = 1000
for i in range(20):
  for num in llista_2:
    if num < petit:
      petit = num
  llista_ordenada.append(petit)
  llista_2.remove(petit)
  petit = 1000
print("llista ordenada= ", llista_ordenada)
print(40 * "=")
#Exercici 1 Crea un programa que geneneri una llista aleatòria de 10 números entre 1 i 500
from random import randint

llista_aleatoria = []
for i in range(10):
  numero = randint(1, 500)
  llista_aleatoria.append(numero)

print("Lista aleatoria =", llista_aleatoria)

#Exercici 2 Crea un programa que crei una llista ordenada de petit a gran amb la llista anterior
llista_ordenada = sorted(llista_aleatoria)
print("Lista ordenada de menor a mayor =", llista_ordenada)

#Exercici 3 Crea un programa que ordeni la llista anterior de gran a petit
llista_ordenada_desc = sorted(llista_aleatoria, reverse=True)
print("Lista ordenada de mayor a menor =", llista_ordenada_desc)
