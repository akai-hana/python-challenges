#Exemple 1 Programa que demana un número enter i mostra per pantalla seu valor doble en bucle. Per sortir del bucle introduir un número negatiu.
while True:
num = int(input("Introdueix un número enter (o un negatiu per sortir): ")
if num < 0:
    break  # Sortir del bucle si és negatiu
print("El doble del número és:", num * 2)

#Exemple 2 Programa que demana un número de més de tres xifres. Si s'introdueix un número de menys de tres xifres ho torna a demanar fins que compleixi la condició. Llavors dona la suma de les xifres.
while True:
  num = input("Introdueix un número de més de tres xifres: ")
  if len(num) < 3 or not num.isdigit():
      print("El número no compleix els requisits.")
  else:
      suma = sum(int(digit) for digit in num)
      print("La suma de les xifres és:", suma)
      break

#Exemple 3 Programa que demana paraules i les guarda en una llista fins que introduim ""
    paraula = input("Introdueix una paraula (o deixa-ho en blanc per sortir): ")
    paraules = []

    while paraula != "":
        paraules.append(paraula)
        paraula = input("Introdueix una altra paraula (o deixa-ho en blanc per sortir): ")

    print("Llista de paraules introduïdes:")
    print(paraules)

#Exercici Programa que demana l'any actual. Si l'any introduit no es correcte, ho torna a demanar les vegades que siguin necessàries. Quan diguem el correcte, ens felicita per l'encert.
any_actual = int(input("Introdueix l'any actual: "))

while any_actual != 2023:
    print("Aquest no és l'any actual. Torna a intentar-ho.")
    any_actual = int(input("Introdueix l'any actual: "))

print("Felicidades! Has encertat l'any actual (2023).")
