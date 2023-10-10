"""1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
"""


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0
        dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]
        base = int(1e9 + 7)
        for i in range(1, m + 1):
            dp[1][1][i] = 1
        for i in range(2, n + 1):
            for x in range(1, min(k, i) + 1):
                for y in range(1, m + 1):
                    dp[i][x][y] = dp[i - 1][x][y] * y
                    for z in range(1, y):
                        dp[i][x][y] += dp[i - 1][x - 1][z]
                    dp[i][x][y] %= base
        return sum(dp[n][k][i] for i in range(1, m + 1)) % base
