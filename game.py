from game_logic import (
    check_game_state,
    is_cell_empty,
    new_board,
    other_player,
    parse_coordinate,
)


def render_board(board):
    """Return the board as text with row and column numbers."""
    lines = ["    1   2   3"]
    for number, row in enumerate(board, start=1):
        cells = " | ".join(cell or " " for cell in row)
        lines.append(f"{number}   {cells}")
        if number < 3:
            lines.append("   ---+---+---")
    return "\n".join(lines)


def ask_coordinate(label):
    """Keep asking until the player enters a valid 1-3 number."""
    while True:
        try:
            return parse_coordinate(input(f"{label} (1-3): "))
        except ValueError as error:
            print(error)


def ask_move(board, player):
    """Keep asking until the player picks an empty cell. Returns (row, col)."""
    while True:
        print(f"Player {player}, your move.")
        row = ask_coordinate("Row")
        col = ask_coordinate("Column")
        if is_cell_empty(board, row, col):
            return row, col
        print("That cell is already taken, try again.")


def play_round():
    """Play one full game and announce the result."""
    board = new_board()
    player = "X"

    while True:
        print()
        print(render_board(board))
        row, col = ask_move(board, player)
        board[row][col] = player

        state = check_game_state(board)
        if state is not None:
            break
        player = other_player(player)

    print()
    print(render_board(board))
    if state == "Draw":
        print("It's a draw!")
    else:
        print(f"Player {state} wins!")


def ask_play_again():
    """Return True if the player answers yes to another game."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        play_round()
        if not ask_play_again():
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame ended. Goodbye!")
