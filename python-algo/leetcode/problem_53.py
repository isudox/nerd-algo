"""53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example:

  Input: [-2,1,-3,4,-1,2,1,-5,4],
  Output: 6
  Explanation:[4,-1,2,1] has the largest sum = 6.

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

    def max_sub_array2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        ans = nums[0]
        smallest = 0
        for i in range(len(nums)):
            temp = nums[i] - smallest
            if temp > ans:
                ans = temp
            if nums[i] < smallest:
                smallest = nums[i]
        return ans

    def max_sub_array3(self, nums: List[int]) -> int:
        ans, pre_sum, minimum = nums[0], 0, 0
        for num in nums:
            pre_sum += num
            ans = max(ans, pre_sum - minimum)
            minimum = min(minimum, pre_sum)
        return ans

    def brute_force(self, nums: List[int]) -> int:
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
