import unittest
import WordWrangler
import random


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

    def test_merge_sort_random(self):
        list1 = random.sample(range(50), 10)
        expected = sorted(list1)
        result = WordWrangler.merge_sort(list1)
        self.assertEqual(result, expected)

    def test_gen_all_strings1(self):
        word = 'ab'
        expected = ['', 'b', 'a', 'ab', 'ba']
        result = WordWrangler.gen_all_strings(word)

        error_message = "expected (order doesn't matter) " + \
                        str(expected) + " but received " + str(result)
        self.assertItemsEqual(result, expected, error_message)

    def test_gen_all_strings2(self):
        word = 'a'
        expected = ['', 'a']
        result = WordWrangler.gen_all_strings(word)

        error_message = "expected (order doesn't matter) " + \
                        str(expected) + " but received " + str(result)
        self.assertItemsEqual(result, expected, error_message)


if __name__ == '__main__':
    unittest.main()
