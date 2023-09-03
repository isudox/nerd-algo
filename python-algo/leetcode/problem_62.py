"""62. Unique Paths
https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        base = int(2e9)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % base
        return dp[-1][-1] % base
