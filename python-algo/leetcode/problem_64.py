"""64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from
top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
from typing import List


class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        # dp[i][j] means min sum from grid[0][0] to grid[i][j].
        dp[0][0] = grid[0][0]
        for i in range(1, cols):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        for i in range(1, rows):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[rows - 1][cols - 1]
