import turtle
import random
import time

from pomme import pomme
from serpent import serpent


def bordure():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.speed(10)
    pen.pensize(2)
    pen.penup()
    pen.goto(-202,-202)
    pen.pendown()
    for i in range (4):
        pen.forward(404)
        pen.left(90)
screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(440, 440)
screen.bgcolor("black")
bordure()

serpent1 = serpent("green","blue",0,19)
serpent1.direction = "right"
serpent1.dessine()
serpent2 = serpent("green","grey",7,19)
serpent2.direction = "left"
serpent2.dessine()

pomme = pomme("#FF0000",random.randint(0,19),random.randint(0,19))
pomme.dessine()


screen.update()
screen.mainloop()
