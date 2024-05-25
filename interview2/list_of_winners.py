"""
/**
 * For a list of votingForms, return a list of candidate names in descending order of their total points.
 */
List<String> findWinner(List<VotingForm> votingForms)

1 user --> 1 vote up to 3 candidates
output: list of candidate names by order total of point

first candidate : gets 3 points
second candidate : 2 points
third : 1 points

votingForm ("isabelle", "john", "sarah" ) ("bla", "bli" "john")
votingForm ("isabelle", "", "")
"""

from collections import defaultdict
from typing import List


# def get_ordered_list_of_candidates_old(votingForms: List[List[str]]) -> List[str]:

#     candidates_vote_count= defaultdict(int) # key: candidate name

#     for votingForm in votingForms:
#         if len(votingForm) >= 1:
#             candidates_vote_count[votingForm[0]]+=3
#         if len(votingForm) >= 2:
#             candidates_vote_count[votingForm[1]]+=2
#         if len(votingForm) >= 3:
#             candidates_vote_count[votingForm[2]]+=1

#     ordered_candidates = sorted([item for item in candidates_vote_count.items()], key = lambda item: item[1], reverse=True)
#     ordered_candidates_name = [ c[0] for c in ordered_candidates ]

#     return ordered_candidates_name 

class VoteCount:

    def __init__(self):
        self.number_of_votes = 0
        self.number_of_first_places = 0

    def add_vote(self, vote: int):
        self.number_of_votes += vote

    def add_first_place(self):
        self.number_of_first_places += 1


def get_ordered_list_of_candidates(votingForms: List[List[str]], tie_break_by_first_place=False) -> List[str]:

    candidates_vote_count= defaultdict(lambda: VoteCount()) # key: candidate name

    for votingForm in votingForms:
        if len(votingForm) >= 1:
            candidates_vote_count[votingForm[0]].add_vote(3)
            candidates_vote_count[votingForm[0]].add_first_place()
        if len(votingForm) >= 2:
            candidates_vote_count[votingForm[1]].add_vote(2)
        if len(votingForm) >= 3:
            candidates_vote_count[votingForm[2]].add_vote(1)

    if tie_break_by_first_place==True:
        ordered_candidates = sorted([item for item in candidates_vote_count.items()], key = lambda item: (item[1].number_of_votes, item[1].number_of_first_places), reverse=True)
    else:
        ordered_candidates = sorted([item for item in candidates_vote_count.items()], key = lambda item: item[1].number_of_votes, reverse=True)
    ordered_candidates_name = [ c[0] for c in ordered_candidates ]

    return ordered_candidates_name 

