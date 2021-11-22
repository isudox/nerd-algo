"""397. Integer Replacement
https://leetcode.com/problems/integer-replacement/
"""
from functools import lru_cache


class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(x: int) -> int:
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + dfs(x // 2)
            return 1 + min(dfs(x + 1), dfs(x - 1))

        return dfs(n)
