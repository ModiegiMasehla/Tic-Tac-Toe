import unittest

import game_logic
import ttt


WIN_LINES = {
    "row 1": [(0, 0), (0, 1), (0, 2)],
    "row 2": [(1, 0), (1, 1), (1, 2)],
    "row 3": [(2, 0), (2, 1), (2, 2)],
    "column 1": [(0, 0), (1, 0), (2, 0)],
    "column 2": [(0, 1), (1, 1), (2, 1)],
    "column 3": [(0, 2), (1, 2), (2, 2)],
    "diagonal": [(0, 0), (1, 1), (2, 2)],
    "anti-diagonal": [(0, 2), (1, 1), (2, 0)],
}


def board_with_line(player, cells):
    board = game_logic.new_board()
    for row, col in cells:
        board[row][col] = player
    return board


class TestCheckGameState(unittest.TestCase):
    def test_every_winning_line_for_both_players(self):
        for player in ("X", "O"):
            for name, cells in WIN_LINES.items():
                with self.subTest(player=player, line=name):
                    board = board_with_line(player, cells)
                    self.assertEqual(game_logic.check_game_state(board), player)

    def test_draw(self):
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]

        self.assertEqual(game_logic.check_game_state(board), "Draw")

    def test_win_on_full_board_is_not_a_draw(self):
        board = [
            ['X', 'X', 'X'],
            ['O', 'O', 'X'],
            ['O', 'X', 'O']
        ]

        self.assertEqual(game_logic.check_game_state(board), "X")

    def test_in_progress(self):
        board = [
            ['X', 'O', ''],
            ['', 'X', ''],
            ['', '', 'O']
        ]

        self.assertIsNone(game_logic.check_game_state(board))

    def test_empty_board_is_in_progress(self):
        self.assertIsNone(game_logic.check_game_state(game_logic.new_board()))

    def test_invalid_board_shape(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O']
        ]

        with self.assertRaises(ValueError):
            game_logic.check_game_state(board)

    def test_invalid_row_length(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X']
        ]

        with self.assertRaises(ValueError):
            game_logic.check_game_state(board)

    def test_invalid_cell_value(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'Z']
        ]

        with self.assertRaises(ValueError):
            game_logic.check_game_state(board)

    def test_find_winner_still_rejects_empty_cells(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', '']
        ]

        with self.assertRaises(ValueError):
            ttt.find_winner(board)


class TestFindWinnerAntiDiagonalFix(unittest.TestCase):
    def test_anti_diagonal_winner_differs_from_top_left(self):
        board = [
            ['O', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'X', 'O']
        ]

        self.assertEqual(ttt.find_winner(board), 'X')

    def test_no_false_anti_diagonal_win(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'X', 'O']
        ]

        self.assertIsNone(ttt.find_winner(board))


class TestMoveValidation(unittest.TestCase):
    def test_parse_valid_coordinates(self):
        self.assertEqual(game_logic.parse_coordinate("1"), 0)
        self.assertEqual(game_logic.parse_coordinate("2"), 1)
        self.assertEqual(game_logic.parse_coordinate("3"), 2)

    def test_parse_ignores_spaces(self):
        self.assertEqual(game_logic.parse_coordinate(" 2 "), 1)

    def test_parse_rejects_non_numbers(self):
        for text in ("abc", "", "  ", "1.5", "-1", "two"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    game_logic.parse_coordinate(text)

    def test_parse_rejects_out_of_range(self):
        for text in ("0", "4", "10"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    game_logic.parse_coordinate(text)

    def test_is_cell_empty(self):
        board = game_logic.new_board()
        board[1][1] = "X"

        self.assertTrue(game_logic.is_cell_empty(board, 0, 0))
        self.assertFalse(game_logic.is_cell_empty(board, 1, 1))

    def test_other_player(self):
        self.assertEqual(game_logic.other_player("X"), "O")
        self.assertEqual(game_logic.other_player("O"), "X")


if __name__ == "__main__":
    unittest.main()
