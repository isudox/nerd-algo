"""2594. Minimum Time to Repair Cars
https://leetcode.cn/problems/minimum-time-to-repair-cars/
"""
import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def helper(limit: int) -> bool:
            cnt = 0
            for r in ranks:
                cnt += int(math.sqrt(limit // r))
                if cnt >= cars:
                    return True
            return False

        ranks.sort()
        lo, hi = 0, ranks[-1] * cars * cars
        while lo < hi:
            mid = (lo + hi) // 2
            if helper(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
