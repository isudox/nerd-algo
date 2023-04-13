"""1828. Queries on Number of Points Inside a Circle
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for i, [x, y, r] in enumerate(queries):
            for a, b in points:
                if (x - a) ** 2 + (y -b) ** 2 <= r ** 2:
                    ans[i] += 1
        return ans
