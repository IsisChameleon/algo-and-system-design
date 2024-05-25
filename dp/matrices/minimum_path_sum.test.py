from minimum_path_sum import minPathSum
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        obstacles = [[1,3,1],[1,5,1],[4,2,1]]
        expected = 7
        actual = minPathSum(obstacles)
        self.assertEqual(actual, expected)

    def test_case_first_case_is_obstacle(self):
        obstacles = [[1]]
        expected = 1
        actual = minPathSum(obstacles)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()