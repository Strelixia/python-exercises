import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor("skyblue")

pen = turtle.Turtle()
pen.speed(100)

# fonction pour dessiner les montagnes
def draw_mountains(pen):
    pen.penup()
    pen.goto(-200,80)
    pen.pendown()
    pen .color(5/255,114/255,3/255)
    pen.fillcolor(5/255,114/255,3/255)
    pen.begin_fill()
    for peak in range(1,11):
        pen.goto(-200+40*peak,randint(40,160))
    pen.goto(200,-200)
    pen.goto(-200,-200)
    pen.goto(-200,80)
    pen.end_fill()
draw_mountains(pen)

# fonction pour dessiner un rectangle
def draw_battlements(pen,x,y,width,height):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.color(0/255, 0/255, 0/255)
    pen.fillcolor(150/255,150/255,150/255)
    pen.begin_fill()
    xEnd = x + width
    while x < xEnd:
        pen.goto(x,y)
        pen.goto(x,y+width)
        pen.goto(x+20,y+height)
        pen.goto(x+20,y)
        if x+20<xEnd:
            pen.goto(x+40,y)
        x=x+40
    pen.end_fill()

def draw_mur(pen,x,y,width,height,crenellation):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.color("dark")
    pen.fillcolor(150/255,150/255,150/255)
    pen.begin_fill()
    pen.goto(x+width,y)
    pen.goto(x+width,y+height)
    pen.goto(x,y+height)
    pen.goto(x,y)
    pen.end_fill()
    if crenellation == True:
        draw_battlements(pen,-20,-150+225,width,20)
    draw_mur(pen,-40,-150,225,150,True)




pen.hideturtle()
screen.mainloop()