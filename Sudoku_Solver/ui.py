import tkinter as tk
from tkinter import messagebox
import random

class SudokuUI:
    def __init__(self, root, puzzle, solution):
        self.root = root
        self.puzzle = puzzle
        self.solution = solution
        self.cells = [[None]*9 for _ in range(9)]
        self.attempts_left = 5

        self.draw_board()

    def draw_board(self):
        for row in range(9):
            for col in range(9):

                frame = tk.Frame(self.root, highlightbackground="black")
                frame.grid(row=row, column=col)

                entry = tk.Entry(frame, width=2, font=("Arial", 20),
                                 justify='center', bd=1, relief="solid")

                if self.puzzle[row][col] != 0:
                    entry.insert(0, str(self.puzzle[row][col]))
                    entry.config(state='disabled')

                entry.grid(row=0, column=0, ipadx=8, ipady=8)

                if row % 3 == 0:
                    frame.config(highlightthickness=3)
                if col % 3 == 0:
                    frame.config(highlightthickness=3)

                entry.bind("<KeyRelease>", lambda e, r=row, c=col: self.validate_input(r, c))

                self.cells[row][col] = entry

    def get_board(self):
        board = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                if val.isdigit():
                    board[i][j] = int(val)
        return board

    def validate_input(self, row, col):
        val = self.cells[row][col].get()

        if not val.isdigit() or int(val) not in range(1, 10):
            self.cells[row][col].delete(0, tk.END)
            return

        num = int(val)

        # simple duplicate check
        for i in range(9):
            if i != col and self.get_board()[row][i] == num:
                self.cells[row][col].config(bg="red")
                return
            if i != row and self.get_board()[i][col] == num:
                self.cells[row][col].config(bg="red")
                return

        self.cells[row][col].config(bg="white")

    def check_solution(self):
        user = self.get_board()
        correct = True

        for i in range(9):
            for j in range(9):
                if user[i][j] != self.solution[i][j]:
                    self.cells[i][j].config(bg="red")
                    correct = False

        if correct:
            messagebox.showinfo("Sudoku", "🎉 Correct!")
        else:
            self.attempts_left -= 1
            messagebox.showwarning("Wrong", f"Attempts left: {self.attempts_left}")

    def give_hint(self):
        empty = [(i, j) for i in range(9) for j in range(9)
                 if self.cells[i][j]['state'] == 'normal' and self.cells[i][j].get() == ""]

        if not empty:
            return

        r, c = random.choice(empty)
        self.cells[r][c].insert(0, str(self.solution[r][c]))

    def solve_board(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j]['state'] == 'normal':
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(self.solution[i][j]))