import unittest
from min_number_of_platforms import min_number_of_platforms

class TestMinNumberOfPlatforms(unittest.TestCase):
    def test_same_arrival_departure(self):
        arr = [1000, 1000, 1000]
        dep = [1000, 1000, 1000]
        self.assertEqual(min_number_of_platforms(arr, dep), 3)

    def test_same_arrival_departure_single_train(self):
        arr = [1000]
        dep = [1000]
        self.assertEqual(min_number_of_platforms(arr, dep), 1)

    def test_same_arrival_departure_two_trains(self):
        arr = [1000, 1000]
        dep = [1000, 1000]
        self.assertEqual(min_number_of_platforms(arr, dep), 2)

    def test_same_arrival_departure_different_times_2(self):
        arr = [2200, 900, 800]
        dep = [2359, 2211, 859]
        self.assertEqual(min_number_of_platforms(arr, dep), 2)

    def test_same_arrival_departure_different_times_3(self):
        arr = [2212, 900, 800]
        dep = [2359, 2211, 900]
        self.assertEqual(min_number_of_platforms(arr, dep), 2)

    def test_same_arrival_departure_edge_case(self):
        arr = [0, 0, 0]
        dep = [0, 0, 0]
        self.assertEqual(min_number_of_platforms(arr, dep), 3)

if __name__ == '__main__':
    unittest.main()