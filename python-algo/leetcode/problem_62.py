"""62. Unique Paths
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
 (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        # dp[i][j] is the number of ways to reach grid[i][j] from start corner.
        dp = [[0] * m for _ in range(n)]
        dp[0] = [1] * m
        for _ in range(n):
            dp[_][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[n - 1][m - 1]
