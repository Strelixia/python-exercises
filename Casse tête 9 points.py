import turtle

sc = turtle.Screen()
sc.bgcolor("black")

pen = turtle.Turtle()
pen.shape("arrow")
pen.speed(1)
pen.color("white")
pen.pensize(1)


def drapeau():
    for i in range(0,3):
        pen.penup()
        pen.goto(-180,-120)
        pen.pendown()
        pen.begin_fill()
        pen.goto(180,-120)
        pen.goto(180,120)
        pen.goto(-180,120)
        pen.goto(-180,-120)
        pen.fillcolor("white")
        pen.end_fill()

        pen.penup()
        pen.goto(-180,-120)
        pen.pendown()
        pen.begin_fill()
        pen.goto(-60,-120)
        pen.goto(-60,120)
        pen.goto(-180,120)
        pen.goto(-180,-120)
        pen.fillcolor("blue")
        pen.end_fill()


        pen.penup()
        pen.goto(60,-120)
        pen.pendown()
        pen.begin_fill()
        pen.goto(180,-120)
        pen.goto(180,120)
        pen.goto(60,120)
        pen.goto(60,-120)
        pen.fillcolor("red")
        pen.end_fill()
drapeau()     
sc.mainloop()