"""15. 3Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which gives
the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        if size < 3:
            return []
        result = []
        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = size - 1
            for j in range(i + 1, size - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
        return result
