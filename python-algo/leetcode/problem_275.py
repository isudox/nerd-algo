"""275. H-Index II
https://leetcode.com/problems/h-index-ii/
"""
from typing import List
import bisect


class Solution:
    def h_index(self, citations: List[int]) -> int:
        lo, hi = 0, citations[-1]
        while lo < hi:
            mid = (lo + hi + 1) >> 1  # ceil
            pos = bisect.bisect_left(citations, mid)
            if len(citations) - pos >= mid:
                if hi == mid:
                    return mid
                lo = mid
            else:
                hi = mid - 1
        return hi
