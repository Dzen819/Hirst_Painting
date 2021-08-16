from data import colors
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.speed(0)
tim.hideturtle()
tim.up()
tim.setpos(-250, -250)
tim.speed(3)

for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        if _ < 9:
            tim.forward(50)
        else:
            tim.speed(0)
            tim.setpos(-250, tim.ycor() + 50)
            tim.speed(3)

screen.exitonclick()
