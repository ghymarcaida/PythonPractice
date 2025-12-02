from turtle import Turtle as t, Screen as s
import random as rand

ghy = t()
ghy.shape("turtle")

#commenting this out because this was actually kind of fun to look at
# for i in range(3, 15):
#     turns = 360/i
#     while turns != 0:
#         ghy.forward(100)
#         ghy.right(turns)
#         turns -= 1

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "purple", "orange", "pink"]

def draw_shapes(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        ghy.forward(100)
        ghy.left(angle)

for i in range (3, 11):
    random_color = rand.choice(colors)
    ghy.color(random_color)
    draw_shapes(i)








screen = s()
screen.exitonclick()