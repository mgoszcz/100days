from time import sleep
from turtle import Screen

from day23_turtle_crossing.car_container import CarContainer
from day23_turtle_crossing.my_turtle import MyTurtle
from day23_turtle_crossing.scoreboard import ScoreBoard
from day23_turtle_crossing.statics import CARS_COUNT_BASE

game_over = False
level_finished = False
level_pause = True

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

difficulty_selected = screen.numinput('Difficulty level', 'Select difficulty level (1 - easy, 2 - medium, 3 - hard): ',
                                      minval=1, maxval=3)

turtle = MyTurtle()
screen.listen()
screen.onkey(key='Up', fun=turtle.move_forward)
screen.onkey(key='Down', fun=turtle.move_backward)

# car = Car()
car_container = CarContainer(CARS_COUNT_BASE * difficulty_selected)
scoreboard = ScoreBoard()
screen.update()

while not game_over:
    scoreboard.add_point()
    screen.update()
    sleep(1)
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
