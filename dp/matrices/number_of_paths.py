"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

"""
1. Data structure to give the answer for all possible states ==> array
-----------------------------------------------------------------------

==> An array that answers the problem for a given state

==> The problem is asking for the number of paths to the final square, so let's have 
dp[row][col]. dp[row][col] represent how many paths there are from the start (top-left corner) to the square at 
(row, col). We will return dp[m - 1][n - 1] where m and n number of rows and columns respectively.

2. A recurrence relation to transition between states:
------------------------------------------------------

The problem says that we are allowed to move down or right. That means, if we are at some square, we arrived from either the square above or the square to the left. These two squares are 
(row - 1, col)
(row - 1, col) and 
(row, col - 1)
(row, col - 1). Since we can arrive at the current square from either of these squares, the number of ways 
to get to the current square is the sum of the number of ways to get to these two squares. 
Either of these may be out of the grid bounds, so we should make sure to check for that.

dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

3. Base cases
--------------

In this problem, we start in the top-left corner. How many ways are there for us to get to the first square? Only 1 - we start on it. 
Therefore, our base case is dp[0][0] = 1

dp[0][0]=1

"""

def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            count_from_the_top = dp[i - 1][j] if i-1>=0 else 0
            count_from_the_left = dp[i][j-1] if j-1>=0 else 0
            dp[i][j] = count_from_the_top + count_from_the_left
    return dp[m - 1][n - 1]

# passed on leetcode 