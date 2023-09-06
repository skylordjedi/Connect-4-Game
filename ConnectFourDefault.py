import numpy as np
import sys

# Board Dimensions
columns = 7
rows = 6

# Create the Board
def create_board():
    default_board = np.full((rows,columns), "[ ]")
    return default_board


def print_board(board):
    for row in board:
        # Use f-strings to format each element with a width of 5 characters
        formatted_row = [f"{cell: ^5}" for cell in row]
        print(" ".join(formatted_row))
    print()

board = create_board()


# Dropping a Piece
def dropPiece(column, sign):
    for i in range(board.shape[1]):
        # To start the inputs at the bottom of the array
        if board[5 - i, column] == "[ ]":
            board[5 - i, column] = sign
            return True
    return False
    
    return board

# Winning Conditions

def winning_move(board, piece):
    # Check horizontal locations for win
    for r in range(rows):
        for c in range(columns - 3):
            if board[r, c] == piece and board[r, c + 1] == piece and board[r, c + 2] == piece and board[r, c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(columns):
        for r in range(rows - 3):
            if board[r, c] == piece and board[r + 1, c] == piece and board[r + 2, c] == piece and board[r + 3, c] == piece:
                return True

    # Check positively sloped diagonals
    for r in range(rows - 3):
        for c in range(columns - 3):
            if board[r, c] == piece and board[r + 1, c + 1] == piece and board[r + 2, c + 2] == piece and board[r + 3, c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for r in range(3, rows):
        for c in range(columns - 3):
            if board[r, c] == piece and board[r - 1, c + 1] == piece and board[r - 2, c + 2] == piece and board[r - 3, c + 3] == piece:
                return True

    return False

# Playing The Game

# Initialise Game Conditions
gameover = False
turn = 0 

# Display Empty Starting Board
print_board(board)

# Starting the Turns
while gameover == False:

    if turn == 0:
        play = int(input("Player 1 Choose a column 0 - 6: "))
        if play < columns:
            if dropPiece(play, 1):
                turn += 1 
                turn = turn % 2 # To alternate between the two players turn but if a wrong input is used, turn will not update
                if winning_move(board, str(1)):
                    print("Player 1 Wins")
                    gameover = True
                    break
            else:
                print("Column Full Try Again")
        else:
            print("Column Input Exceeds Board Limit")

    
    
    elif turn == 1:
        play = int(input("Player 2 Choose a column 0 - 6: "))
        if play < columns:
            if dropPiece(play, 2):
                turn += 1
                turn = turn % 2 # To alternate between the two players turn but if a wrong input is used, turn will not updatef
                if winning_move(board, str(2)):
                    print("Player 2 Wins")
                    gameover = True
                    break
            else:
                print("Column Full Try Again")
        else:
            print("Column Input Exceeds Board Limit")

    
    elif np.all(board != "[ ]"):
                print_board(board)
                print("It's a Draw!")
                gameover = True


    print_board(board)

print_board(board)
if gameover == True:
    sys.exit()
