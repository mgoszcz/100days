from turtle import Turtle, Screen, colormode
from random import randint

turtle = Turtle()
colormode(255)
turtle.speed('fastest')

for angle in range(0, 360, 5):
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.setheading(angle)
    turtle.circle(100)


# turtle.circle(100)
# turtle.setheading(5)
# turtle.circle(100)

screen = Screen()
screen.exitonclick()