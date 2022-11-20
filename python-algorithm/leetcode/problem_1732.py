"""1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/
"""
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        h = 0
        for num in gain:
            h += num
            if h > ans:
                ans = h
        return ans
