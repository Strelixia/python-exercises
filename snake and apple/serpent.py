import turtle

class serpent(turtle.Turtle):
    def __init__(self,colorserp,colorq,x,y):
        super().__init__()
        self.shape("square")
        self.colorserp = colorserp
        self.colorq = colorq
        self.position =  [x,y]
        self.score = 0
        self.direction = "right"
        self.queue = []
    def dessine(self):
        self.clear()
        self.shape("square")
        self.penup()
        self.goto(-190 + self.position[0]*20, 190 - self.position[1]*20)
        self.hideturtle()
        self.stamp()
        for position in self.queue:
            self.color(self.colorq)
            self.goto(-190 + self.position[0]*20, 190 - self.position[1]*20)
            self.stamp()
            if len(self.queue) >= 1:
                self.queue.append(self.position[0],self.position[1])
                self.queue.pop(0)
    def mouvements(self):
        self.direction == "up"
        self.position[1] -= 1
        self.direction == "down"
        self.position[1] += 1
        self.direction == "left"
        self.position[0] -= 1
        self.direction == "right"
        self.position[0] += 1
        self.dessine()
    def grandir(self):
        self.queue.append(self.position[0],self.position[1])

    def morduebord(self):
        if self.position[0]<0 or self.position[0]>20 or self.position[1]<0 or self.position[1]>20:
            return True
        else : 
            return False

    def mordueq(self):
       for i in range(0,len(self.queue)-1):
        if self.position[0]==self.queue[i][0] and self.position[1]==self.queue[i][1]:
         return True
        return False
