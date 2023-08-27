"""403. Frog Jump
https://leetcode.com/problems/frog-jump/
"""
from typing import List
import functools


class Solution:
    def can_cross(self, stones: List[int]) -> bool:
        n = len(stones)
        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                jump = stones[i] - stones[j]
                if jump > j + 1:
                    break
                dp[i][jump] = dp[j][jump - 1] or dp[j][jump] or dp[j][jump + 1]
                if i == n - 1 and dp[i][jump]:
                    return True
        return False

    def can_cross_1(self, stones: List[int]) -> bool:
        """maximum recursion depth error"""

        def dfs(idx: int, jump: int):
            if jump in memo[idx]:
                return memo[idx].get(jump)
            if idx == len(stones) - 1:
                memo[idx][jump] = True
                return True
            ret = False
            for next_jump in range(max(1, jump - 1), jump + 2):
                stone = stones[idx] + next_jump
                for i in range(idx + 1, len(stones)):
                    if stones[i] == stone:
                        ret |= dfs(i, next_jump)
                    elif stones[i] > stone:
                        break
            memo[idx][jump] = ret
            return ret

        memo = [dict() for _ in range(len(stones))]
        ans = dfs(0, 0)
        return ans

    def can_cross_2(self, stones: List[int]) -> bool:
        @functools.cache
        def dfs(i: int, pre: int) -> bool:
            if i == n - 1:
                return True
            for j in range(i + 1, n):
                cur = stones[j] - stones[i]
                if cur > pre + 1:
                    break
                if cur >= pre - 1 and dfs(j, cur):
                    return True
            return False

        if stones[1] - stones[0] > 1:
            return False
        n = len(stones)
        return dfs(1, 1)
