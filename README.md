# Tic-Tac-Toe

A beginner-friendly Python Tic-Tac-Toe project. It started as a "find the winner" exercise and now includes game-state detection (win, draw, in progress) and a playable two-player terminal game.

## Features

- `find_winner(board)` determines the winner of a finished, fully filled board
- `check_game_state(board)` handles games in progress and detects wins and draws
- Two-player terminal game with a numbered board, alternating turns (X goes first) and a play-again prompt
- Input validation: non-numbers, out-of-range values and occupied cells are re-prompted instead of crashing
- Unit tests written with the standard library `unittest` module

## Requirements

- Python 3.8 or newer
- No third-party packages

## Playing the game

```
python game.py
```

Enter a row and a column (1-3) when prompted. Rows are numbered down the left side and columns across the top:

```
    1   2   3
1   X | O |  
   ---+---+---
2     | X |  
   ---+---+---
3     |   | O

Player X, your move.
Row (1-3):
```

The game ends when a player gets three in a row, column or diagonal, or when the board fills up with no winner (a draw).

## Running the tests

```
python -m unittest discover
```

## Project structure

```
.
├── ttt.py                  # find_winner and the shared win-line logic
├── game_logic.py           # check_game_state, move validation, board helpers
├── game.py                 # the terminal game (run this one)
└── tests/
    ├── test_ttt.py         # tests for find_winner
    └── test_game_logic.py  # tests for game state, validation and win lines
```

## How it works

### `find_winner(board)`

Takes a 3x3 board of `"X"` and `"O"` and returns `"X"`, `"O"` or `None`. It raises `ValueError` if the board is not 3x3, contains an unknown value, or contains empty cells (`""`), so it cannot be used on a game in progress.

### `check_game_state(board)`

Accepts boards with empty cells and returns:

| Result   | Meaning                                  |
|----------|------------------------------------------|
| `"X"`    | X has three in a line                    |
| `"O"`    | O has three in a line                    |
| `"Draw"` | The board is full and nobody has won     |
| `None`   | The game is still in progress            |

It raises `ValueError` for a malformed board. Both functions share `find_line_winner` in `ttt.py`, so the win-line logic exists in one place.

### Boards

A board is a list of three rows, each a list of three cells:

```python
board = [
    ["X", "O", ""],
    ["",  "X", ""],
    ["",  "",  "O"],
]
```

Each cell is `"X"`, `"O"`, or `""` for an empty cell (empty cells are only accepted by `check_game_state`).

## Example

```python
from game_logic import check_game_state
from ttt import find_winner

check_game_state([["X", "X", "X"], ["O", "O", ""], ["", "", ""]])  # "X"
check_game_state([["X", "O", ""], ["", "X", ""], ["", "", "O"]])   # None

find_winner([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])   # None
```