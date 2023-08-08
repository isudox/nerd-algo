"""33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            num = nums[mid]
            if num == target:
                return mid
            if num >= nums[lo]:  # num is in left
                if nums[lo] <= target <= num:
                    hi = mid
                else:
                    lo = mid + 1
            elif num <= target <= nums[hi]:
                lo = mid
            else:
                hi = mid - 1
        return -1
