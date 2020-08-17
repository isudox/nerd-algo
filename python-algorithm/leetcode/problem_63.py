"""63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
from typing import List


class Solution:
    def unique_paths_with_obstacles(self, obstacle_grid):
        """
        :type obstacle_grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(obstacle_grid), len(obstacle_grid[0])
        dp = [[1] * cols for _ in range(rows)]
        for _ in range(cols):
            if obstacle_grid[0][_] == 1:
                dp[0][_] = 0
            else:
                dp[0][_] = dp[0][_ - 1]
        for _ in range(rows):
            if obstacle_grid[_][0] == 1:
                dp[_][0] = 0
            else:
                dp[_][0] = dp[_ - 1][0]
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacle_grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[rows - 1][cols - 1]
