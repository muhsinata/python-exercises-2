import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_COLOR = "black"


class GameScreen:

    def __init__(self):
        self.screen_settings()

    def screen_settings(self):
        turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        turtle.bgcolor(SCREEN_COLOR)
        turtle.exitonclick()
