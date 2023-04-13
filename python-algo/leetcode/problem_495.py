"""495. Teemo Attacking
https://leetcode.com/problems/teemo-attacking/
"""
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        end = 0
        for t in timeSeries:
            ans += duration + (0 if end <= t else t - end)
            end = t + duration
        return ans
