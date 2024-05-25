"""
Given two strings S and T, return a list of all the words in S that do not appear in T.

Explanation:

1.Input:

Two strings S and T.
Each string contains words separated by spaces.

2.Output:

A list of words that are present in S but not in T.

3.Steps to Solve:

Split both strings S and T into lists of words.
Create a set of words from T for efficient lookup.
Iterate through the list of words from S and collect those that are not in the set of words from T.
Return the list of words that are unique to S.
"""

def find_words_only_in_s(s, t): 
    return [word for word in s.split() if word not in t.split()]

# o(N*M)

def find_words_only_in_s_optimised(s, t): 
    t_set = set(t.split())
    return [word for word in s.split() if word not in t_set]  
# The membership check word not in t_set takes \(O(1)\) on average for each word because t_set is a set.  

# O(N+M)