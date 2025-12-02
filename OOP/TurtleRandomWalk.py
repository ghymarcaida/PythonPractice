"""
In this project I'm going to make my turtle walk in random directions to create somewhat of an art
"""

from turtle import Turtle as t, Screen as s
import random as r

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "orange", "pink", "royalblue"]

ghy = t()
ghy.pensize(10)

def choose_color():
    random_color = r.choice(colors)
    ghy.color(random_color)

def move_left():
    ghy.left(90)
    ghy.forward(20)

def move_right():
    ghy.right(90)
    ghy.forward(20)

def move():
    direction_choice = [move_left, move_right]
    for i in range (1, 100):
        chosen_direction = r.choice(direction_choice)
        chosen_direction()
        choose_color()

move()


screen = s()
screen.exitonclick()