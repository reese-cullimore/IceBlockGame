import random

def printboard():
    for row in range(1,ymax+1):
        rowtext = ''
        for column in range(1,xmax+1):
            rowtext += ' ' + getsymbol(row, column)
        print(rowtext)

def getsymbol(row,column):
    if ((column, row) == (playerX, playerY)):
        return "I"
    elif ((column, row) == (goalX, goalY)):
        return "G"
    elif ((column, row) in boulders):
        return "0"
    else:
        rand = random.randint(0,8)
        if rand == 0:
            return "'"
        else:
            return '`'

def makemovement(inputKey):
    global playerX, playerY, boulders
    if (inputKey == rightKey):
        intheway = [x for x in boulders if ((x[1] == playerY) and (x[0] > playerX))]
        if intheway == []:
            playerX = xmax
        else:
            firstintheway = min(intheway)
            playerX = firstintheway[0] - 1
    elif (inputKey == upKey):
        intheway = [y for y in boulders if ((y[0] == playerX) and (y[1] < playerY))]
        if intheway == []:
            playerY = 1
        else:
            firstintheway = max(intheway)
            playerY = firstintheway[1] + 1
    elif (inputKey == downKey):
        intheway = [y for y in boulders if ((y[0] == playerX) and (y[1] > playerY))]
        if intheway == []:
            playerY = ymax
        else:
            firstintheway = min(intheway)
            playerY = firstintheway[1] - 1
    elif (inputKey == leftKey):
        intheway = [x for x in boulders if ((x[1] == playerY) and (x[0] < playerX))]
        if intheway == []:
            playerX = 1
        else:
            firstintheway = max(intheway)
            playerX = firstintheway[0] + 1
    else:
        print("That is not an option, I'm sorry")

def makemove():
    global gameplay
    print("\nMove the ice block (I) to its goal (G)\n")
    printboard()
    answer = input()
    makemovement(answer)
    if (playerX == goalX and playerY == goalY):
          print("Success!")
          gameplay = False
    else:
          makemove()
while True:
    gameplay = True
    leftKey = 'a'
    rightKey = 'd'
    upKey = 'w'
    downKey = 's'
    while gameplay is True:
        rand = random.randint(0,1)
        if rand == 0:
            xmax, ymax = 6, 6
            playerX, playerY = 1, 1
            boulders = [(2,2),(5,3),(1,5),(6,6)]
            goalX, goalY = 4, 6
        if rand == 1:
            xmax, ymax = 7, 4
            playerX, playerY = 6, 1
            boulders = [(2,2),(4,1),(6,3),(3,4)]
            goalX, goalY = 5, 3
        makemove()
    print("Would you like to play again? (Yes/No)")
    if not input().lower().startswith('y'):
        break

