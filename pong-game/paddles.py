import turtle
import time

UP = "up"
DOWN = "down"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
X_MARGIN = 30
PADDLE_SQUARE_NUM = 4


class Paddle:

    def __init__(self):
        self.user_square_list = []
        self.pc_square_list = []
        self.x_coordinate = -SCREEN_WIDTH/2+X_MARGIN
        self.y_coordinate = PADDLE_SQUARE_NUM / 2 * -20 + 10
        self.user_paddle = turtle.Turtle("square")
        self.user_paddle.speed("fastest")
        self.user_paddle.penup()
        self.user_paddle.hideturtle()
        self.user_square_list.append(self.user_paddle)
        self.computer_paddle = turtle.Turtle("square")
        self.computer_paddle.speed("fastest")
        self.computer_paddle.penup()
        self.computer_paddle.hideturtle()
        self.pc_square_list.append(self.computer_paddle)
        self.user_paddle.goto(self.x_coordinate, self.y_coordinate)
        self.computer_paddle.goto(-self.x_coordinate, self.y_coordinate)
        self.user_paddle.color("white")
        self.computer_paddle.color("white")
        self.user_paddle.showturtle()
        self.computer_paddle.showturtle()
        self.square_number = PADDLE_SQUARE_NUM
        self.create_user_stick()
        self.create_pc_stick()
        self.pc_paddle_keep_move = True
        self.pc_head = self.pc_square_list[0]

    def create_user_stick(self):

        for square in range(self.square_number):
            square = turtle.Turtle("square")
            square.hideturtle()
            square.speed("fastest")
            square.penup()
            square.color("White")
            square.goto(self.x_coordinate, self.y_coordinate+20)
            square.showturtle()
            self.y_coordinate = square.ycor()

        self.x_coordinate = -SCREEN_WIDTH/2+X_MARGIN
        self.y_coordinate = PADDLE_SQUARE_NUM / 2 * -20 + 10

    def create_pc_stick(self):

        for square in range(self.square_number):
            square = turtle.Turtle("square")
            square.hideturtle()
            square.speed("fastest")
            square.penup()
            square.color("White")
            square.goto(-self.x_coordinate, self.y_coordinate+20)
            square.showturtle()
            self.y_coordinate = square.ycor()

    def move_pc_paddle(self):

        keep_move = True
        pc_head = self.pc_square_list[0]

        while keep_move:

            if pc_head == self.pc_square_list[-1]:

                for square in self.pc_square_list:
                    square.setheading(90)
                    square.forward(20)

                if pc_head.distance(0, SCREEN_HEIGHT / 2) < 10:
                    pc_head = self.pc_square_list[0]

            elif pc_head == self.pc_square_list[0]:

                for square in self.pc_square_list:
                    time.sleep(0.1)
                    square.setheading(270)
                    square.forward(20)

                if self.pc_head.distance(0, -SCREEN_HEIGHT/2) < 10:
                    pc_head = self.pc_square_list[-1]
