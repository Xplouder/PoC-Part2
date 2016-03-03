import unittest
import WordWrangler


class WorldWranglerTests(unittest.TestCase):
    def test_remove_duplicates(self):
        elements_list = [1, 2, 5, 5, 88, 8, 1, 2, 4]
        expected = [1, 2, 5, 88, 8, 4]
        result = WordWrangler.remove_duplicates(elements_list)
        self.assertEqual(result, expected)

    def test_intersect(self):
        elements_list1 = [1, 2, 5, 5, 88, 8, 1, 2, 4]
        elements_list2 = [1, 2, 3, 4]
        expected = [1, 2, 4]
        result = WordWrangler.intersect(elements_list1, elements_list2)
        self.assertEqual(result, expected)

    def test_merge_sort(self):
        list1 = [2, 6, 8, 10]
        expected = [2, 6, 8, 10]
        result = WordWrangler.merge_sort(list1)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
