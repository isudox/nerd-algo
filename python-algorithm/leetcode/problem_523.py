"""523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/
"""
from typing import List


class Solution:
    def check_subarray_sum(self, nums: List[int], k: int) -> bool:
        store = {0: -1}
        for i in range(len(nums)):
            nums[i] = (nums[i] + (nums[i - 1] if i > 0 else 0)) % k
            if nums[i] in store and i - store[nums[i]] >= 2:
                return True
            if nums[i] not in store:
                store[nums[i]] = i
        return False
