"""1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
"""
from typing import List


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[-1] + nums[i]
        return nums
