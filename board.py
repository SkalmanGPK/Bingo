import random

def create_board():
    bingo_board = [[], [], [], [], []]
    numbers = []
    for x in range(1, 26):
        numbers.append(x)
        random.shuffle(numbers)
    for y in range(0, 5):
        while True:
            bingo_board[y].append(numbers[0])
            numbers.append(0)
            numbers.pop(0)
            if len(bingo_board[y]) > 4:
                break
    return bingo_board