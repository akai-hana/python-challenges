""" Antes que nada, mis disculpas Ilde, porque
    este código te va a dar ganas de llorar.
    
    Otra cosa también que te quería decir,
    que porque este Python/turtle es una versión
    antigua, no puedo hacer lo de que las
    circumferencias toquen todas las paredes.
    He hecho que toquen la de la izq. y abajo. """

from turtle import *; import math; penup()
speed(-1) # debug speed-up

"Variables"
f, r, g, b, n, a = [0] * 6 # inicialización previa de variables por temas de seguridad y estándares de programación

# User output
f = input("Introduce el color del fondo:\n(Ej: Beige)\n").lower()
r = int(input("Introduce R (rgb): "))
g = int(input("Introduce G (rgb): "))
b = int(input("Introduce B (rgb): "))
n = int(input("Introduce la cantidad de circulos: "))
a = int(input("Introduce el diametro de circumf.: "))


# debug (Exemple d’entrada 1)
f = "Beige"
r = 0
g = 0
b = 60
n = 4
a = 70


"""
# debug (Exemple d’entrada 2)
f = "Cyan"
r = 80
g = 20
b = 40
n = 3
a = 100
"""

a = a/4
a_static = 0 # inicializar a_static
a_static = a # crear clon de 'a' estático

"Funciones"
 
""" Ilde, sé que odias lo de "main", pero
    es nomenclatura estándar para definir
    la función principal en muchos langs,
    por lo que será lo que se llame aquí. """ 

def main(f, r, g, b, n, a):
    "Introducción"
    goto(-200, -200); left(90)
    dummy = 1 # inicializando el environment
    
    circle(a*dummy*0.05, -180); right(180) # ecualizar la posición de la primera circumf. respecto al eje X
    nose = 0.4 # esto no se porque pero si lo pones a 0.4 funciona bien
    
    "Diámetro y espaciado de circumferencias"
    for i in range(n):
        a = a_static; lon = dummy*a; # igualar a con a_static (el valor de a inicial) y definir longitud por comodidad
        dummy += 1 # aumentar dummy por cada iteración del loop
        
        "Color de las circumferencias"
        fillcolor((r*dummy, g*dummy, b*dummy)) # Setear colores RGB y multiplicarlos por dummy 
        
        circle(-lon+dummy*0.5, 180); circle(-lon*nose, -180); right(90); pendown() # espaciado de circumferencias
        begin_fill(); circle(lon,360); end_fill() # dibujar circulo con colores RGB
        left(90); penup() # poner el cursor como estaba antes
        
        nose = nose/2 # no se como ni porque, pero esto hace que funcione, y eso es todo lo que importa

"Color de fondo"
Screen().bgcolor(f) # dale color a la vida

main(f, r, g, b, n, a)