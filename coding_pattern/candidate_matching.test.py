import unittest
from candidate_matching import Candidate, Availability, Interests, pool_matching

class TestMatchingSystem(unittest.TestCase):

    def setUp(self):
        # Setup some common availability and interests for testing
        self.avail1 = Availability([True, False, True, False, True, False, True, False])
        self.avail2 = Availability([True, True, False, False, True, True, False, False])
        self.interests1 = Interests(["python", "agile", "devops"])
        self.interests2 = Interests(["python", "machine learning", "agile"])
        self.interests3 = Interests(["devops", "cloud", "machine learning"])
        
        # Setup candidates
        self.candidate1 = Candidate("Alice", self.avail1, self.interests1)
        self.candidate2 = Candidate("Bob", self.avail2, self.interests2)
        self.candidate3 = Candidate("Charlie", self.avail1, self.interests3)

    def test_availability_matching(self):
        # Test the availability matching between two candidates
        match_result = self.avail1.get_matching_availability(self.avail2)
        expected_result = [True, False, False, False, True, False, False, False]
        self.assertEqual(match_result.availability, expected_result)

    def test_interest_matching(self):
        # Test the interest matching between two candidates
        match_result = self.interests1.get_matching_interests(self.interests2)
        expected_result = ["python", "agile"]
        self.assertEqual(match_result.interests, expected_result)

    # def test_pool_matching_pairs(self):
    #     # Test the pool_matching function to ensure it correctly forms pairs
    #     candidates = [self.candidate1, self.candidate2, self.candidate3]
    #     matched_groups = pool_matching(candidates, 2)
    #     self.assertTrue(any("Alice" in group[0].name and "Bob" in group[1].name for group in matched_groups))

    # def test_pool_matching_group_size(self):
    #     # Test to ensure the pool_matching function respects the group size
    #     candidates = [self.candidate1, self.candidate2, self.candidate3]
    #     matched_groups = pool_matching(candidates, 3)
    #     # Check that all groups have the correct number of members
    #     all_correct_size = all(len(group) == 3 for group in matched_groups)
    #     self.assertTrue(all_correct_size)

    # def test_pool_matching_no_possible_group(self):
    #     # Test to ensure no group is formed if not enough candidates are available at any time slot
    #     candidates = [self.candidate1]  # Only one candidate available
    #     matched_groups = pool_matching(candidates, 2)
    #     self.assertEqual(len(matched_groups), 0)

if __name__ == '__main__':
    unittest.main()
