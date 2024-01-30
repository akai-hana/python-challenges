from turtle import *

# Lista de colores disponibles
COLORES = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'yellow', 'cyan']

# Formas geométricas #

"Cuadrado"
def dibujar_cuadrado(costado, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(costado)
        left(90)
    end_fill()

"Circulo"
def dibujar_circulo(radio, color):
    fillcolor(color)
    begin_fill()
    circle(radio)
    end_fill()

"Rectángulo"
def dibujar_rectangulo(costado1, costado2, color):
    fillcolor(color)
    begin_fill()
    for i in range(2):
        forward(costado1)
        left(90)
        forward(costado2)
        left(90)
    end_fill()

# Otras funciones #

"Hacer el programa a prueba de balas"
def obtener_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Introduce un número válido.")

"Obtener color"
def obtener_color():
    while True:
        color = input("Selecciona el color de la forma\n(red, blue, green, orange, purple, pink, brown, yellow, cyan): ").lower()
        if color in COLORES:
            return color
        else:
            print("Color no válido. Introduce un color de la lista.")

"Borrar última forma"
def esborra():
    clear()

def main():
    while True:
        print("Selecciona una opción:")
        print("1. Cuadrado")
        print("2. Circulo")
        print("3. Rectángulo")

        opcion = obtener_numero("Selecciona la forma.\n1: Cuadrado\n2: Circulo\n3: Rectangulo\n- ")
        color = obtener_color()

        if opcion == 1:
            costado = obtener_numero("Introduce la longitud de los costados del cuadrado: ")
            esborra()
            dibujar_cuadrado(costado, color)

        elif opcion == 2:
            radio = obtener_numero("Introduce el radio del circulo: ")
            esborra()
            dibujar_circulo(radio, color)

        elif opcion == 3:
            costado1 = obtener_numero("Introduce la longitud del primer costado (x): ")
            costado2 = obtener_numero("Introduce la longitud del segundo costado (y): ")
            esborra()
            dibujar_rectangulo(costado1, costado2, color)

        else:
            print("Opción no válida. Por favor, introduce un número válido.")

        continuar = input("¿Quieres dibujar otra figura? (S/N): ")
        if continuar.lower() != 's':
            esborra()
            break
    done()

main()

""" T H E  E N D """
