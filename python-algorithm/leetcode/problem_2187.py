"""2187. Minimum Time to Complete Trips
https://leetcode.com/problems/minimum-time-to-complete-trips/
"""
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(x: int) -> bool:
            cnt = 0
            for t in time:
                cnt += x // t
            return cnt >= totalTrips

        lo, hi = 1, totalTrips * max(time),
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
