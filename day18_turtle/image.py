from random import randint
from turtle import Turtle, colormode

turtle = Turtle()
turtle.hideturtle()
turtle.speed('fastest')
colormode(255)
turtle.width(10)

while True:
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.setheading(randint(0,361))
    turtle.forward(randint(10,100))
