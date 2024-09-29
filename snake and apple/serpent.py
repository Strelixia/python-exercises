
import turtle


class serpent(turtle.Turtle):
    def __init__(self, colorserp, colorqueue, x, y):
        super().__init__()
        self.colorserp = colorserp
        self.colorqueue = colorqueue
        self.score = 0
        self.position = [x,y]
        self.queue = []
        