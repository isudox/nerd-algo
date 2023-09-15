"""136. Single Number
https://leetcode.com/problems/single-number/
"""
from functools import reduce
from typing import List


def single_number(nums: List[int]) -> int:
    nums.sort()

    for i in range(len(nums)):
        if i == len(nums) - 1:
            return nums[i]
        if i % 2 == 0:
            passed = nums[i] == nums[i + 1]
            if not passed:
                return nums[i]


def reduce_func(nums: List[int]) -> int:
    return reduce(lambda a, b: a ^ b, nums)
