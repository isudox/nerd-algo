"""1335. Minimum Difficulty of a Job Schedule
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
"""
from typing import List


class Solution:
    def min_difficulty(self, job_difficulty: List[int], d: int) -> int:
        n = len(job_difficulty)
        if d > n:
            return -1
        max_d = [[0] * n for _ in range(n)]  # max difficulty between [i:j]
        for i in range(n):
            max_d[i][i] = job_difficulty[i]
            for j in range(i + 1, n):
                max_d[i][j] = max(max_d[i][j - 1], job_difficulty[j])
        dp = [[-1] * (d + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = max_d[0][i]
            for j in range(2, min(i + 1, d) + 1):
                dp[i][j] = 900000
                for k in range(i):
                    if dp[k][j - 1] > -1:
                        dp[i][j] = min(dp[i][j], dp[k][j - 1] + max_d[k + 1][i])
        return dp[-1][-1]
