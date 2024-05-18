from top_voted_candidate import TopVotedCandidate
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        times = [0, 1, 2, 3, 4, 5]
        persons = [0, 1, 1, 0, 0, 1]
        topVotedCandidate = TopVotedCandidate(persons, times)
        self.assertEqual(topVotedCandidate.q(0), 0)
        self.assertEqual(topVotedCandidate.q(1), 1)
        self.assertEqual(topVotedCandidate.q(2), 1)
        self.assertEqual(topVotedCandidate.q(3), 0)
        self.assertEqual(topVotedCandidate.q(4), 0)
        self.assertEqual(topVotedCandidate.q(5), 1)


if __name__ == '__main__':
    unittest.main()