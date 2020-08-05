"""213. House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place
are arranged in a circle. That means the first house is the neighbor of the
last one. Meanwhile, adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken
into on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight
without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
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
