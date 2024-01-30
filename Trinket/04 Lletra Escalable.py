import turtle as t

#definició rectangle control
def rectangle_control(x_inicial,y_inicial,escala):
  	t.color("red")
  	t.penup()
  	t.goto(x_inicial,y_inicial)
  	t.pendown()
  	for i in range (2):
    		t.forward(80*escala)
    		t.left(90)
    		t.forward(120*escala)
    		t.left(90)

#introduccio coordenades i escala
x_ini=int(input("introdueix la x inicial: " ))
y_ini=int(input("introdueix la y inicial: " ))
escala=float(input("introdueix l'escala: "))

# Lletra o
"""
def lletra_o(x_inicial,y_inicial,escala):
    t.penup()
    t.color("white")
    t.goto(x_inicial,y_inicial)
    t.left(90)
    t.forward(40*escala)
    t.pendown()
    for i in range (2):
        t.forward(40*escala)
        t.circle(-40*escala,180)     
    t.penup()
    #tornem turtle a laposició inicial
    t.goto(x_inicial,y_inicial)
    t.setheading(0)
  """
# Lletra S
#t.speed() # debug
def lletra_s(x_inicial,y_inicial,escala):
    t.penup(); t.color("black"); t.goto(x_inicial,y_inicial); # pasos iniciales
    t.left(90); t.forward(40*escala); t.right(180);           # poner la S en posición
    
    
    t.circle(40*escala,20); t.pendown(); t.circle(40*escala,140) 
    
    t.circle(20*escala,75)
    t.circle(55*escala,35); t.circle(-55*escala,30)
    t.circle(-20*escala,75)
    
    t.circle(-40*escala,140); t.forward(2.5)
    t.left(65); 
    
"lletra_o(x_ini,y_ini,escala)"
lletra_s(x_ini,y_ini,escala)
rectangle_control(x_ini,y_ini,escala)