import random

import colorgram
import turtle
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
[rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b)) for color in colors]
tim = Turtle()
turtle.colormode(255)
screen = Screen()
width, height = screen.window_width(), screen.window_height()
screen.setworldcoordinates(0, height, width, 0)
tim.speed('fastest')
for i in range(10):
    tim.penup()
    tim.setx(40)
    tim.sety(45 * i)
    for j in range(10):
        tim.pendown()
        tim.color(random.choice(rgb_colors))
        tim.begin_fill()
        tim.dot(20)
        tim.end_fill()
        tim.penup()
        tim.forward(50)

Screen().exitonclick()
