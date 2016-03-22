import unittest
import FifteenPuzzle


class FifteenPuzzleTests(unittest.TestCase):
    def test_get_matrix_number(self):
        result = FifteenPuzzle.get_matrix_number(4, 2, 2)
        expected = 10
        self.assertEqual(result, expected)
        result = FifteenPuzzle.get_matrix_number(4, 1, 2)
        expected = 6
        self.assertEqual(result, expected)
        result = FifteenPuzzle.get_matrix_number(2, 2, 1)
        expected = 5
        self.assertEqual(result, expected)
        result = FifteenPuzzle.get_matrix_number(2, 1, 1)
        expected = 3
        self.assertEqual(result, expected)
        result = FifteenPuzzle.get_matrix_number(3, 2, 2)
        expected = 8
        self.assertEqual(result, expected)

    def test_lower_row_invariant(self):
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[3, 2, 1],
                                             [6, 5, 4],
                                             [7, 0, 8]])
        result = puzzle.lower_row_invariant(2, 1)
        expected = True
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
