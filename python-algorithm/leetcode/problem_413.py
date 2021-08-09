"""413. Arithmetic Slices
https://leetcode.com/problems/arithmetic-slices/
"""
from typing import List


class Solution:
    def number_of_arithmetic_slices(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        while i < len(nums) - 2:
            j = i + 1
            diff = nums[j] - nums[i]
            while j < len(nums) and nums[j] - nums[j - 1] == diff:
                j += 1
            n = j - i
            if n >= 3:
                ans += (n - 1) * (n - 2) // 2
                i = j - 1
            else:
                i += 1
        return ans
