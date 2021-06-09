"""1049. Last Stone Weight II
https://leetcode.com/problems/last-stone-weight-ii/
"""
from typing import List
from functools import lru_cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, cur: int):
            if i == len(stones):
                nonlocal ans
                ans = min(ans, cur)
            else:
                dfs(i + 1, cur + stones[i])
                dfs(i + 1, abs(cur - stones[i]))

        ans = float('inf')
        dfs(0, 0)
        return ans

    def lastStoneWeightII2(self, stones: List[int]) -> int:
        offset = sum(stones)
        limit = 2 * offset + 1
        dp = [[False] * limit for _ in range(len(stones))]
        # dp[i][target] = dp[i-1][target-nums[i]] or dp[i-1][target+ nums[i]
        dp[0][offset + stones[0]] = True
        dp[0][offset - stones[0]] = True
        for i in range(1, len(stones)):
            for j in range(-offset, offset + 1):
                if offset + j - stones[i] >= 0 and dp[i - 1][offset + j - stones[i]]:
                    dp[i][offset + j] = True
                if offset + j + stones[i] < limit and dp[i - 1][offset + j + stones[i]]:
                    dp[i][offset + j] = True

        for i in range(offset, limit):
            if dp[-1][i]:
                return i - offset
        return 0

