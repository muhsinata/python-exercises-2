from turtle import Turtle

PADDLE_STRETCH_W = 5
PADDLE_STRETCH_H = 1


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_STRETCH_W, stretch_len=PADDLE_STRETCH_H)
        self.penup()
        self.color("white")
        self.goto(x=x_cor, y=y_cor)

    def move_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_cor)

    def move_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_cor)
