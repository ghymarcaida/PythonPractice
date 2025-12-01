from turtle import Turtle as t, Screen as s

tim = t()
tim.shape("turtle")
tim.color("purple")

for i in range(4):
    tim.forward(100)
    tim.right(90)

for i in range(25):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


screen = s()
screen.exitonclick()