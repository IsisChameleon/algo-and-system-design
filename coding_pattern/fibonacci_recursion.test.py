import unittest
from fibonacci_memoization import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_n_0(self):
        fib = fibonacci(0)
        self.assertEqual(0, fib)

    def test_n_1(self):
        fib = fibonacci(1)
        self.assertEqual(1, fib)

    def test_n_2(self):
        fib = fibonacci(2)
        self.assertEqual(1, fib)

    def test_n_3(self):
        fib = fibonacci(3)
        self.assertEqual(2, fib)

    def test_n_4(self):
        fib = fibonacci(4)
        self.assertEqual(3, fib)

    def test_n_5(self):
        fib = fibonacci(5)
        self.assertEqual(5, fib)

if __name__ == '__main__':
    unittest.main()