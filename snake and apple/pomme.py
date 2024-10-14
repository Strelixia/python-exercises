import turtle
import random
class pomme(turtle.Turtle):
    def __init__(self,color,x,y ):
        super().__init__()
        self.shape("circle")
        self.pommecolor = color
        self.position = [x,y]
    def dessine(self):
        self.clear()
        self.shape("circle")
        self.penup()
        self.color(self.pommecolor)
        self.hideturtle()
        self.goto(-190 + self.position[0]*20, 190 - self.position[1]*20)
        self.stamp
    def reaparition(self):
        self.position = [random.randint(0,19), random.randint(0,19)]
        self.dessine()