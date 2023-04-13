"""875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
"""
import bisect
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                if hours > h:
                    return False
            return True
                    
        lo, hi = math.ceil(sum(piles) / h), max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
