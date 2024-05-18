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

from collections import defaultdict
from datetime import datetime
import heapq
from typing import List, Literal

class Candidate:
    def __init__(self, person_number: int, number_of_votes: int, last_vote: datetime, status: Literal['OLD','NEW']='NEW'):
        self.person_number = person_number
        self.number_of_votes = number_of_votes
        self.last_vote = last_vote
        self.status = status

    def add_vote(self, time_t: int):
        self.last_vote = time_t
        self.number_of_votes += 1

    def __lt__(self, other):
        if self.status == 'OLD':
            return False
        if (self.number_of_votes) > other.number_of_votes:
            return True
        if (self.number_of_votes == other.number_of_votes) and (self.last_vote > other.last_vote):
            return True
        return False
    
    def __str__(self):
        return f'Candidate: {self.person_number} Votes: {self.number_of_votes} Last vote: {self.last_vote} Status {self.status}'

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.candidates_finder=defaultdict(None)
        self.candidates_heap=[]

    def _add_candidate(self, person, time_t):
        print(f'adding vote for candidate {person} at time {time_t}')
        number_of_votes = 0
        if person in self.candidates_finder:
            print(f'.... existing candidate {person}')
            old_candidate = self._remove_candidate(person)
            number_of_votes = old_candidate.number_of_votes

        new_candidate = Candidate(person,number_of_votes+1, time_t)
        print(f'... heap before push:',  self.candidates_heap)
        heapq.heappush(self.candidates_heap, new_candidate)
        print(f'... heap after push:',  self.candidates_heap)
        self.candidates_finder[person] = new_candidate

    def _remove_candidate(self, person):
        candidate = self.candidates_finder.pop(person)
        candidate.status = 'OLD'
        return candidate

    def q(self, t: int) -> int:


        for person, time_t in zip(self.persons, self.times):
            print(f'Adding vote for person {person} at time {time_t}')
            if time_t > t:
                break

            self._add_candidate(person, time_t)

            print(f'Heap: {self.candidates_heap}')
            print(f'Candidates finder: {self.candidates_finder}')
            
        return heapq.heappop(self.candidates_heap).person_number


        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)