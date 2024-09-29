
import turtle
from shapes import *

# 2. name your turtle
pen = turtle.Turtle()
# 3. Set up your turtle
pen.speed(100)
pen.color(0/255,0/255,0/255)
wn = turtle.Screen()
wn.bgcolor(66/255,202/255,244/255)

#4. start drawing
drawMountains(pen) 
drawTower(pen,-25,-150,60,300,False)
drawWall(pen,-50,-150,100,195,True)
drawTower(pen,-60,40,118,30,True)
drawWall(pen,-150,-150,300,100,True)
drawTower(pen,-150,-150,60,220,False)
drawTower(pen,90,-150,60,220,False)
drawDoor(pen, 0,-150,50,50,)
drawFlag(pen,120, 120,30,40,"#FF0000")
drawFlag(pen,-120, 120,30,40,"#FFFF00")
drawLoophole(pen,-120,-120,10,30)
drawLoophole(pen,120,-120,10,30)
drawLoophole(pen,30,0,10,30)
drawLoophole(pen,-30,0,10,30)
drawLoophole(pen,-120,0,10,30)
drawLoophole(pen,120, 0,10,30)
drawLoophole(pen,50,-100,10,30)
drawLoophole(pen,-50,-100,10,30)
drawLoophole(pen,0 ,110,10,30)
pen.hideturtle()
wn.mainloop()