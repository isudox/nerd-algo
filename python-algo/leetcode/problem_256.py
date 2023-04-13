"""256. Paint House
https://leetcode.com/problems/paint-house/
"""
from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i: int, pre: int) -> int:
            if i == len(costs):
                return 0
            ret = float('inf')
            for c in range(3):
                if c == pre:
                    continue
                ret = min(ret, costs[i][c] + dfs(i + 1, c))
            return ret

        return dfs(0, -1)
