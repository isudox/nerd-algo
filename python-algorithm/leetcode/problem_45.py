"""45. Jump Game II
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.
"""
from typing import List


class Solution:
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
