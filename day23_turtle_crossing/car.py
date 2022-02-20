from time import sleep
from turtle import Turtle


class Car(Turtle):
    def __init__(self, screen):
        super().__init__()
        self._screen = screen
        self.penup()
        self.goto(-300, 0)

    def move_forward(self):
        self.forward(10)
        sleep(1)
        self._screen.update()