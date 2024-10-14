#A Game of Snake using Python - www.101computing.net/snake-game-using-python/
import turtle
import random
import time
from snake import Snake
from apple import Apple

def displayInstructions():
  print("~~~~~~~~~~~~~~~~~~~~")
  print("~                  ~")
  print("~   Snake Game     ~")
  print("~                  ~")
  print("~~~~~~~~~~~~~~~~~~~~")
  print("")
  print("~~~ Instructions ~~~")
  print(" > Use the arrow keys on your keyboard to control the snake.")
  print(" > Do not let your snake reach the edges of the screen.")
  print(" > Direct your snake to reach the red apple.")
  print(" > Do not let your snake eat/cross its own tail.")
  print("~~~~~~~~~~~~~~~~~~~~")
  print("")
  print(" >>> Double click on the screen to get started...")
  print("")

def drawBorders():
  pen = turtle.Turtle()
  pen.hideturtle()  
  pen.speed(5)
  pen.color("#FFFF00")
  pen.pensize(2)
  pen.penup()
  pen.goto(-202,-202)
  pen.pendown()
  for i in range(4):
    pen.forward(404)
    pen.left(90)

# >>> Setup the Stage
screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(440, 440)
screen.bgcolor("black")

# >>> Draw the white borders
drawBorders()

  
# >>> Add the apple
apple = Apple("#FF0000",random.randint(0,19),random.randint(0,19))
apple.draw()

# >>> Add the Snake...
snake1 = Snake("#810081","#B130B1",0,19)  #Purple Snake in the bottom left corner (0,0) of the 20x20 grid
snake1.direction = "right"
snake1.draw()
snake2 = Snake("green","green",10,19)  #Purple Snake in the bottom left corner (0,0) of the 20x20 grid
snake2.direction = "right"
snake2.draw()
# >>> Display instructions on how to play the game
displayInstructions()

def startGame(x,y):
  global gameOver
  if not gameOver:
    score = 0
    delay = 0.25
    print(" >>> Starting Game")

    # >>> Main game loop
    while not gameOver:  
      screen.bgcolor("black")
      snake1.move() or snake2.move() 
      
  
      # Has the snake gone over the edge of the game window?
      if snake1.isOffScreen() or snake2.isOffScreen():
        print(" >>> Game Over! <<<")
        gameOver=True
        
      #Is the snake biting its own tail!  
      elif snake1.isBitingTail() or snake2.isBitingTail():
        print(" >>> Game Over! <<<")
        gameOver=True
        
      elif snake1.position [0] == snake2.position[0] and snake1.position[1] == snake2.position[1]:
        print(" >>> Game Over! <<<")
        gameOver=Trueh
      # Has the snake reached the apple? 
      elif snake1.position[0] == apple.position[0] and snake1.position[1] == apple.position[1]:
        snake1.score += 1
        print("Score mauve: " + str(snake1.score) + "pts")
        # Extend the tail of the snake
        snake1.grow()
        apple.respawn()

      elif snake2.position[0] == apple.position[0] and snake2.position[1] == apple.position[1]:
        snake2.score += 1
        print("Score vert: " + str(snake2.score) + "pts")
        # Extend the tail of the snake
        snake2.grow()




        # Respawn the apple using a different location
        apple.respawn()
   
      screen.update()
      time.sleep(delay)


# >>> Implementing motion of the snake in all 4 directions
def go_up():
 snake1.direction = "up"

def go_down():
  snake1.direction = "down"
  
def go_right():
  snake1.direction = "right"
 
def go_left():
  snake1.direction = "left"

# >>> Keyboard bindings (using the arrow keys)
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")


def haut():
 snake2.direction = "up"

def bas():
  snake2.direction = "down"
  
def droite():
  snake2.direction = "left"
 
def gauche():
  snake2.direction = "right"

# >>> Keyboard bindings (using the arrow keys)
screen.listen()
screen.onkeypress(haut, "8")
screen.onkeypress(bas, "2")
screen.onkeypress(droite, "4")
screen.onkeypress(gauche, "6")

#The game will only start once the player clicks on the screen
screen.onscreenclick(startGame, 1)

gameOver=False
screen.mainloop()
