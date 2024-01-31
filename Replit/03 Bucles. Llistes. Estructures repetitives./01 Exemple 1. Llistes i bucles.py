#primer exemple. 
lista1=[1,2,3,"quatre","cinc",5>3]
for i in lista1:
	print (i)
#segon exemple. Els strings també son indexables
paraula=input("Escriu una paraula : ")
for lletra in paraula:
	print(lletra)
print(llista1[2])
#tercer exemple. Comptadors. Comptar lletres
num_a=0
for x in paraula:
  if x =="a":
    num_a=num_a+1
print("la paraula", paraula, "te",num_a ,"lletres a")
#quart exemple. Llista de listes
llista2=[5,6,lista1]
for y in lista2:
  print(y)
#cinquè exemple. El programa dels divisors amb llistes
num_prim=[2,3,5,7,11]
num_problema=int(input("Introdueix un numero"))
for i in num_prim:
  if num_problema % i == 0:
    print(num_problema, "es divisible per",i)
    print(num_problema,"/",i,"=",num_problema/i)
    else:
      print(num_problema, " NO es divisible per",i)
    