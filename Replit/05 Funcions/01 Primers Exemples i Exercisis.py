# Exemple 1: Funció salutació
print("EXERCISI 1")
nom = input("Quin es el teu nom?\n")

def salutacio(nom):
  return(f"Hola, {nom}!")
print(salutacio(nom))

# Exemple 2: Funció mitjana
print("EXERCISI 2")

num1 = input("Introdueix el primer nombre: ")
num2 = input("Introdueix el segon nombre: ")

def mitjana(num1, num2):
  return (int(num1) + int(num2)) / 2
print(mitjana(num1, num2))

#Exercici 1. Crea una funció que tingui com argument 2 números enters i retorni el més gran. Nom max2(num_1,num_2)
print("EXERCISI 3")
def max2(num_1, num_2):
    return max(num_1, num_2)

num1 = input("Introdueix el primer nombre: ")
num2 = input("Introdueix el segon nombre: ")

resultat = max2(num1, num2)
print(f"El número més gran entre {num1} i {num2} és: {resultat}")

#Exercici 2. Crea una funció que tingui com argument 4 números enters i retorni el més gran. Nom max4(num_1,num_2,num_3,num_4) Nota: Utilitza la funció del exercici1 dintre de la nova funció
print("EXERCISI 4")
nom = input("Quin es el teu nom?\n")

def salutacio(nom):
  return(f"Hola, {nom}!")
print(salutacio(nom))

def max4(num_1, num_2, num_3, num_4):
    max_12 = max2(num_1, num_2)
    max_34 = max2(num_3, num_4)
    resultat_final = max2(max_12, max_34)
    return resultat_final

num1 = input("Introdueix el primer nombre: ")
num2 = input("Introdueix el segon nombre: ")
num3 = input("Introdueix el tercer nombre: ")
num4 = input("Introdueix el quart nombre: ")

resultat = max4(num1, num2, num3, num4)
print(f"El número més gran entre {num1}, {num2}, {num3} i {num4} és: {resultat}")