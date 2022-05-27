import turtle
import math


for i in range(12):
    t = math.sin(i*30)
    print(i*30, t)


wn = turtle.Screen()
T = turtle.Turtle()
sc = turtle.Screen()
sc.reset()


sc.setworldcoordinates(0, -1.5, 1800, 1.5)



turtle.pencolor("red")
for angle in range(1800):
    y = math.sin(math.radians(angle))
    T.goto(angle, y)







wn.exitonclick()
