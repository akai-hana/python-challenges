    """
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
"Exercici 1 "

import turtle as t
space=50*"*"

print("")
print(space)
print("Exercici 1 \n")

def esborra():
	pregunta = input("Si vols esborrar la pantalla, escriu 1: ")
	if pregunta == "1":
		t.clearscreen()
    
for i in range(4):
  t.forward(100)
  t.left(90)
  
esborra()

print(space)
print("Exercisi 2 \n")

t.pen(pencolor = "red", pensize = 5)
amplada = int(input("Introdueix l'amplada: "))
altura = int(input("Introdueix l'alçada: "))

for i in range(2):
  t.forward(amplada)
  t.left(90)
  t.forward(altura)
  t.left(90)

print("")
esborra()

print("")
print(space)