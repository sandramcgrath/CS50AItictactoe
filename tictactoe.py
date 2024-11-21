"""
Tic Tac Toe Player
"""

import math
import copy
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
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    empty_count = sum(row.count(EMPTY) for row in board)
    
    if empty_count == 0:
        return X
    elif x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_positions = set()
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empty_positions.add((i, j))
    
    return empty_positions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i,j = action

    if board[i][j] is not EMPTY:
        raise ValueError("Impossible move")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O    
        
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # There is a winner
    if winner(board) is not None:
        return True
    
    # There are still empty cells
    for row in board:
        if EMPTY in row:
            return False
    
    # Game finished
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    #Game is finished
    if terminal(board):
        return None

    player_turn = player(board)

    if player_turn == X:
        util_value, best_move = max_value(board)
    else:
        util_value, best_move = min_value(board)

    return best_move

def max_value(board):

    #Game is finished
    if terminal(board):
        return utility(board), None

    #best value initialized to negative infinity
    v = float('-inf')
    best_move = None

    for action in actions(board):

        #Board value after best move from adversary
        min_val, _ = min_value(result(board, action))

        #Update best move if we found one
        if min_val > v:
            v = min_val
            best_move = action

    return v, best_move

def min_value(board):

    #Game is finished
    if terminal(board):
        return utility(board), None

    #Best value initialized to positive infinity
    v = float('inf')
    best_move = None

    for action in actions(board):

        #Value after adversary best move
        max_val, _ = max_value(result(board, action))

        #Update best move if we found one
        if max_val < v:
            v = max_val
            best_move = action

    return v, best_move
