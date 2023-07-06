"""137. Single Number II
https://leetcode.com/problems/single-number-ii/
"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2
