from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move_forward(self):
        if self.ycor() < 280:
            self.forward(10)

    def move_backward(self):
        if self.ycor() > -280:
            self.backward(10)

    def check_if_finished(self):
        if self.ycor() == 280:
            return True
        else:
            return False

    def bounding_rect(self):
        return (self.xcor() - 10, self.xcor() + 10), (self.ycor() - 10, self.ycor() + 10)