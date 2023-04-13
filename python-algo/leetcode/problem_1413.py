"""1413. Minimum Value to Get Positive Step by Step Sum
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minn = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            minn = min(minn, nums[i])
        return 1 if minn >= 0 else 1 - minn
