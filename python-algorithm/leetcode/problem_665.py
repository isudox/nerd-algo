"""665. Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        cnt = 1
        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                continue
            cnt -= 1
            if cnt < 0:
                return False
            if i == 0 or i == n - 1:
                continue
            left, right = nums[i - 1], nums[i + 1]
            if left <= right:
                nums[i] = left
            else:
                nums[i + 1] = nums[i]
        return True
