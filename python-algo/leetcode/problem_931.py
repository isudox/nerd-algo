"""931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/
"""
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp, tmp = matrix[0], [0] * n
        for i in range(1, n):
            tmp = matrix[i]
            for j in range(n):
                tmp[j] += min(dp[j], dp[j + 1] if j + 1 < n else dp[j], dp[j - 1] if j - 1 >= 0 else dp[j])
            dp = tmp
        return min(dp)
