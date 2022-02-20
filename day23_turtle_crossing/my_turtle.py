from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self, screen):
        super().__init__()
        self._screen = screen
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move_forward(self):
        self.forward(10)
        self._screen.update()

    def move_backward(self):
        self.backward(10)
        self._screen.update()
