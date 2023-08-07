"""1749. Maximum Absolute Sum of Any Subarray
https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/
"""
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        ans = minn = maxx = 0
        for i, num in enumerate(nums):
            ans = max(ans, abs(num - minn), abs(num - maxx))
            minn = min(minn, num)
            maxx = max(maxx, num)
        return ans