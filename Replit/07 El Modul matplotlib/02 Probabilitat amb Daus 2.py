import random as r
print("Exercisi 4")
contador=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(36000):
  dau1 = r.randint(1,6)
  dau2 = r.randint(1,6)
  suma = dau1 + dau2
  contador[suma-2] = contador[suma-2]+1
print("Els resultats són", contador)
  
import matplotlib.pyplot as plt
index    = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
contador = [0, 0, 5, 6, 7, 4, 3, 6, 7, 8, 9, 3, 2]
# Per dibuixar tenim una llista amb les ordenades i una altra amb valors
plt.grid (True)
plt.plot (index, contador, '--bo')
plt.show()
# Generem el gràfic amb matplotlib
"""EXERCISI FINAL: dibuixar amb matplotlib la funcio x 2 -5x+4 en el domini -10123456"""