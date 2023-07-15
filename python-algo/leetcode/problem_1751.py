"""1751. Maximum Number of Events That Can Be Attended II
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
"""
from typing import List
from bisect import bisect_right
from functools import cache


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def dfs(x: int, cnt: int) -> int:
            if cnt == 0 or x == n:
                return 0
            y = bisect_right(starts, events[x][1])
            return max(dfs(x + 1, cnt), events[x][2] + dfs(y, cnt - 1))

        events.sort()
        n = len(events)
        starts = [i for i, _, _ in events]
        return dfs(0, k)
