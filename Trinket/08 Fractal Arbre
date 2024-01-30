from turtle import *; penup()

goto(0,-195)
pendown()
left(90)
speed(-1)

def arbre(n,lon,angle):
    if n>=1:
        forward(lon)
    if n>=2:
      lon=3/4*lon
      
      # Part 1
      left(angle)
      arbre(n-1, lon, angle)
      back(lon)
      
      # Part 2
      right(2*angle)
      arbre(n-1,lon,angle)
      back(lon)
      left(angle)
      
arbre(8,100,30)