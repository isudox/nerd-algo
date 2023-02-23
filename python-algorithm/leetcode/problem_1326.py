"""

"""
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i, r in enumerate(ranges):
            a, b = max(0, i - r), min(n, i + r)
            intervals.append((a, b))
        intervals.sort()
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for a, b in intervals:
            if dp[a] == n + 1:
                return -1
            for i in range(a, b + 1):
                dp[i] = min(dp[i], dp[a] + 1)
        return dp[n]
