from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

with open("data.txt") as data:
    high_score = int(data.read())

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

jacob = Snake()
food = Food()
scoreboard = Scoreboard()
while scoreboard.high_score < high_score:
    scoreboard.highest_score()
high_score = 0
game = True

screen.listen()
screen.onkey(jacob.up, "Up")
screen.onkey(jacob.down, "Down")
screen.onkey(jacob.left, "Left")
screen.onkey(jacob.right, "Right")
while game:
    screen.update()
    time.sleep(0.1)
    jacob.move()

    if scoreboard.high_score < high_score:
        scoreboard.highest_score()

    if jacob.snake_parts[0].distance(food) < 15:
        food.refresh()
        jacob.growing()
        scoreboard.add_point()
        high_score += 1
        if scoreboard.high_score < high_score:
            with open("data.txt", "w") as file:
                file.write(str(high_score))
            scoreboard.highest_score()

    if 280 < jacob.snake_parts[0].xcor() or jacob.snake_parts[0].xcor() < -280 or 280 < jacob.snake_parts[0].ycor() or \
            jacob.snake_parts[0].ycor() < -280:
        # scoreboard.game_over()
        jacob.reset()
        high_score = 0
        scoreboard.reset()

    for part in jacob.snake_parts[1:]:
        if jacob.snake_parts[0].distance(part) < 10:
            jacob.reset()
            high_score = 0
            scoreboard.reset()

screen.exitonclick()
