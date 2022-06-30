"""462. Minimum Moves to Equal Array Elements II
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            ans += nums[j] - nums[i]
            i += 1
            j -= 1
        return ans
