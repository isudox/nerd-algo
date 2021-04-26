"""1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

A conveyor belt has packages that must be shipped from one port to another
within D days.

The i^th package on the conveyor belt has a weight of weights[i]. Each day,
we load the ship with packages on the conveyor belt (in the order given by
weights). We may not load more weight than the maximum weight capacity of the
ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within D days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in
5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of
capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6,
7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in
3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
1 <= D <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500
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
