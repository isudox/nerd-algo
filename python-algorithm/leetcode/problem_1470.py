"""1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/
[2,5,1,3,4,7], n = 3
[2,3,5,4,1,7]
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = [], []
        for i in range(n):
            left.append(nums[i])
            right.append(nums[i + n])
        for i in range(n):
            nums[i * 2] = left[i]
            nums[i * 2 + 1] = right[i]
        return nums
