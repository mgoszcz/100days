from turtle import Screen

from day25_csv.us_states_quiz.screen_writer import ScreenWriter
from day25_csv.us_states_quiz.state_container import StateContainer

state_container = StateContainer()
score = 0
MAX = 50
game_in_progress = True

screen = Screen()
screen_writer = ScreenWriter()
screen.setup(725, 491)
screen.bgpic('blank_states_img.gif')

while game_in_progress:
    state = screen.textinput(f'Enter state {score} / {MAX}', 'Enter state')
    if state_container.check_if_state_exists(state):
        score += 1
        screen_writer.write_state_name(state, state_container.get_state_coords(state))
    else:
        game_in_progress = False

screen_writer.game_over(score, MAX)
screen.exitonclick()
