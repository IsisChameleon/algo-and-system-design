import unittest
from quickSort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_mixed_positive_and_negative(self):
        arr = [3, -1, 4, -2, 5, 0]
        quicksort(arr)
        self.assertEqual(arr, [-2, -1, 0, 3, 4, 5])

    def test_all_negative(self):
        arr = [-3, -1, -4, -2, -5]
        quicksort(arr)
        self.assertEqual(arr, [-5, -4, -3, -2, -1])

    def test_all_positive(self):
        arr = [3, 1, 4, 2, 5]
        quicksort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_mixed_with_duplicates(self):
        arr = [3, -1, 4, -2, 5, 0, -1, 3]
        quicksort(arr)
        self.assertEqual(arr, [-2, -1, -1, 0, 3, 3, 4, 5])

    def test_single_element(self):
        arr = [1]
        quicksort(arr)
        self.assertEqual(arr, [1])

if __name__ == '__main__':
    unittest.main()