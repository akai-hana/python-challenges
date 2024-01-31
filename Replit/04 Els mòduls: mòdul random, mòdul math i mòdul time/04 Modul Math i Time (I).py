#Exemple 1. Mòdul math i funció que calcula un logaritme i dona el valor del número pi
import math
print("EXEMPLE 1")
num=float(input("Introdueix un número: "))
num_log2=math.log2(num)
print("El logaritme base 2 de",num,"és",num_log2)
print("El valor de pi és",math.pi)
print(38*"*")
#Exemple 2. Mòdul time. Funció time. Calcularem el temps que tardem en calcular una multiplicació aleatòria
import time
from random import randint
print("EXEMPLE 2")
num1=randint(10,15)
num2=randint(10,15)
resultat=num1*num2
temps1=time.time()
print("temps1=",temps1)
print(num1,"*",num2,"=")
resposta=int(input("resultat?:"))
while resposta != resultat:
  print("resultat incorrecte")
  resposta=int(input("resultat? :"))
temps2=time.time()
print("Has encertat! Has trigat", temps2-temps1, "segons")

#Exemple 3. Mòdul time i random. Funció sleep. Programa que genera 10 números enters aleatoris entre -5 i 10 i espera 2 segons entre cada iteracció

print("EXEMPLE 3")
for i in range (10):
  num=randint(-5,10)
  print(num)
  time.sleep(2)
print(30*"*")

#Exercici 1 Escriu un programa que et demani nom i cognom i que calculi el temps que trigues en escriure aquesta informació

nom = input("Introdueix el teu nom: ")
cognom = input("Introdueix el teu cognom: ")
temps_inici = time.time()

input("Prem Enter quan hagis acabat d'escriure el teu nom i cognom...")
temps_final = time.time()
temps_transcorregut = temps_final - temps_inici

print(f"Has trigat {temps_transcorregut:.2f} segons a escriure el teu nom i cognom.")

#Exercici 2 Programa que demana el radi d'un cercle i informa de la longitud i àrea del cercle. Entre una informació i una altre que passin 2 segons.

radi = float(input("Introdueix el radi del cercle: "))
temps_inici = time.time()

# longitud i area del circulo
longitud = 2 * math.pi * radi
area = math.pi * radi**2

time.sleep(2)
temps_final = time.time()
temps_transcorregut = temps_final - temps_inici

print(f"La longitud del cercle amb radi {radi} és {longitud:.2f}.")
print(f"L'àrea del cercle amb radi {radi} és {area:.2f}.")
print(f"Has trigat {temps_transcorregut:.2f} segons a obtenir aquesta informació.")