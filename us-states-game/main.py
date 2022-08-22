import turtle
import pandas
import write_states

screen = turtle.Screen()
write_states = write_states.WriteState()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

right_guesses = 0
keep_guessing = True

while keep_guessing:

    answer_state = screen.textinput(title=f"{right_guesses}/50 States Correct", prompt="What's state's name?").title()
    answer_check = data[data.state == answer_state].empty

    if not answer_check:

        state_row = data[data.state == answer_state]
        state_x = int(state_row.x)
        state_y = int(state_row.y)
        right_guesses += 1

        write_states.find_state(state_x, state_y)
        write_states.write_state_name(answer_state)





screen.exitonclick()