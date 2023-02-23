"""1140. Stone Game II
https://leetcode.com/problems/stone-game-ii/
"""
from typing import List
import functools


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i: int, m: int) -> int:
            if i == n:
                return 0
            ret = -inf
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                ret = max(ret, pre_sum[i + x] - pre_sum[i] - dfs(i + x, max(m, x)))
            return ret

        pre_sum = [0]
        for p in piles:
            pre_sum.append(pre_sum[-1] + p)
        n = len(piles)
        return (pre_sum[-1] + dfs(0, 1)) // 2
