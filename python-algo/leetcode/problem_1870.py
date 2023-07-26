"""1870. Minimum Speed to Arrive on Time
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
"""
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def helper(x: int) -> bool:
            ret = 0
            for i, d in enumerate(dist):
                a, b = divmod(d, x)
                if b == 0:
                    ret += a
                elif i == len(dist) - 1:
                    ret += d / x
                else:
                    ret += a + 1
                if ret > hour:
                    return False
            return True

        if len(dist) - 1 >= hour:
            return -1
        h, m = int(hour), hour - int(hour)
        lo, hi = max(1, int(sum(dist) / hour)), max(dist)
        if m > 0:
            hi *= 100
        while lo < hi:
            mid = (lo + hi) // 2
            if helper(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo if helper(lo) else -1
