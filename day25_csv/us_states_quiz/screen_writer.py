from turtle import Turtle


class ScreenWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state_name(self, state_name, coords):
        self.goto(coords[0], coords[1])
        self.write(state_name)

    def game_over(self, score, max):
        self.goto(0, 0)
        self.write(f'GAME OVER! You have scored {score} / {max}', align='center', font=('Arial', 20, 'normal'))
