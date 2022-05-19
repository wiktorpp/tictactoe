import os

boardSize = 3
minWinSiZE = 3


def isWin(board):
    win = False
    for i in range(boardSize):
        win = all(board[i]) or win
        win = all([line[i] for line in board]) or win
        win = all([line[index] for index, line in enumerate(board)]) or win
    return win

def printBoard(board, char):
    print(" 012")
    for i, line in enumerate(board):
        print(i, end="")
        for place in line:
            print(char if place else " ", end="")
        print()

player1 = [ [0]*boardSize for i in range(boardSize)]
player2 = [ [0]*boardSize for i in range(boardSize)]

while True:
    print(" 012")
    for i in range(boardSize):
        print(i, end="")
        for j in range(boardSize):
            print("X" if player1[i][j] else "O" if player2[i][j] else " ", end="")
        print()
    print()
    p1move = input("X")
    try:
        p1move = (int(p1move[0]), int(p1move[1]))
        if player2[p1move[0]][p1move[1]] == True:
            print("Error")
        else:
            player1[p1move[0]][p1move[1]] = True
    except:
        pass
    if isWin(player1):
        #while True: print('\a', end="")
        print("win")
        exit()

    print(" 012")
    for i in range(boardSize):
        print(i, end="")
        for j in range(boardSize):
            print("X" if player1[i][j] else "O" if player2[i][j] else " ", end="")
        print()
    print()
    p2move = input("O")
    try:
        p2move = (int(p2move[0]), int(p2move[1]))
        if player1[p2move[0]][p2move[1]] == True:
            #print("Error")
            os.system("shutdown now")
        else:
            player2[p2move[0]][p2move[1]] = True
    except:
        pass
    if isWin(player2):
        #while True: print('\a', end="")
        print("win")
        exit()
