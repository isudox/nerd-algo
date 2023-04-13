"""334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/
"""
from typing import List


def increasing_triplet(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    left_min = [0] * n
    left_min[0] = nums[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], nums[i])
    right_max = [0] * n
    right_max[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], nums[i])
    for i in range(1, n - 1):
        if left_min[i - 1] < nums[i] < right_max[i + 1]:
            return True
    return False
