import tkinter as tk

from tkinter import messagebox   

class NoughtsandCrosses:
    def __init__(self, master): 
        self.master = master
        self.master.title("Noughts and Crosses")

        self.board = [""] * 9

        self.current_player = "X"
        

        self.buttons = []

        for i in range(3):

            row = []

            for j in range(3):

                button = tk.Button(master, text="", font=("Helvetica", 20), width=8, height=4,

                                   command=lambda i=i, j=j: self.on_button_click(i, j))

                button.grid(row=i, column=j)

                row.append(button)

            self.buttons.append(row)


    def on_button_click(self, row, col):

        if self.board[row * 3 + col] == "" and not self.check_winner():

            self.board[row * 3 + col] = self.current_player

            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)


            if self.check_winner():

                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")

                self.reset_game()

            elif "" not in self.board:

                messagebox.showinfo("Game Over", "It's a tie!")

                self.reset_game()

            else:

                self.current_player = "O" if self.current_player == "X" else "X"


    def check_winner(self):

        # Check rows, columns, and diagonals for a win

        for i in range(3):

            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":

                return True

            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":

                return True


        if self.board[0] == self.board[4] == self.board[8] != "":

            return True

        if self.board[2] == self.board[4] == self.board[6] != "":

            return True


        return False


    def reset_game(self):

        self.board = [""] * 9

        for i in range(3):

            for j in range(3):

                self.buttons[i][j].config(text="", state=tk.NORMAL)

        self.current_player = "X"


if __name__ == "__main__":

    root = tk.Tk()
 
    game = NoughtsandCrosses(root)

    root.mainloop()