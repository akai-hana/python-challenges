print("Programa que informa sobre la divisibilitat entre 3")
num = int(input("Introdueix un número: "))
if num % 3 == 0:
    print("El número", num, "és múltiple de 3")
    print(num, "/3 =", num / 3)
else:
    print("El número", num, "no és múltiple de 3")
    print(num, "/3 =", num / 3)
    print("La divisió no és exacta")
