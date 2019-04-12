# -*- coding: utf-8 -*-
"""53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example:

  Input: [-2,1,-3,4,-1,2,1,-5,4],
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:

    def max_sub_array(self, nums: List[int]) -> int:
        """O(n)"""
        assert nums

        max_sum = nums[0]
        cur_sum = nums[0]
        size = len(nums)

        for i in range(1, size):
            if cur_sum <= 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)

        return max_sum

    def brute_force(self, nums: List[int]) -> int:
        """
        brute force approach which not acceptable, O(n^2) complexity.
        :param nums:
        :return:
        """

        def sum_list(nums: List[int], left: int, right: int) -> int:
            summary = 0
            for i in range(left, right + 1):
                summary += nums[i]
            return summary

        size = len(nums)
        maximum = nums[0]
        for i in range(size):
            for j in range(i, size):
                temp_sum = sum_list(nums, i, j)
                if temp_sum > maximum:
                    maximum = temp_sum

        return maximum


if __name__ == '__main__':
    solution = Solution()
    print(solution.test([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.test([1, 2, 3, 4, 5]))
    print(solution.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.max_sub_array([1, 2, 3, 4, 5]))
    print(solution.test([-1]))
