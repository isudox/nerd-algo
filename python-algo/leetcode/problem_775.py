"""775. Global and Local Inversions
https://leetcode.cn/problems/global-and-local-inversions/
"""
from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        max_idx = 0
        for i in range(2, n):
            if nums[i] < nums[max_idx]:
                return False
            if nums[i - 1] > nums[max_idx]:
                max_idx = i - 1
        return True
