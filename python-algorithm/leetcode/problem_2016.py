"""2016. Maximum Difference Between Increasing Elements
https://leetcode.com/problems/maximum-difference-between-increasing-elements/
"""
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimum = nums[0]
        ans = -1
        for i in range(1, len(nums)):
            if nums[i] > minimum:
                ans = max(ans, nums[i] - minimum)
            elif nums[i] < minimum:
                minimum = nums[i]
        return ans
