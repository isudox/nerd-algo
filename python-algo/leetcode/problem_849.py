"""Maximize Distance to Closest Person
"""
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        pre = -1
        for i, s in enumerate(seats):
            if s == 1:
                if pre < 0:
                    ans = i
                else:
                    ans = max(ans, (i - pre) // 2)
                pre = i
        return max(ans, len(seats) - 1 - pre)
