from BST import BST
from isValid import isValid
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(4)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        validity = isValid(root)
        self.assertEqual(validity, True)

    def test_case_2(self):
        root = BST(10)
        root.left = BST(11) #<--- invalid
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        validity = isValid(root)
        self.assertEqual(validity, False)

    def test_case_3(self):
        root = BST(10)
        root.left = BST(5) 
        root.left.left = BST(2)
        root.left.left.left = BST(11) #<--- invalid
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        validity = isValid(root)
        self.assertEqual(validity, False)


if __name__ == '__main__':
    unittest.main()