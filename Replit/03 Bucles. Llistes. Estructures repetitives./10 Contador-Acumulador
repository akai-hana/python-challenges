print('Programa que pedirá números hasta dejar una entrada vacía')
print('El programa cuenta cuántos números se han introducido')
print('y la suma de todos esos números introducidos')
print('(Entrada vacía = Terminar)')
n = 0
suma = 0
seguir = True

while seguir:
  numero = input('Escribe un número: ')
  if numero == '':
    seguir = False
  else:
    numero = eval(numero)
    n = n + 1
    suma = suma + numero

if n > 0:
  media = suma / n
  print('Se han introducido', n, 'números')
  print('Los números suman', suma)
  print('La media de los números introducidos es', media)
else:
  print('No se han introducido números.')
