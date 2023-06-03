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
    """
    Returns player who has the next turn on a board.
    """
    x_count = board[0].count(X) + board[1].count(X) + board[2].count(X)
    O_count = board[0].count(O) + board[1].count(O) + board[2].count(O)
    if x_count == O_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                action.append((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                board_copy[i][j] = X
            elif (board[i][j] == O):
                board_copy[i][j] = O
    if (action[0] not in range(3) or action[1] not in range(3)):
        raise NameError("Invalid Move")
    if (board[action[0]][action[1]] != EMPTY):
        raise NameError("Invalid Move")
    board_copy[action[0]][action[1]] = player(board)
    return board_copy
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        # Row Check
        if (board[i][0] == X and board[i][1] == X and board[i][2] == X):
            return X
        elif (board[i][0] == O and board[i][1] == O and board[i][2] == O):
            return O
        # Column Check
        elif (board[0][i] == X and board[1][i] == X and board[2][i] == X):
            return X
        elif (board[0][i] == O and board[1][i] == O and board[2][i] == O):
            return O
    # Diagonal Check
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O):
        return O
    elif (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    elif (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X or winner(board) == O):
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -100
    for move in actions(board):
        temp = min_value(result(board, move))
        if temp > v:
            v = temp
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 100
    for move in actions(board):
        temp = max_value(result(board, move))
        if temp < v:
            v = temp
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:  # MAX player
        v = -100
        optimal = None
        for move in actions(board):
            temp = min_value(result(board, move))
            if (temp > v):
                v = temp
                optimal = move
        return optimal
    elif player(board) == O:  # MIN player
        v = 100
        optimal = None
        for move in actions(board):
            temp = max_value(result(board, move))
            if (temp < v):
                v = temp
                optimal = move
        return optimal
    