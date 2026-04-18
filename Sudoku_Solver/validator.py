def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True