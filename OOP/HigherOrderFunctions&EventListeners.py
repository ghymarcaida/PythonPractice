from turtle import Turtle as t, Screen as s
"""
Higher order functions are functions that work with other functions.
They are functions that can take functions as an input
NOTE: when passing functions as inputs, never use "()" as it will trigger for the function to be
      executed right there and there. SO NEVER USE EM OR AT LEAST REMEMBER IT
"""
ghy = t()

def move_forward():
    ghy.forward(100)


screen = s()
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()