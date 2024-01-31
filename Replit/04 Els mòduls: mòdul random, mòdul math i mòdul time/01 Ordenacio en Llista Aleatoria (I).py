import random

# Exemple 1: Generar una llista de 10 nombres naturals aleatoris entre 1 i 100
example1 = [random.randint(1, 100) for _ in range(10)]

# Exemple 2: Extreure l'element més petit de la llista i imprimir-ho per pantalla
min_element = min(example1)
print(f"Element més petit: {min_element}")

# Exemple 3: Crear una segona llista on eliminarem aquest element més petit
example3 = example1.copy()  # Copiem la primera llista per a la segona llista
example3.remove(min_element)  # Eliminem l'element més petit de la segona llista

# Exercici 1: Crear una llista de 20 nombres aleatoris entre 1 i 200
exercise1 = [random.randint(1, 200) for _ in range(20)]

# Exercici 2: Extreure l'element més gran de la llista i imprimir-ho per pantalla.
max_element = max(exercise1)
print(f"Element més gran: {max_element}")

# Exercici 3: Eliminar l'element més gran de la llista
exercise1.remove(max_element)