import time # para poder usar la funcion time.sleep
import random

numero_secreto = random.randint(0, 100)

print("Hola!")
time.sleep(3)

# inicio del juego
intentos = 0
while intentos < 7:
    try:
        respuesta = int(input("Digues un número del 0 al 100: "))

        if respuesta < numero_secreto:
            print("La teva resposta és més petita que el número secret.")
        elif respuesta > numero_secreto:
            print("La teva resposta és més gran que el número secret.")
        else:
            print("Has guanyat! El número secret era", numero_secreto)
            break  # termina el juego si la respuesta es correcta

        intentos += 1

    # si el usuario no inputea un numero valido,
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")

# si se pierden todas las vidas,
if intentos == 7:
    print("Has superat el límit d'intents. El número secret era", numero_secreto)
