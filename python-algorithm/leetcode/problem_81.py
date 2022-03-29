"""81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def helper(x: int, y: int) -> bool:
            while x <= y:
                mid = x + (y - x) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    x = mid + 1
                else:
                    y = mid - 1
            return False

        pivot = 0
        for i in range(0, len(nums) - 1):
            if nums[i] == target:
                return True
            if nums[i + 1] < nums[i]:
                pivot = i
                break
        if nums[0] <= target <= nums[pivot]:
            return helper(0, pivot)
        return helper(pivot + 1, len(nums) - 1)
