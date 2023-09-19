"""287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
"""
from typing import List


class Solution:
    def find_duplicate(self, nums: List[int]) -> int:
        # does't meet the requirement of not modify the array.
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
