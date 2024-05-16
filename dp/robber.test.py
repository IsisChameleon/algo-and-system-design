import unittest
from robber import rob

class TestRobber(unittest.TestCase):
    def test_case_1(self):
        houses = [1, 2, 3, 1]
        result = rob(houses)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()