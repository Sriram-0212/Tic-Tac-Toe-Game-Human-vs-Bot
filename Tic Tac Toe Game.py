import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def get_human_move(player):
    while True:
        move = input(f"Player {player}, enter your move (row[1-3] column[1-3]): ")
        if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
            print("Invalid input. Please enter row and column numbers (e.g., 1 2)")
            continue
        row, col = int(move[0]) - 1, int(move[1]) - 1
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Row and column numbers should be between 1 and 3")
            continue
        return row, col

def get_bot_move(board, bot_symbol):
    # Check if the bot can win in the next move
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = bot_symbol
                if check_winner(board) == bot_symbol:
                    board[i][j] = ' '
                    return i, j
                board[i][j] = ' '

    # Check if the opponent can win in the next move and block them
    opponent_symbol = 'O' if bot_symbol == 'X' else 'X'
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = opponent_symbol
                if check_winner(board) == opponent_symbol:
                    board[i][j] = ' '
                    return i, j
                board[i][j] = ' '

    # Otherwise, make a random move
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        if current_player == 'X':
            row, col = get_human_move(current_player)
        else:
            row, col = get_bot_move(board, current_player)
            print(f"Bot moves to ({row + 1}, {col + 1})")
        if board[row][col] != ' ':
            print("That cell is already taken. Try again.")
            continue
        board[row][col] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            if current_player == 'X':
                print(f"Player {winner} wins!")
            else:
                print("Bot wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
