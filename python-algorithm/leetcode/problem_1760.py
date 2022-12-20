"""1760. Minimum Limit of Balls in a Bag
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
"""
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lo, hi = 1, max(nums),
        while lo < hi:
            mid = (lo + hi) // 2
            ops = sum((x - 1) // mid for x in nums)
            if ops <= maxOperations:
                hi = mid
            else:
                lo = mid + 1
        return lo
