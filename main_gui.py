# main_gui.py

import tkinter as tk
from tkinter import messagebox
from logic import PLAYER_X, PLAYER_O, EMPTY, check_winner, is_board_full, best_move

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, row, col):
        if self.board[row][col] == EMPTY:
            # Human move
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if check_winner(self.board, self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
                return
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return

            # Switch to AI move
            self.current_player = PLAYER_O
            self.ai_move()

    def ai_move(self):
        move = best_move(self.board)
        if move:
            row, col = move
            self.board[row][col] = PLAYER_O
            self.buttons[row][col].config(text=PLAYER_O)

            if check_winner(self.board, PLAYER_O):
                messagebox.showinfo("Game Over", f"Player {PLAYER_O} wins!")
                self.reset_game()
                return
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return

        self.current_player = PLAYER_X

    def reset_game(self):
        self.board = [[EMPTY] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = PLAYER_X

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
