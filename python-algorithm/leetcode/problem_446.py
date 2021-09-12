"""446. Arithmetic Slices II - Subsequence
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
"""
import collections
from functools import lru_cache
from typing import List


class Solution:
    def number_of_arithmetic_slices(self, nums: List[int]) -> int:
        ans = 0
        dp = [collections.Counter() for _ in range(len(nums))]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                dp[j][diff] += dp[i][diff] + 1
                ans += dp[i][diff]
        return ans

    # Time Limit Exceeded
    def number_of_arithmetic_slices2(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(pos: int, diff: int) -> int:
            if pos == len(nums) - 1:
                return 0
            ret = 0
            for i in range(pos + 1, len(nums)):
                if nums[i] - nums[pos] == diff:
                    ret += dfs(i, diff) + 1
            return ret

        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                ans += dfs(j, nums[j] - nums[i])
        return ans
