"""167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []
