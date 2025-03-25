# Bingo simulator

A python simulation that demonstrates optimal bingo winning conditions with minimal called numbers.

## Features

- generates random 5x5 bingo boards
- Simulatues number calling with optimal pattern detection
- **Proves mathematically** that 14 numbers is the minimum needed for:
    - Full row
    - Full column
    - Both diagonals
   - Visualizes winning patterns clearly with "X" markers


## Mathematical insight

Demonstrates the rare scenario where:

 X  X  X  X  X
 6  X  2  X 15
 4  X  X 21 25
 5  X 14  X 17
 X  X 19  3  X

- Row complete (5 numbers)
- Column complete (5)
- Both diagonals complete (9 positions with overlaps)
- **Total called numbers: 14** (theoretical minimum)

## Installation

```bash
git clone https://github.com/SkalmanGPK/bingo
cd bingo
pip install -r requirements.txt

Usage

python main.py
Sample output:

=== BINGO! ===
Winning with just 12 numbers!

Original Board:
 5 17 23  1 12
10 21  3 18  8
15 25  7 14 20
 2  9  6 16 24
 4 13 22 11 19

Marked Board:
 X  X  X  X  X
10  X  3  X  8
 X  X  X 14  X
 X  X  X 16  X
 X  X 22  X  X

Project Structure

bingo_game/
├── main.py            # Main game logic
├── board.py           # Board generation
├── input_numbers.py   # Optimal number selection
├── marking.py         # Pattern marking
└── checking.py        # Win condition verification

Contributing
Pull requests welcome! For major changes, please open an issue first.

License
MIT