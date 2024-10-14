from random import randint
grille = []

def ini():
    global grille 
    grille = []
    for row in range(4):
        grille.append([])
        for col in range(4):
            dice = randint(1,6)
            grille[row].append(dice)

def cree():
    global grille
    for row in range(4):
        st = "/ "
        for col in range(4):
            st = st + str(grille[row][col]) + "!"
            print(st)

def paire(nombre):
    if nombre%2 == 0:
        return True
    else:
        return False
    
def impaire(nombre):
    if nombre%2 == 1:
        return True
    else:
        return False
    
ini()
cree()