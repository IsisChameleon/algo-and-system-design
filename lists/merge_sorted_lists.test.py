import unittest
from merge_sorted_lists import merge_sorted_lists, at_the_end_of_each_list

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        sorted_lists = [[1,5,7], [2, 4, 8]]
        list_indexes = [1, 0]
        at_the_end = at_the_end_of_each_list(sorted_lists, list_indexes)
        self.assertEqual(False, at_the_end)

    def test_case_2(self):
        sorted_lists = [[1,5,7], [2, 4, 8]]
        list_indexes = [2, 2]
        at_the_end = at_the_end_of_each_list(sorted_lists, list_indexes)
        self.assertEqual(False, at_the_end)

    def test_case_3(self):
        sorted_lists = [[1,5,7], [2, 4, 8]]
        list_indexes = [2, 3]
        at_the_end = at_the_end_of_each_list(sorted_lists, list_indexes)
        self.assertEqual(False, at_the_end)

if __name__ == '__main__':
    unittest.main()