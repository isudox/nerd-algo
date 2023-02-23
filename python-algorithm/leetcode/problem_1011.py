"""1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""
from typing import List
import bisect


class Solution:
    def ship_within_days(self, weights: List[int], d: int) -> int:
        def helper(cap: int) -> bool:
            days, limit = 1, cap
            i = 0
            while i < n:
                i = bisect.bisect_left(pre_sums, limit)
                if i < n:
                    if pre_sums[i] > limit:
                        i -= 1
                    limit = pre_sums[i] + cap
                    i += 1
                    days += 1
                    if days > d:
                        return False
                    if days == d:
                        return pre_sums[-1] <= limit
            return True

        n = len(weights)
        pre_sums = [0] * n
        pre_sums[0] = max_weight = weights[0]
        for i in range(1, n):
            pre_sums[i] = pre_sums[i - 1] + weights[i]
            max_weight = max(max_weight, weights[i])
        lo, hi = max_weight, pre_sums[-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if helper(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def ship_within_days2(self, weights: List[int], d: int) -> int:
        def can_ship(capacity: int, days: int) -> bool:
            total = 0
            for weight in weights:
                if weight > capacity:
                    return False
                total += weight
                if total > capacity:
                    total = weight
                    days -= 1
                if days < 1:
                    return False
            return True

        lo = hi = 0
        for weight in weights:
            lo = max(lo, weight)
            hi += weight
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_ship(mid, d):
                hi = mid
            else:
                lo = mid + 1
        return lo
