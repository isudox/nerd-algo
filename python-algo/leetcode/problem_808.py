"""808. Soup Servings
https://leetcode.com/problems/soup-servings/
"""
import math


class Solution:
    def soupServings(self, n: int) -> float:
        n = math.ceil(n / 25)
        if n >= 200:
            return 1
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
            dp[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                a = dp[max(i - 4, 0)][j]
                b = dp[max(i - 3, 0)][max(j - 1, 0)]
                c = dp[max(i - 2, 0)][max(j - 2, 0)]
                d = dp[max(i - 1, 0)][max(j - 3, 0)]
                dp[i][j] = 0.25 * (a + b + c + d)
        return dp[n][n]
