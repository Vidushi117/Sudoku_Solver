import random
from validator import is_valid

def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)

                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if fill_board(board):
                            return True

                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    board = [[0]*9 for _ in range(9)]
    fill_board(board)
    return board

def remove_numbers(board, attempts=30):
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if board[row][col] != 0:
            board[row][col] = 0
            attempts -= 1

    return board