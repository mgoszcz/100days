from random import randint
from turtle import Turtle, Screen

is_race_on = True
winner = None
colors = ['red', 'green', 'orange', 'yellow', 'blue', 'purple']
screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title='Make your bet', prompt=f'Which turtle will win? {colors}')

turtles = []

for index, color in enumerate(colors):
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=-125 + index*50)
    turtles.append(turtle)

while is_race_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle
            break

if winner.color()[0] == bet:
    print(f'You won! {winner.color()[0]} turtle won')
else:
    print(f'You lose! {winner.color()[0]} turtle won')

screen.exitonclick()
