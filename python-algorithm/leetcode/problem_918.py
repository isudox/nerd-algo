"""918. Maximum Sum Circular Subarray
https://leetcode.com/problems/maximum-sum-circular-subarray/
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        lo = 0
        ans = nums[0]
        for i, num in enumerate(nums):
            if num - lo > ans:
                ans = num - lo
            if num < lo:
                lo = num
        total = nums[-1]
        hi = nums[0]
        for i in range(1, len(nums) - 1):
            if total - (nums[i] - hi) > ans:
                ans = total - (nums[i] - hi)
            if nums[i] > hi:
                hi = nums[i]
        return ans
