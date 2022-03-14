from time import sleep
from turtle import Screen

from day20_21_snake.food import Food
from day20_21_snake.scoreboard import ScoreBoard
from snake import Snake


def detect_wall_collision(snake_object: Snake) -> bool:
    if abs(snake_object.head.xcor()) > 280 or abs(snake_object.head.ycor()) > 280:
        return True
    return False


def detect_tail_collision(snake_object: Snake) -> bool:
    for segment in snake_object.segments[1:]:
        if snake_object.head.distance(segment.position()[0], segment.position()[1]) < 5:
            return True
    return False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

continue_game = True

while continue_game:
    sleep(0.2)
    screen.update()
    snake.move()
    if snake.head.distance(food.position()[0], food.position()[1]) < 20:
        food.move()
        snake.grow()
        scoreboard.add_point()

    if detect_wall_collision(snake):
        continue_game = False

    if detect_tail_collision(snake):
        continue_game = False

scoreboard.game_over()
scoreboard.update_high_score_if_needed()

screen.exitonclick()
