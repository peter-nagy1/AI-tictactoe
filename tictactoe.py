import random

PLAYER = 'x'
AI = 'o'
currentPlayer = ''
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
position = ' '

aiDictionnary = [] # [[board, weight, position], [board, weight, position], ...]
turnDictionnary = []

def winningMoves():
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] == AI:
            return [str(i)+str(0), str(i)+str(1), str(i)+str(2)]
        if board[0][i] == board[1][i] == board[2][i] == AI:
            return [str(0)+str(i), str(1)+str(i), str(2)+str(i)]
        if board[0][0] == board[1][1] == board[2][2] == AI:
            return [str(0)+str(0), str(1)+str(1), str(2)+str(2)]
        if board[0][2] == board[1][1] == board[2][0] == AI:
            return [str(0)+str(2), str(1)+str(1), str(2)+str(0)]

def gameEnded():
    for x in [PLAYER, AI]:
        for i in range(0,3):
            if (board[i][0] == board[i][1] == board[i][2] == x
            or board[0][i] == board[1][i] == board[2][i] == x
            or board[0][0] == board[1][1] == board[2][2] == x
            or board[0][2] == board[1][1] == board[2][0] == x):
                return x

    isSpace = False
    for i in board:
        for j in i:
            if (j == ' '):
                isSpace = True
    if not isSpace:
        return ''

    return None
        
def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def playerPlay():
    while True:
        position = input("Position [row][column]: ")
        if (position == "q"):
            exit()
        if (len(position) == 2):
            if (representsInt(position[0]) and representsInt(position[1])):
                if (int(position[0])>0 and int(position[0])<4 and int(position[1])>0 and int(position[1])<4):
                    if (board[int(position[0])-1][int(position[1])-1] == ' '):
                        board[int(position[0])-1][int(position[1])-1] = PLAYER
                        return

def aiPlay():
    for aiDict in aiDictionnary:
        if (sameBoard(board, aiDict[0])):
            if (aiDict[1]>=0):
                turnDictionnary.append([boardCopy(), 0, aiDict[2]])
                board[int(aiDict[2][0])][int(aiDict[2][1])] = AI
                return
    for i in random.sample(range(3),3):
        for j in random.sample(range(3),3):
            if (board[i][j] == ' '):
                turnDictionnary.append([boardCopy(), 0, str(i)+str(j)])
                board[i][j] = AI
                return

def boardCopy():
    copy = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(3):
        for j in range(3):
            copy[i][j] = board[i][j]
    return copy

def sameBoard(pBoard, aiBoard):
    for i in range(3):
        for j in range(3):
            if (pBoard[i][j] != aiBoard[i][j]):
                return False
    return True

def extendDictionnary():
    leftoutDict = []
    if (len(aiDictionnary) == 0):
        aiDictionnary.extend(turnDictionnary)
    else:    
        for turnDict in turnDictionnary:
            for aiDict in aiDictionnary:
                if (sameBoard(turnDict[0], aiDict[0]) and turnDict[2] == aiDict[2]):
                    aiDict[1] += turnDict[1]
                    break
                else:
                    leftoutDict.append(turnDict)
                    break
    aiDictionnary.extend(leftoutDict)
    


while True:
    print("NEW GAME\n")

    if (random.randint(0,1) == 0):
        currentPlayer = PLAYER
    else:
        currentPlayer = AI

    turnDictionnary = []
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    while gameEnded() == None:
        # Print board
        for i in range(3):
            print(board[i])
        print("---------------")

        # Turns
        if (currentPlayer == PLAYER):
            playerPlay()
            currentPlayer = AI
        else:
            aiPlay()
            currentPlayer = PLAYER

        # Game ends
        if (gameEnded() != None):
            for i in range(3):
                print(board[i])

            if (gameEnded() == PLAYER):
                print("PLAYER WON\n")
                for i in turnDictionnary:
                    i[1] = -1
            elif (gameEnded() == AI):
                print("AI WON\n")
                for i in turnDictionnary:
                    if i[2] in winningMoves():
                        i[1] = 1
            else:
                print("DRAW\n")
                for i in range(len(turnDictionnary)):
                    turnDictionnary[i][1] = 1
            extendDictionnary()
            aiDictionnary.sort(key=lambda x:x[1], reverse=True)
        

    
