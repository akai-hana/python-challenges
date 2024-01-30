import turtle as t; t.penup()

"\"modo instantáneo\", por si no quieres esperar a que se dibuje"
#t.speed(999)

def dibujo_reloj(): # Dibujo marco reloj
    t.setpos(0, -160); t.pendown(); t.setpos(0, -200) # Poner todo a punto
    
    for i in range(11): # Construcción reloj
        t.circle(200, 30); t.left(90); t.forward(40); t.backward(40); t.right(90);
        """(Si, podría usar un loop de 12 en vez de 11, y eliminar un par de líneas de código,
           pero de esta forma, el reloj se ahorra 4 pasos innecesarios para construirse)"""
    
    t.circle(200, 30); t.penup() # Último paso, por lo del tema de 11

def hora_input(): # Input hora usuario
    print("Introduce la hora del reloj.")
    hora, mins = map(int, input("Formato HH mm (Ej: 12 15, 24 30)\n").split())
    return hora, mins # Devolver hora y mins, para poder reutilizarlos luego al calcular ángulos
    
    """Uso la función .split() para dividir el input en dos partes; la hora y los mins,
       generando una array con ambos elementos, fácilmente reutilizables.
    
       Además, con map(), convierto el input en números enteros, por temas de buen código."""

def calcular_ang_reloj(hora, mins):
    ang_mins = mins * 6 # Ángulo mins, sorprendentemente simple
    
    # Ángulo hora, un poquito mas complicado
    ang_hora = ((hora - 12) * 30) + (ang_mins / 12) if hora >= 12 else (hora * 30) + (ang_mins / 12) # if-else compacto en una sola línea, porque puedo
    
    t.setpos(0, 0); t.left(90)     # Poner el cursor en la posición adecuada
    hora_len = 100; mins_len = 140 # Definir longitud de agujas hora y mins, por comodidad y por buen diseño
    
    return ang_hora, ang_mins, hora_len, mins_len # Devolver cálculo ángulos y longitudes para poder dibujar las agujas

def dibujo_aguja(angulo, longitud): # Estructura-base agujas
    t.right(angulo); t.pendown(); t.forward(longitud) # Dibujar la aguja
    t.penup(); t.backward(longitud); t.left(angulo)   # Restablecer la posición original


def dibujo_aguja_punta(angulo, longitud):
    "Punta hora"
    t.right(angulo); t.forward(longitud); t.right(30); t.pendown() # Ir al final de aguja, offsetear ángulo
    aguja_len = 25                                                 # Definir por comodidad al cambiar tamaño
    
    [t.right(120) or t.forward(aguja_len) for i in range(3)], t.penup() # Dibujar aguja punta (triang. equilátero)
    t.left(30); t.backward(longitud); t.left(angulo)                    # Devolver todo a su posición inicial

"Matias presenta: l’horloge"
dibujo_reloj()                                                                 # Dibujo marco reloj
hora, mins = hora_input()                                                      # Input hora usuario
ang_hora, ang_mins, hora_len, mins_len = calcular_ang_reloj(hora, mins)        # Cálculo de ángulos
dibujo_aguja(ang_hora, hora_len); dibujo_aguja(ang_mins, mins_len)             # Aguja hora/minutos
dibujo_aguja_punta(ang_hora, hora_len); dibujo_aguja_punta(ang_mins, mins_len) # Puntas de las agjs

"THE END"
t.done()