"""45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
"""
from typing import List


class Solution:
    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= n - 1:
                steps = n + 1
                for j in range(1, nums[i] + 1):
                    pass
        return dp[0]

    def jump(self, nums: List[int]) -> int:
        def test(i: int, pre_steps: int):
            if i == size - 1:
                return
            if memo[-1] < size:  # it means already has jumped to last.
                if pre_steps + 1 >= memo[-1]:
                    return
            for j in range(nums[i], 0, -1):
                k = min(i + j, size - 1)
                if memo[k] < size:  # it means jump to nums[k] before.
                    if pre_steps + 1 < memo[k]:  # then we can try to jump.
                        memo[k] = min(pre_steps + 1, memo[k])
                        test(k, pre_steps + 1)
                else:
                    memo[k] = pre_steps + 1
                    test(k, pre_steps + 1)

        size = len(nums)
        if size <= 1:
            return 0
        memo = [size] * size  # memo[i] = the least jumps to the nums[i].
        test(0, 0)
        return memo[-1]
