class Solution:
    def min_steps(self, n: int) -> int:
        dp = [[n] * (n + 1) for _ in range(n + 1)]
        dp[1][0] = 0
        dp[1][1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i][j] = min(dp[i][j], dp[i - j][j] + 1)
            dp[i][i] = min(dp[i]) + 1
        return min(dp[n])
