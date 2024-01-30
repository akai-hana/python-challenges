from yogi import read

print('Este programa calculará la longitud de tu nombre y tu edad')
nombre = input('Por favor, escribe tu nombre: ')  # cojer nombre usuario
longitud_nombre = len(nombre)  # funcion len para longitud del nombre

print('Hola', nombre, 'encantado de saludarte')

if longitud_nombre <= 7:
    print('Tu nombre tiene', longitud_nombre, 'caracteres')
else:
    print('Tienes un nombre largo,', longitud_nombre, 'caracteres')
    
    if ' ' in nombre:  # comprobar si nombre tiene espacio (' ')
        print('Además, tienes un nombre compuesto')
    else:
        print('Además, no se trata de un nombre compuesto') 

# fecha de nacimiento del usuario
fecha_nacimiento = input('Por favor, introduce tu fecha de nacimiento (en formato AAAA-MM-DD): ') # me gusta este formato de fecha porque hay algunos sitios que usan MM-DD-YY, y otros que DD-MM-YY, pero al poner el año primero, no hay confusiones.

# calcular la edad del usuario
from datetime import datetime # libreria para la fecha
fecha_actual = datetime.now()
try:
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    print('Tu edad es:', edad, 'años')
except ValueError:
    print('Formato de fecha incorrecto. Asegúrate de ingresar la fecha en el formato AAAA-MM-DD.')
# las funciones "try" & "except" se usan para tener un fallback en el caso de que el formato de la fecha que inputea el usuario sea invalida, y que en ese caso, informe al usuario del problema.
