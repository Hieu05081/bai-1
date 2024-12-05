print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1, 180):
    painter.left(2)
    drawsq(painter, 100)

turtle.done()
