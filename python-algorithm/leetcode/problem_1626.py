from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        def helper(prev: int, i: int) -> int:
            if i >= n:
                return 0
            if dp[prev + 1][i] != -1:
                return dp[prev + 1][i]
            if prev == -1 or groups[i][1] >= groups[prev][1]:
                dp[prev + 1][i] = max(helper(prev, i + 1), groups[i][1] + helper(i, i + 1))
            else:
                dp[prev + 1][i] = helper(prev, i + 1)
            return dp[prev + 1][i]

        n = len(scores)
        groups = []
        for i in range(n):
            groups.append((ages[i], scores[i],))
        groups.sort(key=lambda x: (x[0], x[1]))
        dp = [[-1] * n for _ in range(n)]
        return helper(-1, 0)
