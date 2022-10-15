from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboad
import time

r_paddle = (350, 0)
l_paddle = (-350, 0)

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)

# First player
first_player = Paddle(r_paddle)

# Second Player
second_player = Paddle(l_paddle)
screen.listen()

scoreboard = Scoreboad()

# shortcuts
screen.onkeypress(first_player.up, "Up")
screen.onkeypress(first_player.down, "Down")
screen.onkeypress(second_player.up, "w")
screen.onkeypress(second_player.down, "s")

# Ball
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.distance(first_player) < 50 and ball.xcor() > 320 or ball.distance(
            second_player) < 50 and ball.xcor() < -320:
        ball.player_collision()

    if ball.xcor() > 350:
        ball.reset()
        scoreboard.right_point()

    if ball.xcor() < -350:
        ball.reset()
        scoreboard.left_point()

screen.exitonclick()
