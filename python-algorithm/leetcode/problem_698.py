"""698. Partition to K Equal Sum Subsets
https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
"""
from typing import List
from functools import lru_cache


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        @lru_cache(None)
        def dfs(state: int, pre: int) -> bool:
            if state == 0:
                return True
            for i in range(len(nums)):
                if nums[i] + pre > avg:
                    break
                if (state >> i) & 1 and dfs(state ^ (1 << i), (nums[i] + pre) % avg):
                    return True
            return False

        summ = sum(nums)
        if summ % k != 0:
            return False
        avg = summ // k
        nums.sort()
        if nums[-1] > avg:
            return False
        return dfs((1 << len(nums)) - 1, 0)
