import random

board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
commands = ['T', 't', 'B', 'b', 'R', 'r', 'L', 'l']

#####
def displayBoard() -> None:
    global board
    print()
    
    for i in range(len(board)):
        for j in range(len(board)):
            print(str(board[i][j]).ljust(5, ' '), end="")
        print()
#####
        
#####
def move(move_side: str) -> None:
    if move_side.lower() == 't':
        for i in range(4):
            for j in range(4):

                temp = board[i][j]
                for k in range(1, 4):
                    if i-k < 0: continue

                    if board[i-k][j] == 0: 
                        board[i-k][j] = temp
                        board[i-k+1][j] = 0
                    elif board[i-k][j] == temp:
                        board[i-k+1][j] = 0
                        board[i-k][j] += temp
                        board[i][j] = 0
                        break
                    else:
                        break

    elif move_side.lower() == 'b':
        for i in range(3, -1, -1):
            for j in range(4):

                temp = board[i][j]
                for k in range(1, 4):
                    if i + k > 3: continue

                    if board[i+k][j] == 0: 
                        board[i+k][j] = temp
                        board[i+k-1][j] = 0
                    elif board[i+k][j] == temp and i != i+k:
                        board[i+k-1][j] = 0
                        board[i+k][j] += temp
                        board[i][j] = 0
                        break
                    else:
                        break

    elif move_side.lower() == 'l':
        
        for i in range(4):
            for j in range(4):

                temp = board[i][j]
                for k in range(1, 4):
                    if j-k < 0: continue

                    if board[i][j-k] == 0:
                        board[i][j-k] = temp
                        board[i][j-k+1] = 0
                    elif board[i][j-k] == temp:
                        board[i][j-k+1] = 0
                        board[i][j-k] += temp
                        board[i][j] = 0
                        break
                    else:
                        break
        
    elif move_side.lower() == 'r':
        for i in range(4):
            for j in range(4):

                temp = board[i][j]
                for k in range(1, 4):
                    if j+k > 3: continue

                    if board[i][j+k] == 0:
                        board[i][j+k] = temp
                        board[i][j+k-1] = 0
                    elif board[i][j+k] == temp:
                        board[i][j+k-1] = 0
                        board[i][j+k] += temp
                        board[i][j] = 0
                        break
                    else:
                        break


#####
    
#####
def checkGameStatus() -> str:
    global board

    count = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return 'win'
            elif board[i][j] != 0:
                count += 1
    if count == 16:
        return 'lost'
    
    return 'continue'
#####

#####
def startGame() -> None:
    global board
    global commands

    while True:

        # choose a random index to put 2
        random_i = 0
        random_j = 0
        while True:
            random_i = random.randint(0, 3)
            random_j = random.randint(0, 3)
            if board[random_i][random_j] == 0:
                break
        board[random_i][random_j] = 2

        # display the game
        displayBoard()

        # check if usr wins or looses
        status = checkGameStatus()
        if status == 'win':
            print('You win!')
            break
        elif status == 'lost':
            print('Game over!')
            break

        # get a move from usr
        usr_res = ''
        while True:
            if usr_res not in commands:
                usr_res = input('Press the command: ')
            else:
                break

        # we have a command, time to move
        move(usr_res)
#####

#####
def init() -> None:
    print('Commands are as follows :')
    print('\'T\' or \'t\' : Move Up')
    print('\'B\' or \'b\' : Move Down')
    print('\'L\' or \'l\' : Move Left')
    print('\'R\' or \'r\' : Move Right')

    startGame()
#####
    
init()