from turtle import Turtle as t, Screen as s
import random as random



ghy = t()
ghy.shape("turtle")
ghy.speed(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def turtle_circle ():
    current_angle = 0
    while current_angle < 360:
        ghy.circle(100)
        # ghy.pencolor(random_color())
        ghy.left(current_angle)
        current_angle += 1

turtle_circle()

s = s()
s.exitonclick()