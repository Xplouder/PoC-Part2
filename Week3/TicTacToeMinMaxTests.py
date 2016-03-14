import unittest
from poc_ttt_provided import TTTBoard
from poc_ttt_provided import PLAYERX as X
from poc_ttt_provided import PLAYERO as O
from poc_ttt_provided import DRAW
from poc_ttt_provided import EMPTY as _
from TicTacToeMinMax import mm_move


class TicTacToeMinMaxTests(unittest.TestCase):
    def test_move_it(self):
        board = TTTBoard(3, False, [[O, X, X],
                                    [O, X, O],
                                    [X, O, X]])
        self.assertIsInstance(board, TTTBoard)
        self.assertIs(type(mm_move(board, X)), tuple)
        score, move = mm_move(board, X)
        self.assertIs(type(score), int)
        self.assertIs(type(move), tuple)
        self.assertEqual(mm_move(board, X), (1, (-1, -1)))
        board = TTTBoard(3, False, [[O, X, X],
                                    [X, O, O],
                                    [O, X, X]])
        self.assertEqual(mm_move(board, DRAW), (0, (-1, -1)))
        board = TTTBoard(3, False, [[O, X, X],
                                    [O, X, O],
                                    [O, O, X]])
        self.assertEqual(mm_move(board, O), (-1, (-1, -1)))

    def test_won_it(self):
        board = TTTBoard(3, False, [[X, X, O],
                                    [O, X, X],
                                    [O, _, O]])
        self.assertEqual(mm_move(board, X), (1, (2, 1)))
        board = TTTBoard(2, False, [[_, _],
                                    [_, _]])
        self.assertEqual(mm_move(board, X), (1, (0, 0)))

    def test_draw(self):
        board = TTTBoard(3, False,
                         [[_, _, X],
                          [_, _, _],
                          [_, _, _]])
        self.assertEqual(mm_move(board, O), (0, (1, 1)))
        board = TTTBoard(3, False,
                         [[X, _, _],
                          [O, O, _],
                          [_, X, _]])
        self.assertEqual(mm_move(board, X), (0, (1, 2)))
        board = TTTBoard(3, False,
                         [[_, _, X],
                          [_, _, _],
                          [_, _, _]])
        self.assertEqual(mm_move(board, O), (0, (1, 1)))

    def test_lost_it(self):
        board = TTTBoard(3, False, [[X, X, O],
                                    [_, X, X],
                                    [O, _, O]])
        self.assertEqual(mm_move(board, O), (-1, (2, 1)))
        
        board = TTTBoard(3, False, [[X, X, O],
                                    [_, X, X],
                                    [O, _, O]])
        self.assertEqual(mm_move(board, O), (-1, (2, 1)))

    def test_bug_case(self):
        board = TTTBoard(3, False, [[X, O, X],
                                    [_, O, _],
                                    [X, _, _]])
        self.assertEqual(mm_move(board, O), (-1, (2, 1)))


if __name__ == '__main__':
    unittest.main()
