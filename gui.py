import tkinter as tk
import numpy as np
import joblib

model = joblib.load('Data/tictac_model.pkl')

root = tk.Tk()
root.title("Tic Tac Toe - AI vs You")

board = [0] * 9
buttons = []

def check_win(player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for triple in win_states:
        if all(board[i] == player for i in triple):
            return True
    return False

player_score = 0
ai_score = 0
tie_score = 0

def update_scoreboard():
    scoreboard.config(text=f"Score - You: {player_score}  AI: {ai_score}  Ties: {tie_score}")

def reset_board():
    global board
    board = [0] * 9
    for btn in buttons:
        btn['text'] = " "
        btn['state'] = 'normal'
    status.config(text="Your move (X)")

def restart_game():
    global player_score, ai_score, tie_score
    player_score = 0
    ai_score = 0
    tie_score = 0
    update_scoreboard()
    reset_board()

def ai_move():
    global ai_score, tie_score
    probs = model.predict_proba([board])[0]
    for idx in np.argsort(probs)[::-1]:
        if board[idx] == 0:
            board[idx] = -1
            buttons[idx]['text'] = 'O'
            buttons[idx]['state'] = 'disabled'
            if check_win(-1):
                status.config(text="AI wins!")
                ai_score += 1
                update_scoreboard()
                disable_all()
            elif all(cell != 0 for cell in board):
                status.config(text="It's a tie!")
                tie_score += 1
                update_scoreboard()
            break

def click(i):
    global player_score, tie_score
    if board[i] == 0:
        board[i] = 1
        buttons[i]['text'] = 'X'
        buttons[i]['state'] = 'disabled'
        if check_win(1):
            status.config(text="You win!")
            player_score += 1
            update_scoreboard()
            disable_all()
        elif all(cell != 0 for cell in board):
            status.config(text="It's a tie!")
            tie_score += 1
            update_scoreboard()
        else:
            ai_move()

def disable_all():
    for btn in buttons:
        btn['state'] = 'disabled'

for i in range(9):
    btn = tk.Button(root, text=" ", font=('Arial', 32), width=3, height=1,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status = tk.Label(root, text="Your move (X)", font=('Arial', 14))
status.grid(row=3, column=0, columnspan=3)

scoreboard = tk.Label(root, text="Score - You: 0  AI: 0  Ties: 0", font=('Arial', 14))
scoreboard.grid(row=4, column=0, columnspan=3)

reset_btn = tk.Button(root, text="Clear", font=('Arial', 12), command=reset_board)
reset_btn.grid(row=5, column=0, columnspan=1)

restart_btn = tk.Button(root, text="Restart", font=('Arial', 12), command=restart_game)
restart_btn.grid(row=5, column=2, columnspan=1)

root.mainloop()