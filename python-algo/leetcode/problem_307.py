"""307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        size = int(n ** 0.5)
        sums = [0] * ((n + size - 1) // size)
        for i, num in enumerate(nums):
            sums[i // size] += num
        self.nums = nums
        self.sums = sums
        self.size = size

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        block1, block2 = left // self.size, right // self.size
        if block1 == block2:
            return sum(self.nums[left:right + 1])
        return sum(self.nums[left:(block1 + 1) * self.size]) + \
               sum(self.sums[block1 + 1: block2]) + \
               sum(self.nums[block2 * self.size: right + 1])
