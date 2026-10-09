import ttt
import unittest


class TestTTT(unittest.TestCase):
    def test_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]

        self.assertEqual(ttt.find_winner(board), None)

    def test_winner_row(self):
        board = [
            ['X', 'X', 'X'],
            ['O', 'O', 'X'],
            ['O', 'X', 'O']
        ]

        self.assertEqual(ttt.find_winner(board), 'X')

    def test_winner_col(self):
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['X', 'X', 'O']
        ]

        self.assertEqual(ttt.find_winner(board), 'X')

    def test_winner_diag(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'X']
        ]

        self.assertEqual(ttt.find_winner(board), 'X')

    def test_winner_diag2(self):
        board = [
            ['O', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O']
        ]

        self.assertEqual(ttt.find_winner(board), 'O')
    
    def test_invalid_board_shape(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O']
        ]

        with self.assertRaises(ValueError):
            ttt.find_winner(board)
    
    def test_invalid_board_shape2(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X']
        ]

        with self.assertRaises(ValueError):
            ttt.find_winner(board)
    
    def test_invalid_board_empty_space(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', '']
        ]

        with self.assertRaises(ValueError):
            ttt.find_winner(board)
    
    def test_invalid_board_unknown_player(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'Z']
        ]

        with self.assertRaises(ValueError):
            ttt.find_winner(board)
    
    def test_has_docstring(self):
        self.assertIsNotNone(ttt.find_winner.__doc__)


if __name__=="__main__":
    unittest.main()
