"""611. Valid Triangle Number
https://leetcode.com/problems/valid-triangle-number/
"""
import bisect
from typing import List


def triangle_number(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    nums.sort()
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            val = nums[i] + nums[j]
            idx = bisect.bisect_left(nums, val)
            if idx == n:
                idx -= 1
            if nums[idx] >= val:
                idx -= 1
            if idx > j:
                ans += idx - j
    return ans
