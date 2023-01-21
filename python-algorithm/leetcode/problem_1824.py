"""1824. Minimum Sideway Jumps
https://leetcode.com/problems/minimum-sideway-jumps/
"""
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[0] * 3 for _ in range(n)]  # dp[i][j]: min jumps to target[i][j]
        dp[0] = [1, 0, 1]
        for i in range(1, n):
            tmp = n + 1
            for j in range(3):
                if obstacles[i] == j + 1:
                    dp[i][j] = n + 1
                else:
                    tmp = min(tmp, dp[i - 1][j])
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = min(dp[i - 1][j], tmp + 1)
        return min(dp[-1])
