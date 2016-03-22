import unittest
import FifteenPuzzle


class FifteenPuzzleTests(unittest.TestCase):
    def test_get_matrix_number(self):
        result = FifteenPuzzle.get_matrix_number(4, 2, 2)
        expected = 10
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        result = FifteenPuzzle.get_matrix_number(4, 1, 2)
        expected = 6
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        result = FifteenPuzzle.get_matrix_number(2, 2, 1)
        expected = 5
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        result = FifteenPuzzle.get_matrix_number(2, 1, 1)
        expected = 3
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
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

    def test_row0_invariant(self):
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[2, 0, 1],
                                             [3, 4, 5],
                                             [6, 7, 8]])
        result = puzzle.row0_invariant(1)
        expected = False
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        self.assertIs(type(result), bool)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[1, 0, 3, 2],
                                             [4, 5, 6, 7],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.row0_invariant(1)
        expected = False
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[1, 0, 2],
                                             [3, 4, 5],
                                             [6, 7, 8]])
        result = puzzle.row0_invariant(1)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[1, 0, 2, 3],
                                             [4, 5, 6, 7],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.row0_invariant(1)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[1, 2, 3, 4, 0],
                                             [5, 6, 7, 8, 9],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.row0_invariant(4)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[2, 4, 1, 0, 3],
                                             [5, 6, 7, 8, 9],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.row0_invariant(3)
        expected = False
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[4, 2, 0, 3],
                                             [5, 1, 6, 7],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.row0_invariant(2)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 5, [[15, 16, 0, 3, 4],
                                             [5, 6, 7, 8, 9],
                                             [10, 11, 12, 13, 14],
                                             [1, 2, 17, 18, 19]])
        result = puzzle.row0_invariant(2)
        expected = False
        self.assertEqual(result, expected)

    def test_row1_invariant(self):
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[2, 3, 4],
                                             [1, 0, 5],
                                             [6, 7, 8]])
        result = puzzle.row1_invariant(1)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        self.assertIs(type(puzzle.row1_invariant(1)), bool)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[4, 3, 2],
                                             [1, 0, 5],
                                             [6, 7, 8]])
        result = puzzle.row1_invariant(1)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[2, 3, 4],
                                             [5, 1, 0],
                                             [6, 7, 8]])
        result = puzzle.row1_invariant(2)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[1, 3, 4, 2],
                                             [0, 6, 5, 7],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.row1_invariant(0)
        expected = False
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[1, 2, 3, 4, 5],
                                             [8, 9, 0, 6, 7],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.row1_invariant(2)
        expected = False
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[1, 5, 2, 3, 4],
                                             [7, 6, 0, 8, 9],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.row1_invariant(2)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[1, 2, 3, 4, 5],
                                             [6, 7, 8, 9, 0],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.row1_invariant(4)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[4, 6, 1, 3],
                                             [5, 2, 0, 7],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.row1_invariant(2)
        expected = True
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[4, 3, 2],
                                             [1, 0, 5],
                                             [6, 7, 8]])
        result = puzzle.row1_invariant(0)
        expected = False
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 5, [[15, 6, 5, 3, 4],
                                             [2, 1, 0, 8, 9],
                                             [10, 11, 12, 13, 14],
                                             [7, 16, 17, 18, 19]])
        result = puzzle.row1_invariant(2)
        expected = False
        self.assertEqual(result, expected)

    def test_solve_row0_tile(self):
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[1, 2, 0],
                                             [3, 4, 5],
                                             [6, 7, 8]])
        result = puzzle.solve_row0_tile(2)
        expected = 'ld'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[2, 4, 5, 0],
                                             [3, 6, 1, 7],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.solve_row0_tile(3)
        expected = 'ldllurrdlurdlurrdluldrruld'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[1, 3, 5, 0],
                                             [2, 6, 4, 7],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.solve_row0_tile(3)
        expected = 'lduldruldurdlurrdluldrruld'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 5, [[1, 5, 6, 0, 4],
                                             [7, 2, 3, 8, 9],
                                             [10, 11, 12, 13, 14],
                                             [15, 16, 17, 18, 19]])
        result = puzzle.solve_row0_tile(3)
        expected = 'lduldurdlurrdluldrruld'
        self.assertEqual(result, expected)

    def test_solve_row1_tile(self):
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[2, 5, 4],
                                             [1, 3, 0],
                                             [6, 7, 8]])
        result = puzzle.solve_row1_tile(2)
        expected = 'uldruldur'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        self.assertIs(type(puzzle.solve_row1_tile(2)), str)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 3, [[1, 4, 2],
                                             [3, 5, 0],
                                             [6, 7, 8]])
        result = puzzle.solve_row1_tile(2)
        expected = 'lur'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[1, 2, 7, 3, 4],
                                             [6, 5, 0, 8, 9],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.solve_row1_tile(2)
        expected = 'uldur'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[1, 2, 6, 3],
                                             [7, 4, 5, 0],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.solve_row1_tile(3)
        expected = 'lllurrdlurrdlur'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(4, 4, [[1, 7, 4, 2],
                                             [3, 5, 6, 0],
                                             [8, 9, 10, 11],
                                             [12, 13, 14, 15]])
        result = puzzle.solve_row1_tile(3)
        expected = 'ulldrruldruldur'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[1, 7, 2, 3, 4],
                                             [6, 5, 0, 8, 9],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.solve_row1_tile(2)
        expected = 'uldruldur'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        puzzle = FifteenPuzzle.Puzzle(3, 5, [[1, 2, 3, 4, 5],
                                             [6, 7, 8, 9, 0],
                                             [10, 11, 12, 13, 14]])
        result = puzzle.solve_row1_tile(4)
        expected = 'lur'
        self.assertEqual(result, expected)

    def test_solve_2x2(self):
        state = FifteenPuzzle.Puzzle(3, 3, [[4, 3, 2],
                                            [1, 0, 5],
                                            [6, 7, 8]])
        result = state.solve_2x2()
        expected = 'uldrul'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        self.assertIs(type(state.solve_2x2()), str)
        # ----------------------------------------------------------------------
        state = FifteenPuzzle.Puzzle(3, 5, [[5, 1, 2, 3, 4],
                                            [6, 0, 7, 8, 9],
                                            [10, 11, 12, 13, 14]])
        result = state.solve_2x2()
        expected = 'ulrdlu'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        state = FifteenPuzzle.Puzzle(2, 2, [[3, 2],
                                            [1, 0]])
        result = state.solve_2x2()
        expected = 'uldrul'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        state = FifteenPuzzle.Puzzle(2, 2, [[1, 3],
                                            [2, 0]])
        result = state.solve_2x2()
        expected = 'ul'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        state = FifteenPuzzle.Puzzle(2, 2, [[0, 1],
                                            [2, 3]])
        result = state.solve_2x2()
        expected = ''
        self.assertEqual(result, expected)

    def test_solve_puzzle(self):
        state = FifteenPuzzle.Puzzle(4, 5, [[15, 16, 0, 3, 4],
                                            [5, 6, 7, 8, 9],
                                            [10, 11, 12, 13, 14],
                                            [1, 2, 17, 18, 19]])
        result = state.solve_puzzle()
        expected = 'rrdddulduldulduuulddrulddrulduruulddruldruldrdlurdluurdd' \
                   'lurrrrulduldulduldurlruldrdlurdluurddlurrrruldurlduldurl' \
                   'duldurlduldurdlurrdluldrrulduldrul'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        state = FifteenPuzzle.Puzzle(4, 4, [[14, 12, 8, 5],
                                            [0, 2, 15, 6],
                                            [4, 13, 7, 9],
                                            [10, 11, 3, 1]])
        result = state.solve_puzzle()
        expected = 'rrrdduullurrdldrulddrulduuulldrruldrulddrulddrulduurulld' \
                   'drulddrulduruuldrulddruldruldrdlurdluurddlurrrllurrdlllu' \
                   'rrdluulddruldururdlludruldruldrdlurdluurddlurrrulldrruld' \
                   'ruldurldlurdlurrdluldrruldlurldulrdlu'
        self.assertEqual(result, expected)
        # ----------------------------------------------------------------------
        state = FifteenPuzzle.Puzzle(4, 4, [[2, 11, 12, 13],
                                            [9, 4, 6, 1],
                                            [5, 7, 8, 3],
                                            [10, 0, 14, 15]])
        result = state.solve_puzzle()
        expected = 'rrlluuurrdllurdlludrulddrulddruldururullddruldruldrdlurd' \
                   'luurddlurrruldruldllurrdluulddruldurrulldruldrdlurdluurd' \
                   'dlurrrlllurrdlurrdlurldulldrruldruldurlduldurdlurrdluldr' \
                   'rulduldrul'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
