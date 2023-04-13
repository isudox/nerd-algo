"""16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:

  Given array nums = [-1, 2, 1, -4], and target = 1.
  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import sys
from typing import List


class Solution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        res, diff = sys.maxsize, sys.maxsize
        count = len(nums)
        nums.sort()
        for i in range(count - 2):
            if 0 < i < count - 2 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, count - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                cur_diff = cur_sum - target
                if cur_diff == 0:
                    return cur_sum
                diff = diff if abs(diff) < abs(cur_diff) else cur_diff
                res = target + diff
                if cur_diff > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res

    def three_sum_closest_1(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = sum(nums[:3])
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur == target:
                    return cur
                if cur > target:
                    k -= 1
                else:
                    j += 1
                if abs(target - cur) < abs(target - ans):
                    ans = cur
        return ans
