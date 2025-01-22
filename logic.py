# logic.py

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to check if the current player has won
def check_winner(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):  # Check rows
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2-i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to get the available moves on the board
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    if check_winner(board, PLAYER_X):
        return -1  # Player X wins
    if check_winner(board, PLAYER_O):
        return 1  # Player O wins
    if is_board_full(board):  # Board full
        return 0

    if maximizing_player:  # AI's turn
        best_score = -float("inf")
        for i, j in get_available_moves(board):
            board[i][j] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:  # Human's turn
        best_score = float("inf")
        for i, j in get_available_moves(board):
            board[i][j] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            best_score = min(score, best_score)
        return best_score

# Function to determine the best move for the AI
def best_move(board):
    best_score = -float("inf")
    move = None
    for i, j in get_available_moves(board):
        board[i][j] = PLAYER_O
        score = minimax(board, 0, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move
