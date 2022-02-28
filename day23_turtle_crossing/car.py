from random import randint
from turtle import Turtle, colormode

colormode(255)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.shapesize(1, 2)


    def move(self, speed):
        self.backward(1 * speed)

    def bounding_rect(self):
        return (self.xcor() - 20, self.xcor() + 20), (self.ycor() -10, self.ycor() + 10)
