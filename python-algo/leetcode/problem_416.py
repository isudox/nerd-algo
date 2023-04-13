"""416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum
"""
from typing import List


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        summary = sum(nums)
        half = summary // 2
        if summary != 2 * half:
            return False
        nums.sort()
        n = len(nums)
        # dp[i][j] means i-th num sum to j
        dp = [[False] * (half + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(half + 1):
                if nums[i] > j:
                    dp[i][j] = False
                elif nums[i] == j:
                    dp[i][j] = True
                elif i < n - 1:
                    dp[i][j] = dp[i + 1][j] or dp[i + 1][j - nums[i]]
        return dp[0][half]

    def can_partition_1(self, nums: List[int]) -> bool:
        summary = sum(nums)
        half = summary // 2
        if summary != 2 * half:
            return False
        nums.sort()
        seen = [[False] * (half + 1) for _ in range(len(nums))]

        def dfs(i: int, target: int) -> bool:
            if i >= len(nums):
                return False
            if nums[i] == target:
                return True
            if nums[i] > target:
                return False
            if seen[i][target]:
                return False
            ret = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            if not ret:
                seen[i][target] = True
            return ret

        return dfs(0, half)
