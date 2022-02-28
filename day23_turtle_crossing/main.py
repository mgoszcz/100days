from threading import Thread
from time import time, sleep
from turtle import Screen, colormode

from day23_turtle_crossing.car import Car
from day23_turtle_crossing.car_container import CarContainer
from day23_turtle_crossing.my_turtle import MyTurtle
from day23_turtle_crossing.scoreboard import ScoreBoard

game_over = False
level_finished = False
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

turtle = MyTurtle()
screen.listen()
screen.onkey(key='Up', fun=turtle.move_forward)
screen.onkey(key='Down', fun=turtle.move_backward)

# car = Car()
car_container = CarContainer(5)
scoreboard = ScoreBoard()
screen.update()

while not game_over:
    scoreboard.add_point()
    while not level_finished:
        level_finished = turtle.check_if_finished()
        game_over = car_container.detect_collision(turtle.bounding_rect())
        if game_over:
            level_finished = True
        car_container.cars_update()
        screen.update()
        sleep(0.1)

    turtle.goto(0, -280)
    level_finished = False
    car_container.increase_speed()


scoreboard.game_over()

screen.exitonclick()