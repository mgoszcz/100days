from turtle import Turtle
from typing import List

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments: List[Turtle] = []
        self._initialize()
        self._heading = 0
        self.head = self.segments[0]

    def _initialize(self):
        for i in range(3):
            self._add_segment((0 - i * MOVE_DISTANCE, 0))

    def _add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        snake_length = len(self.segments)
        for i in range(snake_length - 1, 0, -1):
            segment = self.segments[i]
            segment.goto(self.segments[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def _set_heading(self, heading: int):
        if heading < 180:
            old_heading_check = heading + 180
        else:
            old_heading_check = heading - 180
        if self.head.heading() != old_heading_check:
            self.head.setheading(heading)

    def up(self):
        self._set_heading(90)

    def left(self):
        self._set_heading(180)

    def down(self):
        self._set_heading(270)

    def right(self):
        self._set_heading(0)

    def grow(self):
        self._add_segment(self.segments[-1].position())
