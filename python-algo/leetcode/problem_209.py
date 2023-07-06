"""209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
"""
from typing import List


class Solution:
    def min_sub_arrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        i, j, cur = 0, 0, 0
        move_i = False
        while i <= j < n:
            if move_i:
                cur -= nums[i - 1]
            else:
                cur += nums[j]
            if cur >= s:
                ans = min(ans, j - i + 1)
                i += 1
                move_i = True
            else:
                j += 1
                move_i = False
        return ans if ans <= n else 0
