"""1764. Form Array by Concatenating Subarrays of Another Array
https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
"""
from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pos = 0
        for group in groups:
            while pos + len(group) <= len(nums):
                if nums[pos: pos + len(group)] == group:
                    pos += len(group)
                    break
                pos += 1
            else:
                return False
        return True
