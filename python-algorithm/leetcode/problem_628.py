"""628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/

Given an integer array nums, find three numbers whose product is maximum
and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6

Example 2:

Input: nums = [1,2,3,4]
Output: 24

Example 3:

Input: nums = [-1,-2,-3]
Output: -6

Constraints:

    3 <= nums.length <= 10^4
    -1000 <= nums[i] <= 1000
"""
import sys
from typing import List


class Solution:
    def maximum_product(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= 0:
            return nums[-1] * nums[-2] * nums[-3]
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximum_product_2(self, nums: List[int]) -> int:
        min_1, min_2 = sys.maxsize, sys.maxsize
        max_1, max_2, max_3 = -sys.maxsize, -sys.maxsize, -sys.maxsize
        for num in nums:
            if num < min_1:
                min_1, min_2 = num, min_1
            elif num < min_2:
                min_2 = num
            if num > max_1:
                max_1, max_2, max_3 = num, max_1, max_2
            elif num > max_2:
                max_2, max_3 = num, max_2
            elif num > max_3:
                max_3 = num
        return max(min_1 * min_2 * max_1, max_1 * max_2 * max_3)
