"""1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/
"""
from functools import lru_cache


class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def dfs(x: int) -> int:
            if x == 0:
                return 0
            if x <= 2:
                return 1
            return dfs(x - 3) + dfs(x - 2) + dfs(x - 1)

        return dfs(n)
