"""
Q11. Minimum Number of Platforms

You have been given two arrays, 'AT' and 'DT', representing the arrival and departure times of all trains that reach a railway station.
Your task is to find the minimum number of platforms required for the railway station so that no train needs to wait.
Note :

1. Every train will depart on the same day and the departure time will always be greater than the arrival time. 
For example, A train with arrival time 2240 and departure time 1930 is not possible. 

2. Time will be given in 24H format and colons will be omitted for convenience. 
For example, 9:05AM will be given as "905", or 9:10PM will be given as "2110". 

3. Also, there will be no leading zeroes in the given times. For example, 12:10AM will be given as “10” and not as “0010”.

Input Format:
The first line of input contains an integer 'T' representing the number of test cases. 
The first line of each test case contains an integer 'N', representing the total number of trains. 
The second line of each test case contains 'N' single-spaced separated elements of the array 'AT', representing the arrival times of all the trains. 
The third line of each test case contains 'N' single-spaced separated elements of the array 'DT', representing the departure times of all the trains.

Output Format:
For each test case, return the minimum number of platforms required for the railway station so that no train needs to wait.
Note :
You don't need to print the output, it has already been taken care of. You just need to implement the given function.
Follow up :
Try to solve the problem in O(N) time and O(1) space.
Constraints:
1 <= T <= 10 1 <= N <= 50000 0 <= AT[i] <= DT[i] <= 2359 Where 'AT[i]' and 'DT[i]' are the elements of the arrival and the departure arrays respectively. Time limit: 1 sec
"""

from typing import List
from collections import defaultdict


def min_number_of_platforms(arr: List[int], dep: List[int]) -> int:

    if len(arr) != len(dep):
        raise ValueError("The length of the arrival and departure arrays must be equal")
    
    if len(arr)==0:
        return 0
    
    platforms_increase_at_time_t = [0 for _ in range(2360+1)]
    max_plat=0

    for i in range(len(arr)):
        print(f'Train {i} arrives at {arr[i]} and departs at {dep[i]}')
        platforms_increase_at_time_t[arr[i]] += 1
        platforms_increase_at_time_t[dep[i]+1] -= 1

    # take the max of the cumulative sum of the platforms 
    plat=0
    for t, increase in enumerate(platforms_increase_at_time_t):
        if increase == 0:
            continue
        plat+=increase
        print(f'Current platform count at time {t}: {plat}')
        if plat > max_plat:
            max_plat = plat

    return max_plat