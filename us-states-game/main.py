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
all_states = data.state.to_list()
guessed_states = []
unguessed_states = list(set(all_states) - set(guessed_states))

while keep_guessing:

    answer_state = screen.textinput(title=f"{right_guesses}/50 States Correct", prompt="What's state's name?").title()
    answer_check = data[data.state == answer_state].empty

    if answer_state == "Exit":

        for state in unguessed_states:

            unguessed_state_row = data[data.state == state]
            state_x = int(unguessed_state_row.x)
            state_y = int(unguessed_state_row.y)

            write_states.find_state(state_x, state_y)
            write_states.write_state_name(state)

        break

    if not answer_check:

        state_row = data[data.state == answer_state]
        state_x = int(state_row.x)
        state_y = int(state_row.y)
        right_guesses += 1
        guessed_states.append(answer_state)

        write_states.find_state(state_x, state_y)
        write_states.write_state_name(answer_state)

screen.exitonclick()

