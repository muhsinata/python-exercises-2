import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

right_guesses = 0
keep_guessing = True

while keep_guessing:

    answer_state = screen.textinput(title=f"{right_guesses/50} States Correct", prompt="What's state's name?").title()
    answer_check = data[data.state == answer_state].empty

    if not answer_check:
        




screen.exitonclick()