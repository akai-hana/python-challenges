import turtle as t

"Deficiniones"
# paleta de colores
background = "#9EC388"
borde = "#ECA84F"
pomodoro = "#AD0509"
mozzarella = "#FBC70F"

pepperoni = [ # que sepas que adivinar las coordenadas del pepperoni uno a uno ha sido miserable 
  [-70, -20], [-85, 50], [-25, -75], [-15, -25], [-25, 25], [-30, 80],
  [15, -75], [20, -5], [20, 75], [60, 31], [71, 90], [80, -35]
]

"Preparativos"
t.pensize(5); t.shape("circle")                 # grosor y forma del cursor
screen = t.Screen(); screen.bgcolor(background) # definir y pintar el background

"Funciones"
circulo = lambda radio, color_linea, color_relleno: (t.color(color_linea), t.fillcolor(color_relleno), t.begin_fill(), t.circle(radio), t.end_fill())
muevetee_tortugaa = lambda x, y: (t.penup(), t.goto(x, y), t.pendown()) # comodidad
# lambda porque me gusta

muevetee_tortugaa(0, -125); circulo(150, borde, borde)         # borde
muevetee_tortugaa(0, -100); circulo(125, pomodoro, mozzarella) # salsa
list(map(lambda position: (muevetee_tortugaa(position[0], position[1]), circulo(10, pomodoro, pomodoro)), pepperoni)) # pepperoni

"""utilizo map para iterar función lambda en cada posición pepperoni.
   luego lambda ejecuta muevetee_tortugaa y circulo para cada posición.
   envolver resultado en list() por motivos de buen diseño de código.
   
   Podría usar un for loop y ya pero eso quedaria demasiado aburrido."""

t.color(background); muevetee_tortugaa(0, 25) # reset posicion
[t.pendown() or t.left(45) or t.forward(150) or t.penup() or t.backward(150) for x in range(8)]  # cortapizzas 3.000

t.done # il finale      