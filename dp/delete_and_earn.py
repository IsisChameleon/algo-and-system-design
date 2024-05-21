"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
"""

"""
state = num_deleted at step i
"""

from collections import defaultdict
from typing import List

def deleteAndEarn_Fastest(self, nums: List[int]) -> int:
    if  not nums:
        return 0

    freq = [0] * (max(nums)+1)
    for n in nums:
        freq[n] += n

    dp = [0] * len(freq)
    dp[1] = freq[1]
    for i in range(2, len(freq)):
        dp[i] = max(freq[i] + dp[i-2], dp[i-1])

    return dp[len(freq)-1]


def deleteAndEarn(nums: List[int]) -> int:

    nums_points = defaultdict(int)
    max_number = 0
    for num in nums:
        nums_points[num] += num
        max_number = max(max_number, num)

    # Let's declare a function maxPoints. 
    # We want maxPoints(num) to return the maximum points that we can gain if we only consider 
    # all the elements in nums with values between 0 and num.

    memo_maxPoints = defaultdict(int)

    def maxPoints(x: int):
        # for an arbitrary x, maxPoints(x) = max(maxPoints(x - 1), maxPoints(x - 2) + gain)
        if x == 0:
            return 0
        if x == 1:
            return nums_points[1]
        
        if x in memo_maxPoints:
            return memo_maxPoints[x]
        
        gain = nums_points[x]  # gain if we take x , but then we cannot take x - 1

        memo_maxPoints[x] = max(maxPoints(x - 1), maxPoints(x - 2) + gain)
        return memo_maxPoints[x]
    
    earnings = maxPoints(max_number)
    return earnings

# passing in leetcode but not that performant

    