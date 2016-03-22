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

    def test_solve_interior_tile(self):
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[4, 13, 1, 3],
                                             [5, 10, 2, 7],
                                             [8, 12, 6, 11],
                                             [9, 0, 14, 15]])
        result = puzzle.solve_interior_tile(3, 1)

        expected = "uuu" + "lddru" + "lddruld"
        self.assertEqual(result, expected)

    def test_solve_col0_tile(self):
        puzzle = FifteenPuzzle.Puzzle(3, 2, [[2, 4],
                                             [3, 1],
                                             [0, 5]])
        result = puzzle.solve_col0_tile(2)

        expected = "uruld" + "ruldrdlurdluurddlur"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
