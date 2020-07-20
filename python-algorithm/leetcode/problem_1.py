"""1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in d:
                return [d[target - x], i]
            d[x] = i
