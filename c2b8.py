print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


import turtle
import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

painter = turtle.Turtle()
painter.pensize(3)

for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)

turtle.done()
