"""2141. Maximum Running Time of N Computers
https://leetcode.com/problems/maximum-running-time-of-n-computers/
"""
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        lo, hi = 1, sum(batteries) // n
        while lo < hi:
            mid = (lo + hi) // 2
            tot = 0
            for b in batteries:
                tot += min(b, mid)
            if tot >= mid * n:
                lo = mid
            else:
                hi = mid - 1
        return lo
