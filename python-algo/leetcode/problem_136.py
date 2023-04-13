"""136. Single Number
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except
for one. Find that single one.

Note:

  Your algorithm should have a linear runtime complexity.
  Could you implement it without using extra memory?

Example 1:

  Input: [2,2,1]
  Output: 1

Example 2:

  Input: [4,1,2,1,2]
  Output: 4
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
