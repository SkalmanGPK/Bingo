def check_rows(bingo_board):
    for x in range(0, 5):
        if sum(bingo_board[x]) == 0:
            return True
    return False

def check_columns(bingo_board):
    numbers = []
    for x in range(0, 5):
        numbers.clear()
        for y in range(0, 5):
            numbers.append(bingo_board[y][x])
            if len(numbers) == 5:
                if sum(numbers) == 0:
                    return True
            if sum(numbers) != 0:
                break
    return False

def check_diagonal1(bingo_board):
    numbers = []
    for x in range(0, 5):
        if bingo_board[x][x] == 0:
            numbers.append(bingo_board[x][x])
        if len(numbers) == 5:
            if sum(numbers) == 0:
                return True
        if sum(numbers) > 0:
            break
    return False

def check_diagonal2(bingo_board):
    numbers = []
    x = 4
    for y in range(0, 5):
        if bingo_board[x][y] == 0:
            numbers.append(bingo_board[x][x])
        x -= 1
        if len(numbers) == 5:
            if sum(numbers) == 0:
                return True
        if sum(numbers) > 0:
            break
    return False