"""891. Sum of Subsequence Widths
https://leetcode.com/problems/sum-of-subsequence-widths/
"""
from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        base = int(1e9 + 7)
        nums.sort()
        ans = 0
        x, y = nums[0], 2
        for i in range(1, len(nums)):
            ans = (ans + nums[i] * (y - 1) - x) % base
            x = (x * 2 + nums[i]) % base
            y = y * 2 % base
        return ans % base
