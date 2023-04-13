"""1877. Minimize Maximum Pair Sum in Array
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
"""
from typing import List


class Solution:
    def min_pair_sum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        return ans
