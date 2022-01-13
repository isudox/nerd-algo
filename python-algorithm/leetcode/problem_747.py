"""747. Largest Number At Least Twice of Others
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
"""
from typing import List


def dominant_index(nums: List[int]) -> int:
    max_pos = 0
    max_num = nums[0]
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_pos = i
        nums[i] *= 2
    for i in range(len(nums)):
        if i != max_pos and nums[i] > max_num:
            return -1
    return max_pos
