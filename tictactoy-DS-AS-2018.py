# Tic Tac Toe

import random


def Gameboard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[ 7 ] + ' | ' + board[ 8 ] + ' | ' + board[ 9 ])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[ 4 ] + ' | ' + board[ 5 ] + ' | ' + board[ 6 ])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[ 1 ] + ' | ' + board[ 2 ] + ' | ' + board[ 3 ])
    print('   |   |')


def inputPlayerletter():
    # Lts the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first eLment in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return [ 'X', 'O' ]
    else:
        return [ 'O', 'X' ]


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def MakeAMove(board, letter, move):
    board[ move ] = letter


def isWinner(b, L):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use b instead of board and L instead of letter so we don’t have to type as much.
    return ((b[ 7 ] == L and b[ 8 ] == L and b[ 9 ] == L) or  # across the top
            (b[ 4 ] == L and b[ 5 ] == L and b[ 6 ] == L) or  # across the middL
            (b[ 1 ] == L and b[ 2 ] == L and b[ 3 ] == L) or  # across the bttom

            (b[ 7 ] == L and b[ 4 ] == L and b[ 1 ] == L) or  # down the Lft side
            (b[ 8 ] == L and b[ 5 ] == L and b[ 2 ] == L) or  # down the middL
            (b[ 9 ] == L and b[ 6 ] == L and b[ 3 ] == L) or  # down the right side

            (b[ 7 ] == L and b[ 5 ] == L and b[ 3 ] == L) or  # diagonal
            (b[ 9 ] == L and b[ 5 ] == L and b[ 1 ] == L))  # diagonal


def getboardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeboard = [ ]

    for i in board:
        dupeboard.append(i)

    return dupeboard


def FreeSpace(board, move):
    # Return true if the passed move is free on the passed board.
    return board[ move ] == ' '


def getPlayerMove(board):
    # Lt the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not FreeSpace(board, int(move)):
        print('What is your next move ?')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibLMoves = [ ]
    for i in movesList:
        if FreeSpace(board, i):
            possibLMoves.append(i)

    if len(possibLMoves) != 0:
        return random.choice(possibLMoves)
    else:
        return None


def getComputerMove(board, computerletter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerletter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getboardCopy(board)
        if FreeSpace(copy, i):
            MakeAMove(copy, computerletter, i)
            if isWinner(copy, computerletter):
                return i

                # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getboardCopy(board)
        if FreeSpace(copy, i):
            MakeAMove(copy, playerletter, i)
            if isWinner(copy, playerletter):
                return i

                # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [ 1, 3, 7, 9 ])
    if move != None:
        return move

        # Try to take the center, if it is free.
    if FreeSpace(board, 5):
        return 5

        # Move on one of the sides.
    return chooseRandomMoveFromList(board, [ 2, 4, 6, 8 ])


def isboardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if FreeSpace(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    TheBoard = [ ' ' ] * 10
    playerletter, computerletter = inputPlayerletter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first as player1.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            Gameboard(TheBoard)
            move = getPlayerMove(TheBoard)
            MakeAMove(TheBoard, playerletter, move)

            if isWinner(TheBoard, playerletter):
                Gameboard(TheBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isboardFull(TheBoard):
                    Gameboard(TheBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer’s turn.
            move = getComputerMove(TheBoard, computerletter)
            MakeAMove(TheBoard, computerletter, move)

            if isWinner(TheBoard, computerletter):
                Gameboard(TheBoard)
                print('The computer has beaten you! You lose the game , Try again!.')
                gameIsPlaying = False
            else:
                if isboardFull(TheBoard):
                    Gameboard(TheBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
