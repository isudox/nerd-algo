"""2104. Sum of Subarray Ranges
https://leetcode.com/problems/sum-of-subarray-ranges/
"""
from typing import List


def sub_array_ranges(nums: List[int]) -> int:
    ans = 0
    n = len(nums)
    for i in range(n - 1):
        a, b = nums[i], nums[i]
        for j in range(i + 1, n):
            if nums[j] < a:
                a = nums[j]
            if nums[j] > b:
                b = nums[j]
            ans += b - a
    return ans
