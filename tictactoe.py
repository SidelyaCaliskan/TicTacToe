"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_X = sum([row.count('X') for row in board])
    count_O = sum([row.count('O') for row in board])

    if count_X > count_O:
        return 'O'
    else:
        return 'X'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    # Check rows
    for row in board:
        if row == ['X', 'X', 'X']:
            return 'X'
        elif row == ['O', 'O', 'O']:
            return 'O'

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 'X'
            elif board[0][col] == 'O':
                return 'O'

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 'X'
        elif board[0][0] == 'O':
            return 'O'
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 'X'
        elif board[0][2] == 'O':
            return 'O'

    # If no winner, return None
    return None



def terminal(board):
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if all cells are filled
    for row in board:
        if EMPTY in row:
            return False

    # If there is no winner and all cells are filled, the game is a tie
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner_player = winner(board)
    if winner_player == 'X':
        return 1
    elif winner_player == 'O':
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    Player = player(board)

    if player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)

    return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_move = None

    for move in actions(board):
        min_val, _ = min_value(result(board, move))

        if min_val > v:
            v = min_val
            best_move = move

        if v == 1:
            break

    return v, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_move = None

    for move in actions(board):
        max_val, _ = max_value(result(board, move))

        if max_val < v:
            v = max_val
            best_move = move

        if v == -1:
            break

    return v, best_move
