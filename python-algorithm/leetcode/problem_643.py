"""643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

Given an array consisting of n integers, find the contiguous subarray of
given length k that has the maximum average value. And you need to output the
maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
"""
from typing import List


class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:
        n = len(nums)
        summary = sum(nums[:k])
        maximum = summary
        for i in range(1, n - k + 1):
            summary += nums[i + k - 1] - nums[i - 1]
            if summary > 0:
                maximum = summary
        return maximum / k
