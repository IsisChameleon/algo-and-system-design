import unittest
from logger_limiter import Logger3

class TestLoggerLimiter(unittest.TestCase):

    def test_case_q(self):
        logger = Logger3()
        results = []

        for msg, t in [('foo', 1), ('foo', 11)]:

            result = logger.shouldPrintMessage(t, msg)
            results.append(result)

        self.assertListEqual(results,  [True, True])

    def test_case_2(self):
        logger = Logger3()
        results = []
# [1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]
        for msg, t in [('foo', 1), ('bar', 2), ('foo', 3), ('bar', 8), ("foo", 10), ("foo", 11)]:

            result = logger.shouldPrintMessage(t, msg)
            results.append(result)

        self.assertListEqual(results,  [True, True, False,False,False,True])

if __name__ == '__main__':
    unittest.main()