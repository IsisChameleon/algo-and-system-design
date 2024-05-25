from list_of_winners import get_ordered_list_of_candidates
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        votingForms=[["isabelle", "john", "sarah"]]
        ordered_candidates = get_ordered_list_of_candidates(votingForms)
        self.assertEqual(["isabelle", "john", "sarah"], ordered_candidates)

    def test_case_2(self):
        votingForms=[["isabelle", "john", "sarah"], ["john"]]
        ordered_candidates = get_ordered_list_of_candidates(votingForms)
        self.assertEqual(["john", "isabelle", "sarah"], ordered_candidates)

    def test_case_3(self):
        votingForms=[["isabelle", "john", "sarah"], ["john"], []]
        ordered_candidates = get_ordered_list_of_candidates(votingForms)
        self.assertEqual(["john", "isabelle", "sarah"], ordered_candidates)

    def test_case_4(self):
        votingForms=[["isabelle", "john", "sarah", "john"], ["john"], []]
        ordered_candidates = get_ordered_list_of_candidates(votingForms)
        self.assertEqual(["john", "isabelle", "sarah"], ordered_candidates)

    def test_case_5(self):
        votingForms=[["isabelle", "john", "sarah", "john"], ["john"], [], ["isabelle"], ["john", "richard"]]
        ordered_candidates = get_ordered_list_of_candidates(votingForms)
        self.assertEqual(["john", "isabelle", "richard", "sarah"], ordered_candidates)

    def test_case_6(self):
        votingForms=[]
        ordered_candidates = get_ordered_list_of_candidates(votingForms)
        self.assertEqual([], ordered_candidates)

    def test_case_7(self):
        votingForms=[["isabelle", "john", "sarah" ],["bla", "bli", "john"]]
        ordered_candidates = get_ordered_list_of_candidates(votingForms)
        self.assertEqual(["isabelle", "bla", "john", "bli", "sarah" ], ordered_candidates)


if __name__ == '__main__':
    unittest.main()