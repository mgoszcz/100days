from turtle import Turtle, Screen, colormode

from random import choice, randint

turtle = Turtle()
colormode(255)
turtle.speed('fastest')
turtle.hideturtle()
screen = Screen()
screen.setup(600, 600)
screen.setworldcoordinates(0, 0, 600, 600)

for y in range(50, 550):
    for x in range(50, 550):
        turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.penup()
        turtle.setposition(x, y)
        turtle.pendown()
        turtle.dot(2)

turtle.getscreen().getcanvas().postscript(file='save.eps')

screen.exitonclick()
