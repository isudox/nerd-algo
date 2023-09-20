"""1658. Minimum Operations to Reduce X to Zero
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""
import functools
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        target = nums[-1] - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        ans = len(nums) + 1
        seen = {0: -1}
        for i, num in enumerate(nums):
            diff = num - target
            if diff in seen:
                ans = min(ans, len(nums) - i + seen[diff])
            seen[num] = i
        return ans if ans <= len(nums) else -1
