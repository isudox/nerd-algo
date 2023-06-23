from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1, size2 = len(cost), len(cost[0]),
        m = 1 << size2
        dp = [[float('inf')] * m for _ in range(size1 + 1)]
        dp[0][0] = 0
        for i in range(1, size1 + 1):
            for j in range(m):
                for k in range(size2):
                    if (j & (1 << k)) == 0:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i][j ^ (1 << k)] + cost[i - 1][k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + cost[i - 1][k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][j ^ (1 << k)] + cost[i - 1][k])
        return dp[-1][-1]
