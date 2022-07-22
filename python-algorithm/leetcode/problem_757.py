"""757. Set Intersection Size At Least Two
https://leetcode.com/problems/set-intersection-size-at-least-two/
"""
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda e: (e[1], -e[0]))
        a, b = intervals[0][-1] - 1, intervals[0][-1]
        ans = 2
        for i in range(1, len(intervals)):
            x, y = intervals[i][0], intervals[i][1],
            if x <= a <= y and x <= b <= y:
                continue
            if a < x <= b <= y:
                a, b = b, y
                ans += 1
            else:
                a, b = y - 1, y
                ans += 2
        return ans
