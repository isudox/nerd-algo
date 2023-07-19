"""435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def merge(cur: List[int]) -> int:
            nonlocal pre
            if not pre or pre[1] <= cur[0]:
                pre = cur
                return 0
            if pre[1] >= cur[1]:
                pre = cur
            return 1

        intervals.sort(key=lambda x: x[0])
        pre = []
        ans = 0
        for interval in intervals:
            ans += merge(interval)
        return ans
