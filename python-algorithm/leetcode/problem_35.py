"""35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""
from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
