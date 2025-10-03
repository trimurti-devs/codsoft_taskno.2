import tkinter as tk
from tkinter import messagebox
import math
board_state = [" " for _ in range(9)]
turn = "X"
def check_winner(p):
    combos = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for combo in combos:
        if all(board_state[i] == p for i in combo):
            return True
    return False

def board_full():
    return " " not in board_state

def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if board_full():
        return 0
    if is_max:
        best_val = -math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "O"
                val = minimax(False)
                board_state[i] = " "
                best_val = max(best_val, val)
        return best_val
    else:
        best_val = math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "X"
                val = minimax(True)
                board_state[i] = " "
                best_val = min(best_val, val)
        return best_val

def find_best_move():
    best_val = -math.inf
    move_index = None
    for i in range(9):
        if board_state[i] == " ":
            board_state[i] = "O"
            val = minimax(False)
            board_state[i] = " "
            if val > best_val:
                best_val = val
                move_index = i
    return move_index

def place_mark(idx, player):
    if board_state[idx] == " ":
        board_state[idx] = player
        buttons[idx].config(text=player, state="disabled")

        if check_winner(player):
            messagebox.showinfo(
                "Game Over",
                f"Player {player} takes the win!"
            )
            reset_board()
        elif board_full():
            messagebox.showinfo("Game Over", "It's a draw this time!")
            reset_board()
        return True
    return False

def human_turn(idx):
    if place_mark(idx, "X"):
        ai_turn()

def ai_turn():
    move = find_best_move()
    if move is not None:
        place_mark(move, "O")

def reset_board():
    global board_state
    board_state = [" " for _ in range(9)]
    for b in buttons:
        b.config(text=" ", state="normal")

root = tk.Tk()
root.title("Tic Tac Toe (AI)")

buttons = []
for pos in range(9):
    btn = tk.Button(
        root,
        text=" ",
        font=("Arial", 20),
        width=5, height=2,
        command=lambda pos=pos: human_turn(pos)
    )
    btn.grid(row=pos//3, column=pos%3)
    buttons.append(btn)
restart_btn = tk.Button(root, text="Restart", font=("Arial", 14),
                        command=reset_board)
restart_btn.grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()
