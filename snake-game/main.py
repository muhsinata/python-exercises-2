import turtle as t
import snake as s

screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")

snake = s.Snake()
snake.start_game()

screen.exitonclick()
