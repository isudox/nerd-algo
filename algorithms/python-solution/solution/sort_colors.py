"""75. Sort Colors
https://leetcode.com/problems/sort-colors/

Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order
red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
from typing import List


class Solution:
    def sort_colors_1_pass(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1

    def sort_colors_2_pass(self, nums: List[int]) -> None:
        store = {0: 0, 1: 0, 2: 0}
        for num in nums:
            store[num] += 1
        i = 0
        for k, v in store.items():
            nums[i:i + v] = [k] * v
            i += v
