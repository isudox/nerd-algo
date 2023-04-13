"""153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                ans = nums[i]
        return ans

    def find_min_2(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]
