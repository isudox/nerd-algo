"""790. Domino and Tromino Tiling
https://leetcode.com/problems/domino-and-tromino-tiling/
"""


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0, 0, 0] for _ in range(n + 1)]
        dp[0] = [1, 0, 0]
        base = int(1e9 + 7)
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + (dp[i - 2][0] if i >= 2 else 0)
            dp[i][1] = dp[i - 1][2] + (dp[i - 2][0] if i >= 2 else 0)
            dp[i][2] = dp[i - 1][1] + (dp[i - 2][0] if i >= 2 else 0)
            dp[i][0] %= base
            dp[i][1] %= base
            dp[i][2] %= base
        return dp[-1][0]