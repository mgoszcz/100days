from threading import Thread
from time import time, sleep
from turtle import Screen, colormode

from day23_turtle_crossing.car import Car
from day23_turtle_crossing.my_turtle import MyTurtle
from day23_turtle_crossing.updater import Updater

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

updater = Updater(screen)

turtle = MyTurtle(screen)

screen.listen()
screen.onkey(key='Up', fun=turtle.move_forward)
screen.onkey(key='Down', fun=turtle.move_backward)

car = Car(screen)
screen.update()
# updater.start()

while car.xcor() < 300:
    car.move_forward()
    # sleep(0.1)



# updater.stop()
# screen.exitonclick()