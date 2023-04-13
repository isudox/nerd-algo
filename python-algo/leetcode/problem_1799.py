"""1799. Maximize Score After N Operations
https://leetcode.com/problems/maximize-score-after-n-operations/
"""
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        dp = [0] * (1 << n)
        gcds = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                gcds[i][j] = gcd(nums[i], nums[j])
        bits = 1 << n
        for i in range(1, bits):
            x = bin(i).count('1')
            if x & 1 != 0:
                continue
            for j in range(n):
                if (i >> j) & 1 != 0:
                    for k in range(j + 1, n):
                        if (i >> k) & 1 != 0:
                            dp[i] = max(dp[i], dp[i ^ (1 << j) ^ (1 << k)] + x // 2 * gcds[j][k])
        return dp[-1]
