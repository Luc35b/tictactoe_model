import numpy as np
import random

WINNING_TRIPLETS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def check_winner(board, player):
    for line in WINNING_TRIPLETS:
        if sum(board[i] == player for i in line) == 3:
            return True
    return False

def find_best_move(board, player):
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            if check_winner(board, player):
                board[i] = 0
                return i
            board[i] = 0
    for i in range(9):
        if board[i] == 0:
            board[i] = -player
            if check_winner(board, -player):
                board[i] = 0
                return i
            board[i] = 0
    empty = [i for i, val in enumerate(board) if val == 0]
    return random.choice(empty) if empty else -1

samples = []
for _ in range(10000):
    board = [0] * 9
    moves = random.randint(1, 5)
    player_turn = 1
    for _ in range(moves):
        empty_cells = [i for i, val in enumerate(board) if val == 0]
        if not empty_cells: break
        move = random.choice(empty_cells)
        board[move] = player_turn
        player_turn *= -1
    if board.count(0) == 0:
        continue
    best_move = find_best_move(board, -1)
    if best_move == -1: continue
    samples.append(board + [best_move])

np.savetxt('tictac_single.txt', samples, fmt='%d')
print("Saved tictac_single.txt with", len(samples), "samples.")