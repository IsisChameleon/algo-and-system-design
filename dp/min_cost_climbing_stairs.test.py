from min_cost_climbing_stairs import minCostClimbingStairs
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        costs = [10, 15, 20]
        self.assertEqual(minCostClimbingStairs(costs), 15)

    def test_case_2(self):
        costs = [1,100,1,1,1,100,1,1,100,1]
        self.assertEqual(minCostClimbingStairs(costs), 6)

if __name__ == '__main__':
    unittest.main()