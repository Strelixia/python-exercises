import turtle

arrplan = turtle.Screen()
arrplan.bgcolor("black")
def ligne(color,x,y,z,w):
    l = turtle.Turtle()
    l.color(color)
    l.penup()
    l.goto(x,y)
    l.pendown()
    l.goto(z,w)
ll = ligne("green",-276,150,-276,-50)
lll = ligne("green",100,150,100,-50)
def creer_tortue(color,x,y):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    return t
t1 = creer_tortue("blue",-280,100)
t2 = creer_tortue("white",-280,60)
t3 = creer_tortue("red",-280,20)
t4 = creer_tortue("grey",-280,-20)
nbre_etap = 100
arrivé = 200
for i in range(nbre_etap):
    t1.forward(2)
    t2.forward(4)
    t3.forward(3)
    t4.forward(1)
    if t1.xcor() >= arrivé:
        print("la tortue verte a gagné")
        break
    elif t2.xcor() >= arrivé:
        print("la tortue noire a gagné")
        break
    elif t3.xcor() >= arrivé:
        print("la tortue rose a gagné")
        break
    elif t4.xcor() >= arrivé:
        print("la tortue grise a gagné")
        break
arrplan.mainloop()
