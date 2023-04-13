"""526. Beautiful Arrangement
https://leetcode.com/problems/beautiful-arrangement/
"""
from functools import lru_cache


class Solution:
    def count_arrangement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(pos: int, bits: int) -> int:
            if pos > n:
                return 1
            ret = 0
            for num in range(1, n + 1):
                used = (bits >> num) & 1
                if not used and (num % pos == 0 or pos % num == 0):
                    ret += dfs(pos + 1, bits + (1 << num))
            return ret

        return dfs(1, 0)
