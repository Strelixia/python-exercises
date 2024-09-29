import turtle

sc = turtle.Screen()
sc.bgcolor("black")

pen = turtle.Turtle()
pen.color("white")

def crénelure():
    pen.penup()
    pen.goto(-280,0)
    pen.pendown()
    for i in range(0,100):
        pen.left(90)
        pen.forward(70)  
        pen.right(90)
        pen.forward(20)
        pen.left(-90)
        pen.forward(20)
        pen.left(90)
        pen.forward(30)
        pen.right(-90)
        pen.forward(20)
        pen.right(90)
        pen.forward(20)
        pen.right(90)
        pen.forward(70)
        pen.right(90)
        pen.forward(-40)
        pen.left(-180)
        
crénelure()
sc.mainloop()