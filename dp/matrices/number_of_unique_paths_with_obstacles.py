"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""

from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:

    dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

    dp[0][0] = 1

    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):

            print(f'{i},{j}: [{obstacleGrid[i][j]}]')

            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
                continue

            if i == 0 and j == 0:
                continue

            from_above = dp[i-1][j] if i-1 >= 0 else 0
            from_left = dp[i][j-1] if j-1 >= 0 else 0
            dp[i][j] = from_above + from_left
            print(f'dp[{i}][{j}]=from_above {from_above} + from_left {from_left} = {dp[i][j]}')

    return dp[-1][-1]

# passed on Leetcode

"""
Note we can improve by using obstacle grid as the dp array
In that case is

Complexity Analysis

Time Complexity: O(M×N)O(M \times N)O(M×N). The rectangular grid given to us is of size M×NM \times NM×N and we process each cell just once.
Space Complexity: O(1)O(1)O(1). We are utilizing the obstacleGrid as the DP array. Hence, no extra space.
"""