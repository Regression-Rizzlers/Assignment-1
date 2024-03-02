import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor

# Create the Tic Tac Toe board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        print('-------------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to make a move
def make_move(player, position):
    board[position] = player

# Function to get the available moves
def get_available_moves():
    return [i for i, x in enumerate(board) if x == ' ']

# Model-based AI for the 'O' player
def ai_move(board):
    X = np.array([[board.count('X'), board.count('O'), board.count(' '), 
                  board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]]])
    return model.predict(X)[0]

# Function to play the game
def play_game():
    while True:
        print_board()
        if check_win('X'):
            print('You win!')
            break
        if check_win('O'):
            print('You lose!')
            break
        if ' ' not in board:
            print('It\'s a tie!')
            break
        position = int(input('Enter your move (1-9): ')) - 1
        make_move('X', position)
        available_moves = get_available_moves()
        if available_moves:
            ai_move_index = ai_move(board)
            make_move('O', ai_move_index)

# Load the trained model
def load_model():
    return model

# Start the game
model = load_model()
play_game()