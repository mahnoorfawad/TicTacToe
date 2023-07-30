1#tic tac toe
print ("Welcome to Tic Tac Toe")
print("Player 1 is X")
print("Player 2 is O")
board = ["_", "_","_",
         "_", "_","_",
         "_", "_","_"]
currentP = "X"
winner = None #no val
gamerunning = True
 
#game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#player input
def playerInput(board):
    if currentP == "X":
        inp = int(input("P1 enter an index in 1-9: "))
        if inp >= 1 and inp <=9 and board[inp-1] == "_":
            board[inp-1] = currentP
        else:
            print("Invalid index, oops!") 
    elif currentP == "O":
        inp = int(input("P2 enter an index in 1-9: "))
        if inp >= 1 and inp <=9 and board[inp-1] == "_":
            board[inp-1] = currentP
        else:
            print("Invalid index, oops!") 

# check win / tie
def checkHoriz(board):
    global winner 
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "_":
        winner = board [7]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "_":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner    
    if board[0] == board[4] == board[8] and board[4] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "_":
        winner = board[2]
        return True

def checkTie(board):
    global gamerunning
    if "_" not in board:
        printBoard(board)
        print ("You've tied!!")
        gamerunning = False

    
#switch player 

def switchP():
    global currentP
    if currentP == "X":
        currentP = "O"
    else:
        currentP = "X"

#check for win/tie again

def checkWin():
    global gamerunning
    if checkDiag(board) or checkHoriz(board) or checkRow(board):
        print(f"The winner is ", {winner})
        gamerunning = False

#main game 

while gamerunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchP()
    if gamerunning == False:
        printBoard(board)
        break