import pandas
from turtle import Turtle, Screen

data = pandas.read_csv('50_states.csv')

screen = Screen()
screen.setup(725, 491)
screen.bgpic('blank_states_img.gif')

state = screen.textinput('Enter state', 'Enter state')

screen.exitonclick()