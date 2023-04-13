"""1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
"""
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        i, n = 1, len(nums)
        while i < n:
            if nums[i] < nums[i - 1]:
                break
            i += 1
        if i == n:
            return True
        for j in range(i + 1, n):
            if nums[j] < nums[j - 1]:
                return False
        return nums[-1] <= nums[0]
