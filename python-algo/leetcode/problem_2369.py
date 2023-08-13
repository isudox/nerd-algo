"""2369. Check if There is a Valid Partition For The Array
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
"""
import functools
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @functools.cache
        def helper(i: int) -> bool:
            if i < 0:
                return True
            ret = False
            if i > 0 and nums[i] == nums[i - 1]:
                ret |= helper(i - 2)
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ret |= helper(i - 3)
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ret |= helper(i - 3)
            return ret

        return helper(len(nums) - 1)
