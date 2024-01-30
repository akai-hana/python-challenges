from turtle import *
reset()
speed(-1)
penup()
goto(-150,0)
pendown()
def koch(n,longitud):
    if n == 1:
      forward(longitud)
    else:
      longitud=longitud/3
      
      koch(n-1, longitud)             # Part 1
      left(60);   koch(n-1, longitud) # Part 2
      right(120); koch(n-1, longitud) # Part 3
      left(60);   koch(n-1, longitud) # Part 4

num=int(input("Introdueix el nombre d'iteracions: "))
lon=int(input("Introdueix la longitud inicial: "))

koch(num,lon)