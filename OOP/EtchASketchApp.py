from turtle import Turtle as t, Screen as s


ghy = t()
ghy.shape("turtle")
screen = s()

def move_forward():
    ghy.forward(10)

def move_backward():
    ghy.backward(10)

def turn_left():
    ghy.left(10)

def turn_right():
    ghy.right(10)

def home():
    ghy.clear()
    ghy.home()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=home)

screen.mainloop()
