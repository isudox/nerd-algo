"""34. Find First and Last Position of Element in Sorted Array
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
import bisect
from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        start, end = -1, -1
        idx = bisect.bisect_left(nums, target)
        if nums[idx] == target:
            start = idx
            while idx < n and nums[idx] == nums[start]:
                idx += 1
            end = idx - 1
        return [start, end]
