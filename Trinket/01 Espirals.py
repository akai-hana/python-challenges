import math
import turtle as t
def esborra():
	pregunta=input("Si vols esborrar la pantalla, toca qualsevol lletra : ") 
	t.reset()

#Exercici 1. 
print("EXERCISI 1")
t.speed(5)
voltes=int(input("Introdueix les voltes: "))
longitud=int(input("Introdueix la longitud: "))
for i in range(voltes):
  t.forward(longitud*(i+1))
  t.left(90)
  t.forward(longitud*(i+1))
  t.left(90)
esborra()
print(50*"-")

# Exercici 2.
print("EXERCISI 2")
voltes=int(input("Introdueix les voltes: "))
longitud=int(input("Introdueix la longitud: "))


for i in range(voltes):
    t.circle(longitud*(i),90)  # semicirculo
    t.circle(longitud*(i),90)  # doble de radio que el semicirculo anterior, generando el efecto espiral

esborra()
print(50 * "-")

def esborra():
    pregunta = input("Si vols esborrar la pantalla, toca qualsevol lletra: ")
    t.reset()

# Exercici 3
print("EXERCISI 3")
voltes=int(input("Introdueix el nombre de passos: "))

def generate_fibonacci(n):
    fibonacci_numbers = [1, 1]
    a, b = 1, 1

    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(a)
        a, b = b, a + b  # formula fibonacci

    return fibonacci_numbers

t.right(90) # girarlo para que la espiral sea igual que la foto de classroom



for i in range(3, voltes+3): # empezar 3 paso luego para paridad con foto classroom
    fibonacci_numbers = generate_fibonacci(i)  # transferir funcion a variable
    last_value = fibonacci_numbers[-1] # cojer ultimo valor de array (-1 = ultimo valor)
    # print(last_value) # linea debug para visualizar los valores de fibonacci (son correctos)
    t.circle(last_value*5, 45) # para luego usarlo como radio de circumf.
    t.circle(last_value*5, 45) # (*5 = hacerlo mas grande para paridad con foto classroom)
    
    t.speed(5*last_value) # velocidad dinamica para que no tarde 4 horas en los ultimos pasos

esborra()
print(50 * "-")
t.done()