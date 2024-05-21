from collections import defaultdict
from typing import List
import datetime

class Availability:
    
    def __init__(self, availability: List[bool]):
        self.availability = availability

    def get_matching_availability(self, other):
        print(f'self: {self.availability}')
        print(f'other: {other.availability}')
        common_availability = [i and j for i,j in zip(self.availability, other.availability)] 
        print(f'common: {common_availability}')
        return Availability(common_availability)
    
class Interests:
    def __init__(self, interests: set[str]):
        self.interests = interests

    def get_matching_interests(self, other):
        common_interests = [i for i in self.interests if i in other.interests]
        return Interests(common_interests)
    
class Candidate:
    def __init__(self, name: str, availability: Availability, interests: Interests):
        self.name = name
        self._availability = availability
        self.interests = interests

    def isAvailableAt(self, t: int):
        return self._availability.availability[t]
    
    def get_matching_interest(self, other):
        return self.interests.get_matching_interests(other.interests)
    
    @property
    def availability(self):
        return self._availability.availability
    
def pool_matching(candidates: List[Candidate], group_size: int = 2):
    availability_group = defaultdict(list)

    # assuming time goes from 0 to 7 (8 hours to say something)
    time = 8

    for candidate in candidates:
        for t, avail_t in enumerate(candidate.availability):
            if avail_t :
                availability_group[t].append(candidate)

    # Now that we have a hashmap with group of candidates for each time slot, we want to find 
    # candidates that match timeslot and also interests

        # Step 3: Match candidates within the same availability based on interest overlap
    matched_groups: List[List[Candidate]] = []
    
    for candidates_group in availability_group.values():
        # While there are enough candidates to form a group
        while len(candidates_group) >= group_size:
            # Try to form the best possible group based on interest overlap
            best_group = []
            best_score = 0
            # Generate all combinations for the current group size
            for i in range(len(candidates_group)):
                for j in range(i + 1, len(candidates_group)):
                    current_set = [candidates_group[i], candidates_group[j]]
                    current_score = len(candidates_group[i].get_matching_interest(candidates_group[j]))
                    if current_score > best_score:
                        best_score = current_score
                        best_group = current_set

            # Remove selected candidates from the group and add to results
            if best_group:
                matched_groups.append(best_group)
                for candidate in best_group:
                    candidates_group.remove(candidate)

    return matched_groups



    
