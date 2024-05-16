from typing import List

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

def rob(nums: List[int]) -> int:

# maximumAmount(0)=nums[0]
# maximumAmount(1)=max(nums[0], nums[1])=max(maximumAmount(0), nums[1])
# maximumAmount(2)=max(maximumAmount(0)+nums[2], maximumAmount[1])

# maximumAmount(i)=max(maximumAmount(i-2)+nums[i], maximumAmount(i-1))

# e.g. [4, 6, 1]
    print(f'Number of houses: {len(nums)}')

    if len(nums)==0:
        return 0
    if len(nums)==1:
        return nums[0]
    if len(nums)==2:
        return max(nums[0], nums[1])

    maximumAmount = [0]*len(nums)
    maximumAmount[0]=nums[0]
    maximumAmount[1]=max(nums[0], nums[1])
    for i in range(2, len(nums)):
        maximumAmount[i]=max(maximumAmount[i-2]+nums[i], maximumAmount[i-1])
        print(f'{i}: max {maximumAmount[i]}')

    print(maximumAmount)
    
    return maximumAmount[-1]

        