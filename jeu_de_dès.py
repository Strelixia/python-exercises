from random import randint
grid = []

def reset_grid():
    global grid
    grid = []
    for row in range(4):
        grid.append([])
        for col in range(4):
            dice = randint(1,6)
            grid[row].append(dice)

def display_grid():
    global grid
    for row in range(4):
        st = "| "

        
        for col in range(4):
            st = st + str(grid [row][col]) + "|"
            print(st)

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False
    
def isOdd(number):
    if number%2 == 1:
        return True
    else:
        return False
reset_grid()
display_grid()
score = 0
score1 = 0
score2 = 0
score3 = 0
score4 = 0
if is_even(grid[0][0]) and is_even(grid[0][3]) and is_even(grid[3][0]) and is_even(grid[3][3]):
    print("Four even corners! +20pts")
    score1 = 20  
    if isOdd(grid[0][0]) and isOdd(grid[0][3]) and isOdd(grid[3][0]) and isOdd(grid[3][3]):
        print("Four odd corners! +20pts")
        score2 = score1 + 20
        if is_even(grid[0][3]) and is_even(grid[1][2]) and is_even(grid[2][1]) and is_even(grid[3][0]) and is_even(grid[0][0]) and is_even(grid[1][1]) and is_even(grid[2][2]) and is_even(grid[3][3]):
            print("Four even corners! +20pts")
            score3 = score2 + 20  
            if isOdd(grid[0][3]) and isOdd(grid[1][2]) and isOdd(grid[2][1]) and isOdd(grid[3][0]) and isOdd(grid[0][0]) and isOdd(grid[1][1]) and isOdd(grid[2][2]) and isOdd(grid[3][3]):
                print("Four even corners! +20pts")
                score4 = score3 + 20 
score = score1 + score2 + score3 +  score4
print("\n Grid score:" + str(score) +"pts.")
