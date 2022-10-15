import turtle
from turtle import Turtle, Screen
import pandas as pd

SCORE = 0

screen = turtle.Screen()
screen.setup(725, 491)
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
states = pd.read_csv('50_states.csv')
all_states = [state for state in states['state'].to_list()]
turtle.shape(image)
correct_answer = []

while len(correct_answer) < 50:
    guess = screen.textinput(title=f"{SCORE}/50 States Correct",
                             prompt="What's another state's name?").title()
    if guess == "Exit":
        break
    if guess in all_states:
        SCORE += 1
        correct_answer.append(states[states.state == guess].state.item())
        city = turtle.Turtle()
        city.hideturtle()
        city.penup()
        city.goto(int(states[states.state == guess].x), int(states[states.state == guess].y))
        city.write(states[states.state == guess].state.item())

missed = []
for state in all_states:
    if state not in correct_answer:
        missed.append(state)

pd.DataFrame(missed).to_csv("states_to_learn.csv")