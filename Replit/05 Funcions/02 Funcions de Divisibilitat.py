import time
#Exemple 1 Funció que dona els divisors d'un nombre natural en forma de llista
print("EXEMPLE 1")
def divisors(num):
  list_div=[1]
  for i in range(2,num+1):
    if num % i == 0:
      list_div.append(i)
  return list_div
num1=int(input("Introdueix un nombre natural: "))
print(f"Els divisors de {num1} son {divisors(num1)}.")
print(40*"-")
#Exemple 2. Funció que donat un número indica si es primer (True) o no (False)
print("EXEMPLE 2")
def es_primer(num):
  num_divisors=len(divisors(num))
  if num_divisors==2:
    return True
  else:
    return False
num2=int(input("Introdueix un nombre natural: "))
if es_primer(num2) == True:
  print("El numero",num2,"es primer")
else:
  print("El numero",num2,"NO es primer")
  
print(40*"-")
#Exemple 3. Escriu un programa que donat un número indica si es primer o no i el temps que es triga en resoldre el dubte.
print("EXEMPLE 3")

def es_primer(num):
    if num < 2:
      return False
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        return False
      return True

while True:
  num = int(input("Introdueix un nombre natural (o un número negatiu per sortir): "))

if num < 0:
  print("Programa finalitzat.")
  #break

temps1 = time.time()

if es_primer(num):
  print("El numero", num, "és primer")
else:
  print("El numero", num, "NO és primer")

temps2 = time.time()
print(f"El temps per fer l'operació ha estat {temps2 - temps1} segons")

#Exercici 1. Crea un programa que demani un nombre enter. Si es primer, diu que ho és. Si es compost, dona per pantalla els seus divisors. El programa es repeteix fins introduir un número negatiu.
def es_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def troba_divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

while True:
    try:
        num = int(input("Introduce un número entero (negativo para salir): "))
        if num < 0:
            break

        if es_primer(num):
            print(f"{num} és un número primer.")
        else:
            print(f"{num} és un número compost. Divisors: {troba_divisors(num)}")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

#Exercici 2. Crea un programa que demani un número enter i indiqui si es o no primer i el temps que triga el procés. El programa es repeteix fins introduir un número negatiu. Utilitza el programa per fer investigacions
def es_primer(num):
  if num < 2:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True

while True:
  try:
      num = int(input("Introdueix un número enter (negatiu per sortir): "))

      if num < 0:
          print("Programa finalitzat.")
          break

      temps_inicial = time.time()
      resultat = es_primer(num)
      temps_final = time.time() - temps_inicial

      if resultat:
          print(f"{num} és un número primer.")
      else:
          print(f"{num} no és un número primer.")

      print(f"El procés ha trigat {temps_final:.6f} segons.\n")

  except ValueError: # aqui hago el programa a prueba de balas
      print("Si us plau, introdueix un número enter vàlid.")