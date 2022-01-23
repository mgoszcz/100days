"""
Paint a painting of 10x10 rows of spots
dot radius 20, space between dots 50
"""
from turtle import Turtle, Screen, colormode

from random import choice

import colorgram

turtle = Turtle()
colormode(255)
turtle.speed('fastest')
turtle.hideturtle()
screen = Screen()
screen.setup(600, 600)
screen.setworldcoordinates(0, 0, 550, 550)

colors = colorgram.extract('image.jpg', 30)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

for y in range(1, 11):
    for x in range(1, 11):
        turtle.color(choice(color_list))
        turtle.penup()
        turtle.setposition(x * 50, y * 50)
        turtle.pendown()
        turtle.dot(20)


screen.exitonclick()
