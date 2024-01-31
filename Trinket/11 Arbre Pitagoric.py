from turtle import *; import math
penup(); speed(-1)
goto(-50,-190); pendown()

num=math.sqrt(2)/2

def quadrat(n,lon):
  if n >= 1:
    color(lon,lon,0)
    begin_fill()
    for i in range (4):
      forward(lon)
      left(90)
    end_fill()
    
  if n >= 2:
    left(90)
    forward(lon)
    
    # Part 1
    right(45)
    quadrat(n-1, lon*num)
    
    # Part 2
    forward(lon*num); right(90)
    quadrat(n-1, lon*num)
    right(90); forward(lon*num); left(45)
    forward(lon); left(90)
    
quadrat(6, 100)