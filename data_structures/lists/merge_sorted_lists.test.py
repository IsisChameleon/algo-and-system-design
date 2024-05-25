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

    def test_case_4(self):
        sorted_lists = [[1,5,7], [2, 4, 8, 10]]
        list_indexes = [3, 3]
        at_the_end = at_the_end_of_each_list(sorted_lists, list_indexes)
        self.assertEqual(False, at_the_end)

    def test_case_5(self):
        sorted_lists = [[1,5,7], [2, 4, 8, 10]]
        list_indexes = [3, 4]
        at_the_end = at_the_end_of_each_list(sorted_lists, list_indexes)
        self.assertEqual(True, at_the_end)
    
    def test_case_6(self):
        sorted_lists = [[1,5,7], [2, 4, 8, 10]]
        merged_list = merge_sorted_lists(sorted_lists)
        self.assertEqual([1, 2, 4, 5, 7, 8, 10], merged_list)

    def test_case_7(self):
        sorted_lists = [[1,5,7], [3, 5,11, 13, 15 ],[2, 4, 8, 10]]
        merged_list = merge_sorted_lists(sorted_lists)
        self.assertEqual([1, 2, 3, 4, 5, 5, 7, 8, 10, 11, 13, 15], merged_list)

if __name__ == '__main__':
    unittest.main()