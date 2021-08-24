"""1646. Get Maximum in Generated Array
https://leetcode.com/problems/get-maximum-in-generated-array/
"""
from functools import lru_cache


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        @lru_cache(None)
        def helper(m: int) -> int:
            if m < 2:
                return m
            x, y = divmod(m, 2)
            if y == 0:
                return helper(x)
            if y == 1:
                return helper(x) + helper(x + 1)

        if n < 2:
            return n
        ans = 0
        for i in range(2, n + 1):
            ans = max(ans, helper(i))
        return ans
