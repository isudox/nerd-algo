"""
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set(nums1)
        ans = 100
        for num in nums2:
            if num in seen:
                ans = min(ans, num)
        if ans < 100:
            return ans
        a, b = min(nums1), min(nums2)
        return min(a, b) * 10 + max(a, b)
