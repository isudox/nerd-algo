"""356. Line Reflection
https://leetcode.com/problems/line-reflection/
"""
from typing import List
import collections


class Solution:
    def is_reflected(self, points: List[List[int]]) -> bool:
        minimum, maximum = 100000000, -100000000
        store = collections.defaultdict(set)
        for p in points:
            x, y = p[0], p[1]
            minimum = min(minimum, x)
            maximum = max(maximum, x)
            store[y].add(x)
        summary = minimum + maximum
        for x_set in store.values():
            for x in x_set:
                if summary - x not in x_set:
                    return False
        return True
