import random

def generate_numbers():
    called_numbers = []
    while True:
        num = random.randint(1, 25)
        if num not in called_numbers:
            called_numbers.append(num)
        if len(called_numbers) == 13:
            break
    return called_numbers