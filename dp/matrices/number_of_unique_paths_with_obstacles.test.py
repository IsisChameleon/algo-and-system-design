from number_of_unique_paths_with_obstacles import uniquePathsWithObstacles
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        obstacles = [[0,0,0],[0,1,0],[0,0,0]]
        expected = 2
        actual = uniquePathsWithObstacles(obstacles)
        self.assertEqual(actual, expected)

    def test_case_first_case_is_obstacle(self):
        obstacles = [[1]]
        expected = 0
        actual = uniquePathsWithObstacles(obstacles)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()