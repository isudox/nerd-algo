"""377. Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/
"""
from typing import List


class Solution:
    def combination_sum(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] > target:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(nums[0], target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i - num]
        return dp[-1]
