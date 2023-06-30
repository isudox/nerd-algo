"""1681. Minimum Incompatibility
https://leetcode.com/problems/minimum-incompatibility/
"""
from typing import List
import collections


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums) // k
        counter = collections.Counter(nums)
        for cnt in counter.values():
            if cnt > n:
                return -1
        return 0
