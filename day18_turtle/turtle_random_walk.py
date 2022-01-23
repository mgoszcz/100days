from turtle import Turtle, Screen, colormode
from random import randint

turtle = Turtle()
colormode(255)

turtle.width(10)
turtle.speed('fastest')

while True:
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    angle = randint(0, 3) * 90
    turtle.right(angle)
    turtle.forward(30)

screen = Screen()
screen.exitonclick()