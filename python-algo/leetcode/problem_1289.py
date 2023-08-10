"""Minimum Falling Path Sum II
https://leetcode.com/problems/minimum-falling-path-sum-ii/
"""
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = grid[0]
        for i in range(1, n):
            tmp = [float("inf")] * n
            for j in range(n):
                for k in range(n):
                    if k != j:
                        tmp[j] = min(tmp[j], dp[k] + grid[i][j])
            dp = tmp
        return min(dp)
