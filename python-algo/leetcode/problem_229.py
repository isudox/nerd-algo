"""229. Majority Element II
https://leetcode.com/problems/majority-element-ii/
"""
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        ans = []
        counter = collections.Counter(nums)
        for num, cnt in counter.items():
            if cnt > n:
                ans.append(num)
        return ans
