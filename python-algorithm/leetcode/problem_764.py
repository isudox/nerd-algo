"""764. Largest Plus Sign
https://leetcode.com/problems/largest-plus-sign/
"""
from functools import lru_cache
from typing import List


# TODO: TLE
class Solution:
    def order_of_largest_plus_sign(self, n: int, mines: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(x: int, y: int, d: int) -> int:
            if (x, y) in zeros:
                return 0
            nx, ny = x + moves[d][0], y + moves[d][1]
            if 0 <= nx < n and 0 <= ny < n:
                return 1 + dfs(nx, ny, d)
            return 1

        def helper(x: int, y: int) -> int:
            cnt = n
            for d in range(4):
                cnt = min(cnt, dfs(x, y, d))
            return cnt

        ans = 0
        zeros = set()
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for zero in mines:
            zeros.add(tuple(zero))
        for i in range(n):
            for j in range(n):
                ret = helper(i, j)
                ans = max(ans, ret)
        return ans
