"""
This code is the code I added after being inspired by Angela Yu's answer when I saw her use the "setheading method
"""

from turtle import Turtle as t, Screen as s
import random as r

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "orange", "pink", "royalblue"]
directions = [0, 90, 180, 270]
distance = [20, 40, 60]

ghy = t()
ghy.shape("turtle")
ghy.pensize(10)

def choose_color():
    new_color = r.choice(colors)
    ghy.color(new_color)

def choose_direction():
    r.choice(directions)

def move():
    for i in range(1001):
        new_distance = r.choice(distance)
        ghy.forward(new_distance)
        choose_color()
        new_direction = r.choice(directions)
        ghy.setheading(new_direction)

move()

screen = s()
screen.exitonclick()