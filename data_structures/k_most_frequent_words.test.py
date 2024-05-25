import unittest
from k_most_frequent_words import find_k_most_frequent_words, find_k_most_frequent_words_optimised

class TestKMostFrequentWords(unittest.TestCase):
    def test_case_1(self):
        list_of_words = ['bla', 'bla', 'bli', 'blu', 'bla', 'blu']
        k_words = find_k_most_frequent_words_optimised(list_of_words, 2)
        self.assertListEqual(k_words, ['bla', 'blu'])

    def test_case_2(self):
        list_of_words = ['bla', 'bla', 'bla', 'def', 'bla', 'abc', 'bla', 'def', 'blu', 'def', 'abc', 'abc']
        k_words = find_k_most_frequent_words_optimised(list_of_words, 2)
        self.assertListEqual(k_words, ['bla', 'abc'])

    def test_case_3(self):
        list_of_words = ['bla', 'bla', 'bla', 'aef', 'bla', 'abc', 'bla', 'aef', 'blu', 'aef', 'abc', 'abc']
        k_words = find_k_most_frequent_words_optimised(list_of_words, 2)
        self.assertListEqual(k_words, ['bla', 'abc'])

if __name__ == '__main__':
    unittest.main()