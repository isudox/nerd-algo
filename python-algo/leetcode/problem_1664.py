"""1664. Ways to Make a Fair Array
https://leetcode.com/problems/ways-to-make-a-fair-array/
"""
from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        s = [0, 0]
        for i in range(n):
            s[i % 2] += nums[i]
        ans = 0
        t = [0, 0]
        for i in range(n):
            # del nums[i]
            t[(i + 1) % 2] += nums[i - 1] if i > 0 else 0
            if i % 2 == 0 and t[0] + s[1] - t[1] == t[1] + s[0] - t[0] - nums[i]:
                ans += 1
            elif i % 2 == 1 and t[0] + s[1] - t[1] - nums[i] == t[1] + s[0] - t[0]:
                ans += 1
        return ans
