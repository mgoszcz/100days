from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self._score = 0
        self.hideturtle()
        self.penup()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f'Level: {self._score}', align='left')

    @property
    def score(self):
        return self._score

    def add_point(self):
        self._score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center')
