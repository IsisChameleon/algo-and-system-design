from top_N_collections import find_top_collections
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        file_data = [
            ("file1.txt", "collection1", 150),
            ("file2.txt", "collection1", 300),
            ("file3.txt", "collection2", 200),
            ("file4.txt", "collection3", 400)
        ]
        N = 2
        top_collections, total_size = find_top_collections(file_data, N)
        print("Top N Collections:", top_collections)
        print("Total Size of all files:", total_size)
        self.assertEqual(1050,  total_size)
        self.assertListEqual([('collection1', 450), ('collection3', 400)], top_collections)

if __name__ == '__main__':
    unittest.main()