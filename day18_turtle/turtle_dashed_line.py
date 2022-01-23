from turtle import Turtle, Screen

turtle = Turtle()

for _ in range(20):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

screen = Screen()
screen.exitonclick()
