import tkinter as tk
from generator import generate_full_board, remove_numbers
from ui import SudokuUI

def main():
    root = tk.Tk()
    root.title("Sudoku Game")

    solution = generate_full_board()
    puzzle = [row[:] for row in solution]
    puzzle = remove_numbers(puzzle, 30)

    ui = SudokuUI(root, puzzle, solution)

    tk.Button(root, text="Solve", command=ui.solve_board).grid(row=10, column=0, columnspan=3)
    tk.Button(root, text="Check", command=ui.check_solution).grid(row=10, column=3, columnspan=3)
    tk.Button(root, text="Hint", command=ui.give_hint).grid(row=10, column=6, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()