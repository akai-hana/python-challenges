from turtle import *; penup()
"esta forma de importar me permite saltarme el \'t.\'"

def grid():
    # n = 0.0; m = 0.0 # declarar doubles 'n' y 'm'
    n, m = map(int, input().split()) # asignar output a doubles
    "No añado instrucciones para ser fiel al programa modelo del Classroom"
    return n, m # devolver valores

n, m = grid() # pasar valores a main
o = n/m # crear coordenada o; 'n' adaptada segun 'm'
"mantengo la n original con el fin de usarla como contador dentro de la cuadricula"

"""
# fragmento de código antiguo,
# cuya utilidad era la de amplificar
# el tamaño impreso de la cuadrícula.

amp = 1
m = m*amp; o = n*m # Amplificar variables por 20
"""

def draw_n1(n, m, o):
    goto(-150, 150)
    
    for i in range(n): # contador n
        pendown(); forward(o) # dibujar m distancia
        penup(); backward(o)  # volver a pos. original
        
        right(90); pendown()
        forward(m)           # moverse 'n' segun 'm' (o)
        penup(); left(90)
    
    pendown(); forward(o); penup()

def draw_n2(n, m, o):
    goto(-150, 150); right(90) # preparaciones
    
    for i in range(n): # contador n
        pendown(); forward(o) # dibujar longitud m
        penup(); backward(o)  # volver a pos. original
        
        left(90); pendown()
        forward(m)          # moverse 'n' segun 'm' (o)
        penup(); right(90)
      
    pendown(); forward(o); penup()

def draw_n():
  draw_n1(n, m, o); draw_n2(n, m, o)

# debug
#print(n, m, o) # debug
#speed(-1)

draw_n()

done()