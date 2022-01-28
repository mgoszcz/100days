"""
W - forward
S - backwards
A - conuter-clockwise
D - clockwise
c - clear drawing
"""
from time import sleep
from turtle import Turtle, Screen

W_PRESSED = False
S_PRESSED = False
A_PRESSED = False
D_PRESSED = False

turtle = Turtle()
screen = Screen()

def keep_moving_forward():
    global W_PRESSED
    W_PRESSED = True
    while W_PRESSED:
        turtle.forward(10)
        sleep(0.1)

def stop_moving_forward():
    global W_PRESSED
    W_PRESSED = False

def keep_moving_backward():
    global S_PRESSED
    S_PRESSED = True
    while S_PRESSED:
        turtle.backward(10)
        sleep(0.1)

def stop_moving_backward():
    global S_PRESSED
    S_PRESSED = False

def keep_rotating_clock():
    global D_PRESSED
    D_PRESSED = True
    while D_PRESSED:
        turtle.right(5)
        sleep(0.1)

def stop_rotating_clock():
    global D_PRESSED
    D_PRESSED = False

def keep_rotating_counter_clock():
    global A_PRESSED
    A_PRESSED = True
    while A_PRESSED:
        turtle.left(5)
        sleep(0.1)

def stop_rotating_counter_clock():
    global A_PRESSED
    A_PRESSED = False

def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)

def rotate_clockwise():
    turtle.right(5)

def rotate_counter_clockwise():
    turtle.left(5)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
# screen.onkey(key='w', fun=move_forward)
screen.onkeypress(key='w', fun=keep_moving_forward)
screen.onkeyrelease(key='w', fun=stop_moving_forward)
screen.onkeypress(key='s', fun=keep_moving_backward)
screen.onkeyrelease(key='s', fun=stop_moving_backward)
screen.onkeypress(key='a', fun=keep_rotating_counter_clock)
screen.onkeyrelease(key='a', fun=stop_rotating_counter_clock)
screen.onkeypress(key='d', fun=keep_rotating_clock)
screen.onkeyrelease(key='d', fun=stop_rotating_clock)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='a', fun=rotate_counter_clockwise)
# screen.onkey(key='d', fun=rotate_clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
