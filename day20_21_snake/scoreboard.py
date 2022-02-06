from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self._score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('white')
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self._score}', align='center')

    @property
    def score(self):
        return self._score

    def add_point(self):
        self._score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center')
