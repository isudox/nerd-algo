"""213. House Robber II
https://leetcode.com/problems/house-robber-ii/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i: int, flag: int) -> int:
            if memo[i][flag] != -1:
                return memo[i][flag]
            if i == len(nums) - 1:
                memo[i][flag] = nums[i] if flag == 0 else 0
            elif i == len(nums) - 2:
                memo[i][flag] = max(nums[i], (nums[i + 1] if flag == 0 else 0))
            else:
                memo[i][flag] = max(nums[i] + dfs(i + 2, flag),
                                    dfs(i + 1, flag))
            return memo[i][flag]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        memo = [[-1] * 2 for _ in range(len(nums))]
        return max(dfs(0, 1), dfs(1, 0))

    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = [[0, 0] for _ in range(n)]
        for i in range(1, n):
            dp0[i][0] = max(dp0[i - 1])
            dp0[i][1] = dp0[i - 1][0] + nums[i]
        ans = max(dp0[-1])
        dp1 = [[0, 0] for _ in range(n)]
        dp1[0] = (0, nums[0])
        for i in range(1, n):
            dp1[i][0] = max(dp1[i - 1])
            dp1[i][1] = dp1[i - 1][0] + (0 if i == n - 1 else nums[i])
        return max(ans, max(dp1[-1]))
