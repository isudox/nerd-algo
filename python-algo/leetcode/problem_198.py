"""198. House Robber
https://leetcode.com/problems/house-robber/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp0, dp1 = [0] * n, [0] * n
        dp1[0] = nums[0]
        for i in range(1, n):
            dp1[i] = dp0[i - 1] + nums[i]
            dp0[i] = max(dp0[i - 1], dp1[i - 1])
        return max(dp0[-1], dp1[-1])
