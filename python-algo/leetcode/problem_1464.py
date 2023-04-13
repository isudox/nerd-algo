"""1464. Maximum Product of Two Elements in an Array
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = min(nums[0], nums[1]), max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] >= b:
                a, b = b, nums[i]
            elif nums[i] > a:
                a = nums[i]
        return (a - 1) * (b - 1)
