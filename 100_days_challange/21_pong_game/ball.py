from turtle import Turtle

r_paddle = (350, 0)
l_paddle = (-350, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("purple")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        if self.wall_collision():
            self.y_move *= -1
        move_y = self.ycor() + self.y_move
        move_x = self.xcor() + self.x_move
        self.goto(move_x, move_y)

    def wall_collision(self):
        return self.ycor() > 280 or self.ycor() < -280

    def player_collision(self):
        self.move_speed *= 0.8
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
