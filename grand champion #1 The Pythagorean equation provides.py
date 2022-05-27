import random
import turtle
import math

a = 100
a = int(a)
b = 100
b = int(b)
c = math.sqrt((a**2)+(b**2))
t = turtle.Turtle()


t.forward(a)

t.left(90)

t.forward(b)

t.left(135)
t.forward(c)

for i in range(3):
    i += 1
    t.right(90)
    t.forward(c)


t.setheading(90)

for i in range(3):
    i += 1
    t.right(90)
    t.forward(b)

t.setheading(0)
for i in range(3):
    i += 1
    t.right(90)
    t.forward(a)

print("a =",a)
print("b =",b)

print("c^2=a^2+b^2")
print("c^2 =",a,"**2,+",b,"**2")
print("c^2 =", a**2,"+", b**2)
print("c^2 =", (a**2)+ (b**2))

print("sqrt of c^2=","sqrt of",((a**2)+(b**2)))
print("c =", math.sqrt((a**2)+(b**2)))


