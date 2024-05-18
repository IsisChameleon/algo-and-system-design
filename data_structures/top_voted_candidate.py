"""
You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
 

Example 1:

Input
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
Output
[null, 0, 1, 1, 0, 0, 1]

Explanation
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8); // return 1

"""

"""
https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
Important Bisection Functions 
1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the rightmost position where element has to be inserted is returned.

This function takes 4 arguments, list which has to be worked with, a number to insert, starting position in list to consider, ending position which has to be considered. 

2. bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the leftmost position where element has to be inserted is returned. 

This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered. 
"""

import bisect
from collections import defaultdict
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = defaultdict(int) #key = person
        self.top_person_at_time_t = [] # list_of_tuples (person, vote_count)
        self.times = times
        self.current_top_person_vote = (-1, 0) # tuple (person, vote_count)

        for person in persons:
            self.votes[person] += 1 
            if self.votes[person] >= self.current_top_person_vote[1]:
                self.current_top_person_vote = (person, self.votes[person])

            self.top_person_at_time_t.append(self.current_top_person_vote)

    def q(self, t: int) -> int:
        time_idx = bisect.bisect_right(self.times, t)
        return self.top_person_at_time_t[time_idx-1][0]

     


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)