"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

from typing import List
import math

# Approach 1:  Dynamic programming 2D
#-------------------------------------

"""
Complexity Analysis

Time complexity : O(mn). We traverse the entire matrix once.

Space complexity : O(mn). Another matrix of the same size is used.
"""



def minPathSum(grid: List[List[int]]) -> int:

    dp = [[0]*len(grid[0])]*len(grid)

    dp[0][0] = grid[0][0]

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            print(f'{i},{j}: value [{grid[i][j]}]')
            if i == 0 and j == 0:
                continue

            from_above = dp[i-1][j] if i-1 >= 0 else math.inf
            from_left = dp[i][j-1] if j-1 >= 0 else math.inf
            dp[i][j] = min(from_above, from_left)+grid[i][j]
            print(f'dp[{i}][{j}]=MIN(from_above {from_above} , from_left {from_left})= {min(from_above, from_left)} + grid[{i}][{j}]={grid[i][j]}')

    return dp[-1][-1]