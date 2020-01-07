# -*- coding: utf-8 -*-
"""494. Target Sum
https://leetcode.com/problems/target-sum/

You are given a list of non-negative integers, a1, a2, ..., an, and a target,
S. Now you have 2 symbols + and -. For each integer, you should choose one
from + and - as its new symbol.
⁠

Find out how many ways to assign symbols to make sum of integers equal to
target S.


Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


Note:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
from typing import List


class Solution:
    def brute_force(self, nums: List[int], s: int) -> int:

        def dfs(idx: int, target: int):
            max_sum = sum(nums[idx:])
            if target > max_sum or target < -max_sum:
                return
            if idx == len(nums) - 1:
                nonlocal ways
                if nums[idx] == target:
                    ways += 1
                if nums[idx] == -target:
                    ways += 1
                return
            dfs(idx + 1, target - nums[idx])
            dfs(idx + 1, target + nums[idx])

        ways = 0
        dfs(0, s)
        return ways

    def dfs(self, nums: List[int], s: int) -> int:
        if not nums:
            return 1 if s == 0 else 0
        ways = 0
        ways += self.dfs(nums[1:], s - nums[0])
        ways += self.dfs(nums[1:], s + nums[0])
        return ways
