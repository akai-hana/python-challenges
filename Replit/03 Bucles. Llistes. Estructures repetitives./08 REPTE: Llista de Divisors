def descomposicio_factors_primers(num):
  factors = []
  divisor = 2

  while divisor <= num:
    if num % divisor == 0:
      factors.append(divisor)
      num = num // divisor  # Utilitzem l'operador // per a la divisió entera
    else:
      divisor += 1

  return factors


try:
  num1 = int(
    input("Introdueix un número i el descompondré en factors primers: "))
  if num1 <= 0:
    print("Si us plau, introdueix un nombre natural vàlid (major que 0).")
  else:
    factors_primers = descomposicio_factors_primers(num1)
    print("Llista dels factors primers de", num1, ":")
    print(factors_primers)
except ValueError:
  print("Si us plau, introdueix un número vàlid.")
