import unittest
import collections
from Apocalypse import Apocalypse
from Apocalypse import HUMAN
from Apocalypse import ZOMBIE


class ApocalypseTests(unittest.TestCase):
    def test_clear(self):
        obj = Apocalypse(4, 6, [], [(1, 5), (3, 2)], [(0, 4), (2, 4), (3, 5)])
        obj.clear()
        expected_list = []

        self.assertEqual(obj._human_list, expected_list)
        self.assertEqual(obj._zombie_list, expected_list)
        for row in xrange(obj.get_grid_height()):
            for col in xrange(obj.get_grid_width()):
                self.assertTrue(obj.is_empty(row, col))

    def test_compute_distance_field_human(self):
        obj = Apocalypse(3, 3, [], [], [(2, 2)])
        result = obj.compute_distance_field(HUMAN)
        expected = [[4, 3, 2],
                    [3, 2, 1],
                    [2, 1, 0]]

        self.assertSequenceEqual(expected, result, seq_type=list)

    def test_compute_distance_field_zombie(self):
        obj = Apocalypse(3, 3, [], [(1, 1)], [])
        result = obj.compute_distance_field(ZOMBIE)
        expected = [[2, 1, 2],
                    [1, 0, 1],
                    [2, 1, 2]]

        self.assertSequenceEqual(expected, result, seq_type=list)

    def test_add_human(self):
        obj = Apocalypse(3, 3, [], [(1, 1)], [])
        obj.add_human(1, 1)
        expected = 1

        self.assertEqual(expected, obj.num_humans())

    def test_add_zombie(self):
        obj = Apocalypse(3, 3, [], [], [(1, 1)])
        obj.add_zombie(1, 1)
        expected = 1

        self.assertEqual(expected, obj.num_zombies())

    def test_move_human(self):
        obj = Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
        dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
        obj.move_humans(dist)
        generator = obj.humans()

        self.assertTrue(isinstance(generator, collections.Iterable))

    def test_move_zombies(self):
        obj = Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
        dist = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
        obj.move_zombies(dist)
        generator = obj.zombies()

        self.assertTrue(isinstance(generator, collections.Iterable))


if __name__ == '__main__':
    unittest.main()
