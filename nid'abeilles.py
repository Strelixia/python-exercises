"""
        for i in range (4):
            pen.begin_fill()
            pen.backward(10)
            pen.left(135)
            pen.forward(10)
            pen.right(45)
            pen.forward(10)
            pen.right(45)
            pen.forward(10)
            pen.right(45)
            pen.forward(10)
            pen.left(-45)
            pen.forward(10)
            pen.left(-45)
            pen.forward(10)
            pen.left(-45)
            pen.forward(10)
            pen.right(135)
            pen.forward(100)
            pen.fillcolor("yellow")
            pen.end_fill()  """

import turtle
wn = turtle.Screen()
wn.bgcolor("black")
pen = turtle.Turtle()
pen.shape("arrow")
pen.speed(2)
pen.color("white")
pen.pensize(2)
def exercice(x,y,l):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.begin_fill()
    for i in range (0,6):
        pen.forward(l)
        pen.left(60)
        pen.end_fill()

exercice()
wn.mainloop()