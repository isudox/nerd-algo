"""704. Binary Search
https://leetcode.com/problems/binary-search/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i if nums[i] == target else -1
