"""561. Array Partition I
https://leetcode.com/problems/array-partition-i/
"""
from typing import List


class Solution:
    def array_pair_sum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans
