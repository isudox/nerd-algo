"""540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/
"""
from typing import List


def single_non_duplicate(nums: List[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans


def single_non_duplicate2(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        both_even = (hi - mid) % 2 == 0
        if nums[mid] == nums[mid + 1]:
            if both_even:
                lo = mid + 2
            else:
                hi = mid - 1
        elif nums[mid] == nums[mid - 1]:
            if both_even:
                hi = mid - 2
            else:
                lo = mid + 1
        else:
            return nums[mid]
    return nums[lo]
