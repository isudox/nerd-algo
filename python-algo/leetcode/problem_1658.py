"""1658. Minimum Operations to Reduce X to Zero
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""
import functools
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        @functools.lru_cache(None)
        def dfs(i: int, j: int, target: int) -> int:
            if target == 0:
                return 0
            if i > j or (target < nums[i] and target < nums[j]):
                return len(nums) + 1
            ret = len(nums) + 1
            if target >= nums[i]:
                ret = min(ret, 1 + dfs(i + 1, j, target - nums[i]))
            if target >= nums[j]:
                ret = min(ret, 1 + dfs(i, j - 1, target - nums[j]))
            return ret

        ans = dfs(0, len(nums) - 1, x)
        return ans if ans < len(nums) + 1 else -1

    def minOperations2(self, nums: List[int], x: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        total = nums[-1]
        if total == x:
            return n
        if total < x:
            return -1
        seen = {0: -1}
        ans = -1
        for i in range(n):
            if (nums[i] - total + x) in seen:
                ans = max(ans, i - seen[nums[i] - total + x])
            seen[nums[i]] = i
        return len(nums) - ans if ans > -1 else -1
