import os
from turtle import Turtle

HIGH_SCORE = 'high_score.txt'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self._score = 0
        self._high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('white')

        self._get_high_score()
        self.write_score()

    def _get_high_score(self):
        if os.path.exists(HIGH_SCORE):
            with open(HIGH_SCORE, 'r') as file_handle:
                self._high_score = int(file_handle.read())
        else:
            self._high_score = 0

    def _save_high_score(self):
        with open(HIGH_SCORE, 'w') as file_handle:
            file_handle.write(str(self._score))

    def update_high_score_if_needed(self):
        if self._score > self._high_score:
            self.goto(0, -40)
            self.write('NEW HIGH SCORE!', align='center')
            self._save_high_score()

    def write_score(self):
        self.write(f'Score: {self._score} High Score: {self._high_score}', align='center')

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
