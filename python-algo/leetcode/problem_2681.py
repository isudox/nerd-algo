"""2681. Power of Heroes
https://leetcode.com/problems/power-of-heroes/
"""
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod = int(1e9 + 7)
        nums.sort()
        pre_sum = 0
        dp = 0  # dp[i] = min(sub_set)
        ans = 0
        for i in range(len(nums)):
            dp = (nums[i] + pre_sum) % mod
            pre_sum = (pre_sum + dp) % mod
            ans = (ans + nums[i] * nums[i] * dp) % mod
        return ans
