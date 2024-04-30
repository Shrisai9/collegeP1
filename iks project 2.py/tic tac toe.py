import tkinter as tk
from tkinter import messagebox

def print_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text=board[i][j], font=('Arial', 24), width=5, height=2,
                               command=lambda i=i, j=j: on_button_click(i, j))
            button.grid(row=i, column=j)
            buttons[i][j] = button

def on_button_click(row, col):
    global current_player

    if board[row][col] == ' ':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            root.quit()
        elif is_board_full():
            messagebox.showinfo("Draw", "It's a draw!")
            root.quit()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        messagebox.showerror("Error", "Cell already taken. Try again.")

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def is_board_full():
    for row in board:
        if ' ' in row:
            return False
    return True

board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

root = tk.Tk()
root.title("Tic-Tac-Toe")
buttons = [[None]*3 for _ in range(3)]

print_board()

root.mainloop()
