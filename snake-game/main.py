import turtle as t
import snake as s
from food import Food

screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")

snake = s.Snake()
food = Food()

snake.start_game(food_obj=food)

screen.exitonclick()
