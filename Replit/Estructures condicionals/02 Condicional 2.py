print("Programa per comprovar si un número natural és divisible per 2, 3, 5, 7 i 11")

num = input("Introdueix un número enter: ")
num1 = int(num)

if num1 % 2 == 0:
    print("El número", num1, "SI és divisible per 2. Quocient:", num1 // 2)
else:
    print("El número", num1, "NO és divisible per 2")

if num1 % 3 == 0:
    print("El número", num1, "SI és divisible per 3. Quocient:", num1 // 3)
else:
    print("El número", num1, "NO és divisible per 3")

if num1 % 5 == 0:
    print("El número", num1, "SI és divisible per 5. Quocient:", num1 // 5)
else:
    print("El número", num1, "NO és divisible per 5")

if num1 % 7 == 0:
    print("El número", num1, "SI és divisible per 7. Quocient:", num1 // 7)
else:
    print("El número", num1, "NO és divisible per 7")

if num1 % 11 == 0:
    print("El número", num1, "SI és divisible per 11. Quocient:", num1 // 11)
else:
    print("El número", num1, "NO és divisible per 11")
