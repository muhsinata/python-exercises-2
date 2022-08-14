import turtle
import time

SCORE_COLOR = "black"
FONT = ("Arial", 60, "normal")


class Scoreboard:

    def __init__(self):
        self.user_x_coordinate = -100
        self.user_y_coordinate = 150
        self.computer_x_coordinate = 100
        self.computer_y_coordinate = 150
        self.user_score = 0
        self.computer_score = 0
        self.sleep()
        self.user_score_turtle = turtle.Turtle()
        self.user_score_turtle.hideturtle()
        self.user_score_turtle.color("white")
        self.user_score_turtle.speed("fastest")
        self.user_score_turtle.penup()
        self.sleep()
        self.computer_score_turtle = turtle.Turtle()
        self.computer_score_turtle.hideturtle()
        self.computer_score_turtle.color("white")
        self.computer_score_turtle.speed("fastest")
        self.computer_score_turtle.penup()
        self.score_places()
        self.scores()

    def score_places(self):
        self.user_score_turtle.goto(self.user_x_coordinate, self.user_y_coordinate)
        self.computer_score_turtle.goto(self.computer_x_coordinate, self.computer_y_coordinate)

    def scores(self):
        self.user_score_turtle.write(arg=self.user_score, align="center", font=FONT)
        self.computer_score_turtle.write(arg=self.computer_score, align="center", font=FONT)

    def sleep(self):
        time.sleep(0.2)
