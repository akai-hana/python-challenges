print("Programa que calcula")
a = input("Escribe un número: ")
num1 = float(a)

b = input("Escribe un segundo número: ")
num2 = float(b)

print("Operaciones con " + a + " y " + b + "\n")
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2
divi_entera = num1 // num2
residuo = num1 % num2

# un monton de print-efes
print(f"{a}+{b}=", suma)
print(f"{a}-{b}=", resta)
print(f"{a}*{b}=", multi)
print(f"{a}/{b}=", divi)
print(f"{a}//{b}=", divi_entera, "(División entera)")
print(f"{a}%{b}=", residuo, "(Residuo de la división)")