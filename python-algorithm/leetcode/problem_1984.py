"""1984. Minimum Difference Between Highest and Lowest of K Scores
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
"""
from typing import List


def minimum_difference(nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    ans = nums[k - 1] - nums[0]
    for i in range(1, n - k + 1):
        ans = min(ans, nums[i + k - 1] - nums[i])
    return ans
