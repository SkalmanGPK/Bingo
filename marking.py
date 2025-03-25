def mark_numbers(called_numbers, bingo_board):
    for num in called_numbers:
        for i in range(5):
            for j in range(5):
                if num == bingo_board[i][j]:
                    bingo_board[i][j] = 0 # Will be displayed as X