"""2357. Make Array Zero by Subtracting Equal Amounts
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        while nums:
            while nums and nums[0] == 0:
                nums.pop(0)
            if nums:
                num = nums.pop(0)
                for i in range(len(nums)):
                    nums[i] -= num
                ans += 1
        return ans
