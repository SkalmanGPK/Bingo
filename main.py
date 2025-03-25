import copy
from board import create_board
from input_numbers import generate_numbers
from marking import mark_numbers
from checking import check_rows, check_columns, check_diagonal1, check_diagonal2

def display_board(board, marked_board):
    print("\nCurrent Bingo Board:")
    for i in range(5):
        row_display = []
        for j in range(5):
            if marked_board[i][j] == 0:
                row_display.append(" X")
            else:
                row_display.append(f"{board[i][j]:2}")
        print(" ".join(row_display))

def main():
    attempts = 0
    while True:
        bingo = False    
        original_board = create_board()
        marked_board = copy.deepcopy(original_board)
        called_numbers = generate_numbers()
        mark_numbers(called_numbers, marked_board)
        
        bingo = (check_rows(marked_board) or 
                check_columns(marked_board) or 
                check_diagonal1(marked_board) or 
                check_diagonal2(marked_board))
        
        attempts += 1
        if bingo:
            print("\n=== BINGO! ===")
            print(f"It took {attempts} attempts\n")
            
            print("Original Board:")
            for row in original_board:
                print(" ".join(f"{num:2}" for num in row))
            
            print("\nMarked Board (X = matched):")
            display_board(original_board, marked_board)
            
            print(f"\nNumbers called: {sorted(called_numbers)}")
            break

if __name__ == "__main__":
    main()