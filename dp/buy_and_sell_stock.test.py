from buy_and_sell_stock import maxProfit
import unittest

class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     prices = [1]
    #     fee = 2
    #     self.assertEqual(maxProfit(prices, fee), -1)

    def test_case_1(self):
        prices = [1, 3]
        fee = 2
        print(f'Test case 1: {prices} {fee} -------------->')
        self.assertEqual(maxProfit(prices, fee), 0)

    def test_case_2(self):
        prices = [1, 3, 4]
        fee = 2
        print(f'Test case 2: {prices} {fee} -------------->')
        self.assertEqual(maxProfit(prices, fee), 1)

    def test_case_3(self):
        prices = [1,3,2,8,4,9]
        fee = 2
        print(f'Test case 3: {prices} {fee} -------------->')
        self.assertEqual(maxProfit(prices, fee), 8)

    # def test_case_1(self):
    #     prices = [1,3,7,5,10,3]
    #     fee = 3
    #     self.assertEqual(maxProfit(prices, fee), 6)

if __name__ == '__main__':
    unittest.main()