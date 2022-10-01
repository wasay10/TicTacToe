
board = [" " for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == " "

def printBoard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
     
def isWinner(bor, lett):
    return ((bor[7] == lett and bor[8] == lett and bor[9] == lett) or
    (bor[4] == lett and bor[5] == lett and bor[6] == lett) or
    (bor[1] == lett and bor[2] == lett and bor[3] == lett) or
    (bor[1] == lett and bor[4] == lett and bor[7] == lett) or
    (bor[2] == lett and bor[5] == lett and bor[8] == lett) or
    (bor[3] == lett and bor[6] == lett and bor[9] == lett) or
    (bor[1] == lett and bor[5] == lett and bor[9] == lett) or
    (bor[3] == lett and bor[5] == lett and bor[7] == lett))  
    
def playerMove():
    run = True
    while run:
        move = input("Please select a position to place a \"X\" (1-9)")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("Sorry, space is filled")
            else:
                print("Please type a number within the range: 1-9")
        except:
            print("Please type a number")
            
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) 
    if letter == " " and x != 0]  
    move = 0
    
    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move
                
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
    
def main():
    print("Welcome to Tic Tac Toe")
    printBoard(board)
    
    while not(isBoardFull(board)):
        if not(isWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, Computer Won")
            break
        
        if not(isWinner(board, "X")):
            move = compMove()
            if move == 0:
                print("Tie game")
            else:
                insertLetter("O", move)
                print("Computer placed an \"O\" in position", move, ":")
                printBoard(board)
        else:
            print("Congrats, You Won!")
            break
        
    if isBoardFull(board):
        print("Tie game")


main()