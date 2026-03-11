import tkinter as tk
import random

# Window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

# Game variables
board = [""] * 9
buttons = []

player = "X"
computer = "O"

# Check winner
def check_winner(symbol):
    win_pos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in win_pos:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False


def check_draw():
    return "" not in board


def reset_game():
    global board
    board = [""] * 9
    for b in buttons:
        b.config(text="")


def computer_move():
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = computer
        buttons[move].config(text=computer)

        if check_winner(computer):
            status.config(text="Computer Wins!")
            root.after(2000, reset_game)

        elif check_draw():
            status.config(text="Draw!")
            root.after(2000, reset_game)


def click(i):
    if board[i] == "":
        board[i] = player
        buttons[i].config(text=player)

        if check_winner(player):
            status.config(text="You Win!")
            root.after(2000, reset_game)
            return

        if check_draw():
            status.config(text="Draw!")
            root.after(2000, reset_game)
            return

        computer_move()


# Create board buttons
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status = tk.Label(root, text="Your Turn (X)", font=("Arial", 14))
status.pack(pady=10)

reset = tk.Button(root, text="Restart", command=reset_game)
reset.pack()

root.mainloop()