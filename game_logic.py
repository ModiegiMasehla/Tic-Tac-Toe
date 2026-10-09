from ttt import find_line_winner

EMPTY = ""
PLAYERS = ("X", "O")


def new_board():
    """Return a fresh 3x3 board where every cell is empty."""
    return [[EMPTY] * 3 for _ in range(3)]


def validate_board(board):
    """Raise ValueError unless board is 3x3 and holds only "X", "O" or ""."""
    if len(board) != 3:
        raise ValueError("Board must have 3 rows")
    for row in board:
        if len(row) != 3:
            raise ValueError("Each row must have 3 cells")
        for cell in row:
            if cell not in PLAYERS and cell != EMPTY:
                raise ValueError("Invalid cell: " + repr(cell))


def check_game_state(board):
    """
    Work out the state of a game, finished or still in progress.

    :param board: 3x3 list of lists containing "X", "O" or "" (empty).
    :return: "X" or "O" if that player has won, "Draw" if the board is
        full with no winner, or None if the game is still in progress.
    :raises ValueError: if the board is not 3x3 or has an invalid cell.
    """
    validate_board(board)

    winner = find_line_winner(board)
    if winner is not None:
        return winner

    if any(EMPTY in row for row in board):
        return None
    return "Draw"


def parse_coordinate(text):
    """
    Turn user text "1"-"3" into a 0-based index (0-2).

    :raises ValueError: if the text is not a whole number from 1 to 3.
    """
    text = text.strip()
    if not text.isdigit():
        raise ValueError("Please enter a number")
    number = int(text)
    if number < 1 or number > 3:
        raise ValueError("Number must be between 1 and 3")
    return number - 1


def is_cell_empty(board, row, col):
    """Return True if the 0-based cell (row, col) has not been played."""
    return board[row][col] == EMPTY


def other_player(player):
    """Return the player whose turn comes next."""
    return "O" if player == "X" else "X"
