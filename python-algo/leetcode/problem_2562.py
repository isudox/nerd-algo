"""2562. Find the Array Concatenation Value
https://leetcode.cn/problems/find-the-array-concatenation-value
"""
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            cur = str(nums.pop(0))
            if nums:
                cur += str(nums.pop())
            ans += int(cur)
        return ans