from turtle import Turtle, Screen, colormode
from random import randint

turtle = Turtle()
colormode(255)

for edges in range(3, 11):
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    # turtle.color((255, 255, 255))
    angle = 360/edges
    for _ in range(edges):
        turtle.forward(100)
        turtle.right(angle)


screen = Screen()
screen.exitonclick()
