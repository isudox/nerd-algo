"""2256. Minimum Average Difference
https://leetcode.com/problems/minimum-average-difference/
"""
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = nums[-1] // n
        pos = n - 1
        for i in range(n - 1):
            lavg = nums[i] // (i + 1)
            ravg = (nums[-1] - nums[i]) // (n - i - 1)
            d = abs(lavg - ravg)
            if d < ans:
                ans = d
                pos = i
            elif d == ans and i < pos:
                pos = i
        return pos
