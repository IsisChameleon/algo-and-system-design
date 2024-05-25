import unittest
from max_subarray_sum import max_subarray_sum

class TestMaxSubarraySum(unittest.TestCase):
    def test_case_1(self):
        arr = [34, -50, 42, 14, -5, 86]
        self.assertEqual(max_subarray_sum(arr), 137)

    def test_case_2(self):
        arr = [-5, -1, -8, -9]
        self.assertEqual(max_subarray_sum(arr), -1)

    def test_case_3(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray_sum(arr), 15)

    def test_case_4(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_sum(arr), 6)

    def test_case_5(self):
        arr = [1]
        self.assertEqual(max_subarray_sum(arr), 1)

if __name__ == '__main__':
    unittest.main()