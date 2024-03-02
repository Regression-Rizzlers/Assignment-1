import random

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
            ai_move = random.choice(available_moves)
            make_move('O', ai_move)

# Start the game
play_game()