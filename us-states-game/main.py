import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

right_guesses = 0
keep_guessing = True

data = pandas.read_csv("50_states.csv")

# while keep_guessing:
#
#     answer_state = screen.textinput(title=f"{right_guesses/50} States Correct",
#                                     prompt="What's state's name?").title()

# test = data[data.state == "Alabama"]
# print(test)
# x_coor = test.x
# y_coor = test.y
# print(int(x_coor), int(y_coor))

answer_state = screen.textinput(title=f"{right_guesses/50} States Correct",
                                prompt="What's state's name?").title()

print(int(data[data.state == answer_state].x))


screen.exitonclick()