
import turtle
import  math

t =turtle. Turtle
t. speed (0)
t. colour("red")
turtle. bgcolour ("black")

Def Corazon (n):
  x=16* math. sin(n)**3
  y =13*math. Cos(n)-5*math.cos(
  2*n)-2x math. Cos(3*n)-math. Cos (4*n)
  return x, y
  
  t. penup()
for I in  range (15)
t goto (0,0)
t pendown()
for n in range (0,100,2)
x, y = Corazon (0/10)
t. goto (x*1, y*1)
t. penup ()
t. hind turtle()
turtle. done()