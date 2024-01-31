#Exemple 1
for i in range (10):
	print (i)
#Exemple 2
for i in range (2,10):
  print (i)
#Exemple 3
for i in range (1,20,3):
	print (i)
#Exemple 4
for i in range (10,1,-1):
	print (i)
# Exemple 5: Escriu una llista amb els nombres parells fins 100
nombres_parells = []
for i in range(2, 101, 2):
    nombres_parells.append(i)
print(nombres_parells)
# Exemple 6: Programa que mostra tots els divisors d'un número natural i els guarda en una llista
def troba_divisors(numero):
    divisors = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisors.append(i)
    return divisors

numero_a_comprovar = int(input("Introdueix un número natural: "))
divisors = troba_divisors(numero_a_comprovar)
print(f"Els divisors de {numero_a_comprovar} són: {divisors}")