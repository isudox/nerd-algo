"""1770. Maximum Score from Performing Multiplication Operations
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
"""
import functools
from typing import List


# TODO
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i: int, k: int) -> int:
            if k == len(multipliers):
                return 0
            left = nums[i] * multipliers[k] + dfs(i + 1, k + 1)
            right = nums[len(nums) - 1 - (k - i)] * multipliers[k] + dfs(i, k + 1)
            return max(left, right)

        return dfs(0, 0)
